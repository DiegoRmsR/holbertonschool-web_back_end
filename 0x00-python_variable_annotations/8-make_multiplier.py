#!/usr/bin/env python3

""" Complex types - functions """

from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Args:
        multiplier: factor
    Return:
        multiplies a float by multiplier
    """

    def f(n: float) -> float:
        """ multiplies a float by multiplier """

        return float(n * multiplier)

    return f
