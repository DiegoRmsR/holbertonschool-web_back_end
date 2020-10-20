#!/usr/bin/env python3

""" Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
	"""
    Args:
        multiplier: factor
    Return:
        multiplies a float by multiplier
	"""
	def f(n: float) -> float:
		return float(n * multiplayer)

	return f
