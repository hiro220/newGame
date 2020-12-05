#!/user/bin/env python
# coding:utf-8

import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self):
        self.rect = pygame.Rect(0,0,20,60)
        self.direction = 0
        self.gravity = 1.0

    def move(self, dx, dy):
        # 引数で指定した分だけ移動する
        self.rect.move_ip(dx, dy)
