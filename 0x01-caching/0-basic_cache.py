#!/usr/bin/env python3
"""This is the basic caching file"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """This is the Basic Cache class"""

    def put(self, key, item):
        """This is the put function to put something to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """returns the value of the key cache"""
        return self.cache_data.get(key) if key else None
