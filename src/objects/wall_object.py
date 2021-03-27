import pygame
from pygame.locals import *

class WallObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("image/object/wall.jpg").convert_alpha()
        self.width = width
        self.height = height
        self.rect = Rect(x, y, width, height)
        
    def update(self, player, enemies):
        if pygame.sprite.collide_rect(self, player):
            self.action(player)
        collided_enemy = pygame.sprite.spritecollide(self, enemies, False)
        if collided_enemy:
            for enemy in collided_enemy:
                self.action(enemy)

    def action(self, object):
        xvectols = object.oldrect.centerx
        xvectole = object.rect.centerx
        yvectols = object.oldrect.centery
        yvectole = object.rect.centery

        xvecLen = xvectole - xvectols
        yvecLen = yvectole - yvectols
        if xvecLen > 0:
            Pxvec = pygame.Rect(xvectols + (object.rect.width / 2), yvectols - (object.rect.height / 2), xvecLen, object.rect.height)
        elif xvecLen < 0:
            Pxvec = pygame.Rect(xvectole - (object.rect.width / 2), yvectols - (object.rect.height / 2), xvecLen * -1, object.rect.height)
        else:
            Pxvec = pygame.Rect(-100, -100, -100, -100)
        
        if yvecLen > 0:
            Pyvec = pygame.Rect(xvectols - (object.rect.width / 2) , yvectols + (object.rect.height / 2), object.rect.width, yvecLen)
        elif yvecLen < 0:
            Pyvec = pygame.Rect(xvectols - (object.rect.width / 2), yvectole - (object.rect.height / 2), object.rect.width, yvecLen * -1)
        else:
            Pyvec = pygame.Rect(-100, -100, -100, -100)

        if Pxvec.colliderect(self.rect):
            if xvecLen > 0:
                xvecLen = xvecLen - (self.rect.left - (xvectols + (object.rect.width / 2)))
            else:
                xvecLen = xvecLen - (self.rect.right - (xvectols - (object.rect.width / 2)))
            object.rect.move_ip(-xvecLen, 0)

        if Pyvec.colliderect(self.rect):
            if yvecLen > 0:
                yvecLen = yvecLen - (self.rect.top - (yvectols + (object.rect.height / 2)))
                object.onfloor = True
            else:
                yvecLen = yvecLen - (self.rect.bottom - (yvectols - (object.rect.height / 2)))
            object.rect.move_ip(0, -yvecLen)

class MovingFloor(WallObject):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.oldrect = self.rect.copy()
        self.dx = 5
        self.dy = 0
        
    def update(self, player, enemies):
        self.move(self.dx, self.dy)
        if pygame.sprite.collide_rect(self, player):
            self.extrude_object(player)
        collided_enemy = pygame.sprite.spritecollide(self, enemies, False)
        if collided_enemy:
            for enemy in collided_enemy:
                self.extrude_object(enemy)
        
        super().update(player, enemies)
    
    def extrude_object(self, object):
        xvectols = self.oldrect.centerx
        xvectole = self.rect.centerx
        yvectols = self.oldrect.centery
        yvectole = self.rect.centery

        xvecLen = xvectole - xvectols
        if xvecLen > 0:
            Pxvec = pygame.Rect(xvectols + (self.rect.width / 2), yvectols - (self.rect.height / 2), xvecLen, self.rect.height)
        elif xvecLen < 0:
            Pxvec = pygame.Rect(xvectole - (self.rect.width / 2), yvectols - (object.rect.height / 2), xvecLen * -1, self.rect.height)
        else:
            Pxvec = pygame.Rect(-100, -100, -100, -100)

        if Pxvec.colliderect(object):
            if xvecLen > 0:
                xvecLen = self.rect.right - object.rect.left
            else:
                xvecLen = self.rect.left - object.rect.right
            object.rect.move_ip(xvecLen, 0)

    def move(self, dx, dy):
        self.oldrect = self.rect.copy()
        self.rect.move_ip(dx, dy)
