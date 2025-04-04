import pygame 

class Person(pygame.sprite.Sprite):
    def __init__(self, name, image_path):
        self.name = name
        self.image_path = image_path

    def render(self, x, y, scale):
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect = (self.x, self.y)
    



