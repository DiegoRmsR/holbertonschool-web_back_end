#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Args:
            page: index one with default value 1
            page_size: index two with default value 10
        return:
            dict:
            index: the current start index of the return page. That is the
            index of the first item in the current page. For example if
            requesting page 3 with page_size 20, and no data was removed from
            the dataset, the current index should be 60.
            next_index: the next index to query with. That should be the index
            of the first item after the last item on the current page.
            page_size: the current page size
            data: the actual page of the dataset
        """
        list_dataset = []
        keys_list = list(self.__indexed_dataset.keys())
        assert index + page_size < len(keys_list)
        assert index < len(keys_list)

        if index not in self.__indexed_dataset:
            start_index = keys_list[index]
        else:
            start_index = index

        for i in range(start_index, start_index + page_size):
            if i not in self.__indexed_dataset:
                list_dataset.append(self.__indexed_dataset[keys_list[i]])
            else:
                list_dataset.append(self.__indexed_dataset[i])

        next_index: int = index + page_size

        if index in keys_list:
            next_index
        else:
            next_index = keys_list[next_index]

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(list_dataset),
            'data': list_dataset
        }
