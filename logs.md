INFO:     172.19.0.1:54830 - "POST /chat/completions HTTP/1.1" 200 OK
[2026-02-12 14:17:18,580] INFO in pipeline: Starting OCR pipeline
INFO:pipeline:Starting OCR pipeline
[2026-02-12 14:17:18,580] INFO in pipeline: Streaming mode enabled for OCR pipeline
INFO:pipeline:Streaming mode enabled for OCR pipeline
[2026-02-12 14:17:18,580] INFO in pipeline: Starting VLM streaming invocation
INFO:pipeline:Starting VLM streaming invocation
[2026-02-12 14:17:21,086] INFO in pipeline: VLM streaming invocation completed
INFO:pipeline:VLM streaming invocation completed
INFO:     172.19.0.1:54844 - "POST /pipeline/filter/outlet HTTP/1.1" 200 OK
[2026-02-12 14:18:51,814] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
[2026-02-12 14:18:51,814] INFO in pipeline: Inlet: received 1 messages, current_message_id: b32e24c6-85d5-4e35-a1fc-2b89b5210450
INFO:pipeline:Inlet: received 1 messages, current_message_id: b32e24c6-85d5-4e35-a1fc-2b89b5210450
[2026-02-12 14:18:51,814] INFO in pipeline: Inlet: user messages IDs: [None]
INFO:pipeline:Inlet: user messages IDs: [None]
[2026-02-12 14:18:51,814] INFO in pipeline: Inlet: file_cache_session has 0 cached files
INFO:pipeline:Inlet: file_cache_session has 0 cached files
[2026-02-12 14:18:51,815] INFO in pipeline: _update_messages_with_files: file_cache has 0 entries
INFO:pipeline:_update_messages_with_files: file_cache has 0 entries
[2026-02-12 14:18:51,816] INFO in pipeline: _update_messages_with_files: files_by_message keys: []
INFO:pipeline:_update_messages_with_files: files_by_message keys: []
INFO:     172.19.0.1:58412 - "POST /pipeline/filter/inlet HTTP/1.1" 200 OK
INFO:     172.19.0.1:58420 - "GET /models HTTP/1.1" 200 OK
pipeline
pipeline
INFO:     172.19.0.1:58436 - "POST /chat/completions HTTP/1.1" 200 OK
[2026-02-12 14:18:51,823] INFO in pipeline: Starting OCR pipeline
INFO:pipeline:Starting OCR pipeline
[2026-02-12 14:18:51,823] INFO in pipeline: Streaming mode enabled for OCR pipeline
INFO:pipeline:Streaming mode enabled for OCR pipeline
[2026-02-12 14:18:51,823] INFO in pipeline: Starting VLM streaming invocation
INFO:pipeline:Starting VLM streaming invocation
[2026-02-12 14:18:59,064] INFO in pipeline: VLM streaming invocation completed
INFO:pipeline:VLM streaming invocation completed
INFO:     172.19.0.1:44974 - "POST /pipeline/filter/outlet HTTP/1.1" 200 OK
[2026-02-12 14:19:14,760] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
[2026-02-12 14:19:14,761] INFO in pipeline: Inlet: received 3 messages, current_message_id: e4c62919-7296-4d99-ad7f-80298a13707a
INFO:pipeline:Inlet: received 3 messages, current_message_id: e4c62919-7296-4d99-ad7f-80298a13707a
[2026-02-12 14:19:14,761] INFO in pipeline: Inlet: user messages IDs: [None, None]
INFO:pipeline:Inlet: user messages IDs: [None, None]
[2026-02-12 14:19:14,761] INFO in pipeline: Inlet: file_cache_session has 0 cached files
INFO:pipeline:Inlet: file_cache_session has 0 cached files
Creating model: ('PP-LCNet_x1_0_doc_ori', 'pipelines/PP-LCNet_x1_0_doc_ori')
Creating model: ('PP-DocLayoutV2', 'pipelines/PP-DocLayoutV2')
Creating model: ('PaddleOCR-VL-0.9B', None)
[2026-02-12 14:19:15,452] INFO in pipeline: PaddleOCRVL started for PDF OCR
INFO:pipeline:PaddleOCRVL started for PDF OCR
[2026-02-12 14:19:27,074] INFO in pipeline: Cached OCR result for 1.pdf (id: b5537412-5cfa-4488-960b-f1a211863eab) for message_id: e4c62919-7296-4d99-ad7f-80298a13707a
INFO:pipeline:Cached OCR result for 1.pdf (id: b5537412-5cfa-4488-960b-f1a211863eab) for message_id: e4c62919-7296-4d99-ad7f-80298a13707a
[2026-02-12 14:19:27,307] INFO in pipeline: _update_messages_with_files: file_cache has 1 entries
INFO:pipeline:_update_messages_with_files: file_cache has 1 entries
[2026-02-12 14:19:27,307] INFO in pipeline: _update_messages_with_files: files_by_message keys: ['e4c62919-7296-4d99-ad7f-80298a13707a']
INFO:pipeline:_update_messages_with_files: files_by_message keys: ['e4c62919-7296-4d99-ad7f-80298a13707a']
INFO:     172.19.0.1:47698 - "POST /pipeline/filter/inlet HTTP/1.1" 200 OK
INFO:     172.19.0.1:36564 - "GET /models HTTP/1.1" 200 OK
pipeline
pipeline
INFO:     172.19.0.1:36574 - "POST /chat/completions HTTP/1.1" 200 OK
[2026-02-12 14:19:27,362] INFO in pipeline: Starting OCR pipeline
INFO:pipeline:Starting OCR pipeline
[2026-02-12 14:19:27,362] INFO in pipeline: Streaming mode enabled for OCR pipeline
INFO:pipeline:Streaming mode enabled for OCR pipeline
[2026-02-12 14:19:27,362] INFO in pipeline: Starting VLM streaming invocation
INFO:pipeline:Starting VLM streaming invocation
[2026-02-12 14:19:32,666] INFO in pipeline: VLM streaming invocation completed
INFO:pipeline:VLM streaming invocation completed
INFO:     172.19.0.1:42892 - "POST /pipeline/filter/outlet HTTP/1.1" 200 OK
[2026-02-12 14:19:56,122] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
[2026-02-12 14:19:56,122] INFO in pipeline: Inlet: received 5 messages, current_message_id: 5368b7be-9a81-4c76-b888-3884f9801a95
INFO:pipeline:Inlet: received 5 messages, current_message_id: 5368b7be-9a81-4c76-b888-3884f9801a95
[2026-02-12 14:19:56,122] INFO in pipeline: Inlet: user messages IDs: [None, None, None]
INFO:pipeline:Inlet: user messages IDs: [None, None, None]
[2026-02-12 14:19:56,122] INFO in pipeline: Inlet: file_cache_session has 1 cached files
INFO:pipeline:Inlet: file_cache_session has 1 cached files
Creating model: ('PP-LCNet_x1_0_doc_ori', 'pipelines/PP-LCNet_x1_0_doc_ori')
Creating model: ('PP-DocLayoutV2', 'pipelines/PP-DocLayoutV2')
Creating model: ('PaddleOCR-VL-0.9B', None)
[2026-02-12 14:19:57,015] INFO in pipeline: PaddleOCRVL started for PDF OCR
INFO:pipeline:PaddleOCRVL started for PDF OCR
[2026-02-12 14:20:03,081] INFO in pipeline: Cached OCR result for 2.pdf (id: dd0593a9-a0ca-41be-8ec5-ca051cf581ef) for message_id: 5368b7be-9a81-4c76-b888-3884f9801a95
INFO:pipeline:Cached OCR result for 2.pdf (id: dd0593a9-a0ca-41be-8ec5-ca051cf581ef) for message_id: 5368b7be-9a81-4c76-b888-3884f9801a95
[2026-02-12 14:20:03,287] INFO in pipeline: _update_messages_with_files: file_cache has 2 entries
INFO:pipeline:_update_messages_with_files: file_cache has 2 entries
[2026-02-12 14:20:03,287] INFO in pipeline: _update_messages_with_files: files_by_message keys: ['e4c62919-7296-4d99-ad7f-80298a13707a', '5368b7be-9a81-4c76-b888-3884f9801a95']
INFO:pipeline:_update_messages_with_files: files_by_message keys: ['e4c62919-7296-4d99-ad7f-80298a13707a', '5368b7be-9a81-4c76-b888-3884f9801a95']
INFO:     172.19.0.1:36158 - "POST /pipeline/filter/inlet HTTP/1.1" 200 OK
INFO:     172.19.0.1:47414 - "GET /models HTTP/1.1" 200 OK
pipeline
pipeline
INFO:     172.19.0.1:47424 - "POST /chat/completions HTTP/1.1" 200 OK
[2026-02-12 14:20:03,360] INFO in pipeline: Starting OCR pipeline
INFO:pipeline:Starting OCR pipeline
[2026-02-12 14:20:03,360] INFO in pipeline: Streaming mode enabled for OCR pipeline
INFO:pipeline:Streaming mode enabled for OCR pipeline
[2026-02-12 14:20:03,360] INFO in pipeline: Starting VLM streaming invocation
INFO:pipeline:Starting VLM streaming invocation
[2026-02-12 14:20:06,990] INFO in pipeline: VLM streaming invocation completed
INFO:pipeline:VLM streaming invocation completed
INFO:     172.19.0.1:47440 - "POST /pipeline/filter/outlet HTTP/1.1" 200 OK