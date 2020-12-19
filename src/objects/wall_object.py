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
        # プレイヤーが左からオブジェクトへ衝突した場合
        if player.rect.left < self.rect.left and player.rect.right < self.rect.right:
            player.rect.move_ip(-player.dx, 0)

        # プレイヤーが右からオブジェクトへ衝突した場合
        if self.rect.left < player.rect.left and self.rect.right < player.rect.right:
            player.rect.move_ip(player.dx, 0)

        # プレイヤーが上からオブジェクトへ衝突した場合
        if self.rect.top < player.rect.top and self.rect.bottom < player.rect.bottom:
            player.rect.move_ip(0, -player.dy)

        # プレイヤーが下からオブジェクトへ衝突した場合
        if player.rect.top < self.rect.top and player.rect.bottom < self.rect.bottom:
            player.rect.move_ip(0, player.dy)
            