#!/usr/bin/env python3
"""
    Contains the make_multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        returns a function that multiplies a float by multiplier
        Args:
            multiplier (float): decimal number
        Returns:
            a function that multiplies a float by multiplier
    """
    return lambda num: num * multiplier
