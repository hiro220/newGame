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
            Pxvec = pygame.Rect(xvectols + (player.rect.width / 2), yvectols, xvecLen, 1)
        elif xvecLen < 0:
            Pxvec = pygame.Rect(xvectole - (player.rect.width / 2), yvectols, xvecLen * -1, 1)
        else:
            Pxvec = pygame.Rect(-100, -100, -100, -100)
        
        if yvecLen > 0:
            Pyvec = pygame.Rect(xvectols, yvectols + (player.rect.height / 2), 1, yvecLen)
        elif yvecLen < 0:
            Pyvec = pygame.Rect(xvectols, yvectole - (player.rect.height / 2), 1, yvecLen * -1)
        else:
            Pyvec = pygame.Rect(-100, -100, -100, -100)

        obj_rightline = pygame.Rect(self.rect.right - 1, self.rect.top, 1, self.rect.height)
        obj_leftline = pygame.Rect(self.rect.left, self.rect.top, 1, self.rect.height)
        obj_bottomline = pygame.Rect(self.rect.left, self.rect.bottom - 1, self.rect.width, 1)
        obj_topline = pygame.Rect(self.rect.left, self.rect.top, self.rect.width, 1)

        if Pxvec.colliderect(obj_rightline):
            player.rect.move_ip(player.dx, 0)

        if Pxvec.colliderect(obj_leftline):
            player.rect.move_ip(-player.dx, 0)

        if Pyvec.colliderect(obj_bottomline):
            player.rect.move_ip(0, player.dy)

        if Pyvec.colliderect(obj_topline):
            player.rect.move_ip(0, -player.dy)