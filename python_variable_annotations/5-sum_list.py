#!/usr/bin/env python3
"""
task 5
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """doc func"""
    n = 0
    for i in input_list:
        n = n + i

    return n
