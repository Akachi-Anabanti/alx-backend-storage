#!/usr/bin/env python3
"""A script that defines a python function
'insert_school' that inserts a new document in a collection
based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into a collection"""
    return mongo_collection.insert_one(kwargs).inserted_id 
