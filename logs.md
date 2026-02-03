### Логи
[2026-02-03 13:25:03,111] INFO in pipeline: LLM qwen3vl-8b-instruct-fp8 started
INFO:pipeline:LLM qwen3vl-8b-instruct-fp8 started
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:9099 (Press CTRL+C to quit)
[2026-02-03 13:25:14,656] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
[2026-02-03 13:25:14,656] INFO in pipeline: Inlet: received 1 messages, current_message_id: c2d5e3a0-4284-476d-8c66-f46f86f3bcda
INFO:pipeline:Inlet: received 1 messages, current_message_id: c2d5e3a0-4284-476d-8c66-f46f86f3bcda
[2026-02-03 13:25:14,656] INFO in pipeline: Inlet: user messages IDs: [None]
INFO:pipeline:Inlet: user messages IDs: [None]
[2026-02-03 13:25:14,656] INFO in pipeline: Inlet: file_cache_session has 0 cached files
INFO:pipeline:Inlet: file_cache_session has 0 cached files
[2026-02-03 13:25:14,656] INFO in pipeline: Inlet: message_order: []
INFO:pipeline:Inlet: message_order: []
INFO:ocr_utils.document_graph:Updating messages. file_cache_session has 0 entries: []
INFO:ocr_utils.document_graph:Message order: ['c2d5e3a0-4284-476d-8c66-f46f86f3bcda']
INFO:ocr_utils.document_graph:Messages count: 1, user messages: [None]
[2026-02-03 13:25:14,659] INFO in pipeline: _update_messages_with_files: file_cache has 0 entries
INFO:pipeline:_update_messages_with_files: file_cache has 0 entries
[2026-02-03 13:25:14,659] INFO in pipeline: _update_messages_with_files: files_by_message keys: []
INFO:pipeline:_update_messages_with_files: files_by_message keys: []
[2026-02-03 13:25:14,659] INFO in pipeline: _update_messages_with_files: message_order: ['c2d5e3a0-4284-476d-8c66-f46f86f3bcda']
INFO:pipeline:_update_messages_with_files: message_order: ['c2d5e3a0-4284-476d-8c66-f46f86f3bcda']
[2026-02-03 13:25:14,659] INFO in pipeline: Message (no id, index 0): using target_message_id c2d5e3a0-4284-476d-8c66-f46f86f3bcda, found 0 files
INFO:pipeline:Message (no id, index 0): using target_message_id c2d5e3a0-4284-476d-8c66-f46f86f3bcda, found 0 files
INFO:ocr_utils.document_graph:Updated messages count: 1
Loaded module: pipeline
INFO:     172.19.0.1:50108 - "POST /pipeline/filter/inlet HTTP/1.1" 200 OK
INFO:     172.19.0.1:50118 - "GET /models HTTP/1.1" 200 OK
pipeline
pipeline
INFO:     172.19.0.1:50126 - "POST /chat/completions HTTP/1.1" 200 OK
[2026-02-03 13:25:14,666] INFO in pipeline: Starting OCR pipeline
INFO:pipeline:Starting OCR pipeline
[2026-02-03 13:25:14,666] INFO in pipeline: Streaming mode enabled for OCR pipeline
INFO:pipeline:Streaming mode enabled for OCR pipeline
INFO:root:stream:true:<generator object Pipeline._invoke_vlm.<locals>._stream at 0x780c9306f010>
[2026-02-03 13:25:14,666] INFO in pipeline: Starting VLM streaming invocation
INFO:pipeline:Starting VLM streaming invocation
INFO:httpx:HTTP Request: POST http://qwen3vl-8b-instruct-fp8:8000/v1/chat/completions "HTTP/1.1 200 OK"
[2026-02-03 13:25:18,965] INFO in pipeline: VLM streaming invocation completed
INFO:pipeline:VLM streaming invocation completed
INFO:     172.19.0.1:50138 - "POST /pipeline/filter/outlet HTTP/1.1" 200 OK
[2026-02-03 13:25:55,386] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
[2026-02-03 13:25:55,386] INFO in pipeline: Inlet: received 3 messages, current_message_id: e0b502bf-f4ba-47f8-9a89-b479b72bf4af
INFO:pipeline:Inlet: received 3 messages, current_message_id: e0b502bf-f4ba-47f8-9a89-b479b72bf4af
[2026-02-03 13:25:55,387] INFO in pipeline: Inlet: user messages IDs: [None, None]
INFO:pipeline:Inlet: user messages IDs: [None, None]
[2026-02-03 13:25:55,387] INFO in pipeline: Inlet: file_cache_session has 0 cached files
INFO:pipeline:Inlet: file_cache_session has 0 cached files
[2026-02-03 13:25:55,387] INFO in pipeline: Inlet: message_order: []
INFO:pipeline:Inlet: message_order: []
INFO:ocr_utils.document_graph:New file detected: 1.pdf (id: a770265b-472c-49a6-a8fc-6726d1d0f722)
INFO:ocr_utils.document_graph:Added message_id e0b502bf-f4ba-47f8-9a89-b479b72bf4af to order cache
INFO:ocr_utils.document_graph:Processing 1 files with PaddleOCR for message_id: e0b502bf-f4ba-47f8-9a89-b479b72bf4af
INFO:ocr_utils.file_utils:Downloaded file: 1010422 bytes
INFO:ocr_utils.file_utils:Downloaded 1.pdf to temp file
Creating model: ('PP-LCNet_x1_0_doc_ori', 'pipelines/PP-LCNet_x1_0_doc_ori')
Creating model: ('PP-DocLayoutV2', 'pipelines/PP-DocLayoutV2')
Creating model: ('PaddleOCR-VL-0.9B', None)
[2026-02-03 13:25:57,938] INFO in pipeline: PaddleOCRVL started for PDF OCR
INFO:pipeline:PaddleOCRVL started for PDF OCR
[2026-02-03 13:26:06,796] INFO in pipeline: Cached OCR result for 1.pdf (id: a770265b-472c-49a6-a8fc-6726d1d0f722) for message_id: e0b502bf-f4ba-47f8-9a89-b479b72bf4af
INFO:pipeline:Cached OCR result for 1.pdf (id: a770265b-472c-49a6-a8fc-6726d1d0f722) for message_id: e0b502bf-f4ba-47f8-9a89-b479b72bf4af
[2026-02-03 13:26:07,046] INFO in pipeline: _update_messages_with_files: file_cache has 1 entries
INFO:pipeline:_update_messages_with_files: file_cache has 1 entries
[2026-02-03 13:26:07,046] INFO in pipeline: _update_messages_with_files: files_by_message keys: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af']
INFO:pipeline:_update_messages_with_files: files_by_message keys: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af']
[2026-02-03 13:26:07,046] INFO in pipeline: _update_messages_with_files: message_order: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af']
INFO:pipeline:_update_messages_with_files: message_order: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af']
[2026-02-03 13:26:07,046] INFO in pipeline: Message (no id, index 0): using target_message_id e0b502bf-f4ba-47f8-9a89-b479b72bf4af, found 1 files
INFO:pipeline:Message (no id, index 0): using target_message_id e0b502bf-f4ba-47f8-9a89-b479b72bf4af, found 1 files
[2026-02-03 13:26:07,046] INFO in pipeline:   Files: ['1.pdf']
INFO:pipeline:  Files: ['1.pdf']
[2026-02-03 13:26:07,046] WARNING in pipeline: Message (no id, index 1): index 1 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 1): index 1 >= message_order length 1, no files found
[2026-02-03 13:26:07,046] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af']
[2026-02-03 13:26:07,046] INFO in pipeline:   Current message_order: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af']
INFO:pipeline:  Current message_order: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af']
INFO:     172.19.0.1:33622 - "POST /pipeline/filter/inlet HTTP/1.1" 200 OK
INFO:     172.19.0.1:49694 - "GET /models HTTP/1.1" 200 OK
pipeline
pipeline
INFO:     172.19.0.1:49708 - "POST /chat/completions HTTP/1.1" 200 OK
[2026-02-03 13:26:07,139] INFO in pipeline: Starting OCR pipeline
INFO:pipeline:Starting OCR pipeline
[2026-02-03 13:26:07,140] INFO in pipeline: Streaming mode enabled for OCR pipeline
INFO:pipeline:Streaming mode enabled for OCR pipeline
[2026-02-03 13:26:07,140] INFO in pipeline: Starting VLM streaming invocation
INFO:pipeline:Starting VLM streaming invocation
[2026-02-03 13:26:48,663] INFO in pipeline: VLM streaming invocation completed
INFO:pipeline:VLM streaming invocation completed
INFO:     172.19.0.1:36736 - "POST /pipeline/filter/outlet HTTP/1.1" 200 OK
[2026-02-03 13:27:09,975] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
[2026-02-03 13:27:09,975] INFO in pipeline: Inlet: received 5 messages, current_message_id: 6c035439-0134-4c4d-8afb-f1f115520479
INFO:pipeline:Inlet: received 5 messages, current_message_id: 6c035439-0134-4c4d-8afb-f1f115520479
[2026-02-03 13:27:09,975] INFO in pipeline: Inlet: user messages IDs: [None, None, None]
INFO:pipeline:Inlet: user messages IDs: [None, None, None]
[2026-02-03 13:27:09,975] INFO in pipeline: Inlet: file_cache_session has 1 cached files
INFO:pipeline:Inlet: file_cache_session has 1 cached files
[2026-02-03 13:27:09,975] INFO in pipeline: Inlet: message_order: []
INFO:pipeline:Inlet: message_order: []
Creating model: ('PP-LCNet_x1_0_doc_ori', 'pipelines/PP-LCNet_x1_0_doc_ori')
Creating model: ('PP-DocLayoutV2', 'pipelines/PP-DocLayoutV2')
Creating model: ('PaddleOCR-VL-0.9B', None)
[2026-02-03 13:27:11,043] INFO in pipeline: PaddleOCRVL started for PDF OCR
INFO:pipeline:PaddleOCRVL started for PDF OCR
[2026-02-03 13:27:16,089] INFO in pipeline: Cached OCR result for 2.pdf (id: bec16f17-7ef2-47bd-a22c-fc622157b504) for message_id: 6c035439-0134-4c4d-8afb-f1f115520479
INFO:pipeline:Cached OCR result for 2.pdf (id: bec16f17-7ef2-47bd-a22c-fc622157b504) for message_id: 6c035439-0134-4c4d-8afb-f1f115520479
[2026-02-03 13:27:16,324] INFO in pipeline: _update_messages_with_files: file_cache has 2 entries
INFO:pipeline:_update_messages_with_files: file_cache has 2 entries
[2026-02-03 13:27:16,324] INFO in pipeline: _update_messages_with_files: files_by_message keys: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:_update_messages_with_files: files_by_message keys: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:27:16,324] INFO in pipeline: _update_messages_with_files: message_order: ['6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:_update_messages_with_files: message_order: ['6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:27:16,324] INFO in pipeline: Message (no id, index 0): using target_message_id 6c035439-0134-4c4d-8afb-f1f115520479, found 1 files
INFO:pipeline:Message (no id, index 0): using target_message_id 6c035439-0134-4c4d-8afb-f1f115520479, found 1 files
[2026-02-03 13:27:16,324] INFO in pipeline:   Files: ['2.pdf']
INFO:pipeline:  Files: ['2.pdf']
[2026-02-03 13:27:16,324] WARNING in pipeline: Message (no id, index 1): index 1 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 1): index 1 >= message_order length 1, no files found
[2026-02-03 13:27:16,324] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:27:16,324] INFO in pipeline:   Current message_order: ['6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Current message_order: ['6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:27:16,324] WARNING in pipeline: Message (no id, index 2): index 2 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 2): index 2 >= message_order length 1, no files found
[2026-02-03 13:27:16,324] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:27:16,324] INFO in pipeline:   Current message_order: ['6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Current message_order: ['6c035439-0134-4c4d-8afb-f1f115520479']
INFO:     172.19.0.1:50878 - "POST /pipeline/filter/inlet HTTP/1.1" 200 OK
INFO:     172.19.0.1:55302 - "GET /models HTTP/1.1" 200 OK
pipeline
pipeline
INFO:     172.19.0.1:55306 - "POST /chat/completions HTTP/1.1" 200 OK
[2026-02-03 13:27:16,400] INFO in pipeline: Starting OCR pipeline
INFO:pipeline:Starting OCR pipeline
[2026-02-03 13:27:16,401] INFO in pipeline: Streaming mode enabled for OCR pipeline
INFO:pipeline:Streaming mode enabled for OCR pipeline
[2026-02-03 13:27:16,401] INFO in pipeline: Starting VLM streaming invocation
INFO:pipeline:Starting VLM streaming invocation
[2026-02-03 13:27:40,064] INFO in pipeline: VLM streaming invocation completed
INFO:pipeline:VLM streaming invocation completed
INFO:     172.19.0.1:40750 - "POST /pipeline/filter/outlet HTTP/1.1" 200 OK
[2026-02-03 13:28:13,259] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
[2026-02-03 13:28:13,259] INFO in pipeline: Inlet: received 7 messages, current_message_id: 8c6bb3b7-2fb0-4e48-ae85-124aa8d97f10
INFO:pipeline:Inlet: received 7 messages, current_message_id: 8c6bb3b7-2fb0-4e48-ae85-124aa8d97f10
[2026-02-03 13:28:13,259] INFO in pipeline: Inlet: user messages IDs: [None, None, None, None]
INFO:pipeline:Inlet: user messages IDs: [None, None, None, None]
[2026-02-03 13:28:13,259] INFO in pipeline: Inlet: file_cache_session has 2 cached files
INFO:pipeline:Inlet: file_cache_session has 2 cached files
[2026-02-03 13:28:13,259] INFO in pipeline: Inlet: message_order: []
INFO:pipeline:Inlet: message_order: []
[2026-02-03 13:28:13,261] INFO in pipeline: _update_messages_with_files: file_cache has 2 entries
INFO:pipeline:_update_messages_with_files: file_cache has 2 entries
[2026-02-03 13:28:13,261] INFO in pipeline: _update_messages_with_files: files_by_message keys: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:_update_messages_with_files: files_by_message keys: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:28:13,261] INFO in pipeline: _update_messages_with_files: message_order: ['8c6bb3b7-2fb0-4e48-ae85-124aa8d97f10']
INFO:pipeline:_update_messages_with_files: message_order: ['8c6bb3b7-2fb0-4e48-ae85-124aa8d97f10']
[2026-02-03 13:28:13,261] INFO in pipeline: Message (no id, index 0): using target_message_id 8c6bb3b7-2fb0-4e48-ae85-124aa8d97f10, found 0 files
INFO:pipeline:Message (no id, index 0): using target_message_id 8c6bb3b7-2fb0-4e48-ae85-124aa8d97f10, found 0 files
[2026-02-03 13:28:13,261] WARNING in pipeline: Message (no id, index 1): index 1 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 1): index 1 >= message_order length 1, no files found
[2026-02-03 13:28:13,261] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:28:13,261] INFO in pipeline:   Current message_order: ['8c6bb3b7-2fb0-4e48-ae85-124aa8d97f10']
INFO:pipeline:  Current message_order: ['8c6bb3b7-2fb0-4e48-ae85-124aa8d97f10']
[2026-02-03 13:28:13,261] WARNING in pipeline: Message (no id, index 2): index 2 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 2): index 2 >= message_order length 1, no files found
[2026-02-03 13:28:13,261] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:28:13,261] INFO in pipeline:   Current message_order: ['8c6bb3b7-2fb0-4e48-ae85-124aa8d97f10']
INFO:pipeline:  Current message_order: ['8c6bb3b7-2fb0-4e48-ae85-124aa8d97f10']
[2026-02-03 13:28:13,261] WARNING in pipeline: Message (no id, index 3): index 3 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 3): index 3 >= message_order length 1, no files found
[2026-02-03 13:28:13,261] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:28:13,261] INFO in pipeline:   Current message_order: ['8c6bb3b7-2fb0-4e48-ae85-124aa8d97f10']
INFO:pipeline:  Current message_order: ['8c6bb3b7-2fb0-4e48-ae85-124aa8d97f10']
INFO:     172.19.0.1:53508 - "POST /pipeline/filter/inlet HTTP/1.1" 200 OK
INFO:     172.19.0.1:53520 - "GET /models HTTP/1.1" 200 OK
pipeline
pipeline
INFO:     172.19.0.1:53526 - "POST /chat/completions HTTP/1.1" 200 OK
[2026-02-03 13:28:13,362] INFO in pipeline: Starting OCR pipeline
INFO:pipeline:Starting OCR pipeline
[2026-02-03 13:28:13,362] INFO in pipeline: Streaming mode enabled for OCR pipeline
INFO:pipeline:Streaming mode enabled for OCR pipeline
[2026-02-03 13:28:13,362] INFO in pipeline: Starting VLM streaming invocation
INFO:pipeline:Starting VLM streaming invocation
[2026-02-03 13:28:19,944] INFO in pipeline: VLM streaming invocation completed
INFO:pipeline:VLM streaming invocation completed
INFO:     172.19.0.1:53538 - "POST /pipeline/filter/outlet HTTP/1.1" 200 OK
[2026-02-03 13:28:26,120] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
[2026-02-03 13:28:26,120] INFO in pipeline: Inlet: received 9 messages, current_message_id: af5f2952-61bd-4510-803f-66798a838d1a
INFO:pipeline:Inlet: received 9 messages, current_message_id: af5f2952-61bd-4510-803f-66798a838d1a
[2026-02-03 13:28:26,120] INFO in pipeline: Inlet: user messages IDs: [None, None, None, None, None]
INFO:pipeline:Inlet: user messages IDs: [None, None, None, None, None]
[2026-02-03 13:28:26,120] INFO in pipeline: Inlet: file_cache_session has 2 cached files
INFO:pipeline:Inlet: file_cache_session has 2 cached files
[2026-02-03 13:28:26,120] INFO in pipeline: Inlet: message_order: []
INFO:pipeline:Inlet: message_order: []
[2026-02-03 13:28:26,121] INFO in pipeline: _update_messages_with_files: file_cache has 2 entries
INFO:pipeline:_update_messages_with_files: file_cache has 2 entries
[2026-02-03 13:28:26,121] INFO in pipeline: _update_messages_with_files: files_by_message keys: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:_update_messages_with_files: files_by_message keys: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:28:26,121] INFO in pipeline: _update_messages_with_files: message_order: ['af5f2952-61bd-4510-803f-66798a838d1a']
INFO:pipeline:_update_messages_with_files: message_order: ['af5f2952-61bd-4510-803f-66798a838d1a']
[2026-02-03 13:28:26,121] INFO in pipeline: Message (no id, index 0): using target_message_id af5f2952-61bd-4510-803f-66798a838d1a, found 0 files
INFO:pipeline:Message (no id, index 0): using target_message_id af5f2952-61bd-4510-803f-66798a838d1a, found 0 files
[2026-02-03 13:28:26,121] WARNING in pipeline: Message (no id, index 1): index 1 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 1): index 1 >= message_order length 1, no files found
[2026-02-03 13:28:26,121] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:28:26,121] INFO in pipeline:   Current message_order: ['af5f2952-61bd-4510-803f-66798a838d1a']
INFO:pipeline:  Current message_order: ['af5f2952-61bd-4510-803f-66798a838d1a']
[2026-02-03 13:28:26,121] WARNING in pipeline: Message (no id, index 2): index 2 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 2): index 2 >= message_order length 1, no files found
[2026-02-03 13:28:26,121] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:28:26,121] INFO in pipeline:   Current message_order: ['af5f2952-61bd-4510-803f-66798a838d1a']
INFO:pipeline:  Current message_order: ['af5f2952-61bd-4510-803f-66798a838d1a']
[2026-02-03 13:28:26,121] WARNING in pipeline: Message (no id, index 3): index 3 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 3): index 3 >= message_order length 1, no files found
[2026-02-03 13:28:26,121] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:28:26,121] INFO in pipeline:   Current message_order: ['af5f2952-61bd-4510-803f-66798a838d1a']
INFO:pipeline:  Current message_order: ['af5f2952-61bd-4510-803f-66798a838d1a']
[2026-02-03 13:28:26,121] WARNING in pipeline: Message (no id, index 4): index 4 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 4): index 4 >= message_order length 1, no files found
[2026-02-03 13:28:26,121] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:28:26,121] INFO in pipeline:   Current message_order: ['af5f2952-61bd-4510-803f-66798a838d1a']
INFO:pipeline:  Current message_order: ['af5f2952-61bd-4510-803f-66798a838d1a']
INFO:     172.19.0.1:33446 - "POST /pipeline/filter/inlet HTTP/1.1" 200 OK
INFO:     172.19.0.1:33458 - "GET /models HTTP/1.1" 200 OK
pipeline
pipeline
INFO:     172.19.0.1:33470 - "POST /chat/completions HTTP/1.1" 200 OK
[2026-02-03 13:28:26,218] INFO in pipeline: Starting OCR pipeline
INFO:pipeline:Starting OCR pipeline
[2026-02-03 13:28:26,218] INFO in pipeline: Streaming mode enabled for OCR pipeline
INFO:pipeline:Streaming mode enabled for OCR pipeline
[2026-02-03 13:28:26,219] INFO in pipeline: Starting VLM streaming invocation
INFO:pipeline:Starting VLM streaming invocation
[2026-02-03 13:28:32,171] INFO in pipeline: VLM streaming invocation completed
INFO:pipeline:VLM streaming invocation completed
INFO:     172.19.0.1:34396 - "POST /pipeline/filter/outlet HTTP/1.1" 200 OK
[2026-02-03 13:28:44,718] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
[2026-02-03 13:28:44,718] INFO in pipeline: Inlet: received 11 messages, current_message_id: 64e46ab7-02f0-4508-8cdc-9967d2779ce7
INFO:pipeline:Inlet: received 11 messages, current_message_id: 64e46ab7-02f0-4508-8cdc-9967d2779ce7
[2026-02-03 13:28:44,718] INFO in pipeline: Inlet: user messages IDs: [None, None, None, None, None, None]
INFO:pipeline:Inlet: user messages IDs: [None, None, None, None, None, None]
[2026-02-03 13:28:44,718] INFO in pipeline: Inlet: file_cache_session has 2 cached files
INFO:pipeline:Inlet: file_cache_session has 2 cached files
[2026-02-03 13:28:44,718] INFO in pipeline: Inlet: message_order: []
INFO:pipeline:Inlet: message_order: []
[2026-02-03 13:28:44,720] INFO in pipeline: _update_messages_with_files: file_cache has 2 entries
INFO:pipeline:_update_messages_with_files: file_cache has 2 entries
[2026-02-03 13:28:44,720] INFO in pipeline: _update_messages_with_files: files_by_message keys: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:_update_messages_with_files: files_by_message keys: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:28:44,720] INFO in pipeline: _update_messages_with_files: message_order: ['64e46ab7-02f0-4508-8cdc-9967d2779ce7']
INFO:pipeline:_update_messages_with_files: message_order: ['64e46ab7-02f0-4508-8cdc-9967d2779ce7']
[2026-02-03 13:28:44,720] INFO in pipeline: Message (no id, index 0): using target_message_id 64e46ab7-02f0-4508-8cdc-9967d2779ce7, found 0 files
INFO:pipeline:Message (no id, index 0): using target_message_id 64e46ab7-02f0-4508-8cdc-9967d2779ce7, found 0 files
[2026-02-03 13:28:44,720] WARNING in pipeline: Message (no id, index 1): index 1 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 1): index 1 >= message_order length 1, no files found
[2026-02-03 13:28:44,720] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:28:44,720] INFO in pipeline:   Current message_order: ['64e46ab7-02f0-4508-8cdc-9967d2779ce7']
INFO:pipeline:  Current message_order: ['64e46ab7-02f0-4508-8cdc-9967d2779ce7']
[2026-02-03 13:28:44,720] WARNING in pipeline: Message (no id, index 2): index 2 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 2): index 2 >= message_order length 1, no files found
[2026-02-03 13:28:44,720] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:28:44,720] INFO in pipeline:   Current message_order: ['64e46ab7-02f0-4508-8cdc-9967d2779ce7']
INFO:pipeline:  Current message_order: ['64e46ab7-02f0-4508-8cdc-9967d2779ce7']
[2026-02-03 13:28:44,720] WARNING in pipeline: Message (no id, index 3): index 3 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 3): index 3 >= message_order length 1, no files found
[2026-02-03 13:28:44,720] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:28:44,720] INFO in pipeline:   Current message_order: ['64e46ab7-02f0-4508-8cdc-9967d2779ce7']
INFO:pipeline:  Current message_order: ['64e46ab7-02f0-4508-8cdc-9967d2779ce7']
[2026-02-03 13:28:44,720] WARNING in pipeline: Message (no id, index 4): index 4 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 4): index 4 >= message_order length 1, no files found
[2026-02-03 13:28:44,720] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:28:44,720] INFO in pipeline:   Current message_order: ['64e46ab7-02f0-4508-8cdc-9967d2779ce7']
INFO:pipeline:  Current message_order: ['64e46ab7-02f0-4508-8cdc-9967d2779ce7']
[2026-02-03 13:28:44,720] WARNING in pipeline: Message (no id, index 5): index 5 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 5): index 5 >= message_order length 1, no files found
[2026-02-03 13:28:44,720] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:28:44,720] INFO in pipeline:   Current message_order: ['64e46ab7-02f0-4508-8cdc-9967d2779ce7']
INFO:pipeline:  Current message_order: ['64e46ab7-02f0-4508-8cdc-9967d2779ce7']
INFO:     172.19.0.1:49458 - "POST /pipeline/filter/inlet HTTP/1.1" 200 OK
INFO:     172.19.0.1:49472 - "GET /models HTTP/1.1" 200 OK
pipeline
pipeline
INFO:     172.19.0.1:49484 - "POST /chat/completions HTTP/1.1" 200 OK
[2026-02-03 13:28:44,829] INFO in pipeline: Starting OCR pipeline
INFO:pipeline:Starting OCR pipeline
[2026-02-03 13:28:44,829] INFO in pipeline: Streaming mode enabled for OCR pipeline
INFO:pipeline:Streaming mode enabled for OCR pipeline
[2026-02-03 13:28:44,829] INFO in pipeline: Starting VLM streaming invocation
INFO:pipeline:Starting VLM streaming invocation
[2026-02-03 13:28:53,446] INFO in pipeline: VLM streaming invocation completed
INFO:pipeline:VLM streaming invocation completed
INFO:     172.19.0.1:59960 - "POST /pipeline/filter/outlet HTTP/1.1" 200 OK
[2026-02-03 13:28:59,435] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
[2026-02-03 13:28:59,435] INFO in pipeline: Inlet: received 13 messages, current_message_id: 3a16c1bf-e647-478e-9404-d383549e106b
INFO:pipeline:Inlet: received 13 messages, current_message_id: 3a16c1bf-e647-478e-9404-d383549e106b
[2026-02-03 13:28:59,435] INFO in pipeline: Inlet: user messages IDs: [None, None, None, None, None, None, None]
INFO:pipeline:Inlet: user messages IDs: [None, None, None, None, None, None, None]
[2026-02-03 13:28:59,435] INFO in pipeline: Inlet: file_cache_session has 2 cached files
INFO:pipeline:Inlet: file_cache_session has 2 cached files
[2026-02-03 13:28:59,435] INFO in pipeline: Inlet: message_order: []
INFO:pipeline:Inlet: message_order: []
[2026-02-03 13:28:59,436] INFO in pipeline: _update_messages_with_files: file_cache has 2 entries
INFO:pipeline:_update_messages_with_files: file_cache has 2 entries
[2026-02-03 13:28:59,436] INFO in pipeline: _update_messages_with_files: files_by_message keys: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:_update_messages_with_files: files_by_message keys: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:28:59,436] INFO in pipeline: _update_messages_with_files: message_order: ['3a16c1bf-e647-478e-9404-d383549e106b']
INFO:pipeline:_update_messages_with_files: message_order: ['3a16c1bf-e647-478e-9404-d383549e106b']
[2026-02-03 13:28:59,436] INFO in pipeline: Message (no id, index 0): using target_message_id 3a16c1bf-e647-478e-9404-d383549e106b, found 0 files
INFO:pipeline:Message (no id, index 0): using target_message_id 3a16c1bf-e647-478e-9404-d383549e106b, found 0 files
[2026-02-03 13:28:59,436] WARNING in pipeline: Message (no id, index 1): index 1 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 1): index 1 >= message_order length 1, no files found
[2026-02-03 13:28:59,436] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:28:59,436] INFO in pipeline:   Current message_order: ['3a16c1bf-e647-478e-9404-d383549e106b']
INFO:pipeline:  Current message_order: ['3a16c1bf-e647-478e-9404-d383549e106b']
[2026-02-03 13:28:59,436] WARNING in pipeline: Message (no id, index 2): index 2 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 2): index 2 >= message_order length 1, no files found
[2026-02-03 13:28:59,436] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:28:59,436] INFO in pipeline:   Current message_order: ['3a16c1bf-e647-478e-9404-d383549e106b']
INFO:pipeline:  Current message_order: ['3a16c1bf-e647-478e-9404-d383549e106b']
[2026-02-03 13:28:59,436] WARNING in pipeline: Message (no id, index 3): index 3 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 3): index 3 >= message_order length 1, no files found
[2026-02-03 13:28:59,436] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:28:59,436] INFO in pipeline:   Current message_order: ['3a16c1bf-e647-478e-9404-d383549e106b']
INFO:pipeline:  Current message_order: ['3a16c1bf-e647-478e-9404-d383549e106b']
[2026-02-03 13:28:59,436] WARNING in pipeline: Message (no id, index 4): index 4 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 4): index 4 >= message_order length 1, no files found
[2026-02-03 13:28:59,436] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:28:59,436] INFO in pipeline:   Current message_order: ['3a16c1bf-e647-478e-9404-d383549e106b']
INFO:pipeline:  Current message_order: ['3a16c1bf-e647-478e-9404-d383549e106b']
[2026-02-03 13:28:59,436] WARNING in pipeline: Message (no id, index 5): index 5 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 5): index 5 >= message_order length 1, no files found
[2026-02-03 13:28:59,436] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:28:59,436] INFO in pipeline:   Current message_order: ['3a16c1bf-e647-478e-9404-d383549e106b']
INFO:pipeline:  Current message_order: ['3a16c1bf-e647-478e-9404-d383549e106b']
[2026-02-03 13:28:59,436] WARNING in pipeline: Message (no id, index 6): index 6 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 6): index 6 >= message_order length 1, no files found
[2026-02-03 13:28:59,436] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:28:59,436] INFO in pipeline:   Current message_order: ['3a16c1bf-e647-478e-9404-d383549e106b']
INFO:pipeline:  Current message_order: ['3a16c1bf-e647-478e-9404-d383549e106b']
INFO:     172.19.0.1:59968 - "POST /pipeline/filter/inlet HTTP/1.1" 200 OK
INFO:     172.19.0.1:50386 - "GET /models HTTP/1.1" 200 OK
pipeline
pipeline
INFO:     172.19.0.1:50400 - "POST /chat/completions HTTP/1.1" 200 OK
[2026-02-03 13:28:59,551] INFO in pipeline: Starting OCR pipeline
INFO:pipeline:Starting OCR pipeline
[2026-02-03 13:28:59,551] INFO in pipeline: Streaming mode enabled for OCR pipeline
INFO:pipeline:Streaming mode enabled for OCR pipeline
[2026-02-03 13:28:59,551] INFO in pipeline: Starting VLM streaming invocation
INFO:pipeline:Starting VLM streaming invocation
[2026-02-03 13:29:13,163] INFO in pipeline: VLM streaming invocation completed
INFO:pipeline:VLM streaming invocation completed
INFO:     172.19.0.1:49358 - "POST /pipeline/filter/outlet HTTP/1.1" 200 OK
[2026-02-03 13:29:14,443] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
[2026-02-03 13:29:14,443] INFO in pipeline: Inlet: received 15 messages, current_message_id: 6a703f15-4533-47aa-a399-85fb55574cf8
INFO:pipeline:Inlet: received 15 messages, current_message_id: 6a703f15-4533-47aa-a399-85fb55574cf8
[2026-02-03 13:29:14,443] INFO in pipeline: Inlet: user messages IDs: [None, None, None, None, None, None, None, None]
INFO:pipeline:Inlet: user messages IDs: [None, None, None, None, None, None, None, None]
[2026-02-03 13:29:14,443] INFO in pipeline: Inlet: file_cache_session has 2 cached files
INFO:pipeline:Inlet: file_cache_session has 2 cached files
[2026-02-03 13:29:14,443] INFO in pipeline: Inlet: message_order: []
INFO:pipeline:Inlet: message_order: []
[2026-02-03 13:29:14,444] INFO in pipeline: _update_messages_with_files: file_cache has 2 entries
INFO:pipeline:_update_messages_with_files: file_cache has 2 entries
[2026-02-03 13:29:14,445] INFO in pipeline: _update_messages_with_files: files_by_message keys: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:_update_messages_with_files: files_by_message keys: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:29:14,445] INFO in pipeline: _update_messages_with_files: message_order: ['6a703f15-4533-47aa-a399-85fb55574cf8']
INFO:pipeline:_update_messages_with_files: message_order: ['6a703f15-4533-47aa-a399-85fb55574cf8']
[2026-02-03 13:29:14,445] INFO in pipeline: Message (no id, index 0): using target_message_id 6a703f15-4533-47aa-a399-85fb55574cf8, found 0 files
INFO:pipeline:Message (no id, index 0): using target_message_id 6a703f15-4533-47aa-a399-85fb55574cf8, found 0 files
[2026-02-03 13:29:14,445] WARNING in pipeline: Message (no id, index 1): index 1 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 1): index 1 >= message_order length 1, no files found
[2026-02-03 13:29:14,445] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:29:14,445] INFO in pipeline:   Current message_order: ['6a703f15-4533-47aa-a399-85fb55574cf8']
INFO:pipeline:  Current message_order: ['6a703f15-4533-47aa-a399-85fb55574cf8']
[2026-02-03 13:29:14,445] WARNING in pipeline: Message (no id, index 2): index 2 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 2): index 2 >= message_order length 1, no files found
[2026-02-03 13:29:14,445] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:29:14,445] INFO in pipeline:   Current message_order: ['6a703f15-4533-47aa-a399-85fb55574cf8']
INFO:pipeline:  Current message_order: ['6a703f15-4533-47aa-a399-85fb55574cf8']
[2026-02-03 13:29:14,445] WARNING in pipeline: Message (no id, index 3): index 3 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 3): index 3 >= message_order length 1, no files found
[2026-02-03 13:29:14,445] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:29:14,445] INFO in pipeline:   Current message_order: ['6a703f15-4533-47aa-a399-85fb55574cf8']
INFO:pipeline:  Current message_order: ['6a703f15-4533-47aa-a399-85fb55574cf8']
[2026-02-03 13:29:14,445] WARNING in pipeline: Message (no id, index 4): index 4 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 4): index 4 >= message_order length 1, no files found
[2026-02-03 13:29:14,445] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:29:14,445] INFO in pipeline:   Current message_order: ['6a703f15-4533-47aa-a399-85fb55574cf8']
INFO:pipeline:  Current message_order: ['6a703f15-4533-47aa-a399-85fb55574cf8']
[2026-02-03 13:29:14,445] WARNING in pipeline: Message (no id, index 5): index 5 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 5): index 5 >= message_order length 1, no files found
[2026-02-03 13:29:14,445] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:29:14,445] INFO in pipeline:   Current message_order: ['6a703f15-4533-47aa-a399-85fb55574cf8']
INFO:pipeline:  Current message_order: ['6a703f15-4533-47aa-a399-85fb55574cf8']
[2026-02-03 13:29:14,445] WARNING in pipeline: Message (no id, index 6): index 6 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 6): index 6 >= message_order length 1, no files found
[2026-02-03 13:29:14,445] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:29:14,445] INFO in pipeline:   Current message_order: ['6a703f15-4533-47aa-a399-85fb55574cf8']
INFO:pipeline:  Current message_order: ['6a703f15-4533-47aa-a399-85fb55574cf8']
[2026-02-03 13:29:14,445] WARNING in pipeline: Message (no id, index 7): index 7 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 7): index 7 >= message_order length 1, no files found
[2026-02-03 13:29:14,445] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479']
[2026-02-03 13:29:14,445] INFO in pipeline:   Current message_order: ['6a703f15-4533-47aa-a399-85fb55574cf8']
INFO:pipeline:  Current message_order: ['6a703f15-4533-47aa-a399-85fb55574cf8']
INFO:     172.19.0.1:49368 - "POST /pipeline/filter/inlet HTTP/1.1" 200 OK
INFO:     172.19.0.1:49374 - "GET /models HTTP/1.1" 200 OK
pipeline
pipeline
INFO:     172.19.0.1:49378 - "POST /chat/completions HTTP/1.1" 200 OK
[2026-02-03 13:29:14,591] INFO in pipeline: Starting OCR pipeline
INFO:pipeline:Starting OCR pipeline
[2026-02-03 13:29:14,591] INFO in pipeline: Streaming mode enabled for OCR pipeline
INFO:pipeline:Streaming mode enabled for OCR pipeline
[2026-02-03 13:29:14,591] INFO in pipeline: Starting VLM streaming invocation
INFO:pipeline:Starting VLM streaming invocation
[2026-02-03 13:29:28,435] INFO in pipeline: VLM streaming invocation completed
INFO:pipeline:VLM streaming invocation completed
INFO:     172.19.0.1:42556 - "POST /pipeline/filter/outlet HTTP/1.1" 200 OK
[2026-02-03 13:29:47,132] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
[2026-02-03 13:29:47,132] INFO in pipeline: Inlet: received 17 messages, current_message_id: f979a313-c8d3-4ad5-80ce-175ff3b53288
INFO:pipeline:Inlet: received 17 messages, current_message_id: f979a313-c8d3-4ad5-80ce-175ff3b53288
[2026-02-03 13:29:47,132] INFO in pipeline: Inlet: user messages IDs: [None, None, None, None, None, None, None, None, None]
INFO:pipeline:Inlet: user messages IDs: [None, None, None, None, None, None, None, None, None]
[2026-02-03 13:29:47,132] INFO in pipeline: Inlet: file_cache_session has 2 cached files
INFO:pipeline:Inlet: file_cache_session has 2 cached files
[2026-02-03 13:29:47,132] INFO in pipeline: Inlet: message_order: []
INFO:pipeline:Inlet: message_order: []
Creating model: ('PP-LCNet_x1_0_doc_ori', 'pipelines/PP-LCNet_x1_0_doc_ori')
Creating model: ('PP-DocLayoutV2', 'pipelines/PP-DocLayoutV2')
Creating model: ('PaddleOCR-VL-0.9B', None)
[2026-02-03 13:29:47,860] INFO in pipeline: PaddleOCRVL started for PDF OCR
INFO:pipeline:PaddleOCRVL started for PDF OCR
[2026-02-03 13:29:57,441] INFO in pipeline: Cached OCR result for 6.pdf (id: 92bfddfa-d4e2-4a38-88a4-90771f280d1a) for message_id: f979a313-c8d3-4ad5-80ce-175ff3b53288
INFO:pipeline:Cached OCR result for 6.pdf (id: 92bfddfa-d4e2-4a38-88a4-90771f280d1a) for message_id: f979a313-c8d3-4ad5-80ce-175ff3b53288
[2026-02-03 13:29:57,715] INFO in pipeline: _update_messages_with_files: file_cache has 3 entries
INFO:pipeline:_update_messages_with_files: file_cache has 3 entries
[2026-02-03 13:29:57,715] INFO in pipeline: _update_messages_with_files: files_by_message keys: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:_update_messages_with_files: files_by_message keys: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:29:57,715] INFO in pipeline: _update_messages_with_files: message_order: ['f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:_update_messages_with_files: message_order: ['f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:29:57,715] INFO in pipeline: Message (no id, index 0): using target_message_id f979a313-c8d3-4ad5-80ce-175ff3b53288, found 1 files
INFO:pipeline:Message (no id, index 0): using target_message_id f979a313-c8d3-4ad5-80ce-175ff3b53288, found 1 files
[2026-02-03 13:29:57,716] INFO in pipeline:   Files: ['6.pdf']
INFO:pipeline:  Files: ['6.pdf']
[2026-02-03 13:29:57,716] WARNING in pipeline: Message (no id, index 1): index 1 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 1): index 1 >= message_order length 1, no files found
[2026-02-03 13:29:57,716] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:29:57,716] INFO in pipeline:   Current message_order: ['f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Current message_order: ['f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:29:57,716] WARNING in pipeline: Message (no id, index 2): index 2 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 2): index 2 >= message_order length 1, no files found
[2026-02-03 13:29:57,716] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:29:57,716] INFO in pipeline:   Current message_order: ['f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Current message_order: ['f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:29:57,716] WARNING in pipeline: Message (no id, index 3): index 3 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 3): index 3 >= message_order length 1, no files found
[2026-02-03 13:29:57,716] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:29:57,716] INFO in pipeline:   Current message_order: ['f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Current message_order: ['f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:29:57,716] WARNING in pipeline: Message (no id, index 4): index 4 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 4): index 4 >= message_order length 1, no files found
[2026-02-03 13:29:57,716] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:29:57,716] INFO in pipeline:   Current message_order: ['f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Current message_order: ['f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:29:57,716] WARNING in pipeline: Message (no id, index 5): index 5 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 5): index 5 >= message_order length 1, no files found
[2026-02-03 13:29:57,716] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:29:57,716] INFO in pipeline:   Current message_order: ['f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Current message_order: ['f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:29:57,716] WARNING in pipeline: Message (no id, index 6): index 6 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 6): index 6 >= message_order length 1, no files found
[2026-02-03 13:29:57,716] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:29:57,716] INFO in pipeline:   Current message_order: ['f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Current message_order: ['f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:29:57,716] WARNING in pipeline: Message (no id, index 7): index 7 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 7): index 7 >= message_order length 1, no files found
[2026-02-03 13:29:57,716] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:29:57,716] INFO in pipeline:   Current message_order: ['f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Current message_order: ['f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:29:57,716] WARNING in pipeline: Message (no id, index 8): index 8 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 8): index 8 >= message_order length 1, no files found
[2026-02-03 13:29:57,716] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:29:57,716] INFO in pipeline:   Current message_order: ['f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Current message_order: ['f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:     172.19.0.1:59660 - "POST /pipeline/filter/inlet HTTP/1.1" 200 OK
INFO:     172.19.0.1:53642 - "GET /models HTTP/1.1" 200 OK
pipeline
pipeline
INFO:     172.19.0.1:53650 - "POST /chat/completions HTTP/1.1" 200 OK
[2026-02-03 13:29:57,875] INFO in pipeline: Starting OCR pipeline
INFO:pipeline:Starting OCR pipeline
[2026-02-03 13:29:57,875] INFO in pipeline: Streaming mode enabled for OCR pipeline
INFO:pipeline:Streaming mode enabled for OCR pipeline
[2026-02-03 13:29:57,875] INFO in pipeline: Starting VLM streaming invocation
INFO:pipeline:Starting VLM streaming invocation
[2026-02-03 13:30:25,219] INFO in pipeline: VLM streaming invocation completed
INFO:pipeline:VLM streaming invocation completed
INFO:     172.19.0.1:36548 - "POST /pipeline/filter/outlet HTTP/1.1" 200 OK
[2026-02-03 13:31:26,592] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
[2026-02-03 13:31:26,592] INFO in pipeline: Inlet: received 19 messages, current_message_id: 7586a44b-1f33-4f3c-8f54-c6f9ef98fc99
INFO:pipeline:Inlet: received 19 messages, current_message_id: 7586a44b-1f33-4f3c-8f54-c6f9ef98fc99
[2026-02-03 13:31:26,592] INFO in pipeline: Inlet: user messages IDs: [None, None, None, None, None, None, None, None, None, None]
INFO:pipeline:Inlet: user messages IDs: [None, None, None, None, None, None, None, None, None, None]
[2026-02-03 13:31:26,592] INFO in pipeline: Inlet: file_cache_session has 3 cached files
INFO:pipeline:Inlet: file_cache_session has 3 cached files
[2026-02-03 13:31:26,592] INFO in pipeline: Inlet: message_order: []
INFO:pipeline:Inlet: message_order: []
[2026-02-03 13:31:26,593] INFO in pipeline: _update_messages_with_files: file_cache has 3 entries
INFO:pipeline:_update_messages_with_files: file_cache has 3 entries
[2026-02-03 13:31:26,593] INFO in pipeline: _update_messages_with_files: files_by_message keys: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:_update_messages_with_files: files_by_message keys: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:31:26,593] INFO in pipeline: _update_messages_with_files: message_order: ['7586a44b-1f33-4f3c-8f54-c6f9ef98fc99']
INFO:pipeline:_update_messages_with_files: message_order: ['7586a44b-1f33-4f3c-8f54-c6f9ef98fc99']
[2026-02-03 13:31:26,593] INFO in pipeline: Message (no id, index 0): using target_message_id 7586a44b-1f33-4f3c-8f54-c6f9ef98fc99, found 0 files
INFO:pipeline:Message (no id, index 0): using target_message_id 7586a44b-1f33-4f3c-8f54-c6f9ef98fc99, found 0 files
[2026-02-03 13:31:26,593] WARNING in pipeline: Message (no id, index 1): index 1 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 1): index 1 >= message_order length 1, no files found
[2026-02-03 13:31:26,593] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:31:26,593] INFO in pipeline:   Current message_order: ['7586a44b-1f33-4f3c-8f54-c6f9ef98fc99']
INFO:pipeline:  Current message_order: ['7586a44b-1f33-4f3c-8f54-c6f9ef98fc99']
[2026-02-03 13:31:26,593] WARNING in pipeline: Message (no id, index 2): index 2 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 2): index 2 >= message_order length 1, no files found
[2026-02-03 13:31:26,593] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:31:26,593] INFO in pipeline:   Current message_order: ['7586a44b-1f33-4f3c-8f54-c6f9ef98fc99']
INFO:pipeline:  Current message_order: ['7586a44b-1f33-4f3c-8f54-c6f9ef98fc99']
[2026-02-03 13:31:26,593] WARNING in pipeline: Message (no id, index 3): index 3 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 3): index 3 >= message_order length 1, no files found
[2026-02-03 13:31:26,593] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:31:26,593] INFO in pipeline:   Current message_order: ['7586a44b-1f33-4f3c-8f54-c6f9ef98fc99']
INFO:pipeline:  Current message_order: ['7586a44b-1f33-4f3c-8f54-c6f9ef98fc99']
[2026-02-03 13:31:26,593] WARNING in pipeline: Message (no id, index 4): index 4 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 4): index 4 >= message_order length 1, no files found
[2026-02-03 13:31:26,593] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:31:26,593] INFO in pipeline:   Current message_order: ['7586a44b-1f33-4f3c-8f54-c6f9ef98fc99']
INFO:pipeline:  Current message_order: ['7586a44b-1f33-4f3c-8f54-c6f9ef98fc99']
[2026-02-03 13:31:26,593] WARNING in pipeline: Message (no id, index 5): index 5 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 5): index 5 >= message_order length 1, no files found
[2026-02-03 13:31:26,593] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:31:26,593] INFO in pipeline:   Current message_order: ['7586a44b-1f33-4f3c-8f54-c6f9ef98fc99']
INFO:pipeline:  Current message_order: ['7586a44b-1f33-4f3c-8f54-c6f9ef98fc99']
[2026-02-03 13:31:26,593] WARNING in pipeline: Message (no id, index 6): index 6 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 6): index 6 >= message_order length 1, no files found
[2026-02-03 13:31:26,593] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:31:26,593] INFO in pipeline:   Current message_order: ['7586a44b-1f33-4f3c-8f54-c6f9ef98fc99']
INFO:pipeline:  Current message_order: ['7586a44b-1f33-4f3c-8f54-c6f9ef98fc99']
[2026-02-03 13:31:26,593] WARNING in pipeline: Message (no id, index 7): index 7 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 7): index 7 >= message_order length 1, no files found
[2026-02-03 13:31:26,593] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:31:26,593] INFO in pipeline:   Current message_order: ['7586a44b-1f33-4f3c-8f54-c6f9ef98fc99']
INFO:pipeline:  Current message_order: ['7586a44b-1f33-4f3c-8f54-c6f9ef98fc99']
[2026-02-03 13:31:26,593] WARNING in pipeline: Message (no id, index 8): index 8 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 8): index 8 >= message_order length 1, no files found
[2026-02-03 13:31:26,593] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:31:26,593] INFO in pipeline:   Current message_order: ['7586a44b-1f33-4f3c-8f54-c6f9ef98fc99']
INFO:pipeline:  Current message_order: ['7586a44b-1f33-4f3c-8f54-c6f9ef98fc99']
[2026-02-03 13:31:26,593] WARNING in pipeline: Message (no id, index 9): index 9 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 9): index 9 >= message_order length 1, no files found
[2026-02-03 13:31:26,593] INFO in pipeline:   Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
INFO:pipeline:  Available message_ids in cache: ['e0b502bf-f4ba-47f8-9a89-b479b72bf4af', '6c035439-0134-4c4d-8afb-f1f115520479', 'f979a313-c8d3-4ad5-80ce-175ff3b53288']
[2026-02-03 13:31:26,593] INFO in pipeline:   Current message_order: ['7586a44b-1f33-4f3c-8f54-c6f9ef98fc99']
INFO:pipeline:  Current message_order: ['7586a44b-1f33-4f3c-8f54-c6f9ef98fc99']
INFO:     172.19.0.1:46044 - "POST /pipeline/filter/inlet HTTP/1.1" 200 OK
INFO:     172.19.0.1:46052 - "GET /models HTTP/1.1" 200 OK
pipeline
pipeline
INFO:     172.19.0.1:46062 - "POST /chat/completions HTTP/1.1" 200 OK
[2026-02-03 13:31:26,746] INFO in pipeline: Starting OCR pipeline
INFO:pipeline:Starting OCR pipeline
[2026-02-03 13:31:26,746] INFO in pipeline: Streaming mode enabled for OCR pipeline
INFO:pipeline:Streaming mode enabled for OCR pipeline
[2026-02-03 13:31:26,746] INFO in pipeline: Starting VLM streaming invocation
INFO:pipeline:Starting VLM streaming invocation
[2026-02-03 13:31:33,340] INFO in pipeline: VLM streaming invocation completed
INFO:pipeline:VLM streaming invocation completed
INFO:     172.19.0.1:44804 - "POST /pipeline/filter/outlet HTTP/1.1" 200 OK
[2026-02-03 13:32:34,480] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
[2026-02-03 13:32:34,480] INFO in pipeline: Inlet: received 1 messages, current_message_id: e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb
INFO:pipeline:Inlet: received 1 messages, current_message_id: e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb
[2026-02-03 13:32:34,480] INFO in pipeline: Inlet: user messages IDs: [None]
INFO:pipeline:Inlet: user messages IDs: [None]
[2026-02-03 13:32:34,480] INFO in pipeline: Inlet: file_cache_session has 0 cached files
INFO:pipeline:Inlet: file_cache_session has 0 cached files
[2026-02-03 13:32:34,480] INFO in pipeline: Inlet: message_order: []
INFO:pipeline:Inlet: message_order: []
Creating model: ('PP-LCNet_x1_0_doc_ori', 'pipelines/PP-LCNet_x1_0_doc_ori')
Creating model: ('PP-DocLayoutV2', 'pipelines/PP-DocLayoutV2')
Creating model: ('PaddleOCR-VL-0.9B', None)
[2026-02-03 13:32:35,452] INFO in pipeline: PaddleOCRVL started for PDF OCR
INFO:pipeline:PaddleOCRVL started for PDF OCR
[2026-02-03 13:32:45,342] INFO in pipeline: Cached OCR result for 2.pdf (id: e444ef9e-bf24-40e9-90e1-e72ba4811720) for message_id: e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb
INFO:pipeline:Cached OCR result for 2.pdf (id: e444ef9e-bf24-40e9-90e1-e72ba4811720) for message_id: e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb
[2026-02-03 13:32:52,633] INFO in pipeline: Cached OCR result for 3.pdf (id: 29c92f1b-df7b-4ba7-b352-88c7a47917b9) for message_id: e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb
INFO:pipeline:Cached OCR result for 3.pdf (id: 29c92f1b-df7b-4ba7-b352-88c7a47917b9) for message_id: e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb
[2026-02-03 13:32:52,864] INFO in pipeline: _update_messages_with_files: file_cache has 2 entries
INFO:pipeline:_update_messages_with_files: file_cache has 2 entries
[2026-02-03 13:32:52,864] INFO in pipeline: _update_messages_with_files: files_by_message keys: ['e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb']
INFO:pipeline:_update_messages_with_files: files_by_message keys: ['e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb']
[2026-02-03 13:32:52,864] INFO in pipeline: _update_messages_with_files: message_order: ['e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb']
INFO:pipeline:_update_messages_with_files: message_order: ['e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb']
[2026-02-03 13:32:52,864] INFO in pipeline: Message (no id, index 0): using target_message_id e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb, found 2 files
INFO:pipeline:Message (no id, index 0): using target_message_id e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb, found 2 files
[2026-02-03 13:32:52,864] INFO in pipeline:   Files: ['2.pdf', '3.pdf']
INFO:pipeline:  Files: ['2.pdf', '3.pdf']
INFO:     172.19.0.1:42816 - "POST /pipeline/filter/inlet HTTP/1.1" 200 OK
INFO:     172.19.0.1:57064 - "GET /models HTTP/1.1" 200 OK
pipeline
pipeline
INFO:     172.19.0.1:57074 - "POST /chat/completions HTTP/1.1" 200 OK
[2026-02-03 13:32:52,947] INFO in pipeline: Starting OCR pipeline
INFO:pipeline:Starting OCR pipeline
[2026-02-03 13:32:52,948] INFO in pipeline: Streaming mode enabled for OCR pipeline
INFO:pipeline:Streaming mode enabled for OCR pipeline
[2026-02-03 13:32:52,948] INFO in pipeline: Starting VLM streaming invocation
INFO:pipeline:Starting VLM streaming invocation
[2026-02-03 13:35:30,055] INFO in pipeline: VLM streaming invocation completed
INFO:pipeline:VLM streaming invocation completed
[2026-02-03 13:37:01,609] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
[2026-02-03 13:37:01,609] INFO in pipeline: Inlet: received 3 messages, current_message_id: 91bf28ef-eb48-4019-9049-c3ba1dc5ced2
INFO:pipeline:Inlet: received 3 messages, current_message_id: 91bf28ef-eb48-4019-9049-c3ba1dc5ced2
[2026-02-03 13:37:01,609] INFO in pipeline: Inlet: user messages IDs: [None, None]
INFO:pipeline:Inlet: user messages IDs: [None, None]
[2026-02-03 13:37:01,609] INFO in pipeline: Inlet: file_cache_session has 2 cached files
INFO:pipeline:Inlet: file_cache_session has 2 cached files
[2026-02-03 13:37:01,609] INFO in pipeline: Inlet: message_order: []
INFO:pipeline:Inlet: message_order: []
[2026-02-03 13:37:01,611] INFO in pipeline: _update_messages_with_files: file_cache has 2 entries
INFO:pipeline:_update_messages_with_files: file_cache has 2 entries
[2026-02-03 13:37:01,611] INFO in pipeline: _update_messages_with_files: files_by_message keys: ['e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb']
INFO:pipeline:_update_messages_with_files: files_by_message keys: ['e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb']
[2026-02-03 13:37:01,611] INFO in pipeline: _update_messages_with_files: message_order: ['91bf28ef-eb48-4019-9049-c3ba1dc5ced2']
INFO:pipeline:_update_messages_with_files: message_order: ['91bf28ef-eb48-4019-9049-c3ba1dc5ced2']
[2026-02-03 13:37:01,611] INFO in pipeline: Message (no id, index 0): using target_message_id 91bf28ef-eb48-4019-9049-c3ba1dc5ced2, found 0 files
INFO:pipeline:Message (no id, index 0): using target_message_id 91bf28ef-eb48-4019-9049-c3ba1dc5ced2, found 0 files
[2026-02-03 13:37:01,611] WARNING in pipeline: Message (no id, index 1): index 1 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 1): index 1 >= message_order length 1, no files found
[2026-02-03 13:37:01,611] INFO in pipeline:   Available message_ids in cache: ['e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb']
INFO:pipeline:  Available message_ids in cache: ['e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb']
[2026-02-03 13:37:01,611] INFO in pipeline:   Current message_order: ['91bf28ef-eb48-4019-9049-c3ba1dc5ced2']
INFO:pipeline:  Current message_order: ['91bf28ef-eb48-4019-9049-c3ba1dc5ced2']
INFO:     172.19.0.1:48776 - "POST /pipeline/filter/inlet HTTP/1.1" 200 OK
INFO:     172.19.0.1:48778 - "GET /models HTTP/1.1" 200 OK
pipeline
pipeline
INFO:     172.19.0.1:48782 - "POST /chat/completions HTTP/1.1" 200 OK
[2026-02-03 13:37:01,701] INFO in pipeline: Starting OCR pipeline
INFO:pipeline:Starting OCR pipeline
[2026-02-03 13:37:01,701] INFO in pipeline: Streaming mode enabled for OCR pipeline
INFO:pipeline:Streaming mode enabled for OCR pipeline
[2026-02-03 13:37:01,701] INFO in pipeline: Starting VLM streaming invocation
INFO:pipeline:Starting VLM streaming invocation
[2026-02-03 13:37:09,961] INFO in pipeline: VLM streaming invocation completed
INFO:pipeline:VLM streaming invocation completed
INFO:     172.19.0.1:34650 - "POST /pipeline/filter/outlet HTTP/1.1" 200 OK
[2026-02-03 13:37:21,217] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
[2026-02-03 13:37:21,217] INFO in pipeline: Inlet: received 5 messages, current_message_id: e21f91b7-944a-418b-bcf5-5434fe77ae50
INFO:pipeline:Inlet: received 5 messages, current_message_id: e21f91b7-944a-418b-bcf5-5434fe77ae50
[2026-02-03 13:37:21,217] INFO in pipeline: Inlet: user messages IDs: [None, None, None]
INFO:pipeline:Inlet: user messages IDs: [None, None, None]
[2026-02-03 13:37:21,217] INFO in pipeline: Inlet: file_cache_session has 2 cached files
INFO:pipeline:Inlet: file_cache_session has 2 cached files
[2026-02-03 13:37:21,217] INFO in pipeline: Inlet: message_order: []
INFO:pipeline:Inlet: message_order: []
[2026-02-03 13:37:21,219] INFO in pipeline: _update_messages_with_files: file_cache has 2 entries
INFO:pipeline:_update_messages_with_files: file_cache has 2 entries
[2026-02-03 13:37:21,219] INFO in pipeline: _update_messages_with_files: files_by_message keys: ['e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb']
INFO:pipeline:_update_messages_with_files: files_by_message keys: ['e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb']
[2026-02-03 13:37:21,219] INFO in pipeline: _update_messages_with_files: message_order: ['e21f91b7-944a-418b-bcf5-5434fe77ae50']
INFO:pipeline:_update_messages_with_files: message_order: ['e21f91b7-944a-418b-bcf5-5434fe77ae50']
[2026-02-03 13:37:21,219] INFO in pipeline: Message (no id, index 0): using target_message_id e21f91b7-944a-418b-bcf5-5434fe77ae50, found 0 files
INFO:pipeline:Message (no id, index 0): using target_message_id e21f91b7-944a-418b-bcf5-5434fe77ae50, found 0 files
[2026-02-03 13:37:21,219] WARNING in pipeline: Message (no id, index 1): index 1 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 1): index 1 >= message_order length 1, no files found
[2026-02-03 13:37:21,219] INFO in pipeline:   Available message_ids in cache: ['e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb']
INFO:pipeline:  Available message_ids in cache: ['e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb']
[2026-02-03 13:37:21,219] INFO in pipeline:   Current message_order: ['e21f91b7-944a-418b-bcf5-5434fe77ae50']
INFO:pipeline:  Current message_order: ['e21f91b7-944a-418b-bcf5-5434fe77ae50']
[2026-02-03 13:37:21,219] WARNING in pipeline: Message (no id, index 2): index 2 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 2): index 2 >= message_order length 1, no files found
[2026-02-03 13:37:21,219] INFO in pipeline:   Available message_ids in cache: ['e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb']
INFO:pipeline:  Available message_ids in cache: ['e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb']
[2026-02-03 13:37:21,219] INFO in pipeline:   Current message_order: ['e21f91b7-944a-418b-bcf5-5434fe77ae50']
INFO:pipeline:  Current message_order: ['e21f91b7-944a-418b-bcf5-5434fe77ae50']
INFO:     172.19.0.1:60118 - "POST /pipeline/filter/inlet HTTP/1.1" 200 OK
INFO:     172.19.0.1:60122 - "GET /models HTTP/1.1" 200 OK
pipeline
pipeline
INFO:     172.19.0.1:60136 - "POST /chat/completions HTTP/1.1" 200 OK
[2026-02-03 13:37:21,336] INFO in pipeline: Starting OCR pipeline
INFO:pipeline:Starting OCR pipeline
[2026-02-03 13:37:21,336] INFO in pipeline: Streaming mode enabled for OCR pipeline
INFO:pipeline:Streaming mode enabled for OCR pipeline
[2026-02-03 13:37:21,336] INFO in pipeline: Starting VLM streaming invocation
INFO:pipeline:Starting VLM streaming invocation
[2026-02-03 13:37:29,841] INFO in pipeline: VLM streaming invocation completed
INFO:pipeline:VLM streaming invocation completed
INFO:     172.19.0.1:33956 - "POST /pipeline/filter/outlet HTTP/1.1" 200 OK
[2026-02-03 13:37:43,776] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
[2026-02-03 13:37:43,776] INFO in pipeline: Inlet: received 7 messages, current_message_id: e4d28c81-33c2-4dc3-9ce0-64ad4c88ceba
INFO:pipeline:Inlet: received 7 messages, current_message_id: e4d28c81-33c2-4dc3-9ce0-64ad4c88ceba
[2026-02-03 13:37:43,776] INFO in pipeline: Inlet: user messages IDs: [None, None, None, None]
INFO:pipeline:Inlet: user messages IDs: [None, None, None, None]
[2026-02-03 13:37:43,776] INFO in pipeline: Inlet: file_cache_session has 2 cached files
INFO:pipeline:Inlet: file_cache_session has 2 cached files
[2026-02-03 13:37:43,776] INFO in pipeline: Inlet: message_order: []
INFO:pipeline:Inlet: message_order: []
Creating model: ('PP-LCNet_x1_0_doc_ori', 'pipelines/PP-LCNet_x1_0_doc_ori')
Creating model: ('PP-DocLayoutV2', 'pipelines/PP-DocLayoutV2')
Creating model: ('PaddleOCR-VL-0.9B', None)
[2026-02-03 13:37:44,734] INFO in pipeline: PaddleOCRVL started for PDF OCR
INFO:pipeline:PaddleOCRVL started for PDF OCR
[2026-02-03 13:37:56,283] INFO in pipeline: Cached OCR result for 6.pdf (id: a6b5bf4a-7835-4350-ae4c-ab7d87b907c3) for message_id: e4d28c81-33c2-4dc3-9ce0-64ad4c88ceba
INFO:pipeline:Cached OCR result for 6.pdf (id: a6b5bf4a-7835-4350-ae4c-ab7d87b907c3) for message_id: e4d28c81-33c2-4dc3-9ce0-64ad4c88ceba
[2026-02-03 13:37:56,553] INFO in pipeline: _update_messages_with_files: file_cache has 3 entries
INFO:pipeline:_update_messages_with_files: file_cache has 3 entries
[2026-02-03 13:37:56,553] INFO in pipeline: _update_messages_with_files: files_by_message keys: ['e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb', 'e4d28c81-33c2-4dc3-9ce0-64ad4c88ceba']
INFO:pipeline:_update_messages_with_files: files_by_message keys: ['e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb', 'e4d28c81-33c2-4dc3-9ce0-64ad4c88ceba']
[2026-02-03 13:37:56,554] INFO in pipeline: _update_messages_with_files: message_order: ['e4d28c81-33c2-4dc3-9ce0-64ad4c88ceba']
INFO:pipeline:_update_messages_with_files: message_order: ['e4d28c81-33c2-4dc3-9ce0-64ad4c88ceba']
[2026-02-03 13:37:56,554] INFO in pipeline: Message (no id, index 0): using target_message_id e4d28c81-33c2-4dc3-9ce0-64ad4c88ceba, found 1 files
INFO:pipeline:Message (no id, index 0): using target_message_id e4d28c81-33c2-4dc3-9ce0-64ad4c88ceba, found 1 files
[2026-02-03 13:37:56,554] INFO in pipeline:   Files: ['6.pdf']
INFO:pipeline:  Files: ['6.pdf']
[2026-02-03 13:37:56,554] WARNING in pipeline: Message (no id, index 1): index 1 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 1): index 1 >= message_order length 1, no files found
[2026-02-03 13:37:56,554] INFO in pipeline:   Available message_ids in cache: ['e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb', 'e4d28c81-33c2-4dc3-9ce0-64ad4c88ceba']
INFO:pipeline:  Available message_ids in cache: ['e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb', 'e4d28c81-33c2-4dc3-9ce0-64ad4c88ceba']
[2026-02-03 13:37:56,554] INFO in pipeline:   Current message_order: ['e4d28c81-33c2-4dc3-9ce0-64ad4c88ceba']
INFO:pipeline:  Current message_order: ['e4d28c81-33c2-4dc3-9ce0-64ad4c88ceba']
[2026-02-03 13:37:56,554] WARNING in pipeline: Message (no id, index 2): index 2 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 2): index 2 >= message_order length 1, no files found
[2026-02-03 13:37:56,554] INFO in pipeline:   Available message_ids in cache: ['e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb', 'e4d28c81-33c2-4dc3-9ce0-64ad4c88ceba']
INFO:pipeline:  Available message_ids in cache: ['e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb', 'e4d28c81-33c2-4dc3-9ce0-64ad4c88ceba']
[2026-02-03 13:37:56,554] INFO in pipeline:   Current message_order: ['e4d28c81-33c2-4dc3-9ce0-64ad4c88ceba']
INFO:pipeline:  Current message_order: ['e4d28c81-33c2-4dc3-9ce0-64ad4c88ceba']
[2026-02-03 13:37:56,554] WARNING in pipeline: Message (no id, index 3): index 3 >= message_order length 1, no files found
WARNING:pipeline:Message (no id, index 3): index 3 >= message_order length 1, no files found
[2026-02-03 13:37:56,554] INFO in pipeline:   Available message_ids in cache: ['e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb', 'e4d28c81-33c2-4dc3-9ce0-64ad4c88ceba']
INFO:pipeline:  Available message_ids in cache: ['e26ea2ea-7b9e-4192-839c-f3b8cefaeaeb', 'e4d28c81-33c2-4dc3-9ce0-64ad4c88ceba']
[2026-02-03 13:37:56,554] INFO in pipeline:   Current message_order: ['e4d28c81-33c2-4dc3-9ce0-64ad4c88ceba']
INFO:pipeline:  Current message_order: ['e4d28c81-33c2-4dc3-9ce0-64ad4c88ceba']
INFO:     172.19.0.1:49930 - "POST /pipeline/filter/inlet HTTP/1.1" 200 OK
INFO:     172.19.0.1:46136 - "GET /models HTTP/1.1" 200 OK
pipeline
pipeline
INFO:     172.19.0.1:46142 - "POST /chat/completions HTTP/1.1" 200 OK
[2026-02-03 13:37:56,663] INFO in pipeline: Starting OCR pipeline
INFO:pipeline:Starting OCR pipeline
[2026-02-03 13:37:56,663] INFO in pipeline: Streaming mode enabled for OCR pipeline
INFO:pipeline:Streaming mode enabled for OCR pipeline
[2026-02-03 13:37:56,663] INFO in pipeline: Starting VLM streaming invocation
INFO:pipeline:Starting VLM streaming invocation
[2026-02-03 13:40:16,594] INFO in pipeline: VLM streaming invocation completed
INFO:pipeline:VLM streaming invocation completed
INFO:     172.19.0.1:44210 - "GET /models HTTP/1.1" 200 OK

### Ответ модели на последнее сообщение с прикрепленным 6.pdf
Ты уже прислал файл 6.pdf, и я провёл OCR — текст из него полностью распознан и представлен выше в чистом виде.

Если ты хочешь, чтобы я:

Вывел только распознанный текст без комментариев — вот он:
Бухгалтерский баланс
На 31 декабря 2024 года
Организация — Общество с ограниченной ответственностью "Ндоросль"
Учетный номер плательщика — 117821782
Вид экономической деятельности — Розничная торговля книгами
Организационно-правовая форма — Общество с ограниченной ответственностью
Орган управления — Без ведомственного подчинения
Единица измерения — Тыс. руб.
Адрес — 000011, г. Город, ул. Шестого мая, 12-18Б, пом.14