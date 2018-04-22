from screen import *
import pygame
from random import randint

food = []
pics = ['1.png',
        '2.png',
        '3.png']


class Food(sprite.Sprite):

    def __init__(self):
        sprite.Sprite.__init__(self)
        self.xpos = randint(40, WIDTH-40)
        self.ypos = randint(110, HEIGHT - 40)
        self.type = 0
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.image = pygame.image.load(os.path.join('graphics', 'food', pics[randint(0, len(pics)-1)]))

    def draw(self):
        SCREEN.blit(self.image, (self.xpos, self.ypos))