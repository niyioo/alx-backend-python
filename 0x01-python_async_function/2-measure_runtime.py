#!/usr/bin/env python3
"""
Measure runtime module
"""

import time
import asyncio
from typing import Callable


def measure_time(n: int, max_delay: int, fn: Callable) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay) and return total_time / n.

    Args:
        n (int): Number of times to execute wait_n.
        max_delay (int): Maximum delay in seconds.
        fn (Callable): The function to measure the runtime.

    Returns:
        float: Average execution time per iteration.
    """
    start_time = time.time()
    asyncio.run(fn(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
