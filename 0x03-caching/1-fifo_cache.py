#!/usr/bin/python3
"""
FIFO caching
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO cache inherits from BaseCaching and is a caching system
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
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                keydis = list(self.cache_data.keys())[0]
                del self.cache_data[keydis]
                print("DISCARD: {}".format(keydis))
            self.cache_data[key] = item

    def get(self, key):
        """
        Get items from cache
        """
        if key is not None or key:
            return self.cache_data.get(key)
