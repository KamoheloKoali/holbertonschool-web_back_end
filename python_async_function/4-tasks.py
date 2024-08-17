#!/usr/bin/env python3

"""
    similar function to wait_n but calls task_wait random instead
    Imports:
        asyncio
        typing
        task_wait_random
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        returns a list of all the delays (float values).
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays
