#!/usr/bin/env python3
"""
task 0.....
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
     an asynchronous coroutine that takes in an integer argument..
    """
    Q_max_delay = random.uniform(0, max_delay)
    await asyncio.sleep(Q_max_delay)

    return Q_max_delay
