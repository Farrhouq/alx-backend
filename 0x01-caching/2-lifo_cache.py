#!/usr/bin/env python3
"""This is the lifo cache file"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """This is teh lifo class for caching"""

    def __init__(self):
        """Thisi s a constrcutor"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """The putter function"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                k = self.stack.pop()
                del self.cache_data[k]
                print(f"DISCARD: {k}")
            self.stack.append(key)

    def get(self, key):
        """This is the cache getter"""
        return self.cache_data.get(key) if key else None
