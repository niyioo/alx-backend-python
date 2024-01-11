#!/usr/bin/env python3
"""
Module with type-annotated function make_multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that takes a float multiplier and returns a function
    that multiplies a float by multiplier.

    Parameters:
        multiplier (float): The multiplier to be
        used in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float and
        returns the result of multiplying it by the multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
