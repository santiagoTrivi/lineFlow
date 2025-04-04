import pygame 
from pygame.locals import *
from sys import exit
import pygame_gui
from inputs import SimulationInputs
from randomDB import (customersArrivalTime, agentServingTime)
from customerClass import *
from bank import *

pygame.init()
INFO = pygame.display.Info()

SCREEN_HEIGHT = INFO.current_h
SCREEM_WIDTH = INFO.current_w

SCREEN = pygame.display.set_mode((SCREEM_WIDTH, SCREEN_HEIGHT), FULLSCREEN)
pygame.display.set_caption("LineFlow")
CLOCK = pygame.time.Clock()
MANAGER = pygame_gui.UIManager((SCREEM_WIDTH, SCREEN_HEIGHT))


SIMULATION_INPUTS = SimulationInputs(MANAGER)



while True:
    UI_REFRESH_RATE = CLOCK.tick(60)/1000

    bank = Bank(SCREEN)
    customers: list[Customer] = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
            print(SIMULATION_INPUTS.UNITS_INPUT.get_text())

        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#exit_button":
            pygame.quit()
            exit()

        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_object_id == "#start_button":
            customers = customersArrivalTime(float(SIMULATION_INPUTS.LAMBDA_INPUT.get_text()), int(SIMULATION_INPUTS.UNITS_INPUT.get_text()))
            agents = agentServingTime(float(SIMULATION_INPUTS.MU_INPUT.get_text()), int(SIMULATION_INPUTS.UNITS_INPUT.get_text()), int(SIMULATION_INPUTS.SERVERS_INPUT.get_text()))
            ##for customer in customers:
                ##print(customer.name, customer.arrival_time)
            
            bank.setAgent(agents)
            
            


        MANAGER.process_events(event)

    MANAGER.update(UI_REFRESH_RATE)
    MANAGER.draw_ui(SCREEN)

    pygame.display.update()

