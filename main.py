from config_reader import ConfigReader
from filestore import FileStore
from models.simulation import Simulation
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

config_paths = ['input.medium.fifo','input.medium.lru']

for path in config_paths:
    cache_policy = path.split('.')[2].upper()
    config_reader = ConfigReader(path)

    configs = config_reader.get_config()

    filestore = FileStore(int(configs.num_files), float(configs.pareto_alpha))

    simulation = Simulation(configs)
    result_metrics = simulation.run() ##[(request_id, arrived_seq_id, request_response_time, cache_miss_rate, clock)]

    fig, ax = plt.subplots(2)
    fig.suptitle(cache_policy)

    res = sorted(result_metrics,key = lambda i: i[0])
    x_clock = [res[i][0] for i in range(len(res))]
    y_cache_miss_rate = [res[i][3] for i in range(len(res))]
    ax[0].plot(x_clock, y_cache_miss_rate)
    ax[0].set_title("Cache Miss Ratio")
    ax[0].set(xlabel='#Requests',ylabel="Cache Miss Rate")
    #plt.show() 

    res = sorted(result_metrics,key = lambda i: i[0])
    x_request_id = [res[i][0] for i in range(len(res))]
    y_response_time = [res[i][2] for i in range(len(res))]

    i = 1
    moving_averages = []
    while i < len(y_response_time):
        window = y_response_time[:i]
        window_average = sum(window)/len(window)
        moving_averages.append(window_average)
        i += 1

    ax[1].plot(x_request_id[:-1], moving_averages)
    ax[1].set_title("Average Response Time as per requests")
    ax[1].set(xlabel='#Requests',ylabel="Average Response Time (s)")
    ax[1].set_ylim(1,2)
    fig.tight_layout()
    plt.show()