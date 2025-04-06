import numpy as np
import threading
import time

class Cashier(threading.Thread):
    def __init__(self, mu: float, name: str, queue):
        self.name = name
        self.mu = mu
        self.available: bool = True
        self.queue = queue

        self.setServiceTime()
    

    def run(self):
        while True:
            customer = self.queue.get()
            print(f"{self.name} is serving customer")
            time.sleep(self.service_time)
            print(f"{self.name} finished serving customer")
            self.queue.task_done()


    def setServiceTime(self):
        self.service_time = np.random.exponential(self.mu)

    def setAvailability(self, availability: bool):
        self.available = availability


