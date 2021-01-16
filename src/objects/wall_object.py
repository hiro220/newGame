import pygame
from pygame.locals import *

class WallObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("image/wall.jpg").convert_alpha()
        self.width = width
        self.height = height
        self.rect = Rect(x, y, width, height)
        
    def update(self, player):
        if pygame.sprite.collide_rect(self, player):
            self.action(player)

    def action(self, player):
        xvectols = player.oldrect.centerx
        xvectole = player.rect.centerx
        yvectols = player.oldrect.centery
        yvectole = player.rect.centery

        xvecLen = xvectole - xvectols
        yvecLen = yvectole - yvectols
        if xvecLen > 0:
            Pxvec = pygame.Rect(xvectols + (player.rect.width / 2), yvectols - (player.rect.height / 2), xvecLen, player.rect.height)
        elif xvecLen < 0:
            Pxvec = pygame.Rect(xvectole - (player.rect.width / 2), yvectols - (player.rect.height / 2), xvecLen * -1, player.rect.height)
        else:
            Pxvec = pygame.Rect(-100, -100, -100, -100)
        
        if yvecLen > 0:
            Pyvec = pygame.Rect(xvectols - (player.rect.width / 2) , yvectols + (player.rect.height / 2), player.rect.width, yvecLen)
        elif yvecLen < 0:
            Pyvec = pygame.Rect(xvectols - (player.rect.width / 2), yvectole - (player.rect.height / 2), player.rect.width, yvecLen * -1)
        else:
            Pyvec = pygame.Rect(-100, -100, -100, -100)

        if Pxvec.colliderect(self.rect):
            player.rect.move_ip(-xvecLen, 0)

        if Pyvec.colliderect(self.rect):
            player.rect.move_ip(0, -yvecLen)
            player.onfloor = True