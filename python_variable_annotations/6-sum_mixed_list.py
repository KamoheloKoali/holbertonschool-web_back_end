#!/usr/bin/env python3
"""
    Contains the sum_mixed_list function
"""
from typing import Union


def sum_mixed_list(mxd_lst: Union[float, int]) -> float:
    """
        Returns the sum of all the elements in the list.
        Args:
            mxd_lst (list object): a list of integers and floats
        Returns:
            the sum of all the elements in mxd_lst
    """
    return sum(mxd_lst)
