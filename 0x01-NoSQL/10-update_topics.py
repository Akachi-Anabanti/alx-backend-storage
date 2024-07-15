#!/usr/bin/env python3
"""A script that defines a function update_topics
that changes all the topics of a school document based
on the name"""


def update_topics(mongo_collection, name, topics):
    """Changes all the topics of mongo_collection with
    name = name"""
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
