#!/user/bin/env python
# coding:utf-8

import pygame
from pygame.locals import *
from character.character import Character

class PlayerSample(Character):
    def __init__(self):
        super().__init__()
        self.dx = 10
        self.dy = 10

    def move(self):
        self.oldrect = self.rect.copy()
        # 押されたキーを受け取る
        key = pygame.key.get_pressed()
        if key[K_UP]:                       # 矢印キー上が押されているとき(長押し)
            super().move(0, -self.dy)
            camera.move(0, -self.dy)
            return 0, -self.dy 
        if key[K_DOWN]:                     # 矢印キー下が押されているとき(長押し)
            super().move(0, self.dy)
            camera.move(0, self.dy)
            return 0, self.dy
        if key[K_RIGHT]:                    # 矢印キー右が押されているとき(長押し)
            super().move(self.dx, 0)
            camera.move(self.dx, 0)
            self.direction = 1
            return self.dx, 0
        if key[K_LEFT]:                     # 矢印キー左が押されているとき(長押し)
            super().move(-self.dx, 0)
            camera.move(-self.dx, 0)
            self.direction = 0
            return -self.dx, 0

    def draw(self, screen):
        pygame.draw.rect(screen, (255,0,0), self.rect)
        x = self.rect.x + (self.rect.width * self.direction or -5)
        y = self.rect.y + self.rect.height / 4
        width = 5
        height = 5
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(x, y, width, height))

        