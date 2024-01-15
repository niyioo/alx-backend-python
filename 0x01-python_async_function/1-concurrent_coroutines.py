#!/usr/bin/env python3
"""
Concurrent coroutines module
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to execute wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*delays))
