from game.map.map_base import MapBase

from include.game_object import *

class SampleMap(MapBase):
    def __init__(self, screen):
        super().__init__(screen)
        # 画面内に収まるグリッドのサイズ(58, 30)
        self.map_size = (4000, 100)
        
        # マップに配置する
        self.createObject()
        # ゲームの開始
        super().do()

    def createObject(self):
        for i in range(0, 600, 100):
            WallObject(0, i, 100, 100)

        for i in range(0, 600, 100):
            WallObject(1060, i, 100, 100)

        for i in range(0, 1200, 100):
            WallObject(i, 500, 100, 100)

        for i in range(0, 1200, 100):
            WallObject(i, 0, 100, 100)

        MovingFloor(0, 400, 100, 100)