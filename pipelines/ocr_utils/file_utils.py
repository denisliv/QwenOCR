import base64
import io
import logging

import aiohttp
import fitz
from PIL import Image

logger = logging.getLogger(__name__)


async def download_file(url: str, headers: dict) -> bytes:
    """
    Асинхронно загружает файл по указанному URL с использованием переданных заголовков.

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


def pdf_to_base64_images(pdf_bytes: bytes, filename: str = "") -> list[dict]:
    """
    Конвертирует PDF документ в список base64-кодированных изображений.
    Каждая страница PDF преобразуется в JPEG изображение с увеличением в 2 раза,
    затем кодируется в base64 и форматируется как data URL.

    Args:
        pdf_bytes: Байты PDF файла для конвертации
        filename: Имя файла для логирования (опционально)

    Returns:
        Список словарей в формате:
        [{"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,..."}}, ...]

    Raises:
        Exception: Если не удалось открыть или обработать PDF файл
    """
    image_blocks = []
    try:
        pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            mat = fitz.Matrix(2.0, 2.0)
            pix = page.get_pixmap(matrix=mat, alpha=False)

            img_data = pix.tobytes("jpeg")
            pil_img = Image.open(io.BytesIO(img_data))

            buffered = io.BytesIO()
            pil_img.save(buffered, format="JPEG")
            b64_content = base64.b64encode(buffered.getvalue()).decode("utf-8")
            data_url = f"data:image/jpeg;base64,{b64_content}"

            image_blocks.append({"type": "image_url", "image_url": {"url": data_url}})
        pdf_document.close()
        logger.info(f"PDF converted: {filename} ({len(image_blocks)} pages)")
    except Exception as e:
        logger.error(f"Failed to convert PDF {filename} to images: {e}")
        raise

    return image_blocks


async def process_files(file_urls: list[dict], openwebui_host: str, openwebui_token: str) -> list[dict]:
    """
    Асинхронно обрабатывает список файлов: загружает каждый файл по URL
    и конвертирует PDF в base64-кодированные изображения.

    Args:
        file_urls: Список словарей с информацией о файлах.
                   Каждый словарь должен содержать ключи 'url' и 'name'
        openwebui_host: Базовый URL хоста OpenWebUI
        openwebui_token: Токен авторизации для доступа к API OpenWebUI

    Returns:
        Список блоков изображений в формате для messages API.
        Если токен не установлен, возвращает пустой список.
        Ошибки при обработке отдельных файлов логируются, но не прерывают обработку.
    """
    if not openwebui_token:
        logger.warning("OPENWEBUI_API_KEY not set — skipping file download")
        return []

    headers = {"Authorization": f"Bearer {openwebui_token}"}
    all_image_blocks = []

    for file_meta in file_urls:
        url = f"{openwebui_host}{file_meta['url']}/content"
        filename = file_meta.get("name", "unknown")
        try:
            content = await download_file(url, headers)
            image_blocks = pdf_to_base64_images(content, filename)
            all_image_blocks.extend(image_blocks)
        except Exception as e:
            logger.error(f"Exception processing file {filename}: {e}")

    return all_image_blocks
