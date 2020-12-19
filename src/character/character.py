#!/user/bin/env python
# coding:utf-8

import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, img_path):
        self.image = pygame.image.load(img_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.direction = 0

    def move(self, dx, dy):
        # 引数で指定した分だけ移動する
        self.rect.move_ip(dx, dy)