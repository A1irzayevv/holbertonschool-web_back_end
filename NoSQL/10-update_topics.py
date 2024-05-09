#!/usr/bin/env python3
"""
task 10
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """doc func"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
