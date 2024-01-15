#!/usr/bin/env python3
"""
Measure runtime module
"""

import time
import asyncio
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    and return total_time / n.

    Args:
        n (int): Number of times to execute wait_n.
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: Average execution time per iteration.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
