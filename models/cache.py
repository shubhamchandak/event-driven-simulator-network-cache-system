from models.file import File


class Cache:
    def __init__(self):
        pass
    def get_file(self, file_id) -> File:
        file = File(1, -1)
        return file
    def cache_available(self, fileid) -> bool:
        return False #todo: actual cache implementation
    def add_file(self, file):
        pass #todo: add file to cache based on various policies and cache size
