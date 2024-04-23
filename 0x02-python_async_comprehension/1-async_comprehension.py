#!/usr/bin/env python3
"""
Task 1
"""

import typing
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    import async_generator from the previous task
    """
    output = []
    async for value in async_generator():
        output.append(value)

    return output
