#!/user/bin/env python
# coding:utf-8

import pygame
from pygame.locals import *
from character.character import Character

class PlayerSample(Character):
    def __init__(self):
        super().__init__("image/character/player.png")
        pygame.sprite.Sprite.__init__(self, self.containers)
        # 画像と当たり判定の設定
        self.base_image = self.image
        self.image = pygame.transform.scale(self.image, (80, 100))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        # 移動速度
        self.dx = 10
        self.dy = 10
        # 向き
        self.pre_dire = 1
        self.direction = 1
        # 初期位置
        super().move(100, 100)

    def move(self):
        self.oldrect = self.rect.copy()
        # 押されたキーを受け取る
        self.is_flip = False
        key = pygame.key.get_pressed()
        if key[K_UP]:                       # 矢印キー上が押されているとき(長押し)
            super().move(0, -self.dy)
        if key[K_DOWN]:                     # 矢印キー下が押されているとき(長押し)
            super().move(0, self.dy)
        if key[K_RIGHT]:                    # 矢印キー右が押されているとき(長押し)
            super().move(self.dx, 0)
            self.direction = 1
        if key[K_LEFT]:                     # 矢印キー左が押されているとき(長押し)
            super().move(-self.dx, 0)
            self.direction = 0
        # 向きの設定
        self.image = pygame.transform.flip(self.image, (self.direction != self.pre_dire), False)
        self.pre_dire = self.direction

    def draw(self, screen):
        pygame.draw.rect(screen, (255,0,0), self.rect)
        x = self.rect.x + (self.rect.width * self.direction or -5)
        y = self.rect.y + self.rect.height / 4
        width = 5
        height = 5
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(x, y, width, height))
        

