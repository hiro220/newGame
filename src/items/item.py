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

    def update(self, players):
        """プレイヤーとの当たり判定を求め、アイテムに応じた効果を付与する"""
        collide_list = pygame.sprite.spritecollide(self, players, False)
        if collide_list:
            self.kill()
            for player in collide_list:
                # アイテムと接触したプレイヤーに効果を付与
                self.effect(player)

    def effct(self):
        pass
    