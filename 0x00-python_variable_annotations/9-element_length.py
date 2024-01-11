#!/usr/bin/env python3
"""
Module with type-annotated function element_length.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function that takes an iterable of sequences and returns a list of tuples.
    Each tuple contains an element from the input iterable and its length.

    Parameters:
        lst (Iterable[Sequence]): The input iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple
        contains an element from the input iterable and its length.
    """
    return [(i, len(i)) for i in lst]
