#!/usr/bin/env python3
"""Thisi  the mru cache file"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Thisi sthe mru cache classs"""

    def __init__(self):
        """the initializoer of the classs"""
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """The put function"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if key in self.cache_order:
            self.cache_order.remove(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            k = self.cache_order.pop()
            del self.cache_data[k]
            print("DISCARD: {}".format(k))
        self.cache_order.append(key)

    def get(self, key):
        """The get function"""
        if key is None or key not in self.cache_data:
            return None
        self.cache_order.remove(key)
        self.cache_order.append(key)
        return self.cache_data.get(key)
