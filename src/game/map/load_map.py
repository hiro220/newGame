from game.map.map_base import MapBase
import json
import os

class LoadMap(MapBase):
    def __init__(self):
        self.map_list = []
        self.data = {}

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
        with open(file, 'r', encording='utf-8') as fp:
            self.data = json.load(fp)
        
    def loadMap(self, map_id):
        # マップを読み込む
        self._loadJson(map_id)
        # マップ作成
        for object in self.data['object']:
            pass
        # マップの実行
        super().do()
        