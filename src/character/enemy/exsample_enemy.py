import pygame
from pygame.locals import *
from character.enemy.enemy_base import EnemyBase

class EnemySample(EnemyBase):
    def __init__(self):
        super().__init__(10,True)
        self.dx = 10
        self.dy = 10

    def move(self):
        super().move(self.dx,0)

    def enemy_rule(self):
        print("aaaaaaaa")

    def draw(self, screen):
        pygame.draw.rect(screen, (255,0,0), self.rect)
        x = self.rect.x + (self.rect.width * self.direction or -5)
        y = self.rect.y + self.rect.height / 4
        width = 5
        height = 5
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(x, y, width, height))