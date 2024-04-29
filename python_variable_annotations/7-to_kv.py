#!/usr/bin/env python3
"""
task 7
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """doc func"""
    return (k, v ** 2)
