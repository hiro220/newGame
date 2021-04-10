#!/user/bin/env python
# coding:utf-8

import pygame
from pygame.locals import *

from character.player import PlayerSample
from objects.wall_object import WallObject
from common.timer import Timer

class Game:
    def __init__(self, screen):
        self.clock = pygame.time.Clock()        # 時間管理用
        self.player = PlayerSample()
        self.exit = False
        self.backGround = pygame.Rect(0,0,1000,2000)     #背景
        self.wall_group = pygame.sprite.Group()      # オブジェクト[壁]のグループ 
        self.timers = pygame.sprite.Group()
        self.camera = Camera()

        WallObject.containers = self.wall_group
        Timer.containers = self.timers

        for i in range(0, 600, 100):
            WallObject(0, i, 100, 100)

        for i in range(0, 600, 100):
            WallObject(1060, i, 100, 100)

        for i in range(0, 1200, 100):
            WallObject(i, 500, 100, 100)

        for i in range(0, 1200, 100):
            WallObject(i, 0, 100, 100)

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
        self.timers.update()
        self.backxy = self.player.move()
        print(self.backxy)
        self.wall_group.update(self.player)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # キーボード入力
                self.move()
                pass
            elif event.type == QUIT:
                # 終了(×ボタン)をクリック
                self.exit = True

    def draw(self, screen):
        screen.fill((0,0,0))
        pygame.draw.rect(screen, (255,255,255), self.backGround)   #背景を描画する
        self.player.draw(screen)
        #self.wall_group.draw(screen)


    #背景を動かす
    def move(self):
        print(1)
        #print(self.backxy)
        #self.backGround.move_ip(self.backxy[0], self.backxy[1])