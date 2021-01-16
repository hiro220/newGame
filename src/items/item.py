#!/user/bin/env python
# encoding utf-8

import pygame

class Item(pygame.sprite.Sprite):
    """
    アイテム全般のベースクラス
    キャラクターがアイテムを取得する処理などがある
    アイテム毎の効果はeffect関数に記述する
    """
    def __init__(self):
        pass

    def update(self):
        pass

    def effct(self):
        pass
    