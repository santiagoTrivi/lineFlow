from agentClass import Agent
from customerClass import Customer
from pygame import *

class Bank:
    def __init__(self, screen: Surface) -> None:
        self.screen = screen
        self.queue: list[Customer] = []


    def setAgent(self, agents: list[Agent]) -> None:
        self.agents = agents
        x = 800
        y = 100
        for i, agent in enumerate(self.agents):
            y += 100
            if (i % 5) == 0:
                x = x + 100
                y = 100
            agent.render(x, y, 1)
            self.screen.blit(agent.image, agent.rect)


    def addQueue(self, customer: Customer) -> None:
        x = 400
        y = 600
        if(len(self.queue) == 0):
            customer.render(x, y, 1)
        else:
            last_customer = self.queue[-1]
            x = last_customer.x - 100
            customer.render(x, y, 1)

        self.queue.append(customer)

        self.screen.blit(customer.image, customer.rect)