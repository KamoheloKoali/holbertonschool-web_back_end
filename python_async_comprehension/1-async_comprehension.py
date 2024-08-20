#!/usr/bin/env python3
"""
    defines a coroutine that collects and returns 10 random
    numbers using an async
    comprehensing over async_generator

    Imports:
        typing
        gen
"""

from typing import List

gen = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
        collects and returns 10 random numbers

        Returns:
            numbers (List): a list of float numbers
    """
    numbers: List[float] = [num async for num in gen()]
    return numbers
