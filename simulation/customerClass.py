from personClass import Person

class Customer(Person):
    def __init__(self, name, arrival_time):
        super().__init__(name, "img/right/idle_right_0.png")
        self.arrival_time = arrival_time