import configparser
import os.path

from models.config import Config

class ConfigReader:
    res = Config()
    path = ''
    def __init__(self, path: str):
        print("path: ")
        path = os.path.join(os.path.dirname(__file__), 'config', path)
        print(path)
        if (path is None or not os.path.isfile(path)):
            print('Kindly provide valid path to config file!')
            return
        self.path = path

        parser = configparser.RawConfigParser()
        parser.read(path)
        print(parser.sections())
        simulation_section = 'Simulation'
        self.res.total_req = parser.get(simulation_section, 'Total_Requests')
        self.res.time_limit = parser.get(simulation_section, 'Time_Limit')
        self.res.num_files = parser.get(simulation_section, 'Num_Files')
        self.res.request_rate = parser.get(simulation_section, 'Request_Rate')
        self.res.network_bandwidth = parser.get(simulation_section, 'Network_Bandwidth')
        self.res.access_link_bandwidth = parser.get(simulation_section, 'Access_Link_Bandwidth')
        self.res.round_trip = parser.get(simulation_section, 'Round_Trip')
        self.res.pareto_alpha = parser.get(simulation_section, 'Pareto_Alpha')
        self.res.cache_size = parser.get(simulation_section, 'Cache_Size')
        self.res.cache_type = parser.get(simulation_section, 'Cache_Type')

    def get_config(self):
        return self.res