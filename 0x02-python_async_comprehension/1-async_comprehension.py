#!/usr/bin/env python3
"""
Async Comprehension Module
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Async comprehension to collect 10 random numbers using async_generator.
    """
    return [i async for i in async_generator()]
