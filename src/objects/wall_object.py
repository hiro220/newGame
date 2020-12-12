import pygame
from pygame.locals import *

class WallObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, vy):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("../image/wall.jpg").convert_alpha()
        self.width = width
        self.height = height
        self.rect = Rect(x, y, width, height)
        self.vy = vy
        
    def update(self):
        self.rect.move_ip(0, self.vy)
        # 壁にぶつかったら跳ね返る
        if self.rect.top < 0 or self.rect.bottom > 600:
            self.vy = -self.vy