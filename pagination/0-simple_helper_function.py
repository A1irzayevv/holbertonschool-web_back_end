#!/usr/bin/env python3
"""
task 0
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """doc func"""
    return ((page - 1) * page_size, page * page_size)
