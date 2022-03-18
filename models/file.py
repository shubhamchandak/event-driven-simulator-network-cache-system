class File:
    def __init__(self, file_id, file_size):
        self.id = file_id
        self.size = file_size
    def get_size(self):
        return self.size
    def set_file_size(self, size):
        self.size = size