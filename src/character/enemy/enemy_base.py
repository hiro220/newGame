#!/user/bin/env python
# coding:utf-8

import pygame
from pygame.locals import *
from character.character import Character

class EnemyBase(Character):
    def __init__(self,hp,image_path,gravity=False):
        super().__init__(image_path)
        pygame.sprite.Sprite.__init__(self, self.containers)
        # 画像と当たり判定の設定
        self.base_image = self.image
        self.image = pygame.transform.scale(self.image, (80, 100))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.oldrect = self.rect.copy()

        # 移動速度
        self.dx = 10
        self.dy = 10
        self.enemy_hp = hp
        self.gravity = gravity

        # 向き
        #self.pre_dire = 1
        #self.direction = 1

    def hit(self,damage):
        self.hp -= damage

    
        