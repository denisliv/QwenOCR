
## VisualOCR — OCR-пайплайн PDF/Image → VLM для OpenWebUI

VisualOCR — это пайплайн для OpenWebUI, который принимает PDF‑файлы и изображения, распознаёт их содержимое с помощью `PaddleOCR-VL` (или конвертирует в base64), и передаёт результат в VLM (Vision‑Language Model, например `Qwen3-VL`) для анализа, ответов на вопросы и выполнения инструкций пользователя.

### Структура проекта

```
QwenOCR/
├── readme.md
├── requirements.txt
├── Dockerfile
├── .gitignore
├── fix_paddlex_imports.sh
└── pipelines/
    ├── pipeline.py                    # основной пайплайн (inlet → pipe → outlet, VLM)
    ├── PP-DocLayoutV2/                # модель детекции разметки страницы (PaddleOCR)
    ├── PP-LCNet_x1_0_doc_ori/         # модель классификации ориентации документа
    └── ocr_utils/
        ├── config.py                  # загрузка конфигурации из YAML (AppConfig)
        ├── config.yaml                # настройки VLM, PaddleOCR, OpenWebUI
        ├── state.py                   # состояние графа (DocumentProcessingState)
        ├── document_graph.py          # граф обработки документов для inlet (LangGraph)
        ├── file_utils.py              # скачивание PDF, конвертация в base64-изображения
        ├── markdown_utils.py          # конвертация HTML → markdown с таблицами
        ├── schemas.py                 # StrOutputParser для вывода VLM
        └── prompts/
            ├── __init__.py
            └── system_prompts.py      # системный промпт VLM-ассистента
```

### Общая схема работы

- **Вход в пайплайн (`inlet`)**
  - Из `body["files"]` берутся вложения с типом `application/pdf`.
  - Для каждого PDF формируется список `{url, name, id}`.
  - По `(user_id, chat_id)` ведётся кэш уже обработанных файлов, чтобы не скачивать и не обрабатывать один и тот же файл несколько раз.
  - Валидация входных данных (`user_id`, `chat_id`) выполняется в `inlet()` до запуска графа; при отсутствии ID граф не вызывается.
  - Вся логика обработки файлов реализована как граф `LangGraph` (`document_graph.py`), который последовательно выполняет:
    1. **detect_new_files** — фильтрует PDF-файлы, определяет ещё не обработанные, добавляет в `new_files` и `processed_file_ids`.
    2. **choose_processing_method** — определяет режим обработки по настройке `USING_PADDLEOCR`.
    3. **Условная маршрутизация**:
       - Если новых файлов нет — переход сразу к `update_messages`.
       - Если есть — маршрут в `process_with_paddleocr` или `process_with_vlm` в зависимости от `use_paddle_ocr`.
    4. **process_with_paddleocr** — PaddleOCR для PDF → markdown; при ошибке — fallback на base64-изображения.
    5. **process_with_vlm** — конвертация PDF в base64 PNG-изображения через PyMuPDF.
    6. **update_messages** — подставляет в `body["messages"]` OCR-markdown или base64-изображения с именами файлов к соответствующим пользовательским сообщениям (сопоставление файлов с сообщениями выполняется по позиции user-сообщения — `user_msg_index`).

- **Основная обработка (`pipe`)**
  - Из последнего пользовательского сообщения удаляется служебный префикс OpenWebUI (`### Task:` ... `</context>`).
  - Если в `messages` нет системного промпта — вставляется `SYSTEM_PROMPT` (роль универсального ассистента по работе с визуальным контентом).
  - Вызывается VLM через `ChatOpenAI` (OpenAI-совместимый API):
    - В обычном режиме — возвращается строка.
    - В stream-режиме — возвращается генератор токенов.
  - При превышении максимального размера контекста — возвращается информативное сообщение об ошибке.

- **Режимы обработки файлов**
  - **`USING_PADDLEOCR=False`**: PDF и изображения конвертируются в base64 PNG и передаются напрямую в VLM.
  - **`USING_PADDLEOCR=True`**:
    - **PDF**: PaddleOCR → markdown (HTML → markdown с таблицами); при ошибке — fallback на base64-изображения.
    - **Изображения**: передаются как base64 в VLM.
    - **Текст**: передаётся напрямую в VLM.

- **Завершение пайплайна (`outlet`)**
  - В текущей реализации `outlet` является pass-through и возвращает `body` без изменений.

### Конфигурация и окружение

- **Конфиг VLM и OCR (`AppConfig`)**
  - Конфигурация читается из `pipelines/ocr_utils/config.yaml` замороженным dataclass `AppConfig` и включает:
    - параметры VLM: `vlm_api_url`, `vlm_api_key`, `vlm_model_name`, `temperature`, `presence_penalty`, `repetition_penalty`;
    - параметры изображений: `dpi` (разрешение для конвертации PDF → PNG);
    - параметры PaddleOCR: `using_paddleocr`, `vl_rec_backend`, `vl_rec_server_url`, `vl_rec_model_name` и настройки моделей разметки страницы / ориентации (`layout_detection_*`, `doc_orientation_classify_*`, `layout_threshold`, `layout_nms`, `layout_unclip_ratio`, `layout_merge_bboxes_mode`);
    - настройки OpenWebUI‑интеграции: `openwebui_host`, `openwebui_token`.
  - Любой из ключевых параметров может быть переопределён через Valves:
    - `VLM_API_URL`, `VLM_API_KEY`, `VLM_MODEL_NAME`;
    - `USING_PADDLEOCR`;
    - `VL_REC_BACKEND`, `VL_REC_SERVER_URL`, `VL_REC_MODEL_NAME`;
    - `OPENWEBUI_HOST`, `OPENWEBUI_API_KEY`.

### Жизненный цикл пайплайна в OpenWebUI

- **Инициализация (`on_startup`)**
  - Создаётся клиент `ChatOpenAI` с параметрами из `valves` / `AppConfig` (URL, ключ, модель, temperature, presence_penalty, repetition_penalty).

- **Завершение (`on_shutdown`)**
  - Очищаются кэши файлов и обработанных ID; обнуляется ссылка на VLM; вызывается `gc.collect()`.

### Как использовать

- **В OpenWebUI**
  - Подключите пайплайн `VisualOCR-Ассистент` согласно стандартной схеме интеграции пайплайнов в OpenWebUI.
  - Убедитесь, что:
    - заполнен `pipelines/ocr_utils/config.yaml` (VLM-сервер, PaddleOCR-бэкенд, OpenWebUI-хост);
    - настроены Valves для доступа к VLM и OCR‑backend.
  - В чате с ассистентом прикрепите один или несколько PDF‑файлов или изображений:
    - пайплайн скачает новые файлы, распознает через PaddleOCR (или конвертирует в base64) и передаст в VLM;
    - VLM проанализирует содержимое и ответит на вопрос или выполнит инструкцию пользователя.
