#!/user/bin/env python
# encoding utf-8

import pygame

class Item(pygame.sprite.Sprite):
    """
    アイテム全般のベースクラス
    キャラクターがアイテムを取得する処理などがある
    アイテム毎の効果はeffect関数に記述する
    """
    def __init__(self, img_path="", x=0, y=0):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(img_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)

    def update(self):
        pass

    def effct(self):
        pass
    