#!/usr/bin/python3
"""
LRUCache caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache cache inherits from BaseCaching and is a caching system
    Discard the least recently used item (LRU algorithm)
    """

    def __init__(self):
        """
        call parents
        """
        BaseCaching.__init__(self)
        self.order = []

    def put(self, key, item):
        """
        Add an item from cache
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

            if key in self.order:
                self.order.remove(key)
            self.order.append(key)

            if len(self.order) > BaseCaching.MAX_ITEMS:
                last = self.order.pop(0)
                self.cache_data.pop(last)
                print('DISCARD: {}'.format(last))

    def get(self, key):
        """
        Get items from cache
        """
        try:
            if key in self.order:
                self.order.remove(key)
                self.order.append(key)

            return self.cache_data[key]
        except KeyError:
            return None
