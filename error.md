[2026-02-03 11:25:13,895] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
INFO:ocr_utils.document_graph:New file detected: 3.pdf (id: b1ca9452-03d1-4944-ad03-fe69b8b20d50)
INFO:ocr_utils.document_graph:Added message_id 041c7f4e-e4a6-41c9-9fb7-ce8f4c446e53 to order cache
Expected dict, got <coroutine object _process_paddleocr_node at 0x7c9e64b5cd40>
For troubleshooting, visit: https://docs.langchain.com/oss/python/langgraph/errors/INVALID_GRAPH_NODE_RETURN_VALUE
INFO:     172.19.0.1:43520 - "POST /pipeline/filter/inlet HTTP/1.1" 500 Internal Server Error
[2026-02-03 11:25:41,149] INFO in pipeline: Processing inlet request
INFO:pipeline:Processing inlet request
/usr/local/lib/python3.11/asyncio/queues.py:181: RuntimeWarning: coroutine '_process_paddleocr_node' was never awaited
  raise QueueEmpty
RuntimeWarning: Enable tracemalloc to get the object allocation traceback
INFO:ocr_utils.document_graph:New file detected: 6.pdf (id: b76c3164-2b14-439f-84c7-96941712ed7f)
INFO:ocr_utils.document_graph:Added message_id a4e45b33-919e-43f4-8ad5-8af7fa8aa700 to order cache
Expected dict, got <coroutine object _process_paddleocr_node at 0x7c9e66db9e40>