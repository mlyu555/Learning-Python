import asyncio
import httpx
import threading
import time

client = httpx.AsyncClient()

async def async_main(url, sign):
    response = await client.get(url)
    status_code = response.status_code
    print(f'async_main: {threading.current_thread()}: {sign}:{status_code}')


loop = asyncio.get_event_loop()
tasks = [async_main(url='http://www.baidu.com', sign=i) for i in range(100)]
async_start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
async_end = time.time()
loop.close()
print(async_end - async_start)

# 结果易报错：httpcore.ConnectTimeout
# /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/httpx/_client.py:1978: UserWarning: Unclosed <httpx.AsyncClient object at 0x7fbee6a8b640>. See https://www.python-httpx.org/async/#opening-and-closing-clients for details.