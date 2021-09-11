from game.game import Game
from game.map.map_base import MapBase
import json
import os
from include.game_object import *
from include.map_config import *

class LoadMap(MapBase):
    def __init__(self, screen):
        self.map_list = []
        self.data = {}
        self.screen = screen

    def getMaplist(self):
        # マップのリストを取得
        return self.map_list

    def updateMapInfo(self):
        # 存在するマップ情報の更新
        mapdir = "mapinfo"
        self.map_list = []
        for _root, _dirs, _files in os.walk(mapdir):
            # jsonファイルのみ取得
            files = [_file for _file in _files if '.json' in _file]
            # ファイルのパスをリストに追加
            self.map_list += [os.path.join(_root, file) for file in files]

    def _loadJson(self, map_id):
        # マップ情報があるjsonファイルを読み込む
        file = self.map_list[map_id]
        if not os.path.exists(file):
            assert "ファイルが見つかりません。"
        with open(file, 'r') as fp:
            self.data = json.load(fp)
        
    def loadMap(self, map_id):
        # マップファイルを読み込む
        self._loadJson(map_id)
        # ゲーム初期化
        super().__init__(self.screen)
        # マップ作成
        for _object in self.data[M_OBJECT]:
            _id = _object[M_NAME]
            _x, _y = _object[M_X], _object[M_Y]
            object = GameObject[_id]
            object(_x, _y, *_object[M_ARGS])
            
        # マップの実行
        super().do()
        