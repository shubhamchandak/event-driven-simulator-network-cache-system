from config_reader import ConfigReader
from filestore import FileStore
from models.simulation import Simulation
import numpy as np

np.random.seed(0)

config_path_1 = 'input.medium'
config_reader = ConfigReader(config_path_1)

configs = config_reader.get_config()

filestore = FileStore(int(configs.num_files), float(configs.pareto_alpha))

simulation = Simulation(configs)
simulation.run()