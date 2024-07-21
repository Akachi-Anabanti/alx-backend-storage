#!/usr/bin/env python3

"""A script that setups a redis list"""
import redis
import uuid
import json
from typing import Any


class Cache:
    '''A cache class'''
    def __init__(self):
        '''class constructor'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """Takes data and stores  in redis
        returns : Data ID as str"""

        id = uuid.uuid4().hex
        self._redis.set(id, data)
        return id
