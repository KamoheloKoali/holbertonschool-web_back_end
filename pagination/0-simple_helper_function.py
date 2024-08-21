#!/usr/bin/env python3
"""
    contains a function that takes
    two integer arguments page and page_size
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        returns a tuple of size two containing a start index
        and an end index corresponding to the range of indexes
        to return in a list for those particular pagination parameters

        Args:
            page (int): page number
            page_size (int): size of page
    """
    start_index: int = (page - 1) * page_size
    end_index: int = page * page_size
    return start_index, end_index
