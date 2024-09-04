#!/usr/bin/env python3
"""This is the fifo cache file"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """This is the Fifo Caching class"""

    def __init__(self):
        """This is the constructor"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """This is the put fucntion to add a cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                k = self.queue.pop(0)
                del self.cache_data[k]
                print("DISCARD: {}".format(k))
            self.queue.append(key)

    def get(self, key, item):
        """This is the get function to get a cache"""
        return self.cache_data.get(key) if key else None
