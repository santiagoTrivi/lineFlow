import numpy as np
from customerClass import *
from agentClass import *


def customersArrivalTime(lamba_: float) -> Customer:
    return Customer(f"Customer", lamba_)


def agentServingTime(mu: float, random_numbers_amount: int) -> list[Agent]:
    agents = []
    for i in range(random_numbers_amount):
        agents.append(Agent(f"Agent", mu))
    return agents    


