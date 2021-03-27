from include.window import *
from include.map_config import *
from game.game import Game

class MapBase(Game):
    def __init__(self, screen):
        self.grid_x = WIDTH // GRID_SIZE
        self.grid_y = HEIGHT // GRID_SIZE
        
    def getGridSize(self):
        """グリッドの最大数を取得する"""
        return (self.grid_x, self.grid_y)

    def getCoordin(self, x, y):
        """引数で指定したグリッド座標の左上ピクセル座標を取得する"""
        return (GRID_SIZE * x, GRID_SIZE * y)

