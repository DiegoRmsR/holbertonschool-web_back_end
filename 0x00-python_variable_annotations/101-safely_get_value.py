#!/usr/bin/env python3
""" More involved type annotations """
from typing import Mapping, Any, Sequence, Union


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
		-> Union[Any, T]:
    """ safely get value """
    if key in dct:
        return dct[key]
    else:
        return default
