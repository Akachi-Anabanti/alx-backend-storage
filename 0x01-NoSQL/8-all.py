#!/usr/bin/env python3
'''A script that defines a function that lists all documents in a collection'''


def list_all(mongo_collection):
    '''List all documents in
    mongo_collection'''

    return [doc for doc in mongo_collection.find()]
