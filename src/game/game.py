#!/user/bin/env python
# coding:utf-8

import pygame
from pygame.locals import *

from character.player import PlayerSample
from character.enemy.enemy_base import EnemyBase     #enemyで追加したプログラム
from character.enemy.exsample_enemy import EnemySample   #enemyで追加したプログラム
from objects.wall_object import WallObject, MovingFloor
from common.timer import Timer
from objects.camera import Camera

class Game:
    def __init__(self, screen):
        self.clock = pygame.time.Clock()        # 時間管理用
        self.exit = False
        self.screen = screen

        self.wall_group = pygame.sprite.Group()      # オブジェクト[壁]のグループ 
        self.players = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.timers = pygame.sprite.Group()
        self.camera_group = pygame.sprite.Group()

        PlayerSample.containers = self.players, self.camera_group
        EnemyBase.containers = self.enemies, self.camera_group
        WallObject.containers = self.wall_group, self.camera_group
        Timer.containers = self.timers
        print("containers")

        self.player = PlayerSample(100, 100)
        self.enemy = EnemySample(400,200, self.player)      #enemyで追加したプログラム
        self.camera = Camera(self.camera_group, self.player)

    def do(self):
        self.camera.initCamera()
        while True:
            self.clock.tick(30)         # フレームレート(30fps)
            self.process()
            self.camera.process()
            self.draw(self.screen)
            pygame.display.update()

            if self.exit:
                break

    def process(self):
        self.timers.update()
        event_list = pygame.event.get()     # pygame.event.get()は取得したイベントをキューから削除する。
        self.player.move(event_list)
        self.enemies.update()      #enemyで追加したプログラム
        self.wall_group.update(self.player, self.enemies)

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
        self.enemies.draw(screen)      #enemyで追加したプログラム
        self.wall_group.draw(screen)
        