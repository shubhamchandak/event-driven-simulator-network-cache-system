from __future__ import annotations
from abc import abstractmethod
from collections import OrderedDict
from functools import lru_cache

from numpy import number
from models.file import File


class Cache:

    def create_cache(cache_type: str, capacity: int) -> Cache:
        if cache_type == 'LRU':
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

    @abstractmethod
    def size(self):
        pass 


class LruCache(Cache):
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            print('cache is empty! - returning none')
            return None
        else:
            self.cache.move_to_end(key)
            res =  self.cache[key]
            return res
    
    def available(self, key) -> bool:
        return key in self.cache

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)
        #print('insert file {} to cache. current cache size is {}'.format(key, self.size()))

    def size(self):
        return len(self.cache)