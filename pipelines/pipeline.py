import asyncio
import logging
import os
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s in %(name)s: %(message)s"
    )
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
    Pipeline для OpenWebUI, обеспечивающий работу с VLM моделью для анализа изображений,
    ответов на вопросы по ним и выполнения OCR.
    """

    class Valves(BaseModel):
        """
        Конфигурационные параметры пайплайна.

        Attributes:
            VLM_API_URL: URL API для VLM модели
            VLM_API_KEY: API ключ для VLM модели
            VLM_MODEL_NAME: Название VLM модели
            OPENWEBUI_API_KEY: API ключ для OpenWebUI
            OPENWEBUI_HOST: Хост OpenWebUI
        """

        VLM_API_URL: str
        VLM_API_KEY: str
        VLM_MODEL_NAME: str
        OPENWEBUI_API_KEY: str
        OPENWEBUI_HOST: str

    def __init__(self):
        """
        Инициализирует Pipeline, загружает конфигурацию и настраивает параметры.
        """
        self.name = "OCR Assistant"
        self.description = "Пайплайн OCR для OpenWebUI"
        self.config = AppConfig.from_yaml()
        self.llm = None
        self._files = []

        self.valves = self.Valves(
            **{
                "pipelines": ["*"],
                "VLM_API_URL": os.getenv("VLM_API_URL", self.config.vlm_api_url),
                "VLM_API_KEY": os.getenv("VLM_API_KEY", self.config.vlm_api_key),
                "VLM_MODEL_NAME": os.getenv(
                    "VLM_MODEL_NAME", self.config.vlm_model_name
                ),
                "OPENWEBUI_API_KEY": os.getenv(
                    "OPENWEBUI_API_KEY", self.config.openwebui_token
                ),
                "OPENWEBUI_HOST": os.getenv(
                    "OPENWEBUI_HOST", self.config.openwebui_host
                ),
            }
        )

    async def on_startup(self):
        """
        Вызывается при запуске пайплайна.
        Выполняет инициализацию и подготовку к работе.
        """
        logger.info("OCR Assistant starting up...")
        self.llm = ChatOpenAI(
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
        resp = self.llm.invoke(messages)
        result = parser.invoke(resp)
        logger.info("VLM invocation completed")
        return result

    async def inlet(self, body: dict, user: dict) -> dict:
        """
        Обрабатывает входящий запрос перед отправкой в API.
        Извлекает URL прикрепленных PDF файлов и сохраняет их в self._files.

        Args:
            body: Тело запроса, содержащее информацию о файлах
            user: Информация о пользователе

        Returns:
            Исходное тело запроса без изменений
        """
        logger.info("Processing inlet request")

        files = body.get("files", [])

        if files:
            valid_files = [
                f
                for f in files
                if f.get("file", {}).get("data", {}).get("status") == "completed"
                and f.get("file", {}).get("meta", {}).get("content_type")
                == "application/pdf"
            ]

            self._files = [
                {"url": f["url"], "name": f.get("name", "unknown")} for f in valid_files
            ]
            if self._files:
                logger.info(f"Found {len(self._files)} valid PDF file(s)")

        return body

    async def outlet(self, body: dict, user: Optional[dict] = None) -> dict:
        """
        Обрабатывает исходящий ответ после получения результата от API.
        """
        self._files = []
        logger.info("Cleared files cache")
        return body

    def pipe(
        self, user_message: str, model_id: str, messages: List[dict], body: dict
    ) -> Union[str, dict]:
        """
        Основной метод обработки запроса через пайплайн.
        Загружает файлы из self._files, преобразует их в base64 изображения,
        формирует сообщения для VLM модели и выполняет OCR.

        Args:
            user_message: Сообщение пользователя
            model_id: Идентификатор модели
            messages: Список сообщений для обработки
            body: Тело запроса (не изменяется)

        Returns:
            Результат обработки от VLM модели или сообщение об ошибке
        """
        logger.info("Starting OCR pipeline")
        logger.info(f"Found in pipe: {self._files}")

        try:
            # Формируем новый messages для llm (логика формирования остается такой же - только если есть файлы)
            vlm_messages = messages.copy()

            # Добавляем системный промпт в начало списка сообщений
            # Проверяем, есть ли уже системное сообщение
            has_system_message = any(
                msg.get("role") == "system" for msg in vlm_messages
            )
            if not has_system_message:
                vlm_messages.insert(0, {"role": "system", "content": SYSTEM_PROMPT})
            else:
                # Если системное сообщение уже есть, заменяем его на наш промпт
                for i, msg in enumerate(vlm_messages):
                    if msg.get("role") == "system":
                        vlm_messages[i] = {"role": "system", "content": SYSTEM_PROMPT}
                        break

            if self._files:
                # Загружаем файлы и преобразуем в base64
                logger.info(f"Processing {len(self._files)} file(s)")
                image_blocks = asyncio.run(
                    process_files(
                        self._files,
                        self.valves.OPENWEBUI_HOST,
                        self.valves.OPENWEBUI_API_KEY,
                    )
                )

                if image_blocks:
                    logger.info(f"Generated {len(image_blocks)} image block(s)")
                    # Находим последнее сообщение пользователя
                    last_user_msg_index = None
                    for i in range(len(vlm_messages) - 1, -1, -1):
                        if vlm_messages[i].get("role") == "user":
                            last_user_msg_index = i
                            break

                    if last_user_msg_index is not None:
                        original_content = vlm_messages[last_user_msg_index].get(
                            "content", ""
                        )
                        new_content = []
                        if (
                            isinstance(original_content, str)
                            and original_content.strip()
                        ):
                            new_content.append(
                                {"type": "text", "text": original_content}
                            )
                        new_content.extend(image_blocks)
                        vlm_messages[last_user_msg_index] = {
                            **vlm_messages[last_user_msg_index],
                            "content": new_content,
                        }
                    else:
                        vlm_messages.append({"role": "user", "content": image_blocks})

            result = self._invoke_vlm(vlm_messages)
            logger.info("OCR pipeline completed successfully")
            return result

        except ValueError as e:
            logger.exception("Validation error during processing")
            return f"Validation error: {str(e)}"
        except Exception as e:
            logger.exception("Unexpected error in OCR pipeline")
            return f"Internal processing error: {str(e)}"
