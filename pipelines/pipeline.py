import gc
import logging
import os
import sys
from pathlib import Path

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

from typing import Generator, List, Optional, Union

from langchain_openai import ChatOpenAI
from ocr_utils.config import AppConfig
from ocr_utils.file_utils import (
    download_pdfs_to_temp_paths,
    process_pdf_to_base64_images,
)
from ocr_utils.markdown_utils import html_to_markdown_with_tables
from ocr_utils.prompts import SYSTEM_PROMPT
from paddleocr import PaddleOCRVL
from pydantic import BaseModel

from pipelines.ocr_utils.schemas import parser


class Pipeline:
    """
    Pipeline для OpenWebUI, обеспечивающий работу с VLM и опционально PaddleOCR для PDF.

    - USING_PADDLEOCR=False: PDF/Image/Text → VLM (изображения как base64).
    - USING_PADDLEOCR=True, только текст или изображение: Image/Text → VLM (изображения как base64).
    - USING_PADDLEOCR=True, PDF: OCR через PaddleOCR → Markdown → VLM.
      При ошибке PaddleOCR — fallback на VLM с base64-изображениями.
    """

    class Valves(BaseModel):
        VLM_API_URL: str
        VLM_API_KEY: str
        VLM_MODEL_NAME: str
        USING_PADDLEOCR: bool
        VL_REC_BACKEND: str
        VL_REC_SERVER_URL: str
        VL_REC_MODEL_NAME: str
        OPENWEBUI_HOST: str
        OPENWEBUI_API_KEY: str

    def __init__(self):
        self.name = "VisualOCR-Ассистент"
        self.description = "Пайплайн VisualOCR для OpenWebUI"
        self.config = AppConfig.from_yaml()
        self.vlm = None
        # Кэш изображений/OCR и метаданных: {user_id: {chat_id: {file_id: {message_id: str, filename: str, images?: list[dict], ocr_markdown?: str}}}}}
        self._file_cache = {}
        # Кэш обработанных file_id для быстрой проверки: {user_id: {chat_id: set([file_id1, file_id2, ...])}}
        self._processed_files_cache = {}
        # Порядок появления message_id для правильного сопоставления с сообщениями: {user_id: {chat_id: [message_id1, message_id2, ...]}}
        self._message_order_cache = {}

        self.valves = self.Valves(
            **{
                "pipelines": ["*"],
                "VLM_API_URL": os.getenv("VLM_API_URL", self.config.vlm_api_url),
                "VLM_API_KEY": os.getenv("VLM_API_KEY", self.config.vlm_api_key),
                "VLM_MODEL_NAME": os.getenv("VLM_MODEL_NAME", self.config.vlm_model_name),
                "USING_PADDLEOCR": os.getenv("USING_PADDLEOCR", self.config.using_paddleocr),
                "VL_REC_BACKEND": os.getenv("VL_REC_BACKEND", self.config.vl_rec_backend),
                "VL_REC_SERVER_URL": os.getenv("VL_REC_SERVER_URL", self.config.vl_rec_server_url),
                "VL_REC_MODEL_NAME": os.getenv("VL_REC_MODEL_NAME", self.config.vl_rec_model_name),
                "OPENWEBUI_HOST": os.getenv("OPENWEBUI_HOST", self.config.openwebui_host),
                "OPENWEBUI_API_KEY": os.getenv("OPENWEBUI_API_KEY", self.config.openwebui_token),
            }
        )

    async def on_startup(self):
        logger.info(f"{self.name} starting up...")
        self.vlm = ChatOpenAI(
            base_url=self.valves.VLM_API_URL,
            api_key=self.valves.VLM_API_KEY,
            model=self.valves.VLM_MODEL_NAME,
            temperature=self.config.temperature,
            presence_penalty=self.config.presence_penalty,
            extra_body={"repetition_penalty": self.config.repetition_penalty},
        )
        logger.info(f"LLM {self.valves.VLM_MODEL_NAME} started")

    async def on_shutdown(self):
        logger.info(f"{self.name} shutting down...")

    def _invoke_vlm(self, messages: Optional[List[dict]], stream: bool = False) -> Union[str, Generator[str, None, None]]:
        """
        Выполняет вызов VLM модели для обработки сообщений.
        В обычном режиме возвращает строку, в stream-режиме — генератор токенов.

        Args:
            messages: Список сообщений для обработки VLM моделью
            stream: True или False

        Returns:
            В обычном режиме: строка с результатом обработки от VLM модели.
            В stream-режиме: генератор, по которому можно итерироваться для получения токенов.
        """
        if not stream:
            logger.info("Starting VLM invocation")
            try:
                resp = self.vlm.invoke(messages)
                result = parser.invoke(resp)
                logger.info("VLM invocation completed")
                return result
            except Exception as e:
                logger.exception("Error during VLM invocation")
                error_text = str(e)
                if "decoder prompt" in error_text and "maximum model length" in error_text:
                    return (
                        "Ошибка: Превышен максимально допустимый размер контекста для используемой модели. "
                        "Пожалуйста, начните новый чат или сократите текст текущего запроса."
                    )
                return f"Ошибка: {error_text}"

        def _stream() -> Generator[str, None, None]:
            logger.info("Starting VLM streaming invocation")
            try:
                for chunk in self.vlm.stream(messages):
                    text = getattr(chunk, "content", None)
                    if isinstance(text, str) and text:
                        yield text
            except Exception as e:
                logger.exception("Error during VLM streaming invocation")
                error_text = str(e)
                if "decoder prompt" in error_text and "maximum model length" in error_text:
                    yield (
                        "Ошибка: Превышен максимально допустимый размер контекста для используемой модели. "
                        "Пожалуйста, начните новый чат или сократите текст текущего запроса."
                    )
                else:
                    yield f"Ошибка: {error_text}"
            finally:
                logger.info("VLM streaming invocation completed")

        return _stream()

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
        chat_id = metadata.get("chat_id")
        current_message_id = metadata.get("message_id")

        if not user_id or not chat_id:
            logger.warning("Missing user_id or chat_id, skipping file processing")
            return body

        if user_id not in self._processed_files_cache:
            self._processed_files_cache[user_id] = {}
        if chat_id not in self._processed_files_cache[user_id]:
            self._processed_files_cache[user_id][chat_id] = set()

        if user_id not in self._file_cache:
            self._file_cache[user_id] = {}
        if chat_id not in self._file_cache[user_id]:
            self._file_cache[user_id][chat_id] = {}

        if user_id not in self._message_order_cache:
            self._message_order_cache[user_id] = {}
        if chat_id not in self._message_order_cache[user_id]:
            self._message_order_cache[user_id][chat_id] = []

        processed_file_ids = self._processed_files_cache[user_id][chat_id]
        file_cache_session = self._file_cache[user_id][chat_id]
        message_order = self._message_order_cache[user_id][chat_id]

        if files:
            pdf_valid_files = [f for f in files if f.get("file", {}).get("meta", {}).get("content_type") == "application/pdf"]

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

            if new_files and current_message_id:
                logger.info(f"Processing {len(new_files)} new file(s) for message_id: {current_message_id}")

                if current_message_id not in message_order:
                    message_order.append(current_message_id)
                    logger.info(f"Added message_id {current_message_id} to order cache")

                use_paddle_ocr = getattr(self.valves, "USING_PADDLEOCR", False)
                if use_paddle_ocr:
                    temp_paths = []
                    try:
                        temp_paths = await download_pdfs_to_temp_paths(
                            new_files,
                            self.valves.OPENWEBUI_HOST,
                            self.valves.OPENWEBUI_API_KEY,
                        )
                        if not temp_paths:
                            raise ValueError("No temp paths after download")
                        ocr = PaddleOCRVL(
                            vl_rec_backend=self.valves.VL_REC_BACKEND,
                            vl_rec_server_url=self.valves.VL_REC_SERVER_URL,
                            vl_rec_model_name=self.valves.VL_REC_MODEL_NAME,
                            layout_detection_model_name=self.config.layout_detection_model_name,
                            layout_detection_model_dir=self.config.layout_detection_model_dir,
                            doc_orientation_classify_model_name=self.config.doc_orientation_classify_model_name,
                            doc_orientation_classify_model_dir=self.config.doc_orientation_classify_model_dir,
                            use_doc_orientation_classify=self.config.use_doc_orientation_classify,
                            use_doc_unwarping=self.config.use_doc_unwarping,
                            use_layout_detection=self.config.use_layout_detection,
                            layout_threshold=self.config.layout_threshold,
                            layout_nms=self.config.layout_nms,
                            layout_unclip_ratio=self.config.layout_unclip_ratio,
                            layout_merge_bboxes_mode=self.config.layout_merge_bboxes_mode,
                        )
                        logger.info("PaddleOCRVL started for PDF OCR")
                        for file_meta, input_path in zip(new_files, temp_paths):
                            file_id = file_meta["id"]
                            filename = file_meta["name"]
                            output = ocr.predict(input=input_path)
                            all_md = []
                            for res in output:
                                all_md.append(res.markdown)
                            final_html = ocr.concatenate_markdown_pages(all_md)
                            ocr_markdown = html_to_markdown_with_tables(final_html)
                            file_cache_session[file_id] = {
                                "message_id": current_message_id,
                                "filename": filename,
                                "ocr_markdown": ocr_markdown,
                            }
                            logger.info(f"Cached OCR result for {filename} (id: {file_id}) for message_id: {current_message_id}")
                        del ocr
                        gc.collect()
                    except Exception as e:
                        logger.warning(
                            "PaddleOCR failed, falling back to VLM with base64 images: %s",
                            e,
                        )
                        files_images = await process_pdf_to_base64_images(
                            new_files,
                            self.valves.OPENWEBUI_HOST,
                            self.valves.OPENWEBUI_API_KEY,
                            self.config.dpi,
                        )
                        for file_meta in new_files:
                            file_id = file_meta["id"]
                            filename = file_meta["name"]
                            image_blocks = files_images.get(file_id, [])
                            file_cache_session[file_id] = {
                                "message_id": current_message_id,
                                "filename": filename,
                                "images": image_blocks,
                            }
                            logger.info(
                                f"Cached file {filename} (id: {file_id}) for message_id: {current_message_id} with {len(image_blocks)} images"
                            )
                    finally:
                        for p in temp_paths:
                            Path(p).unlink(missing_ok=True)
                else:
                    files_images = await process_pdf_to_base64_images(
                        new_files,
                        self.valves.OPENWEBUI_HOST,
                        self.valves.OPENWEBUI_API_KEY,
                        self.config.dpi,
                    )
                    for file_meta in new_files:
                        file_id = file_meta["id"]
                        filename = file_meta["name"]
                        image_blocks = files_images.get(file_id, [])
                        file_cache_session[file_id] = {
                            "message_id": current_message_id,
                            "filename": filename,
                            "images": image_blocks,
                        }
                        logger.info(
                            f"Cached file {filename} (id: {file_id}) for message_id: {current_message_id} with {len(image_blocks)} images"
                        )

        if current_message_id and current_message_id not in message_order:
            message_order.append(current_message_id)

        order_from_messages = [m["id"] for m in messages if m.get("role") == "user" and m.get("id")]
        if order_from_messages:
            message_order = order_from_messages

        updated_messages = self._update_messages_with_files(messages, file_cache_session, message_order)
        body["messages"] = updated_messages

        return body

    def _update_messages_with_files(self, messages: List[dict], file_cache: dict, message_order: List[str]) -> List[dict]:
        """
        Обновляет все сообщения пользователя, добавляя изображения/результат ocr и имена файлов
        к соответствующим сообщениям на основе кэша файлов и порядка появления message_id.

        Args:
            messages: Список сообщений
            file_cache: Кэш файлов для текущей сессии {file_id: {message_id, filename, images/ocr_markdown}}
            message_order: Список message_id в порядке их появления

        Returns:
            Обновленный список сообщений
        """
        files_by_message = {}
        for file_id, file_data in file_cache.items():
            msg_id = file_data["message_id"]
            if msg_id not in files_by_message:
                files_by_message[msg_id] = []
            files_by_message[msg_id].append(
                {
                    "file_id": file_id,
                    "filename": file_data.get("filename"),
                    "images": file_data.get("images"),
                    "ocr_markdown": file_data.get("ocr_markdown"),
                }
            )

        user_message_index = 0
        updated_messages = []

        for msg in messages:
            if msg.get("role") != "user":
                updated_messages.append(msg)
                continue

            msg_content = msg.get("content", "")

            user_text = ""
            existing_images = []
            existing_file_names = set()

            if isinstance(msg_content, str):
                user_text = msg_content.strip()
            elif isinstance(msg_content, list):
                text_parts = []
                for item in msg_content:
                    if isinstance(item, dict):
                        if item.get("type") == "text":
                            text = item.get("text", "")
                            text_parts.append(text)
                            if "Имя файла:" in text:
                                for line in text.split("\n"):
                                    if "Имя файла:" in line:
                                        filename = line.split("Имя файла:")[-1].strip()
                                        if filename:
                                            existing_file_names.add(filename)
                        elif item.get("type") == "image_url":
                            existing_images.append(item)
                user_text = "\n".join(text_parts).strip()

            new_content = []

            if user_text:
                new_content.append({"type": "text", "text": user_text})

            msg_id = msg.get("id")
            if msg_id is not None:
                files_for_this_message = files_by_message.get(msg_id, [])
            elif user_message_index < len(message_order):
                target_message_id = message_order[user_message_index]
                files_for_this_message = files_by_message.get(target_message_id, [])
            else:
                files_for_this_message = []

            ocr_parts = [(f["filename"], f["ocr_markdown"]) for f in files_for_this_message if f.get("ocr_markdown")]
            has_images_from_cache = any(f.get("images") for f in files_for_this_message)
            has_any_images = has_images_from_cache or bool(existing_images)

            if ocr_parts:
                mode_block = "[MODE: OCR_POSTPROCESS]\n\n" + "\n\n".join("Имя файла: " + fn + "\n\n" + md for fn, md in ocr_parts)
                new_content.append({"type": "text", "text": mode_block})
                for fn, _ in ocr_parts:
                    existing_file_names.add(fn)

                for file_info in files_for_this_message:
                    images = file_info.get("images")
                    if not images:
                        continue
                    filename = file_info["filename"]
                    if filename not in existing_file_names:
                        new_content.append({"type": "text", "text": f"Имя файла: {filename}"})
                        existing_file_names.add(filename)
                    new_content.extend(images)
                new_content.extend(existing_images)
            elif has_any_images:
                new_content.append({"type": "text", "text": "[MODE: VISION_ANALYSIS]\n\n"})
                for file_info in files_for_this_message:
                    images = file_info.get("images")
                    if not images:
                        continue
                    filename = file_info["filename"]
                    if filename not in existing_file_names:
                        new_content.append({"type": "text", "text": f"Имя файла: {filename}"})
                        existing_file_names.add(filename)
                    new_content.extend(images)
                new_content.extend(existing_images)
            else:
                new_content.append({"type": "text", "text": "[MODE: TEXT_ONLY]\n\n"})
                new_content.extend(existing_images)

            updated_msg = {
                **msg,
                "content": new_content,
            }
            updated_messages.append(updated_msg)
            user_message_index += 1

        return updated_messages

    @staticmethod
    def _strip_task_context_from_message(text: str) -> str:
        """
        Удаляет служебный префикс OpenWebUI/агента, если сообщение начинается с "### Task:"
        и содержит закрывающий тег "</context>".
        """
        if not isinstance(text, str) or not text:
            return text

        normalized = text.replace("\r\n", "\n").lstrip()
        if not (normalized.startswith("### Task:") and "</context>" in normalized):
            return text.strip()

        user_query = normalized.split("</context>", 1)[1].lstrip()
        lines = user_query.split("\n")
        cleaned_lines: list[str] = []
        for line in lines:
            if line.strip() or cleaned_lines:
                cleaned_lines.append(line)
        return "\n".join(cleaned_lines).rstrip()

    async def outlet(self, body: dict, user: Optional[dict] = None) -> dict:
        """
        Обрабатывает исходящий ответ после получения результата от API.
        """
        return body

    def pipe(self, user_message: str, model_id: str, messages: List[dict], body: dict) -> Union[str, Generator[str, None, None]]:
        """
        Основной метод обработки запроса через пайплайн.
        Выполняет вызов VLM модели с подготовленными сообщениями.

        Args:
            user_message: Сообщение пользователя
            model_id: Идентификатор модели
            messages: Список сообщений для обработки
            body: Тело запроса

        Returns:
            В обычном режиме: строка с результатом обработки от VLM модели или сообщение об ошибке.
            В stream-режиме: генератор строк (токенов/фрагментов), совместимый с OpenWebUI Pipelines.
        """
        logger.info("Starting OCR pipeline")
        try:
            for msg in reversed(messages):
                if msg.get("role") != "user":
                    continue
                content = msg.get("content")
                if isinstance(content, str):
                    msg["content"] = self._strip_task_context_from_message(content)
                elif isinstance(content, list):
                    for item in content:
                        if isinstance(item, dict) and item.get("type") == "text" and isinstance(item.get("text"), str):
                            item["text"] = self._strip_task_context_from_message(item["text"])
                break

            has_system_message = any(msg.get("role") == "system" for msg in messages)
            if not has_system_message:
                messages.insert(0, {"role": "system", "content": SYSTEM_PROMPT})

            stream = bool(body.get("stream"))

            if stream:
                logger.info("Streaming mode enabled for OCR pipeline")
                result_gen = self._invoke_vlm(messages, stream=True)
                body["messages"] = messages
                return result_gen

            result = self._invoke_vlm(messages, stream=False)
            body["messages"] = messages
            logger.info("OCR pipeline completed successfully")
            return result

        except ValueError as e:
            logger.exception("Validation error during processing")
            return f"Ошибка: {str(e)}"
        except Exception as e:
            logger.exception("Unexpected error in OCR pipeline")
            return f"Ошибка: {str(e)}"
