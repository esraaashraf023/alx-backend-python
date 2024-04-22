#!/usr/bin/env python3
"""takes 2..."""


import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ that takes in 2 int arguments (in this order):n and max_delay.
    You will spawn wait_random n times with the specified max_delay."""
    tasks = [asyncio.create_task(task_wait_random(max_delay)) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
