import pygame
from pygame.locals import *
from include.map_config import *
from common.objects_origin import ObjectsOrigin 

class WallObject(ObjectsOrigin):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self, self.containers)
        org_image = pygame.image.load("image/object/wall.jpg").convert_alpha()
        self.image = pygame.transform.scale(org_image, (width * GRID_SIZE, height * GRID_SIZE))
        self.width = width
        self.height = height
        self.rect = Rect(x * GRID_SIZE, y * GRID_SIZE, width * GRID_SIZE, height * GRID_SIZE)
        
    def update(self, player, enemies):
        if pygame.sprite.collide_rect(self, player):
            self.action(player) # プレイヤーとの判定
        collided_enemy = pygame.sprite.spritecollide(self, enemies, False)
        if collided_enemy:
            for enemy in collided_enemy:
                self.action(enemy) # 敵キャラとの判定

    def action(self, object):
        # 判定対象の移動ベクトルの始点・終点
        xvectols = object.oldrect.centerx
        xvectole = object.rect.centerx
        yvectols = object.oldrect.centery
        yvectole = object.rect.centery

        # 移動ベクトルの大きさ
        xvecLen = xvectole - xvectols
        yvecLen = yvectole - yvectols

        # x方向の移動ベクトル: 判定対象が右に移動
        if xvecLen > 0:
            Pxvec = pygame.Rect(xvectols + (object.rect.width / 2), yvectols - (object.rect.height / 2), xvecLen, object.rect.height)
        # x方向の移動ベクトル: 判定対象が左に移動
        elif xvecLen < 0:
            Pxvec = pygame.Rect(xvectole - (object.rect.width / 2), yvectols - (object.rect.height / 2), xvecLen * -1, object.rect.height)
        # x方向の移動ベクトル: 判定対象が移動していない
        else:
            Pxvec = pygame.Rect(-100, -100, -100, -100)
        
        # y方向の移動ベクトル: 判定対象が下に移動
        if yvecLen > 0:
            Pyvec = pygame.Rect(xvectols - (object.rect.width / 2) , yvectols + (object.rect.height / 2), object.rect.width, yvecLen)
        # y方向の移動ベクトル: 判定対象が上に移動
        elif yvecLen < 0:
            Pyvec = pygame.Rect(xvectols - (object.rect.width / 2), yvectole - (object.rect.height / 2), object.rect.width, yvecLen * -1)
        # y方向の移動ベクトル: 判定対象が移動していない
        else:
            Pyvec = pygame.Rect(-100, -100, -100, -100)

        # x方向の判定
        # 判定対象が右方向へ移動: 壁の左側に押し出す
        # 判定対象が左方向へ移動: 壁の右側に押し出す
        if Pxvec.colliderect(self.rect):
            if xvecLen > 0:
                xvecLen = xvecLen - (self.rect.left - (xvectols + (object.rect.width / 2)))
            else:
                xvecLen = xvecLen - (self.rect.right - (xvectols - (object.rect.width / 2)))
            object.rect.move_ip(-xvecLen, 0)

        # y方向の判定
        # 判定対象が下方向へ移動: 壁の下側へ押し出す
        # 判定対象が上方向へ移動: 壁の上側へ押し出す
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
            self.extrude_object(player) # プレイヤーのと判定
        collided_enemy = pygame.sprite.spritecollide(self, enemies, False)
        if collided_enemy:
            for enemy in collided_enemy:
                self.extrude_object(enemy) # 敵キャラとの判定
        
        super().update(player, enemies)
    
    def extrude_object(self, object):
        # 自オブジェクトの移動ベクトルの始点・終点
        xvectols = self.oldrect.centerx
        xvectole = self.rect.centerx
        yvectols = self.oldrect.centery
        yvectole = self.rect.centery

        # 自オブジェクトのx方向移動ベクトルの大きさ
        xvecLen = xvectole - xvectols
        # x方向の移動ベクトル: 判定対象が右に移動
        if xvecLen > 0:
            Pxvec = pygame.Rect(xvectols + (self.rect.width / 2), yvectols - (self.rect.height / 2), xvecLen, self.rect.height)
        # x方向の移動ベクトル: 判定対象が左に移動
        elif xvecLen < 0:
            Pxvec = pygame.Rect(xvectole - (self.rect.width / 2), yvectols - (object.rect.height / 2), xvecLen * -1, self.rect.height)
        # x方向の移動ベクトル: 判定対象が移動していない
        else:
            Pxvec = pygame.Rect(-100, -100, -100, -100)

        # x方向の判定
        # 自オブジェクトが右方向へ移動: 壁の右側に押し出す
        # 自オブジェクトが左方向へ移動: 壁の左側に押し出す
        if Pxvec.colliderect(object):
            if xvecLen > 0:
                xvecLen = self.rect.right - object.rect.left
            else:
                xvecLen = self.rect.left - object.rect.right
            object.rect.move_ip(xvecLen, 0)

    def move(self, dx, dy):
        self.oldrect = self.rect.copy()
        self.rect.move_ip(dx, dy)
