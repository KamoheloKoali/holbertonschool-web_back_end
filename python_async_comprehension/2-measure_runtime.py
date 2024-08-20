#!/usr/bin/env python3
"""
    contains a coroutine that executes async_comprehension
    four times in parallel using
    asyncio.gather and measures the runtime

    Imports:
        asyncio
        time
        comp
"""

import asyncio
import time

async_comp = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
        executes async_comprehension
        four times in parallel using
        asyncio.gather and measures and returns the runtime

        Returns:
            the runtime of the program itself
    """
    start: float = time.perf_counter()
    await asyncio.gather(async_comp(), async_comp(),
                         async_comp(), async_comp())
    end: float = time.perf_counter()
    return end - start
