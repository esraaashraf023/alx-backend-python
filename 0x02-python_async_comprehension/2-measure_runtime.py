#!/usr/bin/env python3
"""
Task 2
"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension.
    """
    start_time = time.time()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    end_time = time.time()
    end_time - start_time
    return end_time - start_time
