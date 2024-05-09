#!/usr/bin/env python3
"""
task 8
"""
import pymongo


def list_all(collection):
    """doc func"""
    if not collection:
        return []
    return list(collection.find())
