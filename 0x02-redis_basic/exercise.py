#!/usr/bin/env python3
"""  a Cache class"""
import redis
import uuid
from typing import Union


class Cache:
    """ a Cache class"""
    def __init__(self) -> None:
        """ init of the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store methode"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    @staticmethode
    def get_str(value: bytes) -> str:
        """ get str methode"""
        return str(value)
    
    @staticmethode
    def get_int(value: bytes) -> int:
        """ get int methode"""
     
    def get(self, key: str, fn: Optional[Any] = None) -> Any:
        """ get method"""
        value = self._redis.get(key)
        if fn:
            if fn == int:
                return self.get_int(value)
            elif fn == str:
                return self.get_str(value)
            else:
                return fn(value)
        return value
