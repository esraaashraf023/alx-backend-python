#!/usr/bin/env python3
"""
task 0.....
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that waits for random delay between 0 and max_delay
    """
    Q_max_delay = random.uniform(0, max_delay)
    await asyncio.sleep(Q_max_delay)

    return Q_max_delay
