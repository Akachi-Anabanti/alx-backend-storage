#!/usr/bin/env python3

"""A script that setups a redis list"""
import redis
import uuid
import json
from typing import Union, Optional, Callable
from functools import wraps


def call_history(method: Callable) -> Callable:
    """A decorator that stores the history
    of inputs and outputs for a particular function
    """
    method_name = method.__qualname__
    input_list_key = f"{method_name}:inputs"
    output_list_key = f"{method_name}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # performs the list addition
        self._redis.rpush(input_list_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_list_key, str(output))
        return output
    return wrapper


def count_calls(method: Callable) -> Callable:
    """A decorator that takes a single method
    increments the s the count for that key
    and retuns a callable"""
    method_key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # perform deocrated function here
        self._redis.incr(method_key)
        return method(self, *args, **kwargs)
    return wrapper


def replay(method: Callable) -> Callable:
    """Displays the history of calls of a particular function"""
    method_name = method.__qualname__
    inputs, outputs = f"{method_name}:inputs", f"{method_name}:outputs"

    redis = method.__self__._redis
    call_count = redis.get(method_name).decode('utf-8')
    print(f"{method_name} was called {call_count} times:")
    IOTuple = zip(redis.lrange(inputs, 0, -1), redis.lrange(outputs, 0, -1))
    for inp, outp in list(IOTuple):
        attr, data = inp.decode("utf-8"), outp.decode("utf-8")
        print(f"{method_name}(*{attr}) -> {data}")


class Cache:
    '''A cache class'''
    def __init__(self):
        '''class constructor'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes data and stores  in redis
        returns : Data ID as str"""

        id = uuid.uuid4().hex
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Optional[Callable] = None):
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
