#!/usr/bin/env python3
"""This is the lru file"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """This is the last recently used caching"""

    def __init__(self):
        """The constructor"""
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """the put function"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if key in self.cache_order:
            self.cache_order.remove(key)
        self.cache_order.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            k = self.cache_order.pop(0)
            del self.cache_data[k]
            print("DISCARD: {}".format(k))

    def get(self, key):
        """This is the get method"""
        if key is None or key not in self.cache_data:
            return None
        self.cache_order.remove(key)
        self.cache_order.append(key)
        return self.cache_data.get(key)
