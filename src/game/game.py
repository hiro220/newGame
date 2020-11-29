#!/user/bin/env python
# coding:utf-8

import pygame
from pygame.locals import *

from character.player import PlayerSample

class Game:
    def __init__(self, screen):
        self.player = PlayerSample()
        self.exit = False
        self.do(screen)

    def do(self, screen):
        while True:
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
                pass
            elif event.type == QUIT:
                # 終了(×ボタン)をクリック
                self.exit = True


    def draw(self, screen):
        screen.fill((255,255,255))
        self.player.draw(screen)

    