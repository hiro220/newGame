#!/user/bin/env python
# coding:utf-8

import pygame
from pygame.locals import *
from character.character import Character

from include.map_config import *

class EnemyBase(Character):
    def __init__(self, x, y, image_path, size_x, size_y):
        super().__init__(image_path)
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.setInitGridPos(x, y)
        # 画像と当たり判定の設定
        self.base_image = self.image
        self.image = pygame.transform.scale(self.image, (int(size_x*GRID_SIZE), int(size_y*GRID_SIZE)))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
    
        # 移動速度
        self.dx = 10
        self.dy = 10
        self.enemy_hp = 10
        self.gravity = 0

        # 特定の場所の移動する
        self.move(x*GRID_SIZE,y*GRID_SIZE)


    def set_gravity(self, gravity_par):
        self.gravity = gravity_par

    def set_hp(self, hp):
        self.enemy_hp = hp

    def update(self):
        self.gravity_effect()
        

    def hit(self,damage):
        self.hp -= damage
    

    def gravity_effect(self):
        super().move(0, self.gravity)
    
    # プレイヤーとのあたり判定を測定
    def collision_detection(self, player):
        if self.rect.colliderect(player.rect):
            return True
        else:
            return False



    
        