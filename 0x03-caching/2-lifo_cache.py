#!/usr/bin/python3
"""
LIFO caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO cache inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
        initialiaze
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item from cache
        """
        if key is not None or item is not None:
            if self.get(key) is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    keydis = list(self.cache_data.keys())[-1]
                    del self.cache_data[keydis]
                    print("DISCARD: {}".format(keydis))
            else:
                del self.cache_data[key]
            self.cache_data[key] = item

    def get(self, key):
        """
        Get items from cache
        """
        if key is not None or key:
            return self.cache_data.get(key)
