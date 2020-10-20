#!/usr/bin/env python3
""" Complex types - string and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
	"""
	Args:
		k: String
		v: Union: int or float
	Return:
		Tuple with string and int or float
	"""
	return (k + v*v)
