import pygame
from pygame.locals import *

class DeathObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("image/object/wall.jpg").convert_alpha() #とりあえず
        self.width = width
        self.height = height
        self.rect = Rect(x, y, width, height)
        self.i = 0

    def update(self, player, enemies):
        if pygame.sprite.collide_rect(self, player):
            self.action(player)
        collided_enemy = pygame.sprite.spritecollide(self, enemies, False)
        if collided_enemy:
            for enemy in collided_enemy:
                self.action(enemy)

    def action(self, object):
        #画像は消えるけど接触判定は残ってる
        self.i+=1
        print(self.i)
        object.kill()

