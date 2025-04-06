import numpy as np
import random

class Customer:
    def __init__(self, lambda_):
        self.id = random.randint(1, 1000)
        self.arrival_time = np.random.poisson(lambda_)