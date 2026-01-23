import base64
import io
import logging
import os
import sys

import aiohttp
import fitz
from PIL import Image

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

import json
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Union

from langchain_openai import ChatOpenAI
from ocr_utils.config import AppConfig
from ocr_utils.schemas import parser
from pydantic import BaseModel


class Pipeline:
    class Valves(BaseModel):
        VLM_API_URL: str
        VLM_API_KEY: str
        VLM_MODEL_NAME: str
        OPENWEBUI_API_KEY: str
        OPENWEBUI_HOST: str

    def __init__(self):
        self.name = "OCR Assistant"
        self.description = "Пайплайн OCR для OpenWebUI"
        self.config = AppConfig.from_yaml()
        self._files = []

        self.valves = self.Valves(
            **{
                "pipelines": ["*"],
                "VLM_API_URL": os.getenv("VLM_API_URL", self.config.vlm_api_url),
                "VLM_API_KEY": os.getenv("VLM_API_KEY", self.config.vlm_api_key),
                "VLM_MODEL_NAME": os.getenv("VLM_MODEL_NAME", self.config.vlm_model_name),
                "OPENWEBUI_API_KEY": os.getenv("OPENWEBUI_API_KEY", self.config.openwebui_token),
                "OPENWEBUI_HOST": os.getenv("OPENWEBUI_HOST", self.config.openwebui_host),
            }
        )

    async def on_startup(self):
        """Вызывается при запуске пайплайна."""
        logger.info("OCR Assistant starting up...")

    async def on_shutdown(self):
        """Вызывается при остановке пайплайна."""
        logger.info("OCR Assistant shutting down...")

    def _invoke_vlm(self, messages: list[str] | None) -> str:
        """Выполняет OCR через VLM и возвращает результат"""

        llm = ChatOpenAI(
            base_url=self.valves.VLM_API_URL,
            api_key=self.valves.VLM_API_KEY,
            model=self.valves.VLM_MODEL_NAME,
            temperature=self.config.temperature,
            presence_penalty=self.config.presence_penalty,
            extra_body={"repetition_penalty": self.config.repetition_penalty},
        )
        logger.info(f"LLM info: {llm}")
        resp = llm.invoke(messages)
        result = parser.invoke(resp)
        logger.info("VLM invocation completed.")
        return result

    async def inlet(self, body: dict, user: dict) -> dict:
        """Modifies form data before the OpenAI API request."""
        logger.info("Processing inlet request")

        messages = body.get("messages", [])
        files = body.get("files", [])

        if files:
            valid_files = [
                f
                for f in files
                if f.get("file", {}).get("data", {}).get("status") == "completed"
                and f.get("file", {}).get("meta", {}).get("content_type") == "application/pdf"
            ]

            if not self.valves.OPENWEBUI_API_KEY:
                logger.warning("OPENWEBUI_API_KEY not set — skipping file download")
            else:
                headers = {"Authorization": f"Bearer {self.valves.OPENWEBUI_API_KEY}"}
                image_blocks = []

                async with aiohttp.ClientSession() as session:
                    for file_meta in valid_files:
                        url = f"{self.valves.OPENWEBUI_HOST}{file_meta['url']}/content"
                        filename = file_meta["name"]
                        try:
                            async with session.get(url, headers=headers) as resp:
                                if resp.status == 200:
                                    content = await resp.read()
                                    logger.info(f"Downloaded PDF: {filename} ({len(content)} bytes)")

                                    try:
                                        pdf_document = fitz.open(stream=content, filetype="pdf")
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
                                        logger.info(f"PDF converted: {filename}")
                                    except Exception as e:
                                        logger.error(f"Failed to convert PDF {filename} to images: {e}")
                                else:
                                    error_text = await resp.text()
                                    logger.error(f"Failed to download {filename}: HTTP {resp.status} – {error_text}")
                        except Exception as e:
                            logger.error(f"Exception downloading {filename}: {e}")

                if image_blocks:
                    last_user_msg_index = None
                    for i in range(len(messages) - 1, -1, -1):
                        if messages[i].get("role") == "user":
                            last_user_msg_index = i
                            break

                    if last_user_msg_index is not None:
                        original_content = messages[last_user_msg_index].get("content", "")
                        new_content = []
                        if isinstance(original_content, str) and original_content.strip():
                            new_content.append({"type": "text", "text": original_content})
                        new_content.extend(image_blocks)
                        messages[last_user_msg_index]["content"] = new_content
                    else:
                        messages.append({"role": "user", "content": image_blocks})

        body["messages"] = messages
        try:
            current_dir = Path(__file__).parent.resolve()
            dump_dir = current_dir / "inlet_dumps"
            dump_dir.mkdir(exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
            filepath = dump_dir / f"dump_{timestamp}.json"

            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(body, f, ensure_ascii=False, indent=2)

            logger.info(f"Saved inlet body to {filepath}")
        except Exception as e:
            logger.error(f"Failed to save inlet body: {e}")

        return body

    async def outlet(self, body: dict, user: Optional[dict] = None) -> dict:
        pass

    def pipe(self, user_message: str, model_id: str, messages: List[dict], body: dict) -> Union[str, dict]:
        logger.info("=== Starting OCR pipeline ===")

        try:
            result = self._invoke_vlm(messages)
            logger.info("=== OCR pipeline completed ===")
            return result

        except ValueError as e:
            logger.exception("Validation error during processing")
            return f"Ошибка валидации: {str(e)}"
        except Exception as e:
            logger.exception("Unexpected error in OCR pipeline")
            return f"Внутренняя ошибка обработки: {str(e)}"
