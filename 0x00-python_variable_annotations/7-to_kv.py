#!/usr/bin/env python3
"""
Module with type-annotated function to_kv.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function that takes a string and an int OR float and returns a tuple.
    The first element of the tuple is the string k.
    The second element is the square of the int/float v
    and is annotated as a float.

    Parameters:
        k (str): The input string.
        v (Union[int, float]): The input int or float.

    Returns:
        Tuple[str, float]: A tuple containing the string k
        and the square of v as a float.
    """
    return (k, v ** 2.0)
