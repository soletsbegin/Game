import pygame
import os.path
from screen import *
from snake import *

NUMBERS = {'0': pygame.image.load(os.path.join('graphics', 'numb', '0.png')),
           '1': pygame.image.load(os.path.join('graphics', 'numb', '1.png')),
           '2': pygame.image.load(os.path.join('graphics', 'numb', '2.png')),
           '3': pygame.image.load(os.path.join('graphics', 'numb', '3.png')),
           '4': pygame.image.load(os.path.join('graphics', 'numb', '4.png')),
           '5': pygame.image.load(os.path.join('graphics', 'numb', '5.png')),
           '6': pygame.image.load(os.path.join('graphics', 'numb', '6.png')),
           '7': pygame.image.load(os.path.join('graphics', 'numb', '7.png')),
           '8': pygame.image.load(os.path.join('graphics', 'numb', '8.png')),
           '9': pygame.image.load(os.path.join('graphics', 'numb', '9.png')),
           }


class Bar():
    """
    Любой элемент который не меняет свое положение.
    """
    def __init__(self, x, y, w, h, color, path=None):
            self.xpos = x
            self.ypos = y
            self.color = color
            if path == None:
                self.path = False
                self.image = pygame.Surface((w, h))
            elif path != None:
                self.path = True
                self.image = pygame.image.load(path)

    def draw(self, screen):
        if self.path:
            screen.blit(self.image, (self.xpos, self.ypos))
        else:
            self.image.fill(self.color)
            screen.blit(self.image, (self.xpos, self.ypos))

    def move(self):
        self.ypos -= 40


class Number():
    """
    Цифровая панель.
    """
    def __init__(self, x, y, x2, y2, x3, y3):
        self.pos1 = (x, y)
        self.pos2 = (x2, y2)
        self.pos3 = (x3, y3)
        self.image1 = pygame.image.load(os.path.join('graphics', 'numb', '0.png'))
        self.image2 = pygame.image.load(os.path.join('graphics', 'numb', '0.png'))
        self.image3 = pygame.image.load(os.path.join('graphics', 'numb', '0.png'))
        self.image1.set_colorkey((0, 0, 0))
        self.image2.set_colorkey((0, 0, 0))
        self.image3.set_colorkey((0, 0, 0))

    def change_num(self, float):
        """

        """
        try:
            first, second, third = str(float)[0], str(float)[2], str(float)[3]
            self.image1 = NUMBERS[first]
            self.image2 = NUMBERS[second]
            self.image3 = NUMBERS[third]
        except IndexError: pass

    def draw(self, screen):
        screen.blit(self.image1, self.pos1)
        screen.blit(self.image2, self.pos2)
        screen.blit(self.image3, self.pos3)


class Text():
    """
    Любой элемент который не меняет свое положение.
    """

    def __init__(self, x, y, path):
        self.xpos = x
        self.ypos = y
        self.image = pygame.image.load(path)

    def draw(self, screen):
        screen.blit(self.image, (self.xpos, self.ypos))


if __name__ ==  "__main__":
    import doctest
    doctest.testmod()