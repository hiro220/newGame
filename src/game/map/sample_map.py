from game.map.map_base import MapBase

from include.game_object import *

class SampleMap(MapBase):
    def __init__(self, screen):
        super().__init__(screen)
        # 画面内に収まるグリッドのサイズ(29, 15)
        self.map_size = (100, 30)
        
        # マップに配置する
        self.createObject()
        # ゲームの開始
        super().do()

    def createObject(self):
        
        for i in range(0, 15, 1):
            WallObject(0, i, 1, 1)
            print(i)
        
        for i in range(0, 30, 1):
            WallObject(i, 0, 1, 1)

        for i in range(0, 15, 1):
            WallObject(28, i, 1, 1)

        for i in range(0,29, 1):
            WallObject(i, 14, 1, 1)

        



        #for i in range(0, 3, 1):
        #    WallObject(0, i, 10, 10)

        #for i in range(0, 600, 100):
        #    WallObject(1060, i, 100, 100)

        #for i in range(0, 1200, 100):
        #    WallObject(i, 500, 100, 100)

        #for i in range(0, 1200, 100):
        #    WallObject(i, 0, 100, 100)

        MovingFloor(0, 13, 1, 1)
        MovingFloor(0, 12, 1, 1)
        