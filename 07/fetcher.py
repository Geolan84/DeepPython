import asyncio
import aiohttp
import sys


async def fetch_urls(workers_count: int):
    pass

async def main():
    workers_count = 5
    if len(sys.argv) == 2:
        workers_count = int(sys.argv[1])
    asyncio.create_task(fetch_urls(workers_count))

asyncio.run(main())