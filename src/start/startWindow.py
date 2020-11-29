#!/usr/bin/env python
# coding:utf-8

import pygame
from pygame.locals import *
import os

class StartWindow:
    def __init__(self, screen):
        font = pygame.font.Font(None, 25)
        self.game_text = font.render("START", True, (255,255,255))   #テキストSTART_GAME
        self.end_text = font.render("EXIT", True, (255, 255, 255))          #テキストEnd
        self.choice_text = font.render("->", True, (255,255,255))       #選択矢印->
        self.select = 0
        self.exit = False
        self.do(screen)

    def do(self, screen):
        while True:
            self.process()
            self.draw(screen)

            if self.exit:
                break

    def process(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    self.keyReturn()
                    break
                elif event.key == K_UP:
                    self.select = (self.select - 1) % 2
                elif event.key == K_DOWN:
                    self.select = (self.select + 1) % 2

            elif event.type == QUIT:
                self.exit = True

    def draw(self, screen):
        print("Now Selected : ", end="")
        screen.blit(self.game_text, [530, 300])         # START GAMEを描画
        screen.blit(self.end_text, [530, 360])          # EXITを描画
        if self.select == 0:
            y = 300
            print("Start")
        elif self.select == 1:
            y = 360
            print("End")
        screen.blit(self.choice_text, [505, y])    #選択矢印->をEndの横へ描画
        
    def keyReturn(self):
        if self.select == 0:
            pass
        elif self.select == 1:
            self.exit = True