from config_reader import ConfigReader
from models.simulation import Simulation
import numpy as np

np.random.seed(0)

config_path_1 = 'input.medium'
config_reader = ConfigReader(config_path_1)

simulation = Simulation(config_reader.get_config())
simulation.run()