from common.objects_origin import ObjectsOrigin
import pygame
from pygame.locals import *
from include.game_object import GameObject
from include.window import *
from include.map_config import *
from objects.wall_object import WallObject
from common.object_tab import ObjectTab

import os
import json

class CreateMap:
    def __init__(self, screen):
        font = pygame.font.Font(None, 25)
        self.exit_text = font.render("Q(click x)", True, (255,0,0))   #テキストSTART_GAME
        self.exit = False
        
        # マップ作成用情報
        self.object_list = []                       # 設置済みオブジェクト一覧
        self.data = {"object" : self.object_list}   # マップ情報
        self.setted_grid = []                       # オブジェクト設置済み座標リスト
        self.mouse_down = False                     # マウス押下状態
        self.object_id = "-1"                       # 選択中のオブジェクト

        # オブジェクト表示タブ
        self.tab = ObjectTab(screen, 1060, 0)

        self.clock = pygame.time.Clock()        # 時間管理用
        self.screen = screen

        self.object = pygame.sprite.Group()
        ObjectsOrigin.containers = self.object

        self.obj = None

        self.do()

    def do(self):
        while True:
            self.clock.tick(30)         # フレームレート(30fps)
            self.process()
            self.draw(self.screen)
            pygame.display.update()

            if self.exit:
                break
    
    def process(self):
        event_list = pygame.event.get()     # pygame.event.get()は取得したイベントをキューから削除する。

        self.tab.updateClickedButton(event_list)
        self.object_id = self.tab.retButtonID()

        for event in event_list:
            if event.type == QUIT:
                # 終了(×ボタン)をクリック
                self.saveMap()
                self.exit = True
            # マウス操作
            if event.type == MOUSEBUTTONUP and event.dict["button"] == 1:
                # 左クリック
                self.mouse_down = False
            if event.type == MOUSEBUTTONDOWN and event.dict["button"] == 1:
                # 左クリック押下
                self.mouse_down = True
                x, y = self.pix2Grid(event.dict["pos"])
                self.setObject(x, y)
            if event.type == MOUSEMOTION and self.mouse_down:
                # マウス移動
                x, y = self.pix2Grid(event.dict["pos"])
                self.setObject(x, y)

    def draw(self, screen):
        self.screen.fill((255,255,255))
        self.showGrid()
        self.screen.blit(self.exit_text, [10, 10])         # START GAMEを描画
        self.object.draw(screen)
        self.tab.showTab()

    def showGrid(self):
        gridx_size, gridy_size = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
        for x in range(gridx_size):
            pygame.draw.line(self.screen, (0,0,0), (x*GRID_SIZE, 0), (x*GRID_SIZE, HEIGHT))
        for y in range(gridy_size):
            pygame.draw.line(self.screen, (0,0,0), (0, y*GRID_SIZE), (WIDTH, y*GRID_SIZE))

    def pix2Grid(self, position):
        # ピクセル位置からグリッド位置に変換する
        x, y = position
        return x // GRID_SIZE, y // GRID_SIZE


    def setObject(self, x, y):
        # すでにオブジェクトのある座標は無視する
        if (x, y) in self.setted_grid:
            return
        # 選択中でない
        if "-1" == self.object_id:
            return
        # オブジェクト情報の追加
        obj_info = {"name" : self.object_id, "x" : x, "y" : y}
        self.setted_grid += [(x, y)]
        self.object_list += [obj_info]
        # オブジェクト描画処理
        GameObject[self.object_id](x, y)
        
    def saveMap(self):
        # 作成したマップ情報を保存
        filepath = "mapinfo/map1.json"
        if not os.path.exists("mapinfo"):
            os.mkdir("mapinfo")
        fp = open(filepath, 'w', encoding="utf-8")
        json.dump(self.data, fp, indent=2)
        fp.close()
