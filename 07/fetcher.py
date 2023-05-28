"""Async fetcher for urls."""
import argparse
import asyncio
import time
import aiohttp


FILE_NAME = 'urls.txt'


def get_urls():
    """This method returns all urls from file. Makes mocking easier."""
    with open(FILE_NAME, "r", encoding="utf-8") as urls:
        return urls.readlines()


async def fetch_url(session, sem, urls_queue):
    """Http request with semaphore."""
    while True:
        url = await urls_queue.get()
        try:
            async with sem:
                async with session.get(url) as resp:
                    # First 50 letters of text.
                    print('I received: ', str(await resp.text())[:50])
        finally:
            urls_queue.task_done()


async def process_links(semaphore_limit, workers_count=None):
    """Iterate on urls and create tasks for workers."""
    if not isinstance(semaphore_limit, int) or semaphore_limit < 1:
        raise ValueError("Limit should be positive integer!")
    semaphore = asyncio.Semaphore(semaphore_limit)
    urls_queue = asyncio.Queue()
    for url in get_urls():
        await urls_queue.put(url)
    if workers_count is None:
        workers_count = urls_queue.qsize()
    elif workers_count < 1:
        raise ValueError("Count of workers can't be less than 1!")
    start = time.time()
    async with aiohttp.ClientSession() as session:
        workers = [
            asyncio.create_task(fetch_url(session, semaphore, urls_queue))
            for _ in range(workers_count)
        ]
        await urls_queue.join()
        for worker in workers:
            worker.cancel()
    print('TIME', time.time() - start)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', type=int, choices=range(1, 21), default=4)
    parser.add_argument('-w', type=int, choices=range(1, 50), required=False)
    args = parser.parse_args()
    asyncio.run(process_links(args.c, args.w))
