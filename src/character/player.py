#!/user/bin/env python
# coding:utf-8

import pygame
from pygame.locals import *
from character.character import Character

class PlayerSample(Character):
    def __init__(self):
        super().__init__()
        self.dx = 10
        self.jump = 70
        self.onfloor = False

    def move(self):
        self.oldrect = self.rect.copy()
        # 押されたキーを受け取る
        key = pygame.key.get_pressed()
        self.natural_down()
        if key[K_d]:                    # 矢印キー右が押されているとき(長押し)
            super().move(self.dx, 0)
            self.direction = 1
        if key[K_a]:                     # 矢印キー左が押されているとき(長押し)
            super().move(-self.dx, 0)
            self.direction = 0
        if key[K_SPACE] and self.onfloor == True:
            super().move(0, -self.jump)
            self.onfloor = False

    def natural_down(self):
        if self.onfloor == False:
            super().move(0, self.gravity)

    def draw(self, screen):
        pygame.draw.rect(screen, (255,0,0), self.rect)
        x = self.rect.x + (self.rect.width * self.direction or -5)
        y = self.rect.y + self.rect.height / 4
        width = 5
        height = 5
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(x, y, width, height))
        

