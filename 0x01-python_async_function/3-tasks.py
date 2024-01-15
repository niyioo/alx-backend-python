#!/usr/bin/env python3
"""
Tasks module
"""

import asyncio
from typing import Callable


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task that runs wait_random with the given max_delay.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task: Task representing the execution of wait_random.
    """
    loop = asyncio.get_event_loop()
    return loop.create_task(__import__('0-basic_async_syntax')
                            .wait_random(max_delay))
