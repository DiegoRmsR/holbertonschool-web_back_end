#!/usr/bin/env python3
"""
1. Simple pagination
"""

import csv
import math
from typing import List, Tuple


def index_range(page, page_size) -> Tuple[int, int]:
    """
    Args:
        page: index one
        page_size: index two
    Return:
        Tuple of int
    """
    start_index = (page - 1) * page_size
    end_index = page_size * page
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Args:
            page: index one with default value 1
            page_size: index two with default value 10
        return:
            appropriate page of the dataset (i.e. the correct list of rows).
        """
        assert 0 < isinstance(page, int)
        assert 0 < isinstance(page_size, int)
        i_range = index_range(page, page_size)
        self.dataset()
        if self.__dataset is None:
            return []
        return self.__dataset[i_range[0]:i_range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Args:
            page: index one with default value 1
            page_size: index two with default value 10
        return:
            dict:
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """

        data = self.get_page(page, page_size)

        data_set = self.__dataset

        len_data_set = len(data_set) if data_set else 0

        total_pages = math.ceil(len_data_set / page_size)

        next_page = page + 1 if page < total_pages else None

        prev_page = page - 1 if page > 1 else None

        hyper_dict = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
        return hyper_dict
