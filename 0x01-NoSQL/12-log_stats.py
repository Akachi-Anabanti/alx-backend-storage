#!/usr/bin/env python3
"""A script that describes nginx logs"""
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
db = client.logs

print(f'{db.nginx.count()} logs')

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

print("Methods:")
for method in methods:
    method_count = db.nginx.count_documents({'method': method})
    print(f'\tmethod {method}: {method_count}')
