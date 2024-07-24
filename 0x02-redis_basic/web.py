#!/usr/bin/env python3
"""A script that implements a web cache tracker"""
import redis
import requests
from functools import wraps
from typing import Callable

r = redis.Redis()


def cache_count(func: Callable) -> Callable:
    """decorator monitors the call count"""

    @wraps(func)
    def wrapper(url: str):
        r.incr(f"count:{url}")  # increment the count key

        # check if the cached content already exists and return it instead
        cached_content = r.get(f"cached:{url}")

        if cached_content:
            return cached_content.decode("utf-8")

        # else call the method with the url
        content = func(url)

        # set the expiration and the content
        r.setex(f"cached:{url}", 10, content)

        return content
    return wrapper


@cache_count
def get_page(url: str) -> str:
    """Uses the request module to get the HTML content
    of a url and keeps count of the number of requests made"""
    response = requests.get(url)
    return response.text
