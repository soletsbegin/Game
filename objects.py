import pygame
from  pygame import *
import os


WIDTH = 1024
HEIGTH = 768
SCREEN = pygame.Surface((WIDTH, HEIGTH))
SPEED = {
    '0': 0,
    '1': 0.2,
    '2': 0.5,
    '3': 0.8,
    '4': 1.1,
    '5': 1.4}


class Head(sprite.Sprite):
    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y
        self.bitmap = pygame.image.load(os.path.join('graphics','headup.png'))
        self.rect = Rect(x, y, 60,60)
        self.limits = {'x': 1, 'y': 1}

    def check_position(self):
        if self.xpos > WIDTH:
            self.xpos = 0
        if self.xpos < -60:
            self.xpos = WIDTH
        if self.ypos > HEIGTH:
            self.ypos = 0
        if self.ypos < -60:
            self.ypos = HEIGTH

    def go_down(self):
        self.ypos += SPEED['5']
        self.bitmap = pygame.image.load(os.path.join('graphics','headdown.png'))
        self.check_position()

    def go_up(self):
        self.ypos -= SPEED['5']
        self.bitmap = pygame.image.load(os.path.join('graphics','headup.png'))

        self.check_position()

    def go_left(self):
        self.xpos -= SPEED['5']
        self.bitmap = pygame.image.load(os.path.join('graphics','headleft.png'))

        self.check_position()

    def go_right(self):
        self.xpos += SPEED['5']
        self.bitmap = pygame.image.load(os.path.join('graphics','headright.png'))
        self.check_position()

    def render(self):
        SCREEN.blit(self.bitmap, (self.xpos, self.ypos))


class Platform():
        def __init__(self, x, y, filename):
            self.xpos = x
            self.ypos = y
            self.bitmap = pygame.image.load(os.path.join('graphics', filename))
            self.limits = {'x': 1, 'y': 1}

        def motion(self):
            if self.limits['y'] == 1:
                self.ypos += SPEED['5']
                if self.ypos > WIDTH-60:
                    self.limits['y'] = 0
            else:
                self.ypos -= SPEED['5']
                if self.ypos < 0:
                    self.limits['y'] = 1

        def render(self):
            SCREEN.blit(self.bitmap, (self.xpos, self.ypos))

