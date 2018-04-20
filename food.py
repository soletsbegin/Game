from screen import *
import pygame
from random import randint

food = dict()


class Food(sprite.Sprite):

    def __init__(self):
        sprite.Sprite.__init__(self)
        self.xpos = randint(40, WIDTH-40)
        self.ypos = randint(40, HEIGTH-40)
        self.type = 0
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.image = pygame.Surface((40, 40))

    def draw(self):
        self.image.fill(self.color)
        SCREEN.blit(self.image, (self.xpos, self.ypos))