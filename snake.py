import os
import pygame
from  pygame import *
from random import randint
from screen import *


WIDTH = 1920
HEIGHT = 1080
TEXTURES = (pygame.image.load(os.path.join('graphics', 'tx', 't1.jpg')),
            pygame.image.load(os.path.join('graphics', 'tx', 't2.jpg')),
            pygame.image.load(os.path.join('graphics', 'tx', 't3.jpg')),
            pygame.image.load(os.path.join('graphics', 'tx', 't4.jpg')),
            pygame.image.load(os.path.join('graphics', 'tx', 't5.jpg')),
            pygame.image.load(os.path.join('graphics', 'tx', 't6.jpg')),
            pygame.image.load(os.path.join('graphics', 'tx', 't7.jpg')),
            pygame.image.load(os.path.join('graphics', 'tx', 't8.jpg')))
SCREEN = Surface((WIDTH, HEIGHT))
SPEED = {
    '0': 0,
    '1': 0.8,
    '2': 1,
    '3': 1.5,
    '4': 2.2,
    '5': 3}


class Snake():
    def __init__(self):
        self.head = Head(1000, 500)
        self.body = [self.head,
                     Section(self.head.xpos - 30, self.head.ypos + 10),
                     Section(self.head.xpos - 60, self.head.ypos + 10),
                     Section(self.head.xpos - 90, self.head.ypos + 10),
                     Tail(self.head.xpos - 120, self.head.ypos + 10)]

    def draw(self, screen):
        for s in reversed(self.body):
            s.draw(screen)

    def add_sect(self):
        self.body[1] = Section(self.head.xpos, self.head.ypos)

    def change_condition(self, action):
        pass

    def move(self):
        self.head.move()


class Head(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xpos = x
        self.ypos = y
        self.image = pygame.image.load(os.path.join('graphics', 'headright.png'))
        self.rect = Rect(x, y, 60,60)
        self.limits = {'x': 1, 'y': 1}
        self.vector = 'right'

    def check_position(self):
        if self.xpos > WIDTH:
            self.xpos = 0
        if self.xpos < -60:
            self.xpos = WIDTH
        if self.ypos > HEIGHT:
            self.ypos = 0
        if self.ypos < -60:
            self.ypos = HEIGHT

    def change_vector(self, action):
        if action == 'right' and self.vector != 'left': self.vector = 'right'
        elif action == 'left' and self.vector != 'right': self.vector = 'left'
        elif action == 'down' and self.vector != 'up': self.vector = 'down'
        elif action == 'up' and self.vector != 'down': self.vector = 'up'
        else: return False

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
        self.image = pygame.image.load(os.path.join('graphics', 'headdown.png'))
        self.check_position()

    def go_up(self):
        self.ypos -= SPEED['5']
        self.image = pygame.image.load(os.path.join('graphics', 'headup.png'))
        self.check_position()

    def go_left(self):
        self.xpos -= SPEED['5']
        self.image = pygame.image.load(os.path.join('graphics', 'headleft.png'))
        self.check_position()

    def go_right(self):
        self.xpos += SPEED['5']
        self.image = pygame.image.load(os.path.join('graphics', 'headright.png'))
        self.check_position()

    def draw(self, screen):
        screen.blit(self.image, (self.xpos, self.ypos))


class Section(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xpos = x
        self.ypos = y
        self.vector = 'right'
        self.image = pygame.image.load(os.path.join('graphics', 'sectionright.png'))

    def draw(self, screen):
        screen.blit(self.image, (self.xpos, self.ypos))

    def change_vector(self, action):
        if action == 'right':
            self.image = pygame.image.load(os.path.join('graphics', 'sectionright.png'))
            self.vector = 'right'
        if action == 'left':
            self.image = pygame.image.load(os.path.join('graphics', 'sectionleft.png'))
            self.vector = 'left'
        if action == 'down':
            self.image = pygame.image.load(os.path.join('graphics', 'sectiondown.png'))
            self.vector = 'down'
        if action == 'up':
            self.image = pygame.image.load(os.path.join('graphics', 'sectionup.png'))
            self.vector = 'up'


class Tail(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xpos = x
        self.ypos = y
        self.vector = 'right'
        self.image = pygame.image.load(os.path.join('graphics', 'end.png'))

    def draw(self, screen):
        screen.blit(self.image, (self.xpos, self.ypos))

    def change_vector(self, action):
        if action == 'right':
            self.image = pygame.image.load(os.path.join('graphics', 'end.png'))
            self.vector = 'right'
        if action == 'left':
            self.image = pygame.image.load(os.path.join('graphics', 'end.png'))
            self.vector = 'left'
        if action == 'down':
            self.image = pygame.image.load(os.path.join('graphics', 'end.png'))
            self.vector = 'down'
        if action == 'up':
            self.image = pygame.image.load(os.path.join('graphics', 'end.png'))
            self.vector = 'up'