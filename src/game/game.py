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
        self.exit = False
        
        self.wall_group = pygame.sprite.Group()      # オブジェクト[壁]のグループ 
        self.players = pygame.sprite.Group()
        self.timers = pygame.sprite.Group()
        PlayerSample.containers = self.players
        Timer.containers = self.timers
        self.player = PlayerSample()
        
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
        event_list = pygame.event.get()     # pygame.event.get()は取得したイベントをキューから削除する。
        self.player.move(event_list)
        self.wall_group.update(self.player)

        for event in event_list:
            if event.type == KEYDOWN:
                # キーボード入力
                pass
            elif event.type == QUIT:
                # 終了(×ボタン)をクリック
                self.exit = True

    def draw(self, screen):
        screen.fill((255,255,255))
        self.players.draw(screen)
        self.wall_group.draw(screen)
        
