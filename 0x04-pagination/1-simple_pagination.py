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
        assert 0 < page, page_size
        i_range = index_range(page, page_size)
        self.dataset()
        if self.__dataset is None:
            return []
        return self.__dataset[i_range[0], i_range[1]]
