import pygame
from pygame.locals import *

class WallObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("../image/wall.jpg").convert_alpha()
        self.width = width
        self.height = height
        self.rect = Rect(x, y, width, height)
        
    def update(self):
