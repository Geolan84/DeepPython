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
        """Tests get() with values which doesn't exist."""
        cache = LRUCache(5)
        self.assertIsNone(cache["Not exist"])
        cache["New key"] = 56
        self.assertIsNone(cache["Not exist"])

    def test_unhashable_keys(self):
        """Tests that set() raises ValueError if key is unhashable."""
        cache = LRUCache()
        with self.assertRaises(ValueError):
            cache[[]] = "Some value"
        with self.assertRaises(ValueError):
            cache[{}] = "Some value"

    def test_single_element_cache(self):
        """Tests lru-cache with only one element."""
        cache = LRUCache(1)
        self.assertIsNone(cache["first"])
        cache["first"] = 125
        self.assertEqual(cache["first"], 125)
        cache["second"] = "Second item"
        self.assertIsNone(cache["first"])
        self.assertEqual(cache["second"], "Second item")

    def test_set_by_existant_key(self):
        """Tests set method when cache is full."""
        cache = LRUCache(2)
        cache["k1"] = "val1"
        cache["k2"] = "val2"
        self.assertEqual(cache["k1"], "val1")
        self.assertEqual(cache["k2"], "val2")
        cache["k1"] = "new_val"
        # Also two elements remain.
        self.assertEqual(cache["k1"], "new_val")
        self.assertEqual(cache["k2"], "val2")

    def test_order_of_displacement(self):
        """Tests order of displacement after get and set actions."""
        cache = LRUCache(4)
        cache["k1"] = "val1"
        cache["k2"] = "val2"
        cache["k3"] = "val3"
        cache["k4"] = "val4"
        cache["k5"] = "val5"
        # val1 removed, because it was the oldest.
        self.assertIsNone(cache["k1"])
        self.assertEqual(cache["k2"], "val2")
        # Now val2 is recently used, val3 will be removed next.
        cache["k6"] = "val6"
        self.assertIsNone(cache["k3"])

    def test_overloaded_cache(self):
        """Tests cache when count of items become greater than capacity."""
        cache = LRUCache(2)
        cache["k1"] = "val1"
        cache["k2"] = "val2"
        self.assertEqual(cache["k2"], "val2")
        self.assertEqual(cache["k1"], "val1")
        cache["k3"] = "val3"
        self.assertEqual(cache["k3"], "val3")
        self.assertIsNone(cache["k2"])
        self.assertEqual(cache["k1"], "val1")
