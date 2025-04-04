from personClass import Person
import numpy as np

class Customer(Person):
    def __init__(self, name, lambda_):
        super().__init__(name, "img/right/idle_right_0.png")
        self.arrival_time = np.random.poisson(lambda_)