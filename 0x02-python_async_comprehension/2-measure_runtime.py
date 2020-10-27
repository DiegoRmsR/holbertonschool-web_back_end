#!/usr/bin/env python3
""" Run time for four parallel comprehensions """
import asyncio
import random
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Args:
        Voit
    Return:
        Float total runtime
    """
    start_time = time()

    result = [async_comprehension() for i in range(4)]
    await asyncio.gather(*result)

    end_time = time()

    total_time = end_time - start_time
    return total_time
