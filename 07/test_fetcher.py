from unittest import mock
import unittest
import asyncio
import contextlib
import random
import time
from fetcher import process_links

test_links = {"https://www.python.org/",
              "https://dart.dev/",
              "https://go.dev/",
              "https://kotlinlang.org/",
              "https://www.swift.org/",
              "https://openjdk.org/projects/jdk",
              "https://www.r-project.org/",
              "https://fortran-lang.org/en/",
              "https://scratch.mit.edu/"}


class TestAsyncFetcher(unittest.IsolatedAsyncioTestCase):

    async def test_http_and_generator_mocks(self):
        with mock.patch("fetcher.url_generator", side_effect=generator_mock) as mock_gen, mock.patch("aiohttp.ClientSession.get", side_effect=HttpGetMock) as http_mock:
            await process_links(5)
            called_urls = set([x.args[0] for x in http_mock.call_args_list])
            self.assertEqual(called_urls, test_links)
            mock_gen.assert_called_once_with()

    async def test_semaphore(self):
        with mock.patch("fetcher.url_generator", side_effect=generator_mock) as mock_gen, mock.patch("aiohttp.ClientSession.get", side_effect=HttpGetMock) as http_mock:
            start = time.time()
            await process_links(1)
            slow_semaphore = time.time() - start
            start = time.time()
            await process_links(9)
            fast_semaphore = time.time() - start
            # Sometimes it is not a truth, but on big numbers it works.
            self.assertGreaterEqual(slow_semaphore, fast_semaphore)

    async def test_negative_semaphore(self):
        with mock.patch("fetcher.url_generator", side_effect=generator_mock), mock.patch("aiohttp.ClientSession.get", side_effect=HttpGetMock):
            with self.assertRaises(ValueError):
                await process_links(-1)
            with self.assertRaises(ValueError):
                await process_links(0)
            with self.assertRaises(ValueError):
                await process_links(-50)


def generator_mock():
    for link in test_links:
        yield link


class HttpGetMock(contextlib.AsyncContextDecorator):
    def __init__(self, url):
        self.url = url
        self.status = f"200 {url}"

    async def __aenter__(self):
        await asyncio.sleep(random.random()/4)
        return self

    def __str__(self):
        return f"(Mock): {self.url}"

    async def __aexit__(self, *exc):
        return False
