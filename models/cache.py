from abc import abstractmethod
from collections import OrderedDict
from functools import lru_cache

from numpy import number
from models.file import File


class Cache:
    def __init__(self, cache_type: str, capacity: int):
        if type == 'LRU':
            return LruCache(capacity)

    @abstractmethod
    def get(self, key: number) -> File:
        pass

    @abstractmethod
    def available(self, key: number) -> bool:
        pass

    @abstractmethod
    def put(self, key: number, value: File):
        pass 


class LruCache(Cache):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return None
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
    
    def available(self, key) -> bool:
        return key in self.cache

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)

