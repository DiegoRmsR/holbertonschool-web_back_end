#!/usr/bin/python3
"""
basic dictionary
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache  inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """
        Add an item from cache
        """
        if key or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get items from cache
        """

        if key is not None or key:
            return self.cache_data.get(key)
