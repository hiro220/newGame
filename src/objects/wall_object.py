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
            else:
                yvecLen = yvecLen - (self.rect.bottom - (yvectols - (object.rect.height / 2)))
            object.rect.move_ip(0, -yvecLen)
            object.onfloor = True

class MovingFloor(WallObject):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.dx = 5
        self.dy = 0
    
    def update(self, player, enemies):
        self.move(self.dx, self.dy)
        super().update(player, enemies)
    
    def move(self, dx, dy):
        self.rect.move_ip(dx, dy)

class DeathObject(WallObject):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("image/object/wall.jpg").convert_alpha() #とりあえず
        self.width = width
        self.height = height
        self.rect = Rect(x, y, width, height)
        self.i = 0 

    def action(self, object):
        #画像は消えるけど接触判定は残ってる
        self.i+=1
        print(self.i)
        object.kill()
