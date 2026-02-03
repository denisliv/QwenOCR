"""
Состояние для графа обработки документов (LangGraph).
Используется в inlet-пайплайне для передачи данных между узлами.
"""

from typing import Any, List, Optional, Set, TypedDict


class DocumentProcessingState(TypedDict, total=False):
    """
    Состояние обработки входящего запроса с файлами и сообщениями.

    Все поля опциональны (total=False), т.к. заполняются по мере прохождения графа.
    Ссылки на кэши (processed_file_ids, file_cache_session, message_order) мутируются
    узлами на месте и привязаны к кэшам Pipeline.
    """

    # Исходные данные запроса (вход)
    body: dict[str, Any]
    user: dict[str, Any]

    # Извлечённые из body/user
    user_id: Optional[str]
    chat_id: Optional[str]
    current_message_id: Optional[str]
    files: List[dict[str, Any]]
    messages: List[dict[str, Any]]

    # Кэши сессии (те же ссылки, что в Pipeline; мутируются узлами)
    processed_file_ids: Set[str]
    file_cache_session: dict[str, Any]
    message_order: List[str]

    # Результаты этапов
    new_files: List[dict[str, Any]]
    use_paddle_ocr: bool
    skip_processing: bool
    errors: List[str]
