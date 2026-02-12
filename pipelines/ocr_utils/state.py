from typing import Any, List, Optional, Set, TypedDict


class DocumentProcessingState(TypedDict, total=False):
    """
    Состояние графа обработки входящего запроса.
    """

    body: dict[str, Any]

    user_id: Optional[str]
    chat_id: Optional[str]
    current_message_id: Optional[str]
    files: List[dict[str, Any]]
    messages: List[dict[str, Any]]

    processed_file_ids: Set[str]
    file_cache_session: dict[str, Any]

    new_files: List[dict[str, Any]]
    use_paddle_ocr: bool
    errors: List[str]
