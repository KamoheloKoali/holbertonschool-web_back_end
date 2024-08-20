#!/usr/bin/env python3
"""
    contains the function async_generator
    that yeilds a random number every second

    Imports:
        - asyncio
        - typing
"""

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[int, None, None]:
    """
        Yields a random number every second
    """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
