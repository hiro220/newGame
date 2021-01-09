#!/user/bin/env python
# coding:utf-8

import pygame
from pygame.locals import *

from character.player import PlayerSample

class Game:
    def __init__(self, screen):
        self.clock = pygame.time.Clock()        # 時間管理用
        self.player = PlayerSample()
        self.exit = False
        self.backGround = pygame.Rect(0,0,1000,2000)     #背景
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


    #背景を動かす
    def move(self):
        self.backGround.move_ip(10, 10)