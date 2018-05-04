"""Реализация змейки: голова, сектора, хвост.
"""

import os

import pygame

import mainvars

SPEED = {
    '0': 0,
    '1': 0.8,
    '2': 1,
    '3': 1.5,
    '4': 20,
    '5': 40}


def intersect(obj1, obj2):
    if obj1.xpos == obj2.xpos and obj1.ypos == obj2.ypos:
        return True
    else:
        return False


class Snake:
    """
    Змея в целом.
    """
    def __init__(self):
        self.head = Head(800, 480)
        self.body = [CheckPoint(0, 360, 1, 1),
                     Section(self.head.xpos, self.head.ypos),
                     Section(self.head.xpos, self.head.ypos),
                     Section(self.head.xpos, self.head.ypos),
                     Section(self.head.xpos, self.head.ypos),
                     ]

    def draw(self, screen):
        for s in reversed(self.body):
            s.draw(screen)
        self.head.draw(screen)

    def add_sect(self):
        """
        Add sectors in the list(self.body).
        """
        self.body.append(Section(self.head.xpos-1, self.head.ypos-1))

    def turn(self, action):
        """
        This method change direction of the first element of snake.
        """
        self.head.change_vector(action)

    def change_condition(self):
        """
        Main method of snakes move.
        Moves each next segment to the position of the previous.
        """
        temp = [(s.xpos, s.ypos, s.vector) for s in self.body]
        self.head.move()
        self.body[0].change_pos(self.head)
        for s in range(1, len(self.body)):
            self.body[s].xpos = temp[s-1][0]
            self.body[s].ypos = temp[s-1][1]
            self.body[s].change_vector(temp[s-1][2])

    def intersect1(self):
        """Check intersection of the  Head with other sections.

        """
        for b in range(1, len(self.body)):
            if intersect(self.head, self.body[b]):
                self.body = self.body[0:b]
                return True

    def reset(self):
        self.head.reset()
        self.body = self.body[:4]


class Head:
    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y
        self.start = (x, y)
        self.image = pygame.image.load(os.path.join('graphics', 'head.png'))
        self.limits = {'x': 1, 'y': 1}
        self.vector = 'right'

    def check_position(self):
        if self.xpos > mainvars.WIDTH-40:
            self.xpos = 0
        if self.xpos < 0:
            self.xpos = mainvars.WIDTH
        if self.ypos > mainvars.HEIGHT-40:
            self.ypos = 120
        if self.ypos < 120:
            self.ypos = mainvars.HEIGHT

    def change_vector(self, action):
        if action == 'right' and self.vector != 'left' and self.vector != 'right':
            self.vector = 'right'
            self.image = pygame.image.load(os.path.join('graphics', 'head.png'))
        elif action == 'left' and self.vector != 'right' and self.vector != 'left':
            self.image = pygame.image.load(os.path.join('graphics', 'head.png'))
            self.vector = 'left'
        elif action == 'down' and self.vector != 'up' and self.vector != 'down':
            self.image = pygame.image.load(os.path.join('graphics', 'head.png'))
            self.vector = 'down'
        elif action == 'up' and self.vector != 'down' and self.vector != 'up':
            self.image = pygame.image.load(os.path.join('graphics', 'head.png'))
            self.vector = 'up'
        else:
            return False

    def move(self):
        if self.vector == 'right':
            self.xpos += SPEED['5']
            self.check_position()
        if self.vector == 'left':
            self.xpos -= SPEED['5']
            self.check_position()
        if self.vector == 'down':
            self.ypos += SPEED['5']
            self.check_position()
        if self.vector == 'up':
            self.ypos -= SPEED['5']
            self.check_position()

    def reset(self):
        self.xpos, self.ypos = self.start
        self.vector = 'right'

    def draw(self, screen):
        screen.blit(self.image, (self.xpos, self.ypos))


class Section:
    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y
        self.vector = 'right'
        self.color = mainvars.COLORS['blue']
        self.image = pygame.image.load(os.path.join('graphics', 'sect.png'))

    def draw(self, screen):
        screen.blit(self.image, (self.xpos, self.ypos))

    def change_vector(self, action):
        if action == 'right':
            self.vector = 'right'
        if action == 'left':
            self.vector = 'left'
        if action == 'down':
            self.vector = 'down'
        if action == 'up':
            self.vector = 'up'


# class Tail:
#     def __init__(self, x, y):
#         self.xpos = x
#         self.ypos = y
#         self.vector = 'right'
#         self.image = pygame.Surface((40, 40))
#
#     def draw(self, screen):
#         # self.image.fill(COLORS['blue'])
#         screen.blit(self.image, (self.xpos, self.ypos))
#
#     def change_vector(self, action):
#         if action == 'right':
#             self.image = pygame.image.load(os.path.join('graphics', 'endright.png'))
#             self.vector = 'right'
#         if action == 'left':
#             self.image = pygame.image.load(os.path.join('graphics', 'endleft.png'))
#             self.vector = 'left'
#         if action == 'down':
#             self.image = pygame.image.load(os.path.join('graphics', 'enddown.png'))
#             self.vector = 'down'
#         if action == 'up':
#             self.image = pygame.image.load(os.path.join('graphics', 'endup.png'))
#             self.vector = 'up'
#

class CheckPoint:
    def __init__(self, x, y, w, h):
        self.xpos = x
        self.ypos = y
        self.vector = 'right'
        self.image = pygame.Surface((w, h))

    def change_pos(self, obj):
        if obj.vector == 'up':
            self.xpos = obj.xpos
            self.ypos = obj.ypos
            self.vector = obj.vector
        if obj.vector == 'down':
            self.xpos = obj.xpos
            self.ypos = obj.ypos
            self.vector = obj.vector
        if obj.vector == 'left':
            self.xpos = obj.xpos
            self.ypos = obj.ypos
            self.vector = obj.vector
        if obj.vector == 'right':
            self.xpos = obj.xpos
            self.ypos = obj.ypos
            self.vector = obj.vector

    def draw(self, screen):
        pass
