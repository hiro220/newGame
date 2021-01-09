#!/user/bin/env python
# coding:utf-8

import pygame
from pygame.locals import *
from character.character import Character

class EnemyBase(Character):
    def __init__(self,hp,gravity):
        super().__init__()
        self.dx = 10
        self.dy = 10
        self.enemy_hp = hp
        self.gravity = grabity

    def move(self):
        super().move(self.dx,self.dy)

    def hp(self,damege):
        self.hp -= damege

    
        