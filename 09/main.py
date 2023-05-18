"""Custom LRUCache for caching data."""
import collections
import sys
import logging
from collections.abc import Hashable


class LRUCache:
    """Class of custom LRU cache."""
    OrderedItem = collections.namedtuple("OrderedItem", ["priority", "value"])

    def __init__(self, limit=42):
        if limit < 1:
            raise ValueError("LRU size should be greater than 0!")
        self.__cache = {}
        self.__capacity = limit
        self.__length = 0

    def __update_priority(self):
        """Updates priority of all items and checks items for deletion."""
        logging.debug("Priorities updated.")
        key_to_delete = None
        for key, item in self.__cache.items():
            self.__cache[key] = self.OrderedItem(item.priority+1, item.value)
            if item.priority+1 == self.__capacity:
                key_to_delete = key
        return key_to_delete

    def get(self, key):
        """Get value by key from cashe."""
        try:
            result = self.__cache[key].value
            self.__update_priority()
            self.__cache[key] = self.OrderedItem(0, self.__cache[key].value)
            logging.info(f"Got item by key '{key}'.")
            return result
        except KeyError:
            logging.info(f"Key '{key}' doesn't exist.")
            return None

    def set(self, key, value):
        """Add new key-value pair to cashe."""
        if not isinstance(key, Hashable):
            logging.debug(f"Got unhashable object in key: {key}")
            raise ValueError("Key should be hashable! Implement __hash__()!")
        delete_key = self.__update_priority()
        if self.__length < self.__capacity:
            self.__length += 1
        elif delete_key is not None:
            logging.info(f"Set {key} when dict is overloaded.")
            del self.__cache[delete_key]
        if key in self.__cache.keys():
            logging.info(f"Set existant key '{key}'")
        else:
            logging.info(f"Set with key '{key}', which doesn't exist.")
        self.__cache[key] = self.OrderedItem(0, value)


class OnlySetFilter(logging.Filter):
    def filter(self, record):
        return record.getMessage().startswith('Set ')


if __name__ == "__main__":
    full = logging.getLogger()
    full.setLevel(logging.DEBUG)
    file_cache = logging.FileHandler(
        "cache.log",
    )
    full.addHandler(file_cache)
    if "-f" in sys.argv:
        full.addFilter(OnlySetFilter())
    if "-s" in sys.argv:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        full.addHandler(console_handler)

cache = LRUCache(2)

cache.set("k1", "val1")
cache.set("k1", "val2")
cache.get("k2")
cache.get("k1")
cache.set("k2", "val2")
cache.set("k3", "val2")
