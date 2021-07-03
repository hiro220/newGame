from common.objects_origin import ObjectsOrigin
from include.map_config import GRID_SIZE
import pygame
from pygame.locals import *
from include.game_object import GameObject
from game.map.button import Button

class ObjectTab:
    def __init__(self, screen, x, y):
        self.screen = screen

        self.x = x
        self.y = y

        self.button_dict = {}       # ボタンを格納するリスト 
        self.select_button = "-1"   # 選択中のボタンID

        ObjectsOrigin.containers = pygame.sprite.Group()

        self.setObjects()

    def showTab(self):
        # タブを表示
        pygame.draw.rect(self.screen, (255,0,0), (self.x, self.y, 100, 600))

    def setObjects(self):
        # オブジェクトに対応するボタンを生成
        for i, (key, value) in enumerate(GameObject.items()):
            obj = value(0, 0)
            self.button_dict[key] = Button(self.screen, self.x + 10, i * GRID_SIZE, obj.rect.width, obj.rect.height, obj.image)

    def updateClickedButton(self, event_list):
        # 選択中のオブジェクトを更新
        for key, button in self.button_dict.items():
            if button.isClicked(event_list):
                self.select_button = key

    def retButtonID(self):
        # 選択中のオブジェクトIDをreturn
        return self.select_button