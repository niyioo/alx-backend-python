#!/usr/bin/env python3
"""
Module with type-annotated function sum_mixed_list.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function that takes a list of integers and floats and
    returns their sum as a float.

    Parameters:
        mxd_lst (List[Union[int, float]]): The input list
        of integers and floats.

    Returns:
        float: The sum of the input list of integers and floats.
    """
    return sum(mxd_lst)
