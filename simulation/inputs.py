import pygame_gui
import pygame

class SimulationInputs():

    def __init__(self, manager: pygame_gui.UIManager) -> None:
        WIDTH = 300

        LABELS_FROM = 5

        self.LAMBDA_LABEL = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((LABELS_FROM, 50), (WIDTH, 50)), text="lambda", manager=manager, object_id="#main_label")
        self.LAMBDA_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((200, 60), (WIDTH, 50)), manager=manager, object_id="#main_text_entry")
        
        self.MU_LABEL = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((LABELS_FROM, 100), (WIDTH, 50)), text="mu", manager=manager, object_id="#main_label")
        self.MU_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((200, 110), (WIDTH, 50)), manager=manager, object_id="#main_text_entry")
        
        self.UNITS_LABEL = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((LABELS_FROM, 150), (WIDTH, 50)), text="unidades", manager=manager, object_id="#main_label")
        self.UNITS_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((200, 160), (WIDTH, 50)), manager=manager, object_id="#main_text_entry")
        
        self.SERVERS_LABEL = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((LABELS_FROM, 200), (WIDTH, 50)), text="servidores", manager=manager, object_id="#main_label")
        self.SERVERS_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((200, 210), (WIDTH, 50)), manager=manager, object_id="#main_text_entry")

        self.start = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 260), (WIDTH - 150, 50)), text="iniciar", manager=manager, object_id="#start_button")
        self.load = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 260), (WIDTH - 150, 50)), text="cargar", manager=manager, object_id="#load_button")
        self.close = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 800), (WIDTH - 150, 50)), text="exit", manager=manager, object_id="#exit_button")