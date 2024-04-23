#!/usr/bin/env python3
"""
TASK 1
"""

import typing
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    coroutine will collect 10 random numbers using an async
    """
    output = []
    async for value in async_generator():
        output.append(value)

    return output
