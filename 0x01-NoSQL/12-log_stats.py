#!/usr/bin/env python3
"""A script that describes nginx logs"""
from pymongo import MongoClient


def log_parsing():
    """Parses nginx logs"""
    # connects to the mongoclient
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs  # establishes a connection tho the db

    # prints the total document count
    print(f'{db.nginx.count()} logs')

    # set of methods to check
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # loops to count the document
    print("Methods:")
    for method in methods:
        method_count = db.nginx.count_documents({'method': method})
        print(f'\tmethod {method}: {method_count}')

    # counts the paths to /status
    status_paths = db.nginx.count_documents(
            {'method': 'GET', 'path': '/status'}
            )

    # prints the total number of paths
    print(f'{status_paths} status check')


if __name__ == "__main__":
    log_parsing()
