import logging
import os
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s in %(name)s: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

pipelines_dir = os.path.dirname(__file__)
if pipelines_dir not in sys.path:
    sys.path.insert(0, pipelines_dir)

from typing import List, Optional, Union

from langchain_openai import ChatOpenAI
from ocr_utils.config import AppConfig
from ocr_utils.file_utils import process_files
from ocr_utils.prompts import SYSTEM_PROMPT
from ocr_utils.schemas import parser
from pydantic import BaseModel


class Pipeline:
    """
    Pipeline для OpenWebUI, обеспечивающий работу с VLM моделью для анализа изображений и выполнения OCR.
    """

    class Valves(BaseModel):
        """
        Конфигурационные параметры пайплайна.

        Attributes:
            VLM_API_URL: URL API для VLM модели
            VLM_API_KEY: API ключ для VLM модели
            VLM_MODEL_NAME: Название VLM модели
            DPI: Желаемое разрешение изображений
            OPENWEBUI_API_KEY: API ключ для OpenWebUI
            OPENWEBUI_HOST: Хост OpenWebUI
        """

        VLM_API_URL: str
        VLM_API_KEY: str
        VLM_MODEL_NAME: str
        DPI: int
        OPENWEBUI_HOST: str
        OPENWEBUI_API_KEY: str

    def __init__(self):
        """
        Инициализирует Pipeline, загружает конфигурацию и настраивает параметры.
        """
        self.name = "OCR-Ассистент"
        self.description = "Пайплайн OCR для OpenWebUI"
        self.config = AppConfig.from_yaml()
        self.vlm = None
        # Кэш изображений и метаданных: {user_id: {session_id: {file_id: {message_id: str, filename: str, images: list[dict]}}}}
        self._file_cache = {}
        # Кэш обработанных file_id для быстрой проверки: {user_id: {session_id: set([file_id1, file_id2, ...])}}
        self._processed_files_cache = {}
        # Порядок появления message_id для правильного сопоставления с сообщениями: {user_id: {session_id: [message_id1, message_id2, ...]}}
        self._message_order_cache = {}

        self.valves = self.Valves(
            **{
                "pipelines": ["*"],
                "VLM_API_URL": os.getenv("VLM_API_URL", self.config.vlm_api_url),
                "VLM_API_KEY": os.getenv("VLM_API_KEY", self.config.vlm_api_key),
                "VLM_MODEL_NAME": os.getenv("VLM_MODEL_NAME", self.config.vlm_model_name),
                "DPI": os.getenv("DPI", self.config.dpi),
                "OPENWEBUI_HOST": os.getenv("OPENWEBUI_HOST", self.config.openwebui_host),
                "OPENWEBUI_API_KEY": os.getenv("OPENWEBUI_API_KEY", self.config.openwebui_token),
            }
        )

    async def on_startup(self):
        """
        Вызывается при запуске пайплайна.
        Выполняет инициализацию VLM и подготовку к работе.
        """
        logger.info("OCR Assistant starting up...")
        self.vlm = ChatOpenAI(
            base_url=self.valves.VLM_API_URL,
            api_key=self.valves.VLM_API_KEY,
            model=self.valves.VLM_MODEL_NAME,
            temperature=self.config.temperature,
            presence_penalty=self.config.presence_penalty,
            extra_body={"repetition_penalty": self.config.repetition_penalty},
        )
        logger.info("VLM started")

    async def on_shutdown(self):
        """
        Вызывается при остановке пайплайна.
        Выполняет очистку ресурсов и завершение работы.
        """
        logger.info("OCR Assistant shutting down...")

    def _invoke_vlm(self, messages: list[str] | None) -> str:
        """
        Выполняет вызов VLM модели для обработки сообщений и возвращает результат.

        Args:
            messages: Список сообщений для обработки VLM моделью

        Returns:
            Строка с результатом обработки от VLM модели
        """
        resp = self.vlm.invoke(messages)
        result = parser.invoke(resp)
        logger.info("VLM invocation completed")
        return result

    async def inlet(self, body: dict, user: dict) -> dict:
        """
        Обрабатывает входящий запрос перед отправкой в API.
        Определяет новые файлы, обрабатывает их, сохраняет в кэш с message_id,
        и обновляет все сообщения пользователя, добавляя изображения и имена файлов.

        Args:
            body: Тело запроса, содержащее информацию о файлах и сообщениях
            user: Информация о пользователе

        Returns:
            Тело запроса с обновленными сообщениями
        """
        logger.info("Processing inlet request")
        files = body.get("files", [])
        metadata = body.get("metadata", {})
        messages = body.get("messages", [])
        user_id = metadata.get("user_id") or user.get("id")
        session_id = metadata.get("session_id")
        current_message_id = metadata.get("message_id")

        if not user_id or not session_id:
            logger.warning("Missing user_id or session_id, skipping file processing")
            return body

        # Инициализируем кэши для пользователя и сессии, если нужно
        if user_id not in self._processed_files_cache:
            self._processed_files_cache[user_id] = {}
        if session_id not in self._processed_files_cache[user_id]:
            self._processed_files_cache[user_id][session_id] = set()

        if user_id not in self._file_cache:
            self._file_cache[user_id] = {}
        if session_id not in self._file_cache[user_id]:
            self._file_cache[user_id][session_id] = {}

        if user_id not in self._message_order_cache:
            self._message_order_cache[user_id] = {}
        if session_id not in self._message_order_cache[user_id]:
            self._message_order_cache[user_id][session_id] = []

        processed_file_ids = self._processed_files_cache[user_id][session_id]
        file_cache_session = self._file_cache[user_id][session_id]
        message_order = self._message_order_cache[user_id][session_id]

        # Определяем и обрабатываем новые файлы
        if files:
            pdf_valid_files = [
                f
                for f in files
                if f.get("file", {}).get("data", {}).get("status") == "completed"
                and f.get("file", {}).get("meta", {}).get("content_type") == "application/pdf"
            ]

            # Определяем новые файлы (те, которые еще не были обработаны)
            new_files = []
            for f in pdf_valid_files:
                file_id = f.get("id") or f.get("file", {}).get("id")
                if file_id and file_id not in processed_file_ids:
                    new_files.append(
                        {
                            "url": f["url"],
                            "name": f.get("name", "unknown.pdf"),
                            "id": file_id,
                        }
                    )
                    processed_file_ids.add(file_id)
                    logger.info(f"New file detected: {f.get('name', 'unknown.pdf')} (id: {file_id})")

            # Обрабатываем новые файлы и сохраняем в кэш
            if new_files and current_message_id:
                has_new_files = True
                logger.info(f"Processing {len(new_files)} new file(s) for message_id: {current_message_id}")
                files_images = await process_files(
                    new_files,
                    self.valves.OPENWEBUI_HOST,
                    self.valves.OPENWEBUI_API_KEY,
                    self.valves.DPI,
                )

                # Добавляем message_id в порядок появления, если его еще нет
                if current_message_id not in message_order:
                    message_order.append(current_message_id)
                    logger.info(f"Added message_id {current_message_id} to order cache")

                # Сохраняем каждый файл в кэш с текущим message_id
                for file_meta in new_files:
                    file_id = file_meta["id"]
                    filename = file_meta["name"]
                    # Получаем изображения для этого конкретного файла
                    image_blocks = files_images.get(file_id, [])
                    file_cache_entry = {
                        "message_id": current_message_id,
                        "filename": filename,
                        "images": image_blocks,
                    }
                    file_cache_session[file_id] = file_cache_entry
                    logger.info(f"Cached file {filename} (id: {file_id}) for message_id: {current_message_id} with {len(image_blocks)} images")

        # Обновляем все сообщения пользователя, добавляя изображения и имена файлов
        # Это нужно делать всегда, даже если нет новых файлов, чтобы восстановить изображения из кэша
        # (так как OpenWebUI заменяет историю на свою без прикрепленных изображений)
        updated_messages = self._update_messages_with_files(messages, file_cache_session, message_order)
        body["messages"] = updated_messages

        return body

    def _update_messages_with_files(self, messages: List[dict], file_cache: dict, message_order: List[str]) -> List[dict]:
        """
        Обновляет все сообщения пользователя, добавляя изображения и имена файлов
        к соответствующим сообщениям на основе кэша файлов и порядка появления message_id.

        Args:
            messages: Список сообщений
            file_cache: Кэш файлов для текущей сессии {file_id: {message_id, filename, images}}
            message_order: Список message_id в порядке их появления

        Returns:
            Обновленный список сообщений
        """
        # Создаем словарь для быстрого поиска файлов по message_id
        # {message_id: [{file_id, filename, images}, ...]}
        files_by_message = {}
        for file_id, file_data in file_cache.items():
            msg_id = file_data["message_id"]
            if msg_id not in files_by_message:
                files_by_message[msg_id] = []
            files_by_message[msg_id].append({
                "file_id": file_id,
                "filename": file_data["filename"],
                "images": file_data["images"],
            })

        # Отслеживаем порядковый номер сообщений пользователя для сопоставления с файлами
        user_message_index = 0
        updated_messages = []
        
        for msg in messages:
            if msg.get("role") != "user":
                updated_messages.append(msg)
                continue

            msg_content = msg.get("content", "")
            
            # Обрабатываем контент в зависимости от типа (логика очистки сообщений)
            user_text = ""
            existing_images = []
            existing_file_names = set()

            if isinstance(msg_content, str):
                content_normalized = msg_content.replace("\r\n", "\n").lstrip()
                if content_normalized.startswith("### Task:") and "</context>" in content_normalized:
                    user_query = content_normalized.split("</context>", 1)[1].lstrip()
                    lines = user_query.split("\n")
                    cleaned_lines = []
                    for line in lines:
                        if line.strip() or cleaned_lines:
                            cleaned_lines.append(line)
                    user_text = "\n".join(cleaned_lines).rstrip()
                else:
                    user_text = msg_content.strip()
            elif isinstance(msg_content, list):
                # Если контент уже список, извлекаем текстовые части и существующие изображения
                text_parts = []
                for item in msg_content:
                    if isinstance(item, dict):
                        if item.get("type") == "text":
                            text = item.get("text", "")
                            text_parts.append(text)
                            # Проверяем, есть ли уже имя файла в тексте
                            # Может быть несколько "Имя файла:" в одном тексте
                            if "Имя файла:" in text:
                                # Извлекаем все имена файлов из текста
                                for line in text.split("\n"):
                                    if "Имя файла:" in line:
                                        filename = line.split("Имя файла:")[-1].strip()
                                        if filename:
                                            existing_file_names.add(filename)
                        elif item.get("type") == "image_url":
                            existing_images.append(item)
                user_text = "\n".join(text_parts).strip()

            # Формируем новый контент
            new_content = []

            # Добавляем оригинальный текст пользователя, если есть
            if user_text:
                new_content.append({"type": "text", "text": user_text})

            # Определяем, какие файлы относятся к текущему сообщению пользователя
            # Используем порядковый номер сообщения пользователя и порядок появления message_id
            if user_message_index < len(message_order):
                target_message_id = message_order[user_message_index]
                files_for_this_message = files_by_message.get(target_message_id, [])
                
                # Добавляем имена файлов и изображения для файлов этого сообщения
                for file_info in files_for_this_message:
                    filename = file_info["filename"]
                    images = file_info["images"]
                    
                    # Добавляем имя файла, если его еще нет
                    if filename not in existing_file_names:
                        file_name_text = f"Имя файла: {filename}"
                        new_content.append({"type": "text", "text": file_name_text})
                        existing_file_names.add(filename)
                    
                    # Добавляем изображения для этого файла
                    new_content.extend(images)

            # Добавляем существующие изображения (если есть)
            new_content.extend(existing_images)

            updated_msg = {
                **msg,
                "content": new_content,
            }
            updated_messages.append(updated_msg)
            user_message_index += 1

        return updated_messages

    async def outlet(self, body: dict, user: Optional[dict] = None) -> dict:
        """
        Обрабатывает исходящий ответ после получения результата от API.
        """
        return body

    def pipe(self, user_message: str, model_id: str, messages: List[dict], body: dict) -> Union[str, dict]:
        """
        Основной метод обработки запроса через пайплайн.
        Выполняет только вызов VLM модели с подготовленными сообщениями.

        Args:
            user_message: Сообщение пользователя
            model_id: Идентификатор модели
            messages: Список сообщений для обработки (уже обновлены в inlet)
            body: Тело запроса

        Returns:
            Результат обработки от VLM модели или сообщение об ошибке
        """
        logger.info("Starting OCR pipeline")
        try:
            has_system_message = any(msg.get("role") == "system" for msg in messages)
            if not has_system_message:
                messages.insert(0, {"role": "system", "content": SYSTEM_PROMPT})

            result = self._invoke_vlm(messages)
            body["messages"] = messages
            logger.info("OCR pipeline completed successfully")
            return result

        except ValueError as e:
            logger.exception("Validation error during processing")
            return f"Validation error: {str(e)}"
        except Exception as e:
            logger.exception("Unexpected error in OCR pipeline")
            return f"Internal processing error: {str(e)}"
