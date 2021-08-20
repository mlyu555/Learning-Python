import asyncio
import httpx
import threading
import time

def sync_main(url, sign):
    response = httpx.get(url).status_code
    print(f'sync_main: {threading.current_thread()}: {sign}: {response}')

sync_start = time.time()
[sync_main(url='http://www.baidu.com', sign=i) for i in range(100)]
sync_end = time.time()
print(sync_end - sync_start)