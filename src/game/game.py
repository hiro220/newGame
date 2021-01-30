#!/user/bin/env python
# coding:utf-8

import pygame
from pygame.locals import *

from character.player import PlayerSample
from character.enemy.enemy_base import EnemyBase     #enemyで追加したプログラム
from character.enemy.exsample_enemy import EnemySample   #enemyで追加したプログラム
from objects.wall_object import WallObject
from common.timer import Timer
from items.item import Item
from items.sample import SampleItem

class Game:
    def __init__(self, screen):
        self.clock = pygame.time.Clock()        # 時間管理用
        self.exit = False

        self.wall_group = pygame.sprite.Group()      # オブジェクト[壁]のグループ 
        self.players = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.timers = pygame.sprite.Group()
        self.items = pygame.sprite.Group()

        PlayerSample.containers = self.players
        EnemyBase.containers = self.enemies
        Timer.containers = self.timers
        WallObject.containers = self.wall_group
        Item.containers = self.items

        self.player = PlayerSample()
        self.enemy = EnemySample()      #enemyで追加したプログラム
        
        for i in range(0, 600, 100):
            WallObject(0, i, 100, 100)

        for i in range(0, 600, 100):
            WallObject(1060, i, 100, 100)

        for i in range(0, 1200, 100):
            WallObject(i, 500, 100, 100)

        for i in range(0, 1200, 100):
            WallObject(i, 0, 100, 100)

        SampleItem(700,430)

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
        self.player.move()
        self.enemies.update()      #enemyで追加したプログラム
        self.wall_group.update(self.player)
        self.items.update(self.players)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # キーボード入力
                pass
            elif event.type == QUIT:
                # 終了(×ボタン)をクリック
                self.exit = True

    def draw(self, screen):
        screen.fill((255,255,255))
        self.players.draw(screen)
        self.enemies.draw(screen)      #enemyで追加したプログラム
        self.wall_group.draw(screen)
        self.items.draw(screen)
        
