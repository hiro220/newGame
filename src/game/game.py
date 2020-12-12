#!/user/bin/env python
# coding:utf-8

import pygame
from pygame.locals import *

from character.player import PlayerSample
from objects.wall_object import WallObject

class Game:
    def __init__(self, screen):
        self.clock = pygame.time.Clock()        # 時間管理用
        self.player = PlayerSample()
        self.left_wall = pygame.Rect(-10,0,15,200)
        self.right_wall = pygame.Rect(1155,0,5,200)
        self.exit = False
        self.do(screen)

        self.wall_group = pygame.sprite.Group()      # オブジェクト[壁]のグループ 
        WallObject.containers = self.wall_group

        self.wall1 = WallObject("image/wall.jpg", 0, 0, 15, 200, 5)
        self.wall2 = WallObject("image/wall.jpg", 0, 0, 1160, -15, 5)

    def do(self, screen):
        while True:
            self.clock.tick(30)         # フレームレート(30fps)
            self.process()
            self.draw(screen)
            pygame.display.update()

            if self.exit:
                break

    def process(self):
        self.player.move()
        self.wall_group.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # キーボード入力
                pass
            elif event.type == QUIT:
                # 終了(×ボタン)をクリック
                self.exit = True


    def draw(self, screen):
        screen.fill((255,255,255))
        self.player.draw(screen)
        self.wall_group.draw()
        pygame.draw.rect(screen, (0,0,255), self.left_wall)
        pygame.draw.rect(screen, (0,0,255), self.right_wall)

    