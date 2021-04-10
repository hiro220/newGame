import pygame

class Camera:
    def __init__(self, screen):
        self.exit = False
        self.backGround = pygame.Rect(0,0,1000,2000)     #背景
        self.wall_group = pygame.sprite.Group()      # オブジェクト[壁]のグループ 
        self.timers = pygame.sprite.Group()
        
        CameraObject.containers = self.camera_group
        Timer.containers = self.timers

        for i in range(0, 600, 100):
            WallObject(0, i, 100, 100)

        for i in range(0, 600, 100):
            WallObject(1060, i, 100, 100)

        for i in range(0, 1200, 100):
            WallObject(i, 500, 100, 100)

        for i in range(0, 1200, 100):
            WallObject(i, 0, 100, 100)

        self.do(screen)