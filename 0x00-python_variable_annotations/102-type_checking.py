#!/usr/bin/env python3
"""
Module for zooming into an array.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms into the given array by repeating each element
    a certain number of times.

    Parameters:
        lst (Tuple): The input tuple (array) to be zoomed into.
        factor (int): The zoom factor, indicating how many
        times each element should be repeated. Default is 2.

    Returns:
        List: A list containing each element of the input array
        repeated according to the zoom factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
