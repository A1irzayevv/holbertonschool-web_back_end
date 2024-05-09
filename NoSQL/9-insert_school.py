#!/usr/bin/env python3
"""
task 9
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """doc func"""
    if len(kwargs) == 0:
        return None
    return mongo_collection.insert(kwargs)
