#!/usr/bin/env python3
"""
Tasks
"""
import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def wait_n(n: int = 0 , max_delay: int = 10) ->List[float]:
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
