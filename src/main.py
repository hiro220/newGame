#!/usr/bin/env python
# conding:utf-8

import pygame
from pygame.locals import *
import sys
import os
import argparse

from include import window

parser = argparse.ArgumentParser(description='ReK')
parser.add_argument('-c', '--cheat', action='store_true', help="チート")
args = parser.parse_args()

class Main(pygame.sprite.Sprite):

    def __init__(self, args):
        """pygame、ウィンドウなどの初期化処理"""
        pygame.init()   # pygameの初期化
        #self.data = db.load(cheat)
        self.args = args
        #self.data_check()

        if os.name == "posix":
            # Linux系OSの場合
            self.screen = pygame.display.set_mode((window.WIDTH, window.HEIGHT), flags=pygame.RESIZABLE)   # ウィンドウをWIDTH×HEIGHTで作成する
        if os.name == 'nt':
            # Windows
            self.screen = pygame.display.set_mode((window.WIDTH, window.HEIGHT))   # ウィンドウをWIDTH×HEIGHTで作成する

if __name__=='__main__':
    game = Main(args.cheat)
    #game.do()