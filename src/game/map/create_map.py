from common.objects_origin import ObjectsOrigin
import pygame
from pygame.locals import *
from include.game_object import *
from include.window import *
from include.map_config import *

class CreateMap:
    def __init__(self, screen):
        font = pygame.font.Font(None, 25)
        self.exit_text = font.render("Q(click x)", True, (255,0,0))   #テキストSTART_GAME
        self.exit = False

        self.clock = pygame.time.Clock()        # 時間管理用
        self.screen = screen

        self.object = pygame.sprite.Group()
        ObjectsOrigin.containers = self.object

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
        self.screen.fill((255,255,255))
        self.showGrid()
        self.screen.blit(self.exit_text, [10, 10])         # START GAMEを描画
        self.object.draw(screen)   

    def read_objects(self):
        for key, value in GameObject.items():
            value(14, int(key))

    def showGrid(self):
        gridx_size, gridy_size = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
        for x in range(gridx_size):
            pygame.draw.line(self.screen, (0,0,0), (x*GRID_SIZE, 0), (x*GRID_SIZE, HEIGHT))
        for y in range(gridy_size):
            pygame.draw.line(self.screen, (0,0,0), (0, y*GRID_SIZE), (WIDTH, y*GRID_SIZE))
