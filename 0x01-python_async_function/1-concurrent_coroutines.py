#!/usr/bin/env python3
"""
task 1....
"""


import typing
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Import wait_random from the previous python file that you’ve written and write an async routine...
    """
    Q_delayes = []
    for _ in range(n):
        Q_delayes.append(wait_random(max_delay))

    out_put = []
    for k in asyncio.as_completed(Q_delayes):
        out_put.append(await k)

    return out_put
