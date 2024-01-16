#!/usr/bin/env python3
"""
Async Generator Module
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Async generator that yields a random number between 0 and
    10 after waiting 1 second asynchronously.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)