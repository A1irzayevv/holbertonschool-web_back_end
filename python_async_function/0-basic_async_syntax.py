#!/usr/bin/env python3
"""
task 0
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """doc func"""
    v = random.uniform(0, max_delay)
    await asyncio.sleep(v)
    return v
