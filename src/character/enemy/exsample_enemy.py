import pygame
from pygame.locals import *
from character.enemy.enemy_base import EnemyBase

class EnemySample(EnemyBase):
    def __init__(self):
        super().__init__(10,"image/character/enemy.png")
        self.dx = 10
        self.dy = 0
        super().move(100, 100)

    def update(self):
        self.oldrect = self.rect.copy()
        super().move(self.dx,0)
        #print("x:",self.rect.x,"y:",self.rect.y)

    def enemy_rule(self):
        print("未実装")