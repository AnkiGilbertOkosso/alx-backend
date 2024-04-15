#!/usr/bin/env python3
"""Last-In First-Out caching module.

This module implements a Last-In First-Out (LIFO) caching mechanism
represented by the `LIFOCache` class. It allows storing and
retrieving items from a dictionary with a LIFO removal mechanism
when the cache limit is reached.

"""

from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Represents an object that allows storing and retrieving items
    from a dictionary with a LIFO removal mechanism when the limit is reached.

    This class inherits from `BaseCaching`, providing basic caching
    functionality.

    Attributes:
        cache_data (OrderedDict): An ordered dictionary to store cached items.
    """

    def __init__(self):
        """Initializes the cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.

        Args:
            key: The key to identify the item.
            item: The item to be cached.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(last=True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieves an item by key.

        Args:
            key: The key to retrieve the item.

        Returns:
            The cached item if found, otherwise None.
        """
        return self.cache_data.get(key, None)
