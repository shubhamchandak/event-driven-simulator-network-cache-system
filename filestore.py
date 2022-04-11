import numpy as np

from models.file import File

class FileStore:
    files = []
    popularities = [] #probability associated with files
    num_files = 0
    def __init__(self, num_files: int, alpha_pareto: float):
        self.num_files = num_files
        file_sizes = np.random.pareto(alpha_pareto, num_files)
        popularities = np.random.pareto(alpha_pareto, num_files)
        sum_prob = np.sum(popularities)
        FileStore.popularities = popularities / sum_prob
        FileStore.files = [File(file_id=i, file_size=size) for i, size in enumerate(file_sizes)]

    def get_file():
        return np.random.choice(a=FileStore.files, p=FileStore.popularities, size=1, replace=True)[0]
