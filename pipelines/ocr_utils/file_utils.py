import base64
import logging
import tempfile
from pathlib import Path

import aiohttp
import fitz

logger = logging.getLogger(__name__)


async def download_file(url: str, headers: dict) -> bytes:
    """
    Асинхронно загружает файл по указанному URL.

    Args:
        url: URL файла для загрузки
        headers: Словарь с HTTP заголовками, включая авторизацию

    Returns:
        Байты загруженного файла

    Raises:
        Exception: Если HTTP статус ответа не равен 200 или произошла ошибка при загрузке
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            if resp.status == 200:
                content = await resp.read()
                logger.info(f"Downloaded file: {len(content)} bytes")
                return content
            else:
                error_text = await resp.text()
                raise Exception(f"Failed to download file: HTTP {resp.status} – {error_text}")


def pdf_to_base64_images(
    pdf_bytes: bytes,
    filename: str = "",
    dpi: int = 150,
) -> list[dict]:
    """
    Конвертирует PDF документ в список base64-кодированных PNG-изображений.
    Каждая страница рендерится с заданным DPI, кодируется в base64 и возвращается как data URL.

    Args:
        pdf_bytes: Байты PDF файла для конвертации.
        filename: Имя файла для логирования.
        dpi: Желаемое разрешение в DPI.

    Returns:
        Список словарей в формате:
        [{"type": "image_url", "image_url": {"url": "data:image/png;base64,..."}}, ...]

    Raises:
        Exception: Если не удалось открыть или обработать PDF файл.
    """
    image_blocks = []
    try:
        matrix = fitz.Matrix(dpi / 72.0, dpi / 72.0)
        pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")

        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            pix = page.get_pixmap(matrix=matrix, alpha=False)
            png_data = pix.tobytes("png")
            b64_content = base64.b64encode(png_data).decode("utf-8")
            data_url = f"data:image/png;base64,{b64_content}"
            image_blocks.append({"type": "image_url", "image_url": {"url": data_url}})
        pdf_document.close()
        logger.info(f"PDF converted: {filename} ({len(image_blocks)} pages) at {dpi} DPI")

    except Exception as e:
        logger.error(f"Failed to convert PDF {filename} to images: {e}")
        raise

    return image_blocks


async def process_pdf_to_base64_images(
    file_urls: list[dict],
    openwebui_host: str,
    openwebui_token: str,
    dpi: int,
) -> dict[str, list[dict]]:
    """
    Асинхронно обрабатывает список файлов: загружает каждый файл по URL
    и конвертирует PDF в base64-кодированные изображения.
    Возвращает словарь с изображениями для каждого файла.

    Args:
        file_urls: Список словарей с информацией о файлах.
                   Каждый словарь должен содержать ключи 'url', 'name' и 'id'
        openwebui_host: Базовый URL хоста OpenWebUI
        openwebui_token: Токен авторизации для доступа к API OpenWebUI
        dpi: Разрешение для конвертации PDF в изображения

    Returns:
        Словарь {file_id: [image_blocks]} с блоками изображений для каждого файла.
        Если токен не установлен, возвращает пустой словарь.
    """
    if not openwebui_token:
        logger.warning("OPENWEBUI_API_KEY not set — skipping file download")
        return {}

    headers = {"Authorization": f"Bearer {openwebui_token}"}
    files_images = {}

    for file_meta in file_urls:
        url = f"{openwebui_host}{file_meta['url']}/content"
        filename = file_meta.get("name", "unknown.pdf")
        file_id = file_meta.get("id")

        try:
            content = await download_file(url, headers)
            image_blocks = pdf_to_base64_images(content, filename, dpi)
            logger.info(f"Processed file {filename} ({len(image_blocks)} pages)")
            if file_id:
                files_images[file_id] = image_blocks
            else:
                logger.warning(f"File {filename} has no id, skipping")
        except Exception as e:
            logger.error(f"Exception processing file {filename}: {e}")

    return files_images


async def download_pdf_to_temp_path(
    url: str,
    headers: dict,
    filename_hint: str = "document.pdf",
) -> str:
    """
    Загружает PDF по URL и сохраняет во временный файл.

    Args:
        url: URL файла для загрузки
        headers: Словарь с HTTP заголовками, включая авторизацию
        filename_hint: Подсказка имени файла для расширения

    Returns:
        Путь к временному файлу

    Raises:
        Exception: Если загрузка не удалась или не удалось записать файл
    """
    content = await download_file(url, headers)
    suffix = Path(filename_hint).suffix or ".pdf"
    fd, path = tempfile.mkstemp(suffix=suffix)
    try:
        with open(fd, "wb") as f:
            f.write(content)
        return path
    except Exception:
        Path(path).unlink(missing_ok=True)
        raise


async def download_pdfs_to_temp_paths(
    file_list: list[dict],
    openwebui_host: str,
    openwebui_token: str,
) -> list[str]:
    """
    Загружает список PDF-файлов по URL OpenWebUI и сохраняет во временные файлы.

    Args:
        file_list: Список словарей с ключами url и name
        openwebui_host: Базовый хост OpenWebUI
        openwebui_token: Токен авторизации OpenWebUI

    Returns:
        Список путей к временным файлам

    Raises:
        Exception: Если загрузка хотя бы одного файла не удалась
    """
    if not openwebui_token:
        logger.warning("OPENWEBUI_API_KEY not set — skipping file download")
        return []

    headers = {"Authorization": f"Bearer {openwebui_token}"}
    paths = []

    for file_meta in file_list:
        url = f"{openwebui_host.rstrip('/')}{file_meta['url']}/content"
        name = file_meta.get("name", "unknown.pdf")
        try:
            path = await download_pdf_to_temp_path(url, headers, name)
            paths.append(path)
            logger.info(f"Downloaded {name} to temp file")
        except Exception as e:
            logger.error(f"Failed to download {name}: {e}")
            for p in paths:
                Path(p).unlink(missing_ok=True)
            raise

    return paths
