class Request:
    def __init__(self, id, file_id, creation_time):
        self.id = id
        self.file_id = file_id
        self.creation_time = creation_time
        self.response_file_size = -1
    def get_requestid(self):
        return self.id
    def get_file_id(self):
        return self.file_id
    def get_creation_time(self):
        return self.creation_time
    def set_response_file_size(self, file_size):
        self.response_file_size = file_size
    def get_response_file_size(self):
        return self.response_file_size