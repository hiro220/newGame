import pygame
from pygame.locals import *

class WallObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("../image/wall.jpg").convert_alpha()
        self.width = width
        self.height = height
        self.rect = Rect(x, y, width, height)
        
    def update(self, player):
        if pygame.sprite.collide_rect(self, player):
            self.action(player)

    def action(self, player):
        print("old", player.oldrect.left, "new", player.rect.left)
        xvectols = player.oldrect.centerx
        xvectole = player.rect.centerx
        print("xvectole: ", xvectole)
        yvectols = player.oldrect.centery
        yvectole = player.rect.centery

        xvecLen = xvectole - xvectols
        yvecLen = yvectole - yvectols
        print("xvecLen: ", xvecLen)
        if xvecLen > 0:
            print("result", xvectols)
            Pxvec = pygame.Rect(xvectols + (player.rect.width / 2), yvectols, xvecLen, 1)
            print("PxvecLeft: ", Pxvec.left, "Pxvecright: ", Pxvec.right, "Pxvectop", Pxvec.top, "Pxvecbottom", Pxvec.bottom)
        elif xvecLen < 0:
            Pxvec = pygame.Rect((xvectole - (player.rect.width / 2)), yvectols, xvecLen * -1, 1)
        else:
            return
        
        if yvecLen > 0:
            Pyvec = pygame.Rect(xvectols, yvectols, 0, yvectole)

        obj_rightline = pygame.Rect(self.rect.right - 1, self.rect.top, 1, self.rect.bottom)
        obj_leftline = pygame.Rect(self.rect.left, self.rect.top, 1, self.rect.height)
        print("obj_leftline.left", obj_leftline.left, "obj_left_line.right", obj_leftline.right, "obj_leftline.top", obj_leftline.top, "obj_left_line.bottom", obj_leftline.bottom)
        obj_bottomline = pygame.Rect(self.rect.left, self.rect.bottom, self.rect.right, 0)
        obj_topline = pygame.Rect(self.rect.left, self.rect.top, self.rect.bottom, 0)

        print("Pxvecx", Pxvec.left, Pxvec.right, ": obj_rightline", obj_rightline.right)
        if Pxvec.colliderect(obj_rightline):
            player.rect.move_ip(player.dx, 0)
            print("left")

        if Pxvec.colliderect(obj_leftline):
            player.rect.move_ip(-player.dx, 0)
            print("right")

        #if Pyvec.colliderect(obj_bottomline):
        #    player.rect.move_ip(player.dy, 0)
        #    print("top")

        #if Pyvec.colliderect(obj_topline):
        #    player.rect.move_ip(-player.dy, 0)
        #    print("bottom")