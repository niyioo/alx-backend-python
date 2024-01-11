#!/usr/bin/env python3
"""
Module with type-annotated function safely_get_value.
"""
from typing import TypeVar, Mapping, Any, Union, Optional


T = TypeVar('T')


def safely_get_value(
    dct: Mapping, key: Any, default: Optional[T] = None
) -> Union[Any, T]:
    """
    Function that safely gets the value associated with
    the given key from a dictionary.

    Parameters:
        dct (Mapping): The input dictionary.
        key (Any): The key to look up in the dictionary.
        default (Optional[T]): The default value to return if
        the key is not present. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key,
        or the default value if the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
