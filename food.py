import os
from random import randint

import pygame

import mainvars as m

food = []


class Food:
    def __init__(self):
        self.xpos, self.ypos = self.rand_pos()
        self.image = pygame.image.load(os.path.join('graphics', 'food', '111.png'))

    @staticmethod
    def rand_pos():
        while True:
            x = randint(40, m.WIDTH-40)
            y = randint(160, m.HEIGHT-40)
            if x % 40 == 0 and y % 40 == 0:
                return x, y

    def draw(self, screen):
        screen.blit(self.image, (self.xpos, self.ypos))
