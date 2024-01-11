#!/usr/bin/env python3
"""
Module with type-annotated function floor.
"""
import math


def floor(n: float) -> int:
    """
    Function that takes a float argument and returns its floor as an integer.

    Parameters:
        n (float): The input float number.

    Returns:
        int: The floor of the input float number.
    """
    return math.floor(n)
