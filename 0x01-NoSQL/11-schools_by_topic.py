#!/usr/bin/env python3
"""A script that returns a list from a collection with
 criteria"""


def schools_by_topic(mongo_collection, topic):
    """Creates a list of schools by topic"""
    return list(mongo_collection.find({"topics": topic}))
