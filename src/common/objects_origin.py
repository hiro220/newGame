import pygame

class ObjectsOrigin(pygame.sprite.Sprite):
    def __init__(self):
        self.image = None


    def get_image(self):
        return self.image