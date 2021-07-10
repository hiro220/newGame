from include.window import HEIGHT, WIDTH
import pygame
from pygame.locals import *

class Button(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, width, height, image_path):
        self.screen = screen
        if type(image_path) == str:
            # image_pathがパス名指定なら画像ロード 
            self.image = pygame.image.load(image_path).convert_alpha()
        else:
            # image_pathがイメージに変換されているものとする
            self.image = image_path

        self.mouse_down = False     # このボタンの左クリック押下状態
        self.is_visible = False     # ボタンの表示可否

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

    def isClicked(self, event_list):
        # クリックされたならtrue
        for event in event_list:
            # マウス操作
            if event.type == MOUSEBUTTONUP and event.dict["button"] == 1:
                # 左クリック
                x, y = event.dict["pos"]
                # ボタン内で押下後離された
                if self.isPosInButton(x, y) and self.mouse_down:
                    self.mouse_down = False
                    # イベントリストからボタン押下イベント削除
                    event_list.remove(event)
                    return True 
                else:
                    self.mouse_down = False 

            if event.type == MOUSEBUTTONDOWN and event.dict["button"] == 1:
                # 左クリック押下
                x, y = event.dict["pos"]
                self.mouse_down = self.isPosInButton(x, y)
                # イベントリストからボタン押下イベント削除
                if self.mouse_down:
                    event_list.remove(event)

        return False
    
    def isPosInButton(self, x, y):
        # 表示状態かつボタン内クリック
        bool_x = (self.x <= x <= self.x + self.width)
        bool_y = (self.y <= y <= self.y + self.height)
        return bool_x and bool_y and self.is_visible

    def setVisible(self, bool_visible):
        # ボタンの表示状態を変更
        self.is_visible = bool_visible