#!/usr/bin/env python3
"""
    Contains the sum_list function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
         takes a list input_list of floats as argument and
         returns their sum as a float
         Args:
            input_list (list object): a list of float numbers
        Returns:
            a sum of the elements in input_list as a float
    """
    return sum(input_list)
