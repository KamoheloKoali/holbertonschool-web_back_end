#!/usr/bin/env python3
"""simple pagination
    this script implements a method to get data using pagination

    Imports:
        - csv
        - math
        - typing
"""
import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Args:
        page (int): page number
        page_size (int): size of page

    Returns:
        Tuple[int, int]: tuple containing start and end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset.

        Args:
            page (int): Page number (must be greater than 0)
            page_size (int): Number of items per page (must be greater than 0)

        Returns:
            List[List]: A list of rows
            from the dataset corresponding to the page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)

        dataset = self.dataset()
        if start_index < len(dataset):
            return dataset[start_index:end_index]
        return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Returns a dictionary containing pagination information.

        Args:
            page (int): Page number (must be greater than 0)
            page_size (int): Number of items per page (must be greater than 0)

        Returns:
            Dict[str, Any]: A dictionary containing pagination details
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
