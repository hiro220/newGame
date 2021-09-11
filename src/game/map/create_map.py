from common.objects_origin import ObjectsOrigin
import pygame
from pygame.locals import *
from common.scrollBar import ScrollBar
from include.game_object import GameObject
from include.window import *
from include.map_config import *
from objects.wall_object import WallObject
from common.object_tab import ObjectTab

import os
import json

class CreateMap:
    def __init__(self, screen, map_id = 1):
        font = pygame.font.Font(None, 25)
        self.exit_text = font.render("Q(click x)", True, (255,0,0))   #テキストSTART_GAME
        self.exit = False
        
        # マップ作成用情報
        self.map_id = map_id
        self.samnail = "image/samnail/map{}.png".format(self.map_id)
        self.object_list = []                       # 設置済みオブジェクト一覧
        self.data = {M_OBJECT : self.object_list}   # マップ情報
        self.setted_grid = []                       # オブジェクト設置済み座標リスト
        self.mouse_down = False                     # マウス押下状態
        self.object_id = "-1"                       # 選択中のオブジェクト

        # オブジェクト表示タブ
        self.tab = ObjectTab(screen, 1060, 0)

        # スクロールバー
        scrollw_rect = Rect(0, HEIGHT-10, WIDTH, 10)
        self.scroll_width = ScrollBar(scrollw_rect, WIDTH // GRID_SIZE, 80, 1)
        scrollh_rect = Rect(WIDTH-10, 0, 10, HEIGHT-10)
        self.scroll_height = ScrollBar(scrollh_rect, HEIGHT // GRID_SIZE, 50, 1, vertical=True)
        self.current_pos = (0, 0)               # 表示しているグリッド位置

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
        pygame.key.set_repeat()
        event_list = pygame.event.get()     # pygame.event.get()は取得したイベントをキューから削除する。

        # スクロールバーの処理
        self.scrollProcess(event_list)

        self.tab.updateClickedButton(event_list)
        self.object_id = self.tab.retButtonID()
        
        for event in event_list:
            if event.type == QUIT:
                # 終了(×ボタン)をクリック
                self.saveMap()
                self.exit = True
            if event.type == KEYDOWN and event.key == K_s:
                self.saveSamnail()
            # マウス操作
            if (event.type == MOUSEBUTTONUP) and (event.dict["button"] == 1):
                # 左クリック
                self.mouse_down = False
            if (event.type == MOUSEBUTTONDOWN) and (event.dict["button"] == 1):
                # 左クリック押下
                self.mouse_down = True
                x, y = self.pix2Grid(event.dict["pos"])
                self.setObject(x, y)
            if (event.type == MOUSEMOTION) and self.mouse_down:
                # マウス移動
                x, y = self.pix2Grid(event.dict["pos"])
                self.setObject(x, y)

    def draw(self, screen):
        self.screen.fill((255,255,255))
        self.showGrid()
        self.screen.blit(self.exit_text, [10, 10])         # START GAMEを描画
        self.object.draw(screen)
        self.tab.showTab()
        self.scroll_height.draw(screen)
        self.scroll_width.draw(screen)

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
        # 実位置の調整
        act_x, act_y = x + self.current_pos[0], y + self.current_pos[1]
        # 選択中でない
        if "-1" == self.object_id:
            return
        # 消しゴムツール
        if ERASER == self.object_id:
            self.deleteObject(act_x, act_y)
            return
        # すでにオブジェクトのある座標は無視する
        if (act_x, act_y) in self.setted_grid:
            return
        # オブジェクト情報の追加
        obj_info = {M_NAME : self.object_id, M_X : act_x, M_Y : act_y, M_ARGS:[]}
        self.setted_grid += [(act_x, act_y)]
        self.object_list += [obj_info]
        # オブジェクト描画処理
        GameObject[self.object_id](x, y)
        
    def saveMap(self):
        # サムネイルを保存していないならここで保存
        if M_SAMNAIL not in self.data:
            self.saveSamnail()
        # 作成したマップ情報を保存
        filepath = "mapinfo/map{}.json".format(self.map_id)
        if not os.path.exists("mapinfo"):
            os.mkdir("mapinfo")
        fp = open(filepath, 'w', encoding="utf-8")
        json.dump(self.data, fp, indent=2)
        fp.close()

    def deleteObject(self, x, y):
        # すでに配置済みのオブジェクトを削除する
        # 配置済み座標管理リストから削除
        if (x, y) in self.setted_grid:
            self.setted_grid.remove((x, y))
        # マップデータから削除
        for object in self.object_list:
            if (object[M_X] == x) and (object[M_Y] == y):
                # forの元リストをremoveすると順序が狂うがこの条件のみなので問題ない
                # 今後同じ座標にオブジェクトがおけるようになるなら実装見直しが必要
                self.object_list.remove(object)
        # 描画グループから削除
        for object in self.object.sprites():
            obj_x, obj_y = object.grid_pos
            if (obj_x == x) and (obj_y == y):
                object.kill()

    def scrollProcess(self, event_list):
        # スクロールバーの処理
        self.scroll_width.updateBarWithMouse(event_list)
        self.scroll_height.updateBarWithMouse(event_list)
        current_x = self.scroll_width.getWindowPosition()
        current_y = self.scroll_height.getWindowPosition()
        dx = (self.current_pos[0] - current_x) * GRID_SIZE
        dy = (self.current_pos[1] - current_y) * GRID_SIZE
        
        # スクロールバーの位置に応じて画面のオブジェクトを移動する
        if (dx != 0) or (dy != 0):
            self.current_pos = (current_x, current_y)
            for object in self.object.sprites():
                object.rect.move_ip(dx, dy)

    def saveSamnail(self):
        # 現在の画面を画像に保存する
        self.screen.fill((255,255,255))
        self.object.draw(self.screen)
        pygame.display.update()
        samnail_dir = "image/samnail"
        # パスが存在しなければ作成する
        if not os.path.exists(samnail_dir):
            os.mkdir(samnail_dir)
        pygame.image.save(self.screen, self.samnail)
        self.data[M_SAMNAIL] = self.samnail
        self.draw(self.screen)