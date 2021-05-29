from include.window import WIDTH, HEIGHT

class Camera:
    def __init__(self, group, player):
        self.group = group
        self.player = player

    def process(self):
        # プレイヤーの位置に合わせて全オブジェクトを移動させる
        player_oldpos = self.player.oldrect.center
        player_newpos = self.player.rect.center
        dx = player_oldpos[0] - player_newpos[0]
        dy = player_oldpos[1] - player_newpos[1]
        for object in self.group.sprites():
            object.rect.move_ip(dx, dy)

    def initCamera(self):
        player_newpos = self.player.rect.center
        dx = WIDTH // 2 - player_newpos[0]
        dy = HEIGHT // 2 - player_newpos[1]
        for object in self.group.sprites():
            object.rect.move_ip(dx, dy)
