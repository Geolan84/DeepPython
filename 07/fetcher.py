"""Async fetcher for urls."""
import asyncio
import time
import sys
import aiohttp


FILE_NAME = 'urls.txt'
WORKERS_COUNT = 4
FILL_SIZE = 4


def url_generator():
    """Generator for reading urls row by row."""
    file = open(FILE_NAME, 'r', encoding="utf-8")
    with file:
        while (line := file.readline().rstrip('\n')):
            yield line


async def fetch_url(url, sem):
    """Http request with semaphore."""
    async with aiohttp.ClientSession() as session:
        async with sem:
            async with session.get(url) as resp:
                print('I received: ', resp.status)


async def async_worker(queue, semaphore):
    """Worker for url from queue."""
    while True:
        url = await queue.get()
        try:
            await fetch_url(url, semaphore)
        finally:
            queue.task_done()


async def process_links(semaphore_limit):
    """Iterate on urls and create tasks for workers."""
    if not isinstance(semaphore_limit, int) or semaphore_limit < 1:
        raise ValueError("Limit should be positive integer!")
    generator = url_generator()
    semaphore = asyncio.Semaphore(semaphore_limit)
    queue = asyncio.Queue()
    workers = [asyncio.create_task(async_worker(queue, semaphore))
               for _ in range(WORKERS_COUNT)]
    is_urls_exists = True
    start = time.time()
    while is_urls_exists:
        # Fill the queue with new FILL_SIZE elements.
        for _ in range(FILL_SIZE):
            try:
                queue.put_nowait(next(generator))
            except StopIteration:
                is_urls_exists = False
        # Wait for workers.
        await queue.join()

    print('TIME', time.time() - start)

    for worker in workers:
        worker.cancel()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Specify limit of async requests!\n'
              'For example: "python fetcher.py 5"')
    else:
        try:
            LIMIT = int(sys.argv[1])
            if LIMIT < 1:
                raise ValueError()
            asyncio.run(process_links(LIMIT))
        except ValueError:
            print('Limit should be positive integer!')
