#!/user/bin/env python
# coding:utf-8

import pygame
from pygame.locals import *
from character.character import Character

class EmenySample(Character):
    def __init__(self):x
        super().__init__()
        self.dx = 10
        self.dy = 10

    def move(self):
        super().move(self.dx,self.dy)
    
    def enemy_rule(self):