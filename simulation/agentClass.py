from personClass import Person

class Agent(Person):
    def __init__(self, name, serving_time: list[float] ):
        super().__init__(name, "img/left/idle_left_0.png")
        self.available: bool = True
        self.serveing_time: list[float] = serving_time

    def setAvailability(self, availability: bool):
        self.available = availability

    def isAvailable(self) -> bool:
        return self.available