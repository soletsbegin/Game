import os
import pygame
from  pygame import *
from random import randint
from screen import *

SPEED = {
    '0': 0,
    '1': 0.8,
    '2': 1,
    '3': 1.5,
    '4': 2.2,
    '5': 30}


def intersect(obj1, obj2):
    s1_x, s1_y = obj1.xpos, obj1.ypos
    s2_x, s2_y = obj2.xpos, obj2.ypos
    if (s1_x > s2_x - 40) and (s1_x < s2_x + 40) and (s1_y > s2_y - 40) and (s1_y < s2_y + 40):
        return True
    else:
        return False


class Snake():
    def __init__(self):
        self.head = Head(1000, 500)
        self.body = [self.head,
                     Section(self.head.xpos, self.head.ypos),
                     Section(self.head.xpos, self.head.ypos),
                     Section(self.head.xpos, self.head.ypos),
                     Tail(self.head.xpos, self.head.ypos)]
        self.group = pygame.sprite.Group()
        for s in range(2, len(self.body)):
            self.group.add(self.body[s])

    def draw(self, screen):
        for s in reversed(self.body):
            s.draw(screen)

    def add_sect(self):
        self.body.insert(1, Section(self.head.xpos, self.head.ypos))

    def turn(self, action):
        self.head.change_vector(action)

    def change_condition(self):
        temp = [(s.xpos, s.ypos, s.vector) for s in self.body]
        self.head.move()
        for s in range(1, len(self.body)):
            self.body[s].xpos = temp[s-1][0]
            self.body[s].ypos = temp[s-1][1]
            self.body[s].change_vector(temp[s-1][2])

    def intersect(self):
        for s in self.group:
            if sprite.spritecollide(self.head, self.group, 0): return True


class Head(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xpos = x
        self.ypos = y
        self.image = pygame.image.load(os.path.join('graphics', 'headright.png'))
        self.rect = Rect(self.xpos, self.ypos, 50, 50)
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
            self.xpos += SPEED['5']
            self.image = pygame.image.load(os.path.join('graphics', 'headright.png'))
            self.check_position()
        if self.vector == 'left':
            self.xpos -= SPEED['5']
            self.image = pygame.image.load(os.path.join('graphics', 'headleft.png'))
            self.check_position()
        if self.vector == 'down':
            self.ypos += SPEED['5']
            self.image = pygame.image.load(os.path.join('graphics', 'headdown.png'))
            self.check_position()
        if self.vector == 'up':
            self.ypos -= SPEED['5']
            self.image = pygame.image.load(os.path.join('graphics', 'headup.png'))
            self.check_position()

    def draw(self, screen):
        screen.blit(self.image, (self.xpos, self.ypos))


class Section(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xpos = x
        self.ypos = y
        self.vector = 'right'
        self.rect = Rect(x, y, 40, 40)
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
        self.rect = Rect(x, y, 40, 40)
        self.image = pygame.image.load(os.path.join('graphics', 'end.png'))

    def draw(self, screen):
        screen.blit(self.image, (self.xpos, self.ypos))

    def change_vector(self, action):
        if action == 'right':
            self.image = pygame.image.load(os.path.join('graphics', 'endright.png'))
            self.vector = 'right'
        if action == 'left':
            self.image = pygame.image.load(os.path.join('graphics', 'endleft.png'))
            self.vector = 'left'
        if action == 'down':
            self.image = pygame.image.load(os.path.join('graphics', 'enddown.png'))
            self.vector = 'down'
        if action == 'up':
            self.image = pygame.image.load(os.path.join('graphics', 'endup.png'))
            self.vector = 'up'