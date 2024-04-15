#!/usr/bin/env python3
"""Most Recently Used caching module.

This module implements a Most Recently Used (MRU) caching mechanism
represented by the `MRUCache` class. It allows storing and
retrieving items from a dictionary with an MRU removal mechanism
when the cache limit is reached.

"""

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Represents an object that allows storing and retrieving items from a
    dictionary with a Most Recently Used (MRU) removal mechanism
    when the limit is reached.

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
                mru_key, _ = self.cache_data.popitem(last=False)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """Retrieves an item by key.

        Args:
            key: The key to retrieve the item.

        Returns:
            The cached item if found, otherwise None.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
