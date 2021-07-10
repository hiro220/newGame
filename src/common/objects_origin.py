import pygame

class ObjectsOrigin(pygame.sprite.Sprite):
    def __init__(self):
        self.image = None
        self.grid_pos = (-1, -1)

    def setInitGridPos(self, x, y):
        # グリッドの初期位置
        self.grid_pos = (x, y)

    def get_image(self):
        return self.image