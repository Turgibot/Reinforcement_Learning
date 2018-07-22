import numpy as np
import matplotlib.pyplot as plt


class Bandit:
    def __init__(self, true_mean):
        self.true_mean = true_mean
        self.mean = 0
        self.counter = 0


    def pull_handle(self):
        return np.random.rand() + self.id
    