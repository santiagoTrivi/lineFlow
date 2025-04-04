import numpy as np
from customerClass import *
from agentClass import *


def customersArrivalTime(lambda_: float, variables_amount: int) -> list[Customer]:
    customers = []
    db = np.random.poisson(lambda_, variables_amount).tolist()
    for row, item in enumerate(db):
        customers.append(Customer(f"Customer{row}", item))
    return customers


def agentServingTime(mu: float, variables_amount: int, random_numbers_amount: int) -> list[Agent]:
    agents = []

    for i in range(random_numbers_amount):
        agents.append(Agent(f"Agent{i}", np.random.exponential(mu, variables_amount).tolist()))
    return agents    
