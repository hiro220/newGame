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
        self.exit = False
        self.wall_group = pygame.sprite.Group()      # オブジェクト[壁]のグループ 
        WallObject.containers = self.wall_group
        WallObject(0, 0, 15, 600)
        WallObject(1145, 0, 15, 600)
        WallObject(0, 545, 1160, 15)
        self.do(screen)

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
        self.collide_judge(self.player, self.wall_group)

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
        self.wall_group.draw(screen)

    def collide_judge(self, player, wall_group):
        print(player.rect.left)
        collide_list = pygame.sprite.spritecollide(player, wall_group, False)
        if collide_list:
            for collided_object in collide_list:
                collided_object.update(player)
        else:
            print("debug")

    