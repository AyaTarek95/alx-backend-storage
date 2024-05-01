#!/usr/bin/env python3
"""  a Cache class"""
import redis
import uuid
from typing import Union


class Cache:
    """ a Cache class"""
    def __init__(self)-> None:
        """ init of the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float])-> str:
        """store methode"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
