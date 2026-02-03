### Логи
[2026-02-03 12:54:50,666] INFO in pipeline: VisualOCR-Ассистент starting up...
INFO:pipeline:VisualOCR-Ассистент starting up...
[2026-02-03 12:54:50,781] INFO in pipeline: LLM qwen3vl-8b-instruct-fp8 started
INFO:pipeline:LLM qwen3vl-8b-instruct-fp8 started
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:9099 (Press CTRL+C to quit)
[2026-02-03 12:55:26,119] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
[2026-02-03 12:55:26,119] INFO in pipeline: Inlet: received 1 messages, current_message_id: 96c153f8-60d3-4348-ac24-0a818193e8f5
INFO:pipeline:Inlet: received 1 messages, current_message_id: 96c153f8-60d3-4348-ac24-0a818193e8f5
[2026-02-03 12:55:26,119] INFO in pipeline: Inlet: user messages IDs: [None]
INFO:pipeline:Inlet: user messages IDs: [None]
[2026-02-03 12:55:26,119] INFO in pipeline: Inlet: file_cache_session has 0 cached files
INFO:pipeline:Inlet: file_cache_session has 0 cached files
[2026-02-03 12:55:26,119] INFO in pipeline: Inlet: message_order: []
INFO:pipeline:Inlet: message_order: []
INFO:ocr_utils.document_graph:Updating messages. file_cache_session has 0 entries: []
INFO:ocr_utils.document_graph:Message order: ['96c153f8-60d3-4348-ac24-0a818193e8f5']
INFO:ocr_utils.document_graph:Messages count: 1, user messages: [None]
[2026-02-03 12:55:26,122] INFO in pipeline: _update_messages_with_files: file_cache has 0 entries
INFO:pipeline:_update_messages_with_files: file_cache has 0 entries
[2026-02-03 12:55:26,122] INFO in pipeline: _update_messages_with_files: files_by_message keys: []
INFO:pipeline:_update_messages_with_files: files_by_message keys: []
[2026-02-03 12:55:26,122] INFO in pipeline: _update_messages_with_files: message_order: ['96c153f8-60d3-4348-ac24-0a818193e8f5']
INFO:pipeline:_update_messages_with_files: message_order: ['96c153f8-60d3-4348-ac24-0a818193e8f5']
[2026-02-03 12:55:26,122] INFO in pipeline: Message (no id, index 0): using target_message_id 96c153f8-60d3-4348-ac24-0a818193e8f5, found 0 files
INFO:pipeline:Message (no id, index 0): using target_message_id 96c153f8-60d3-4348-ac24-0a818193e8f5, found 0 files
INFO:ocr_utils.document_graph:Updated messages count: 1
Loaded module: pipeline
INFO:     172.19.0.1:58070 - "POST /pipeline/filter/inlet HTTP/1.1" 200 OK
INFO:     172.19.0.1:58074 - "GET /models HTTP/1.1" 200 OK
pipeline
pipeline
INFO:     172.19.0.1:58088 - "POST /chat/completions HTTP/1.1" 200 OK
[2026-02-03 12:55:26,129] INFO in pipeline: Starting OCR pipeline
INFO:pipeline:Starting OCR pipeline
[2026-02-03 12:55:26,129] INFO in pipeline: Using original messages: 1 messages
INFO:pipeline:Using original messages: 1 messages
[2026-02-03 12:55:26,129] INFO in pipeline: Streaming mode enabled for OCR pipeline
INFO:pipeline:Streaming mode enabled for OCR pipeline
INFO:root:stream:true:<generator object Pipeline._invoke_vlm.<locals>._stream at 0x7c31c8ff3010>
[2026-02-03 12:55:26,129] INFO in pipeline: Starting VLM streaming invocation
INFO:pipeline:Starting VLM streaming invocation
INFO:httpx:HTTP Request: POST http://qwen3vl-8b-instruct-fp8:8000/v1/chat/completions "HTTP/1.1 200 OK"
[2026-02-03 12:55:28,441] INFO in pipeline: VLM streaming invocation completed
INFO:pipeline:VLM streaming invocation completed
INFO:     172.19.0.1:58096 - "POST /pipeline/filter/outlet HTTP/1.1" 200 OK
[2026-02-03 12:55:36,034] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
[2026-02-03 12:55:36,034] INFO in pipeline: Inlet: received 3 messages, current_message_id: 22df7255-559a-4ba1-9f73-8ad3e71a63e6
INFO:pipeline:Inlet: received 3 messages, current_message_id: 22df7255-559a-4ba1-9f73-8ad3e71a63e6
[2026-02-03 12:55:36,034] INFO in pipeline: Inlet: user messages IDs: [None, None]
INFO:pipeline:Inlet: user messages IDs: [None, None]
[2026-02-03 12:55:36,034] INFO in pipeline: Inlet: file_cache_session has 0 cached files
INFO:pipeline:Inlet: file_cache_session has 0 cached files
[2026-02-03 12:55:36,034] INFO in pipeline: Inlet: message_order: []
INFO:pipeline:Inlet: message_order: []
INFO:ocr_utils.document_graph:New file detected: 1.pdf (id: 5055b4ed-eac3-4b4f-927c-47164ff64250)
INFO:ocr_utils.document_graph:Added message_id 22df7255-559a-4ba1-9f73-8ad3e71a63e6 to order cache
INFO:ocr_utils.document_graph:Processing 1 files with PaddleOCR for message_id: 22df7255-559a-4ba1-9f73-8ad3e71a63e6
INFO:ocr_utils.file_utils:Downloaded file: 1010422 bytes
INFO:ocr_utils.file_utils:Downloaded 1.pdf to temp file
Creating model: ('PP-LCNet_x1_0_doc_ori', 'pipelines/PP-LCNet_x1_0_doc_ori')
Creating model: ('PP-DocLayoutV2', 'pipelines/PP-DocLayoutV2')
Creating model: ('PaddleOCR-VL-0.9B', None)
[2026-02-03 12:55:38,619] INFO in pipeline: PaddleOCRVL started for PDF OCR
INFO:pipeline:PaddleOCRVL started for PDF OCR
[2026-02-03 12:55:45,942] INFO in pipeline: Cached OCR result for 1.pdf (id: 5055b4ed-eac3-4b4f-927c-47164ff64250) for message_id: 22df7255-559a-4ba1-9f73-8ad3e71a63e6
INFO:pipeline:Cached OCR result for 1.pdf (id: 5055b4ed-eac3-4b4f-927c-47164ff64250) for message_id: 22df7255-559a-4ba1-9f73-8ad3e71a63e6
[2026-02-03 12:55:46,200] INFO in pipeline: _update_messages_with_files: file_cache has 1 entries
INFO:pipeline:_update_messages_with_files: file_cache has 1 entries
[2026-02-03 12:55:46,200] INFO in pipeline: _update_messages_with_files: files_by_message keys: ['22df7255-559a-4ba1-9f73-8ad3e71a63e6']
INFO:pipeline:_update_messages_with_files: files_by_message keys: ['22df7255-559a-4ba1-9f73-8ad3e71a63e6']
[2026-02-03 12:55:46,200] INFO in pipeline: _update_messages_with_files: message_order: ['22df7255-559a-4ba1-9f73-8ad3e71a63e6']
INFO:pipeline:_update_messages_with_files: message_order: ['22df7255-559a-4ba1-9f73-8ad3e71a63e6']
[2026-02-03 12:55:46,200] INFO in pipeline: Message (no id, index 0): using target_message_id 22df7255-559a-4ba1-9f73-8ad3e71a63e6, found 1 files
INFO:pipeline:Message (no id, index 0): using target_message_id 22df7255-559a-4ba1-9f73-8ad3e71a63e6, found 1 files
[2026-02-03 12:55:46,200] INFO in pipeline:   Files: ['1.pdf']
INFO:pipeline:  Files: ['1.pdf']
[2026-02-03 12:55:46,200] WARNING in pipeline: Message (no id, index 1): index 1 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 1): index 1 >= message_order length 1, no files found
[2026-02-03 12:55:46,200] INFO in pipeline:   Available message_ids in cache: ['22df7255-559a-4ba1-9f73-8ad3e71a63e6']
INFO:pipeline:  Available message_ids in cache: ['22df7255-559a-4ba1-9f73-8ad3e71a63e6']
[2026-02-03 12:55:46,200] INFO in pipeline:   Current message_order: ['22df7255-559a-4ba1-9f73-8ad3e71a63e6']
INFO:pipeline:  Current message_order: ['22df7255-559a-4ba1-9f73-8ad3e71a63e6']
INFO:     172.19.0.1:52834 - "POST /pipeline/filter/inlet HTTP/1.1" 200 OK
INFO:     172.19.0.1:41988 - "GET /models HTTP/1.1" 200 OK
pipeline
pipeline
INFO:     172.19.0.1:41998 - "POST /chat/completions HTTP/1.1" 200 OK
[2026-02-03 12:55:46,328] INFO in pipeline: Starting OCR pipeline
INFO:pipeline:Starting OCR pipeline
[2026-02-03 12:55:46,328] INFO in pipeline: Using original messages: 3 messages
INFO:pipeline:Using original messages: 3 messages
[2026-02-03 12:55:46,328] INFO in pipeline: Streaming mode enabled for OCR pipeline
INFO:pipeline:Streaming mode enabled for OCR pipeline
[2026-02-03 12:55:46,328] INFO in pipeline: Starting VLM streaming invocation
INFO:pipeline:Starting VLM streaming invocation
[2026-02-03 12:56:23,335] INFO in pipeline: VLM streaming invocation completed
INFO:pipeline:VLM streaming invocation completed
INFO:     172.19.0.1:46690 - "POST /pipeline/filter/outlet HTTP/1.1" 200 OK
[2026-02-03 12:57:17,448] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
[2026-02-03 12:57:17,448] INFO in pipeline: Inlet: received 5 messages, current_message_id: 907d5ba6-5b08-467b-ab24-b4a69cc29b68
INFO:pipeline:Inlet: received 5 messages, current_message_id: 907d5ba6-5b08-467b-ab24-b4a69cc29b68
[2026-02-03 12:57:17,448] INFO in pipeline: Inlet: user messages IDs: [None, None, None]
INFO:pipeline:Inlet: user messages IDs: [None, None, None]
[2026-02-03 12:57:17,448] INFO in pipeline: Inlet: file_cache_session has 1 cached files
INFO:pipeline:Inlet: file_cache_session has 1 cached files
[2026-02-03 12:57:17,448] INFO in pipeline: Inlet: message_order: []
INFO:pipeline:Inlet: message_order: []
Creating model: ('PP-LCNet_x1_0_doc_ori', 'pipelines/PP-LCNet_x1_0_doc_ori')
Creating model: ('PP-DocLayoutV2', 'pipelines/PP-DocLayoutV2')
Creating model: ('PaddleOCR-VL-0.9B', None)
[2026-02-03 12:57:18,170] INFO in pipeline: PaddleOCRVL started for PDF OCR
INFO:pipeline:PaddleOCRVL started for PDF OCR
[2026-02-03 12:57:23,426] INFO in pipeline: Cached OCR result for 2.pdf (id: 2514dbb9-77ee-4bb2-9850-cf9267b0c163) for message_id: 907d5ba6-5b08-467b-ab24-b4a69cc29b68
INFO:pipeline:Cached OCR result for 2.pdf (id: 2514dbb9-77ee-4bb2-9850-cf9267b0c163) for message_id: 907d5ba6-5b08-467b-ab24-b4a69cc29b68
[2026-02-03 12:57:23,663] INFO in pipeline: _update_messages_with_files: file_cache has 2 entries
INFO:pipeline:_update_messages_with_files: file_cache has 2 entries
[2026-02-03 12:57:23,663] INFO in pipeline: _update_messages_with_files: files_by_message keys: ['22df7255-559a-4ba1-9f73-8ad3e71a63e6', '907d5ba6-5b08-467b-ab24-b4a69cc29b68']
INFO:pipeline:_update_messages_with_files: files_by_message keys: ['22df7255-559a-4ba1-9f73-8ad3e71a63e6', '907d5ba6-5b08-467b-ab24-b4a69cc29b68']
[2026-02-03 12:57:23,663] INFO in pipeline: _update_messages_with_files: message_order: ['907d5ba6-5b08-467b-ab24-b4a69cc29b68', '22df7255-559a-4ba1-9f73-8ad3e71a63e6']
INFO:pipeline:_update_messages_with_files: message_order: ['907d5ba6-5b08-467b-ab24-b4a69cc29b68', '22df7255-559a-4ba1-9f73-8ad3e71a63e6']
[2026-02-03 12:57:23,663] INFO in pipeline: Message (no id, index 0): using target_message_id 907d5ba6-5b08-467b-ab24-b4a69cc29b68, found 1 files
INFO:pipeline:Message (no id, index 0): using target_message_id 907d5ba6-5b08-467b-ab24-b4a69cc29b68, found 1 files
[2026-02-03 12:57:23,663] INFO in pipeline:   Files: ['2.pdf']
INFO:pipeline:  Files: ['2.pdf']
[2026-02-03 12:57:23,663] INFO in pipeline: Message (no id, index 1): using target_message_id 22df7255-559a-4ba1-9f73-8ad3e71a63e6, found 1 files
INFO:pipeline:Message (no id, index 1): using target_message_id 22df7255-559a-4ba1-9f73-8ad3e71a63e6, found 1 files
[2026-02-03 12:57:23,663] INFO in pipeline:   Files: ['1.pdf']
INFO:pipeline:  Files: ['1.pdf']
[2026-02-03 12:57:23,663] WARNING in pipeline: Message (no id, index 2): index 2 >= message_order length 2, no files found
WARNING:pipeline:Message (no id, index 2): index 2 >= message_order length 2, no files found
[2026-02-03 12:57:23,664] INFO in pipeline:   Available message_ids in cache: ['22df7255-559a-4ba1-9f73-8ad3e71a63e6', '907d5ba6-5b08-467b-ab24-b4a69cc29b68']
INFO:pipeline:  Available message_ids in cache: ['22df7255-559a-4ba1-9f73-8ad3e71a63e6', '907d5ba6-5b08-467b-ab24-b4a69cc29b68']
[2026-02-03 12:57:23,664] INFO in pipeline:   Current message_order: ['907d5ba6-5b08-467b-ab24-b4a69cc29b68', '22df7255-559a-4ba1-9f73-8ad3e71a63e6']
INFO:pipeline:  Current message_order: ['907d5ba6-5b08-467b-ab24-b4a69cc29b68', '22df7255-559a-4ba1-9f73-8ad3e71a63e6']
INFO:     172.19.0.1:39042 - "POST /pipeline/filter/inlet HTTP/1.1" 200 OK
INFO:     172.19.0.1:39056 - "GET /models HTTP/1.1" 200 OK
pipeline
pipeline
INFO:     172.19.0.1:39062 - "POST /chat/completions HTTP/1.1" 200 OK
[2026-02-03 12:57:23,737] INFO in pipeline: Starting OCR pipeline
INFO:pipeline:Starting OCR pipeline
[2026-02-03 12:57:23,737] INFO in pipeline: Using original messages: 5 messages
INFO:pipeline:Using original messages: 5 messages
[2026-02-03 12:57:23,737] INFO in pipeline: Streaming mode enabled for OCR pipeline
INFO:pipeline:Streaming mode enabled for OCR pipeline
[2026-02-03 12:57:23,737] INFO in pipeline: Starting VLM streaming invocation
INFO:pipeline:Starting VLM streaming invocation
[2026-02-03 12:58:08,378] INFO in pipeline: VLM streaming invocation completed
INFO:pipeline:VLM streaming invocation completed
INFO:     172.19.0.1:54214 - "POST /pipeline/filter/outlet HTTP/1.1" 200 OK
[2026-02-03 12:58:09,786] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
[2026-02-03 12:58:09,786] INFO in pipeline: Inlet: received 7 messages, current_message_id: 98c06b54-3e17-43d6-b291-c68d73643e61
INFO:pipeline:Inlet: received 7 messages, current_message_id: 98c06b54-3e17-43d6-b291-c68d73643e61
[2026-02-03 12:58:09,786] INFO in pipeline: Inlet: user messages IDs: [None, None, None, None]
INFO:pipeline:Inlet: user messages IDs: [None, None, None, None]
[2026-02-03 12:58:09,786] INFO in pipeline: Inlet: file_cache_session has 2 cached files
INFO:pipeline:Inlet: file_cache_session has 2 cached files
[2026-02-03 12:58:09,786] INFO in pipeline: Inlet: message_order: []
INFO:pipeline:Inlet: message_order: []
[2026-02-03 12:58:09,788] INFO in pipeline: _update_messages_with_files: file_cache has 2 entries
INFO:pipeline:_update_messages_with_files: file_cache has 2 entries
[2026-02-03 12:58:09,788] INFO in pipeline: _update_messages_with_files: files_by_message keys: ['22df7255-559a-4ba1-9f73-8ad3e71a63e6', '907d5ba6-5b08-467b-ab24-b4a69cc29b68']
INFO:pipeline:_update_messages_with_files: files_by_message keys: ['22df7255-559a-4ba1-9f73-8ad3e71a63e6', '907d5ba6-5b08-467b-ab24-b4a69cc29b68']
[2026-02-03 12:58:09,788] INFO in pipeline: _update_messages_with_files: message_order: ['98c06b54-3e17-43d6-b291-c68d73643e61', '22df7255-559a-4ba1-9f73-8ad3e71a63e6', '907d5ba6-5b08-467b-ab24-b4a69cc29b68']
INFO:pipeline:_update_messages_with_files: message_order: ['98c06b54-3e17-43d6-b291-c68d73643e61', '22df7255-559a-4ba1-9f73-8ad3e71a63e6', '907d5ba6-5b08-467b-ab24-b4a69cc29b68']
[2026-02-03 12:58:09,788] INFO in pipeline: Message (no id, index 0): using target_message_id 98c06b54-3e17-43d6-b291-c68d73643e61, found 0 files
INFO:pipeline:Message (no id, index 0): using target_message_id 98c06b54-3e17-43d6-b291-c68d73643e61, found 0 files
[2026-02-03 12:58:09,788] INFO in pipeline: Message (no id, index 1): using target_message_id 22df7255-559a-4ba1-9f73-8ad3e71a63e6, found 1 files
INFO:pipeline:Message (no id, index 1): using target_message_id 22df7255-559a-4ba1-9f73-8ad3e71a63e6, found 1 files
[2026-02-03 12:58:09,788] INFO in pipeline:   Files: ['1.pdf']
INFO:pipeline:  Files: ['1.pdf']
[2026-02-03 12:58:09,788] INFO in pipeline: Message (no id, index 2): using target_message_id 907d5ba6-5b08-467b-ab24-b4a69cc29b68, found 1 files
INFO:pipeline:Message (no id, index 2): using target_message_id 907d5ba6-5b08-467b-ab24-b4a69cc29b68, found 1 files
[2026-02-03 12:58:09,788] INFO in pipeline:   Files: ['2.pdf']
INFO:pipeline:  Files: ['2.pdf']
[2026-02-03 12:58:09,788] WARNING in pipeline: Message (no id, index 3): index 3 >= message_order length 3, no files found
WARNING:pipeline:Message (no id, index 3): index 3 >= message_order length 3, no files found
[2026-02-03 12:58:09,788] INFO in pipeline:   Available message_ids in cache: ['22df7255-559a-4ba1-9f73-8ad3e71a63e6', '907d5ba6-5b08-467b-ab24-b4a69cc29b68']
INFO:pipeline:  Available message_ids in cache: ['22df7255-559a-4ba1-9f73-8ad3e71a63e6', '907d5ba6-5b08-467b-ab24-b4a69cc29b68']
[2026-02-03 12:58:09,788] INFO in pipeline:   Current message_order: ['98c06b54-3e17-43d6-b291-c68d73643e61', '22df7255-559a-4ba1-9f73-8ad3e71a63e6', '907d5ba6-5b08-467b-ab24-b4a69cc29b68']
INFO:pipeline:  Current message_order: ['98c06b54-3e17-43d6-b291-c68d73643e61', '22df7255-559a-4ba1-9f73-8ad3e71a63e6', '907d5ba6-5b08-467b-ab24-b4a69cc29b68']
INFO:     172.19.0.1:54222 - "POST /pipeline/filter/inlet HTTP/1.1" 200 OK
INFO:     172.19.0.1:54238 - "GET /models HTTP/1.1" 200 OK
pipeline
pipeline
INFO:     172.19.0.1:54248 - "POST /chat/completions HTTP/1.1" 200 OK
[2026-02-03 12:58:09,882] INFO in pipeline: Starting OCR pipeline
INFO:pipeline:Starting OCR pipeline
[2026-02-03 12:58:09,882] INFO in pipeline: Using original messages: 7 messages
INFO:pipeline:Using original messages: 7 messages
[2026-02-03 12:58:09,882] INFO in pipeline: Streaming mode enabled for OCR pipeline
INFO:pipeline:Streaming mode enabled for OCR pipeline
[2026-02-03 12:58:09,882] INFO in pipeline: Starting VLM streaming invocation
INFO:pipeline:Starting VLM streaming invocation
[2026-02-03 12:58:18,824] INFO in pipeline: VLM streaming invocation completed
INFO:pipeline:VLM streaming invocation completed
INFO:     172.19.0.1:36492 - "POST /pipeline/filter/outlet HTTP/1.1" 200 OK

### Ответ модели на предпоследнее сообщение с прикрепленным 2.pdf
Текст уже распознан и представлен выше — это результат OCR из файла 1.pdf.

Если вы хотите, чтобы я:

исправил форматирование (например, таблицы, переносы, структуру),
выделил ключевые данные (УНП, даты, счета, контакты),
оформил в виде отчета или таблицы,
или что-то ещё — просто скажите!
Вот текущий текст без изменений (как он был распознан):

Индивидуальный предприниматель Мирная Марфа Кощеевна
210000, Дубов, а/я 3. Тел. (Viber, Telegram): +375 (12) 147 14 47
marfamirnaya@inbox.ru
код абонента в АИС МВ (мСМДО) Org5458
р/с ВУ40 РЖСВ 3013 1245 1256 4587 4589 в «Прбанк»
ОАО ЦБУ 00, код банка РУУ2Х, УНП 458963103

25.09.2025 №49

ЗАО «Альфа-Банк» (СМДО)
антикризисного управляющего в
производстве по делу о банкротстве ООО
«Дом СИЗ» — индивидуального
предпринимателя

210000, Дубов, а/я 3.
Мирной Марфы Кощеевны
Тел. (Viber, Telegram): +375 (12) 147 14 47
код абонента в АИС МВ (мСМДО) Org5458

О предоставлении информации
Определением суда Пушкинской области от 14.06.2025 по делу №1526 принято заявление о банкротстве, в отношении общества с ограниченной ответственностью «Дом СИЗ» (УНП 321654987) (далее — должник) возбуждено производство по делу о банкротстве и открыто конкурсное производство, антикризисным управляющим должника назначен индивидуальный предприниматель Мирная Марфа Кощеевна (далее — антикризисный управляющий). Вышеуказанное определение суда размещено в открытом доступе.

Руководствуясь пунктами 25 и 74 статьи 457, абзацем 1 статьи 248, абзацем 3 статьи 26 Закона Дубравинска от 23 декабря 2012 г. №7-3 «Об управлении делами», в целях решения задач ООО "Дом СИЗ"

прошу предоставить:
выписки по всем счетам открытым в ЗАО «Альфа-Банк» обществом с
ограниченной ответственностью «Дом СИЗ»

за последние три года;

сведения о лицах, имевших право распоряжаться банковскими
счетами (с указанием периода);

сведения о полученных и погашенных банковских кредитах за
последние три года.

Запрашиваемую информацию прошу направить мне по адресу электронной
почты либо по средствам СМДО.

Одновременно разъясняю, что ЗАО «Альфа-Банк» вправе предъявить мне
как антикризисному управляющему должника свои требования кредитора.

Антикризисный управляющий
ООО «Дом СИЗ»
индивидуальный предприниматель

дата, подпись и печать
М.К. Мирная

Если нужно — могу оформить в виде таблицы, выделить данные или исправить артефакты. Готов помочь!

### Ответ модели на последнее сообщение: "Сколько файлов я тебе прислал?"
Вы прислали два файла:

1.pdf — это письмо антикризисного управляющего Мирной Марфы Кощеевны в ЗАО «Альфа-Банк» с запросом на предоставление банковской информации по ООО «Дом СИЗ».
2.pdf — это письмо (или запрос) от ООО «Калинка» в ЗАО «Альфа-Банк» с просьбой предоставить справку о закрытии счета ООО «МирТрудМай».
Оба файла уже были распознаны и представлены в текстовом виде выше.

Если нужно — могу сравнить, объединить или выделить ключевые данные из обоих документов. Готов помочь!