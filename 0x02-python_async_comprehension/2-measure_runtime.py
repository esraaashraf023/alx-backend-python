#!/usr/bin/env python3
"""TASK 2"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """should measure the total runtime and return it"""
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.time()
    end_time - start_time
    return end_time - start_time
