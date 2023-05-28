"""Tests for async fetcher."""
from unittest import mock
import unittest
import asyncio
import contextlib
import random
import time

import aiohttp

from fetcher import process_links, fetch_url

TEST_LINKS = {"https://www.python.org/",
              "https://dart.dev/",
              "https://go.dev/",
              "https://kotlinlang.org/",
              "https://www.swift.org/",
              "https://openjdk.org/projects/jdk",
              "https://www.r-project.org/",
              "https://fortran-lang.org/en/",
              "https://scratch.mit.edu/"}


class TestAsyncFetcher(unittest.IsolatedAsyncioTestCase):
    """TestCase for async fetcher."""
    async def test_http_and_generator_mocks(self):
        """Tests calls for http get and url generator."""
        with mock.patch("fetcher.get_urls", return_value = TEST_LINKS)\
             as mock_gen,\
             mock.patch("aiohttp.ClientSession.get", side_effect=HttpGetMock)\
             as http_mock:
            await process_links(5)
            called_urls = {x.args[0] for x in http_mock.call_args_list}
            self.assertEqual(called_urls, TEST_LINKS)
            mock_gen.assert_called_once_with()

    async def test_semaphore(self):
        """Tests impact of increasing semaphore limit."""
        with mock.patch("fetcher.get_urls", return_value = TEST_LINKS),\
             mock.patch("aiohttp.ClientSession.get", side_effect=HttpGetMock):
            start = time.time()
            await process_links(1, 10)
            slow_semaphore = time.time() - start
            start = time.time()
            await process_links(5, 10)
            fast_semaphore = time.time() - start
            # Sometimes it is not a truth, but on big numbers it always works.
            self.assertGreaterEqual(slow_semaphore, fast_semaphore)

    async def test_only_coroutine(self):
        """Tests coroutine."""
        with mock.patch("aiohttp.ClientSession.get", side_effect=HttpGetMock)\
             as http_mock:
            semaphore = asyncio.Semaphore(1)
            urls_queue = asyncio.Queue()
            for url in TEST_LINKS:
                await urls_queue.put(url)
            async with aiohttp.ClientSession() as session:
                loop = asyncio.get_running_loop()
                loop.create_task(fetch_url(session, semaphore, urls_queue))
                await urls_queue.join()
            called_urls = {x.args[0] for x in http_mock.call_args_list}
            self.assertEqual(called_urls, TEST_LINKS)

    async def test_negative_semaphore(self):
        """Tests incorrect values for semaphore limit."""
        with mock.patch("fetcher.get_urls", return_value = TEST_LINKS),\
             mock.patch("aiohttp.ClientSession.get", side_effect=HttpGetMock):
            with self.assertRaises(ValueError):
                await process_links(-1, 5)
            with self.assertRaises(ValueError):
                await process_links(0, 5)
            with self.assertRaises(ValueError):
                await process_links(-50, 5)

    async def test_negative_workers_count(self):
        """Tests incorrect values for workers count."""
        with mock.patch("fetcher.get_urls", return_value=TEST_LINKS),\
             mock.patch("aiohttp.ClientSession.get", side_effect=HttpGetMock):
            with self.assertRaises(ValueError):
                await process_links(1, -50)
            with self.assertRaises(ValueError):
                await process_links(5, 0)
            with self.assertRaises(ValueError):
                await process_links(10, -1)

    async def test_other_url_count(self):
        """Tests process links with 3 urls."""
        test_urls = {
            "https://www.python.org/",
            "https://dart.dev/",
            "https://go.dev/"
        }
        with mock.patch("fetcher.get_urls", return_value = test_urls)\
             as mock_gen,\
             mock.patch("aiohttp.ClientSession.get", side_effect=HttpGetMock)\
             as http_mock:
            await process_links(5)
            called_urls = {x.args[0] for x in http_mock.call_args_list}
            self.assertEqual(called_urls, test_urls)
            mock_gen.assert_called_once_with()


class HttpGetMock(contextlib.AsyncContextDecorator):
    """Mock context decorator for aiohttp.ClientSession.get."""
    def __init__(self, url):
        self.url = url

    async def __aenter__(self):
        await asyncio.sleep(random.random()/4)
        return self

    async def text(self):
        """Mock text method."""
        return f"Some text from {self.url}"

    async def __aexit__(self, *exc):
        return False
