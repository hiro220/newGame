import pygame
from pygame.locals import *

class WallObject(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, width, height, vy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.width = width
        self.height = height
        self.rect = Rect(x, y, width, height)
        self.vy = vy
        
    def update(self):
        self.rect.move_ip(0, self.vy)
        # 壁にぶつかったら跳ね返る
        if self.rect.top < 0 or self.rect.bottom > 1169:
            self.vy = -self.vy