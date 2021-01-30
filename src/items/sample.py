
import pygame
from items.item import Item
from common.timer import Timer

class SampleItem(Item):
    def __init__(self, x=0, y=0):
        super().__init__("image/item/sample.png", x, y)


    def effect(self, character):
        character.dx += 10
        Timer(3000, self.recover, character)

    def recover(self, character):
        character.dx -= 10