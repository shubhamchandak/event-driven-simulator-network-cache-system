from models.file import File


class Request:
    def __init__(self, id, file: File, creation_time):
        self.id = id
        self.file = file
        self.creation_time = creation_time
    def get_requestid(self):
        return self.id
    def get_file(self) -> File:
        return self.file
    def get_creation_time(self):
        return self.creation_time