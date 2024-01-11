#!/usr/bin/env python3
"""
Module with type-annotated function concat.
"""


def concat(str1: str, str2: str) -> str:
    """
    Function that takes two string arguments and
    returns their concatenated string.

    Parameters:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        str: The concatenated string of str1 and str2.
    """
    return str1 + str2
