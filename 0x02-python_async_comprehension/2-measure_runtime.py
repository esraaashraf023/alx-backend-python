#!/usr/bin/env python3
"""
Task 2
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension four times in parallel using asyncio.gather.
    """
    start_time = time.perf_counter()

    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )

    end_time = time.perf_counter()
    return end_time - start_time

runtime = asyncio.run(measure_runtime())
print(f"Total runtime: {runtime} seconds")
