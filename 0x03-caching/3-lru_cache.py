from base_caching import BaseCaching
"""
LRUCache caching
"""


class LRUCache(BaseCaching):
    """
    LRUCache cache inherits from BaseCaching and is a caching system

    Discard the least recently used item (LRU algorithm)
    """
    def __init__(self):
        """
        initialiaze
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item from cache
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                keydis = self.order.pop(0)
                del self.cache_data[keydis]
                print("DISCARD: {}".format(keydis))
            else:
                del self.cache_data[key]

            if key in self.order:
                self.order.remove(key)
                self.order.append(key)
            else:
                self.order.append(key)

            self.cache_data[key] = item

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
