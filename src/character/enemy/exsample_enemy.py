import pygame
from pygame.locals import *
from character.enemy.exsample_enemy import EnemyBase

class PlayerSample(Character):
    def __init__(self):
        super().__init__()
        self.dx = 10
        self.dy = 10

    def move(self):
    
    def update(self):

    def enemy_rule(self):
        
    def draw(self, screen):
        pygame.draw.rect(screen, (255,0,0), self.rect)
        x = self.rect.x + (self.rect.width * self.direction or -5)
        y = self.rect.y + self.rect.height / 4
        width = 5
        height = 5
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(x, y, width, height))