import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION

class ScrollBar(pygame.sprite.Sprite):
    def __init__(self, rect, view_size, max_size, step, current=0, vertical=False):
        # 処理用変数
        self.max_size = max_size    # スクロールバーで扱う最大サイズ
        self.current = current      # 現在位置
        self.view_size = view_size  # 画面に表示する量
        self.step = step            # 1段階でどれだけ移動するか
        # 表示用変数
        self.is_vertical = vertical # バーが縦方向か
        self.rect = rect            # 全体のRect
        self.bar_rect = None        # スクロールバーのRect
        self.bar_pos = 0            # スクロールバーの位置
        self.is_visible = True      # 表示有無
        # マウス処理用変数
        self.is_mouse_down = False  # 左クリック押下状態
        self.cursor_pos = (0, 0)    # 前回のマウスカーソルの位置
        self.resizeBar()


    def setMaxSize(self, max_size):
        # 扱う実サイズを更新する
        self.max_size = max_size
        self.resizeBar()

    def resizeBar(self):
        # バーのサイズを計算
        max_size = self.rect.height if self.is_vertical else self.rect.width
        bar_size = int(self.view_size * max_size / self.max_size)
        # バーの位置を計算
        self.bar_pos = int(self.current * max_size / self.max_size)
        # バーをリサイズ
        if self.is_vertical:
            # 縦長のバー
            self.bar_rect = pygame.Rect(self.rect.left, self.bar_pos, self.rect.width, bar_size)
        else:
            # 横長のバー
            self.bar_rect = pygame.Rect(self.bar_pos, self.rect.top, bar_size, self.rect.height)

    def updateBarWithMouse(self, event_list):
        # マウスのドラッグでバーの位置を変える
        for event in event_list:
            if (event.type == MOUSEBUTTONDOWN) and (event.dict["button"] == 1) and self.isBarClicked(event.dict["pos"]):
                # マウス押下処理はイベントリストから除去する
                event_list.remove(event)
                self.is_mouse_down = True
                self.cursor_pos = event.dict["pos"]
            if (event.type == MOUSEBUTTONUP) and (event.dict["button"] == 1):
                self.is_mouse_down = False
            if (event.type == MOUSEMOTION) and self.is_mouse_down:
                # スクロールバーのドラッグ
                self.moveBar(event.dict["pos"])

    def moveBar(self, position):
        # カーソルの移動量計算
        if self.is_vertical:
            cursor = position[1]
            pre_cursor = self.cursor_pos[1]
            max_size = self.rect.height
        else:
            cursor = position[0]
            pre_cursor = self.cursor_pos[0]
            max_size = self.rect.width
        move_step = int(self.step * max_size / self.max_size)   # 設定したバーの移動量に合わせた移動量
        cur_move_size = cursor - pre_cursor                     # カーソルの移動量
        # 指定の移動量以上カーソルが移動していたなら、バーを移動させる
        if abs(cur_move_size) >= move_step:
            # カーソルの移動量の細かい部分は切り捨て、move_stepの倍数分だけバーを移動
            x = move_step * (cur_move_size // move_step) * (not self.is_vertical)
            y = move_step * (cur_move_size // move_step) * (self.is_vertical)
            self.bar_rect.move_ip(x, y)
            self.bar_rect.clamp_ip(self.rect)
            # カーソルの位置更新
            self.cursor_pos = (self.cursor_pos[0] + x, self.cursor_pos[1] + y)
            # 現在のウィンドウ位置更新
            bar_pos = self.bar_rect.top if self.is_vertical else self.bar_rect.left
            self.current = bar_pos  // move_step

    def draw(self, screen):
        # 枠の描画
        pygame.draw.rect(screen, (200, 200, 200), self.rect)
        # バーの描画
        pygame.draw.rect(screen, (150, 150, 150), self.bar_rect)
        # 縁の描画
        pygame.draw.rect(screen, (180, 180, 180), self.rect, 1)

    def getWindowPosition(self):
        # ウィンドウ位置を取得する
        return self.current

    def setCurrentPosition(self, current):
        # 現在のウィンドウ位置を更新する
        self.current = current
        self.resizeBar()

    def isBarClicked(self, pos):
        # バーをクリックされたか
        bool_x = self.bar_rect.left <= pos[0] <= self.bar_rect.right
        bool_y = self.bar_rect.top <= pos[1] <= self.bar_rect.bottom
        return bool_x and bool_y and self.is_visible