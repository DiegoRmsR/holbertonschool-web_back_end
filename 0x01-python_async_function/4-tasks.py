#!/usr/bin/env python3
"""
Tasks
"""
import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) ->List[float]:
    """
    Args:
        max_delay: max wait
        n: spawn wait_random
    Return:
        float random of  multiples tasks
    """
    delays = []
    queue = []

    for _ in range(n):
        queue.append(task_wait_random(max_delay))

    for i in asyncio.as_completed(queue):
        delay = await i
        delays.append(delay)

    return delays
