#!/usr/bin/env python3
"""Task 4"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Take the code from wait_n and alter it into a new function task_wait_n.."""
    random_delay_list: List[float] = []

    for i in range(n):
        random_delay_list.append(await task_wait_random(max_delay))

    return sorted(random_delay_list)
