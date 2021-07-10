from common.objects_origin import ObjectsOrigin
from include.map_config import GRID_SIZE
import pygame
from pygame.locals import *
from include.game_object import GameObject
from common.button import Button

class ObjectTab:
    def __init__(self, screen, x, y):
        self.screen = screen

        self.x = x
        self.y = y
        self.width = 100
        self.height = 600

        self.button_dict = {}       # ボタンを格納するリスト 
        self.select_button = "-1"   # 選択中のボタンID
        self.isvisible = True       # タブの表示状態(非表示実装時に初期値False)

        ObjectsOrigin.containers = pygame.sprite.Group()

        self.setObjects()

    def showTab(self):
        # タブを表示
        pygame.draw.rect(self.screen, (255,0,0), (self.x, self.y, self.width, self.height))
        for button in self.button_dict.values():
            if self.isInTab(button.rect):
                button.setVisible(True)
                self.screen.blit(button.image, button.rect)
            else:
                button.setVisible(False)

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
        # タブ内のクリック判定
        for event in event_list:
            if event.type in (MOUSEBUTTONUP, MOUSEBUTTONDOWN) and event.dict["button"] == 1:
                x, y = event.dict["pos"]
                # タブ上をクリックしていたならイベント削除
                if self.isInTab(Rect(x, y, 1, 1)):
                    event_list.remove(event)

    def retButtonID(self):
        # 選択中のオブジェクトIDをreturn
        return self.select_button
    
    def isInTab(self, rect):
        bool_x = (self.x <= rect.left <= self.x + self.width)
        bool_w = (self.x <= rect.right <= self.x + self.width)
        bool_y = (self.y <= rect.top <= self.y + self.height)
        bool_h = (self.y <= rect.bottom <= self.y + self.height)

        return bool_x and bool_w and bool_y and bool_h and self.isvisible