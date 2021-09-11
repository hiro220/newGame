import pygame
from pygame.locals import *

from include.window import *
from include.map_config import *
from game.map.load_map import LoadMap
from game.map.create_map import CreateMap
from common.button import Button
import json

class SelectMap:
    def __init__(self, screen):
        self.screen = screen
        self.select = 0         # 現在選択しているマップ
        self.map_num = 1        # 存在するマップ数(1以上)

        self.exit = False

        self.load_map = LoadMap(screen)
        self.loadMaps()

        self.map_group = pygame.sprite.Group()
        Button.containers = self.map_group

        self.do()

    def do(self):
        while True:
            self.process()
            self.draw()
            pygame.display.update()

            if self.exit:
                break

    def process(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # キーボード入力
                if event.key == K_RETURN:
                    self.keyReturn()
                    break
                elif event.key == K_LEFT:
                    self.select = (self.select - 1) % self.map_num
                elif event.key == K_RIGHT:
                    self.select = (self.select + 1) % self.map_num

            elif event.type == QUIT:
                # 終了(×ボタン)をクリック
                self.exit = True


    def draw(self):
        self.screen.fill((0,0,0))
        for button in self.map_buttons:
            self.screen.blit(button.image, button.rect)
    
    def keyReturn(self):
        CreateMap(self.screen, self.select)
        pygame.key.set_repeat()

    def loadMaps(self):
        # map除法の更新
        self.load_map.updateMapInfo()
        self.map_list = self.load_map.getMaplist()
        self.map_num = len(self.map_list)
        self.loadSamnail()

    def loadSamnail(self):
        # サムネイル画像へのパスから画像をボタンとして読み込む
        self.map_buttons = []
        for num, file_path in enumerate(self.map_list):
            map_info = json.load(open(file_path))
            num += 1
            width, height = WIDTH // 2, HEIGHT // 2
            x, y = WIDTH - width * 3 // 2, HEIGHT - height * 3 // 2
            button = Button(self.screen, x * num, y, width, height, map_info[M_SAMNAIL])
            button.setVisible(True)
            self.map_buttons += [button]