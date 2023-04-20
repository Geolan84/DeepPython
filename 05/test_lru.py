"""Unit tests for lru cache implementation."""
import unittest
from lru_cache import LRUCache


class TestLRU(unittest.TestCase):
    """Test case for custom LRUCache."""
    def test_invalid_limit(self):
        """Tests invalid capacity of cache in init."""
        with self.assertRaises(ValueError):
            LRUCache(0)
        with self.assertRaises(ValueError):
            LRUCache(-5)

    def test_get_none(self):
        """Tests get() with values which does not exist."""
        cache = LRUCache(5)
        self.assertIsNone(cache.get("Not exist"))
        cache.set("New key", 56)
        self.assertIsNone(cache.get("Not exist"))

    def test_priority_changes(self):
        """Tests priority of values after get() and set() calls."""
        cache = LRUCache(3)
        self.assertEqual(cache._LRUCache__cache, {})
        cache.set("First item", 345)
        self.assertEqual(cache._LRUCache__cache["First item"].priority, 0)
        cache.set("Second item", 45645)
        self.assertEqual(cache._LRUCache__cache["First item"].priority, 1)
        self.assertEqual(cache._LRUCache__cache["Second item"].priority, 0)
        cache.get("First item")
        self.assertEqual(cache._LRUCache__cache["First item"].priority, 0)
        self.assertEqual(cache._LRUCache__cache["Second item"].priority, 1)

    def test_unhashable_keys(self):
        """Tests that set() raises ValueError if key is unhashable."""
        cache = LRUCache()
        with self.assertRaises(ValueError):
            cache.set([], "Some value")
        with self.assertRaises(ValueError):
            cache.set({}, "Some value")

    def test_overloaded(self):
        """Tests cache when count of items become greater than capacity."""
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")
        cache.set("k3", "val3")
        self.assertEqual(cache.get("k3"), "val3")
        self.assertIsNone(cache.get("k2"))
        self.assertEqual(cache.get("k1"), "val1")
