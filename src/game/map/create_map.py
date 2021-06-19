import pygame
from pygame.locals import *
from include.game_object import *

class CreateMap:
    def __init__(self, screen):
        font = pygame.font.Font(None, 25)
        self.exit_text = font.render("Q(click x)", True, (255,255,255))   #テキストSTART_GAME
        self.exit = False

        self.clock = pygame.time.Clock()        # 時間管理用
        self.screen = screen

        self.obj = None

        self.do()

    def do(self):
        while True:
            self.clock.tick(30)         # フレームレート(30fps)
            self.process()
            self.read_objects()
            self.draw(self.screen)
            pygame.display.update()

            if self.exit:
                break
    
    def process(self):
        event_list = pygame.event.get()     # pygame.event.get()は取得したイベントをキューから削除する。
        for event in event_list:
            if event.type == QUIT:
                # 終了(×ボタン)をクリック
                self.exit = True


    def draw(self, screen):
        self.screen.fill((0,0,0))
        self.screen.blit(self.exit_text, [10, 10])         # START GAMEを描画   
        self.screen.blit(self.obj, (500, 300))

    def read_objects(self):
        obj = GameObject["1"]()
        self.obj = obj.get_image()
