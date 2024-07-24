#!/usr/bin/env python3
"""A script that implements a web cache tracker"""
import redis
import requests
from functools import wraps
from typing import Callable

r = redis.Redis()


def cache_count(expiration: int = 10):
    """Caches and sets expiration for 10 secs"""
    def decorator(func: Callable) -> Callable:
        """decorator monitors the call count"""
        @wraps(func)
        def wrapper(url: str):
            count_key = f"count:{url}"
            r.incr(count_key)  # increment the count key
            # check if the cached content already exists and return it instead
            cached_content = r.get(f"cached:{url}")
            if cached_content:
                return cached_content.decode("utf-8")
            # else call the method with the url
            content = func(url)
            # set the expiration and the content
            r.setex(f"cached:{url}", expiration, content)
            return content
        return wrapper
    return decorator


@cache_count()
def get_page(url: str) -> str:
    """Uses the request module to get the HTML content
    of a url and keeps count of the number of requests made"""
    response = requests.get(url)
    return response.text
