import pygame
from  pygame import *
from random import randint
import os


WIDTH = 1920
HEIGTH = 1080
TEXTURES =[pygame.image.load(os.path.join('graphics', 'tx', 't1.jpg')),
           pygame.image.load(os.path.join('graphics', 'tx', 't2.jpg')),
           pygame.image.load(os.path.join('graphics', 'tx', 't3.jpg')),
           pygame.image.load(os.path.join('graphics', 'tx', 't4.jpg')),
           pygame.image.load(os.path.join('graphics', 'tx', 't5.jpg')),
           pygame.image.load(os.path.join('graphics', 'tx', 't6.jpg')),
           pygame.image.load(os.path.join('graphics', 'tx', 't7.jpg')),
           pygame.image.load(os.path.join('graphics', 'tx', 't8.jpg'))]
SCREEN = Surface((WIDTH, HEIGTH))
SPEED = {
    '0': 0,
    '1': 0.8,
    '2': 1,
    '3': 1.5,
    '4': 2.2,
    '5': 3}


class Head(sprite.Sprite):
    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y
        self.bitmap = pygame.image.load(os.path.join('graphics','headup.png'))
        self.rect = Rect(x, y, 60,60)
        self.limits = {'x': 1, 'y': 1}
        self.vector = 'right'

    def check_position(self):
        if self.xpos > WIDTH:
            self.xpos = 0
        if self.xpos < -60:
            self.xpos = WIDTH
        if self.ypos > HEIGTH:
            self.ypos = 0
        if self.ypos < -60:
            self.ypos = HEIGTH

    def change_vector(self, action):
        if action == 'right' and self.vector != 'left': self.vector = 'right'
        if action == 'left' and self.vector != 'right': self.vector = 'left'
        if action == 'down' and self.vector != 'up': self.vector = 'down'
        if action == 'up' and self.vector != 'down': self.vector = 'up'

    def move(self):
        if self.vector == 'right':
            self.go_right()
        if self.vector == 'left':
            self.go_left()
        if self.vector == 'down':
            self.go_down()
        if self.vector == 'up':
            self.go_up()

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


class Body(sprite.Sprite):

    def __init__(self):
        self.xpos = 0
        self.ypos = 0




class Food(sprite.Sprite):

    food = dict()

    def __init__(self):
        self.xpos = randint(40, WIDTH-40)
        self.ypos = randint(40, HEIGTH-40)
        self.type = 0
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.image = pygame.Surface((40, 40))

    def draw(self):
        self.image.fill(self.color)
        SCREEN.blit(self.image, (self.xpos, self.ypos))

