from models.request import Request


class Event:
    def __init__(self, type, creation_time, event_time, request):
        self.type = type
        self.creation_time = creation_time
        self.event_time = event_time
        self.request = request
    def get_request(self) -> Request:
        return self.request
    def get_event_time(self):
        return self.event_time
    def get_type(self):
        return self.type