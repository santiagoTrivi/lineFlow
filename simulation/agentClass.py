from personClass import Person
import numpy as np

class Agent(Person):
    def __init__(self, name, mu: float):
        super().__init__(name, "img/left/idle_left_0.png")
        self.mu = mu
        self.available: bool = True
        self.serveing_time = np.random.exponential(self.mu)

    def setAvailability(self, availability: bool):
        self.available = availability

    def isAvailable(self) -> bool:
        return self.available
    
    def updateServingTimeAndAvailability(self) -> None:
        self.serveing_time = np.random.exponential(self.mu)
        self.available = True