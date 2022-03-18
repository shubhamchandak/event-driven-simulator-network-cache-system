from urllib import request
import numpy as np
from queue import PriorityQueue, Queue

from models.cache import Cache
from models.file import File
from models.event import Event
from models.request import Request


class Simulation:
    def __init__(self): 
        self.num_of_request = 0
        self.clock = 0.0
        self.ra = 15
        self.rc = 1000
        self.queue: PriorityQueue[Event] = PriorityQueue()
        self.cache = Cache()
        self.alpha_pareto_file_size = 5.0 ##must be float
        self.alpha_pareto_file_id = 100.0 ##must be float
        self.lamda_inter_arrival = 1000
        self.total_time_of_requests_served = 0
        self.num_of_request_served = 0
        self.fifo_queue: Queue[Request] = Queue(maxsize=0)
        self.max_request = 1000 #simulation to be run over {} requests

    def handle_new_request_event(self, event: Event):
        request = event.get_request()
        file_id = request.get_file_id()
        if self.cache.cache_available(file_id):
            file = self.cache.get_file(file_id)
            new_event_time = self.clock + file.get_size() / self.rc
            file_received_event = Event("file_received", self.clock, new_event_time, request)
            self.add_new_event(file_received_event)
        else: 
            new_event_time = self.clock + self.get_roundtrip_time()
            request.set_response_file_size(self.get_new_file_size())
            arrive_at_queue_event = Event("arrive_at_queue", self.clock, new_event_time, request)
            self.add_new_event(arrive_at_queue_event)
            if(self.num_of_request < self.max_request):
                self.generate_new_request_event()

    def handle_file_received_event(self, event: Event):
        request = event.get_request()
        self.num_of_request_served += 1
        total_time = self.clock - request.get_creation_time()
        self.total_time_of_requests_served += total_time
        print('request: ' + request.get_requestid() + ' has been served at ' + self.clock)

    def handle_arrive_at_queue_event(self, event: Event):
        request = event.get_request()
        file_size = request.get_response_file_size()
        if(self.fifo_queue.empty()):
            event_time = self.clock + file_size / self.ra
            new_event = Event("depart_queue", self.clock, event_time, request)
            self.add_new_event(new_event)
        else:
            self.fifo_queue.put(request)

    def handle_depart_queue_event(self, event: Event):
        request = event.get_request()
        new_file = File(request.get_file_id(), request.get_response_file_size())
        self.cache.add_file(new_file)
        new_event_time = self.clock + new_file.get_size() / self.rc
        new_event = Event("file_received", self.clock, new_event_time, request)
        self.add_new_event(new_event)
        if not self.fifo_queue.empty():
            new_request = self.fifo_queue.get()
            file_size = new_request.get_response_file_size()
            new_depart_queue_event = Event("depart_queue", self.clock, self.clock + file_size/self.ra, new_request)
            self.add_new_event(new_depart_queue_event)

    def add_new_event(self, event: Event):
        self.queue.put(event.get_event_time(), event)

    def get_roundtrip_time(self):
        return np.random.lognormal() #check

    def generate_new_request_event(self):
        event_time = self.clock + self.get_interarrival()
        self.num_of_request += 1
        new_request = Request(self.num_of_request, self.get_new_file_id(), self.clock)
        new_request_event = Event("new_request", self.clock, event_time, new_request)
        self.add_new_event(new_request_event)

    def get_interarrival(self):
        return np.random.exponential(1./self.lamda_inter_arrival)

    def get_new_file_size(self):
        return np.random.pareto(a=self.alpha_pareto_file_size)

    def get_new_file_id(self):
        return np.random.pareto(a=self.alpha_pareto_file_id)
    
    def run(self):
        self.generate_new_request_event()
        while not self.queue.empty:
            event = self.queue.get()
            event_type = event.get_type()
            match event_type:
                case "new_request": 
                    self.handle_new_request_event(event)
                    break
                case "arrive_at_queue":
                    self.handle_arrive_at_queue_event(event)
                    break
                case "depart_queue":
                    self.handle_depart_queue_event(event)
                    break
                case "file_received":
                    self.handle_file_received_event(event)
                    break
        return self.total_time_of_requests_served / self.num_of_request_served


np.random.seed(0)

s = Simulation()
s.run()