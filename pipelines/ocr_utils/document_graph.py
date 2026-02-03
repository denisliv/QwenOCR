"""
Граф обработки документов на LangGraph.
Узлы реализуют этапы inlet: валидация, определение новых файлов, выбор метода, обработка, обновление сообщений.
"""

import logging
from typing import Literal

from langgraph.graph import END, StateGraph

from ocr_utils.file_utils import process_pdf_to_base64_images
from ocr_utils.state import DocumentProcessingState

logger = logging.getLogger(__name__)


def _validate_input_node(state: DocumentProcessingState) -> dict:
    """Извлекает user_id, chat_id, files, messages из body/user; при ошибке помечает skip."""
    body = state.get("body") or {}
    user = state.get("user") or {}
    metadata = body.get("metadata", {})
    updates: dict = {
        "user_id": metadata.get("user_id") or user.get("id"),
        "chat_id": metadata.get("chat_id"),
        "current_message_id": metadata.get("message_id"),
        "files": body.get("files", []),
        "messages": body.get("messages", []),
    }
    if not updates["user_id"] or not updates["chat_id"]:
        logger.warning("Missing user_id or chat_id, skipping file processing")
        updates["skip_processing"] = True
    return updates


def _detect_new_files_node(state: DocumentProcessingState) -> dict:
    """Определяет новые PDF-файлы и добавляет их в new_files и в processed_file_ids."""
    files = state.get("files") or []
    processed_file_ids = state.get("processed_file_ids")
    current_message_id = state.get("current_message_id")
    message_order = state.get("message_order") or []

    pdf_valid = [
        f
        for f in files
        if (f.get("file") or {}).get("meta", {}).get("content_type") == "application/pdf"
    ]

    new_files = []
    for f in pdf_valid:
        file_id = f.get("id") or (f.get("file") or {}).get("id")
        if file_id and (processed_file_ids is None or file_id not in processed_file_ids):
            new_files.append({
                "url": f["url"],
                "name": f.get("name", "unknown.pdf"),
                "id": file_id,
            })
            if processed_file_ids is not None:
                processed_file_ids.add(file_id)
            logger.info(f"New file detected: {f.get('name', 'unknown.pdf')} (id: {file_id})")

    if new_files and current_message_id and current_message_id not in message_order:
        message_order.append(current_message_id)
        logger.info(f"Added message_id {current_message_id} to order cache")

    return {"new_files": new_files}


def _choose_method_node(state: DocumentProcessingState, *, pipeline) -> dict:
    """Определяет использование PaddleOCR из настроек (valves)."""
    use_paddle_ocr = getattr(pipeline.valves, "USING_PADDLEOCR", False)
    return {"use_paddle_ocr": use_paddle_ocr}


def _route_new_files(state: DocumentProcessingState) -> Literal["has_new_files", "no_new_files"]:
    """Маршрут: есть ли новые файлы и нужно ли их обрабатывать."""
    if state.get("skip_processing"):
        return "no_new_files"
    new_files = state.get("new_files") or []
    current_message_id = state.get("current_message_id")
    if not new_files or not current_message_id:
        return "no_new_files"
    return "has_new_files"


def _route_processing_method(state: DocumentProcessingState) -> Literal["paddleocr", "vlm"]:
    """Маршрут: PaddleOCR или VLM."""
    return "paddleocr" if state.get("use_paddle_ocr") else "vlm"


async def _process_paddleocr_node(
    state: DocumentProcessingState, *, pipeline
) -> dict:
    """Обрабатывает новые файлы через PaddleOCR (с fallback на VLM при ошибке)."""
    new_files = state.get("new_files") or []
    current_message_id = state.get("current_message_id")
    file_cache_session = state.get("file_cache_session") or {}
    if not new_files or not current_message_id:
        return {}
    await pipeline._process_files_with_paddleocr(
        new_files, current_message_id, file_cache_session
    )
    return {}


async def _process_vlm_node(
    state: DocumentProcessingState, *, pipeline
) -> dict:
    """Обрабатывает новые файлы как base64-изображения для VLM."""
    new_files = state.get("new_files") or []
    current_message_id = state.get("current_message_id")
    file_cache_session = state.get("file_cache_session") or {}
    if not new_files or not current_message_id:
        return {}
    files_images = await process_pdf_to_base64_images(
        new_files,
        pipeline.valves.OPENWEBUI_HOST,
        pipeline.valves.OPENWEBUI_API_KEY,
        pipeline.config.dpi,
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
    return {}


def _cache_results_node(state: DocumentProcessingState) -> dict:
    """Обновляет порядок сообщений после обработки (current_message_id, order_from_messages)."""
    current_message_id = state.get("current_message_id")
    message_order = state.get("message_order") or []
    messages = state.get("messages") or []

    if current_message_id and current_message_id not in message_order:
        message_order.append(current_message_id)

    order_from_messages = [
        m["id"] for m in messages if m.get("role") == "user" and m.get("id")
    ]
    if order_from_messages:
        message_order.clear()
        message_order.extend(order_from_messages)

    return {}


def _update_messages_node(state: DocumentProcessingState, *, pipeline) -> dict:
    """Подставляет в сообщения изображения/OCR и имена файлов, записывает body['messages']."""
    body = state.get("body") or {}
    messages = state.get("messages") or []
    file_cache_session = state.get("file_cache_session") or {}
    message_order = state.get("message_order") or []

    # Повторяем логику cache_results на случай перехода no_new_files → update_messages
    current_message_id = state.get("current_message_id")
    if current_message_id and current_message_id not in message_order:
        message_order.append(current_message_id)
    order_from_messages = [
        m["id"] for m in messages if m.get("role") == "user" and m.get("id")
    ]
    if order_from_messages:
        message_order.clear()
        message_order.extend(order_from_messages)

    updated = pipeline._update_messages_with_files(
        messages, file_cache_session, message_order
    )
    body["messages"] = updated
    return {"body": body}


def create_processing_graph(pipeline):
    """
    Собирает и компилирует граф обработки документов для inlet.

    Args:
        pipeline: экземпляр Pipeline (для доступа к valves, config, кэшам и методам).

    Returns:
        Скомпилированный CompiledStateGraph.
    """
    workflow = StateGraph(DocumentProcessingState)

    workflow.add_node("validate_input", _validate_input_node)
    workflow.add_node("detect_new_files", _detect_new_files_node)
    workflow.add_node(
        "choose_processing_method",
        lambda s: _choose_method_node(s, pipeline=pipeline),
    )
    workflow.add_node(
        "process_with_paddleocr",
        lambda s: _process_paddleocr_node(s, pipeline=pipeline),
    )
    workflow.add_node(
        "process_with_vlm",
        lambda s: _process_vlm_node(s, pipeline=pipeline),
    )
    workflow.add_node("cache_results", _cache_results_node)
    workflow.add_node(
        "update_messages",
        lambda s: _update_messages_node(s, pipeline=pipeline),
    )

    workflow.set_entry_point("validate_input")
    workflow.add_edge("validate_input", "detect_new_files")
    workflow.add_conditional_edges(
        "detect_new_files",
        _route_new_files,
        {
            "has_new_files": "choose_processing_method",
            "no_new_files": "update_messages",
        },
    )
    workflow.add_conditional_edges(
        "choose_processing_method",
        _route_processing_method,
        {
            "paddleocr": "process_with_paddleocr",
            "vlm": "process_with_vlm",
        },
    )
    workflow.add_edge("process_with_paddleocr", "cache_results")
    workflow.add_edge("process_with_vlm", "cache_results")
    workflow.add_edge("cache_results", "update_messages")
    workflow.add_edge("update_messages", END)

    return workflow.compile()
