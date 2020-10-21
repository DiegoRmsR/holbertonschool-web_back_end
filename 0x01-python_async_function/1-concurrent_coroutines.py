#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    Args:
        max_delay: max wait
        n: spawn wait_random
    Return:
        float random
    """
    delays = []
    queue = []

    for _ in range(n):
        queue.append(wait_random(max_delay))

    for i in asyncio.as_completed(queue):
        delay = await i
        delays.append(delay)

    return delays
