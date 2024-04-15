#!/usr/bin/env python3
"""Basic caching module.

This module implements a basic caching mechanism represented
by the `BasicCache` class, which allows storing and
retrieving items from a dictionary-based cache.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents an object that allows storing and retrieving items
    from a dictionary.
    This class inherits from `BaseCaching`, providing
    basic caching functionality.
    Attributes:
        cache_data (dict): A dictionary to store cached items.
    """

    def put(self, key, item):
        """Adds an item in the cache.

        Args:
            key: The key to identify the item.
            item: The item to be cached.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.

        Args:
            key: The key to retrieve the item.

        Returns:
            The cached item if found, otherwise None.
        """
        return self.cache_data.get(key, None)
