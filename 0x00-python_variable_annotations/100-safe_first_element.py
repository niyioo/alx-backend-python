#!/usr/bin/env python3
"""
Module with duck-typed annotations for the function safe_first_element.
"""
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Function that takes a sequence and returns its first element,
    or None if the sequence is empty.

    Parameters:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Union[Any, None]: The first element of the sequence,
        or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
