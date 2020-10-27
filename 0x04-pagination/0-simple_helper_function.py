#!/usr/bin/env python3
"""
0. Simple helper function
"""

from typing import Tuple


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
