#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination.

This script implements a hypermedia pagination mechanism for accessing
a dataset of popular baby names stored in a CSV file. It provides
methods to retrieve a page of data based on an index, along with
information about the current page and links to the next page.
"""

import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.

    Attributes:
        DATA_FILE (str): The filename of the CSV data file.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Retrieves info about a page from a given index and with
        a specified size.

        Args:
            index (int, optional): The starting index for the page.
            If None, the index starts from 0. Default is None.
            page_size (int, optional): The number of items per page.
            Default is 10.

        Returns:
            Dict: A dictionary containing information about the
            requested page, including the index, links to the next
            page, the page size, and the data.
        """
        data = self.indexed_dataset()
        assert index is not None and index >= 0 and index <= max(data.keys())
        page_data = []
        data_count = 0
        next_index = None
        start = index if index else 0
        for i, item in data.items():
            if i >= start and data_count < page_size:
                page_data.append(item)
                data_count += 1
                continue
            if data_count == page_size:
                next_index = i
                break
        page_info = {
            'index': index,
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data,
        }
        return page_info
