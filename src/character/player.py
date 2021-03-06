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
        self.onfloor = False
        # 向き
        self.pre_dire = 1
        self.direction = 1
        # 初期位置
        super().move(100, 100)

        self.jump_count = 0
        pygame.key.set_repeat(5, 10)

    def move(self, event_list):
        self.oldrect = self.rect.copy()
        # 押されたキーを受け取る
        self.is_flip = False
        key = pygame.key.get_pressed()
        self.natural_down()
        if key[K_d]:                    # 矢印キー右が押されているとき(長押し)
            super().move(self.dx, 0)
            self.direction = 1
        if key[K_a]:                     # 矢印キー左が押されているとき(長押し)
            super().move(-self.dx, 0)
            self.direction = 0

        for event in event_list:
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.jump_count += 1
                    self.jump()
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    self.onfloor = False
                    self.jump_count = 0
                               
        
         # 向きの設定
        self.image = pygame.transform.flip(self.image, (self.direction != self.pre_dire), False)
        self.pre_dire = self.direction

    def jump(self):
        if self.onfloor and self.jump_count < 50:
            super().move(0, -self.dy)
    
    def natural_down(self):
        super().move(0, self.gravity)

