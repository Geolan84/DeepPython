import collections
from collections.abc import Hashable


class LRUCache:

    OrderedItem = collections.namedtuple("OrderedItem", ["priority", "value"])

    def __init__(self, limit=42):
        if limit < 1:
            raise ValueError("LRU size should be greater than 0!")
        self.__cache = dict()
        self.__capacity = limit
        self.__length = 0

    def __update_priority(self):
        """Updates priority of all items and checks items for deletion."""
        key_to_delete = None
        for key, item in self.__cache.items():
            self.__cache[key] = self.OrderedItem(item.priority+1, item.value)
            if item.priority+1 == self.__capacity:
                key_to_delete = key
        return key_to_delete

    def get(self, key):
        try:
            result = self.__cache[key].value
            self.__update_priority()
            self.__cache[key] = self.OrderedItem(0, self.__cache[key].value)
            return result
        except KeyError:
            return None

    def set(self, key, value):
        """Add new key-value pair to cashe."""
        if not isinstance(key, Hashable):
            raise ValueError("Key should be hashable! Implement __hash__()!")
        delete_key = self.__update_priority()
        if self.__length < self.__capacity:
            self.__length += 1
        elif delete_key is not None:
            del self.__cache[delete_key]
        self.__cache[key] = self.OrderedItem(0, value)
