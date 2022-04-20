from config_reader import ConfigReader
from filestore import FileStore
from models.simulation import Simulation
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

config_paths = ['input.light','input.medium', 'input.heavy']

for path in config_paths:
        
    config_reader = ConfigReader(path)

    configs = config_reader.get_config()

    filestore = FileStore(int(configs.num_files), float(configs.pareto_alpha))

    simulation = Simulation(configs)
    result_metrics = simulation.run() ##[(request_id, arrived_seq_id, request_response_time, cache_miss_rate, clock)]

    res = sorted(result_metrics,key = lambda i: i[4])
    x_clock = [res[i][4] for i in range(len(res))]
    y_cache_miss_rate = [res[i][3] for i in range(len(res))]
    plt.scatter(x_clock, y_cache_miss_rate)
    plt.show() 

    res = sorted(result_metrics,key = lambda i: i[0])
    x_request_id = [res[i][0] for i in range(len(res))]
    y_response_time = [res[i][2] for i in range(len(res))]
    plt.plot(x_request_id, y_response_time)
    plt.show()