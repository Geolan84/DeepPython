"""Custom LRUCache for caching data."""
from collections.abc import Hashable


class LRUCache:
    """Class of custom LRU cache."""
    def __init__(self, limit=42):
        if limit < 1:
            raise ValueError("LRU size should be greater than 0!")
        self.cache = {}
        self.limit = limit

    def __getitem__(self, key):
        """Get value by key from cashe."""
        if key not in self.cache:
            return None
        val = self.cache.pop(key)
        self.cache[key] = val
        return val

    def __setitem__(self, key, value):
        """Add new key-value pair to cashe."""
        if not isinstance(key, Hashable):
            raise ValueError("Key should be hashable! Implement __hash__()!")
        if key in self.cache:
            self.cache.pop(key)
        else:
            if len(self.cache) == self.limit:
                del self.cache[next(iter(self.cache))]
        self.cache[key] = value
