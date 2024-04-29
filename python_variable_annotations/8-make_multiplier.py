#!/usr/bin/env python3
"""
task 8
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """doc func"""
    def multiply(num: float) -> float:
        """doc func0"""
        return num * multiplier
    return multiply
