from cashier import Cashier
from queue import Queue

class Bank:
    def __init__(self, lambda_: float, mu: float, cashiers_amount: int):
        self.queue = Queue()
        self.lambda_ = lambda_
        self.mu = mu
        self.cashiers: list[Cashier] = [Cashier(mu, f"Cashier {i}") for i in range(cashiers_amount)]


    def add_customer(self, customer):
        print(f"Customer {customer} arrived")
        self.queue.put(customer)