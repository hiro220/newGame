import pygame
from pygame.locals import *
from character.enemy.enemy_base import EnemyBase

class EnemySample(EnemyBase):
    def __init__(self, player):
        super().__init__(10,"image/character/enemy.png",1, player)
        self.dx = 0
        self.dy = 0
        super().move(200, 100)
        self.rule_flag = 0

    def update(self):
        self.oldrect = self.rect.copy()
        super().update()

        self.enemy_rule()
        super().move(self.dx,self.dy)

        if self.collision_detection():
            print("プレイヤーと当たってます。")
        else:
            print("プレイヤーと当たっていません。")

    def enemy_rule(self):
        self.rule_flag += 1
        if self.rule_flag >= 60 and self.rule_flag < 180:
            self.dx = 3
        elif self.rule_flag >= 180:
            self.dx = 6
            
