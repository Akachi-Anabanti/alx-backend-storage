#!/usr/bin/env python3

"""A script that setups a redis list"""
import redis
import uuid
import json
from typing import Union, Optional, Callable


class Cache:
    '''A cache class'''
    def __init__(self):
        '''class constructor'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes data and stores  in redis
        returns : Data ID as str"""

        id = uuid.uuid4().hex
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Optional[Callable]=None):
        """Retrieves the value of the key from db
            and converts to original format"""
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, data: str) -> str:
        """converts a string"""
        return data.decode('utf-8', 'strict')

    def get_int(self, data: str) -> int:
        """Returns int value of decode byte"""
        return int(data)
