import pygame
from pygame import *
import os
from random import randint
from elements import *

BACKGROUND_COLOR = (34, 139, 34)
COLORS = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'red': (255, 0, 0),
    'grey': (96, 96, 96)
}
WIDTH = 1024
HEIGHT = 768
TEXTURES =[pygame.image.load(os.path.join('graphics', 'tx', 't1.png')),
           pygame.image.load(os.path.join('graphics', 'tx', 't2.png')),
           pygame.image.load(os.path.join('graphics', 'tx', 't3.jpg')),
           pygame.image.load(os.path.join('graphics', 'tx', 't4.jpg')),
           pygame.image.load(os.path.join('graphics', 'tx', 't5.jpg')),
           pygame.image.load(os.path.join('graphics', 'tx', 't6.jpg')),
           pygame.image.load(os.path.join('graphics', 'tx', 't7.jpg')),
           pygame.image.load(os.path.join('graphics', 'tx', 't8.png'))]
SCREEN = Surface((WIDTH, HEIGHT))
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hungry Snake')


class Screen():
    def __init__(self):
        self.image = TEXTURES[randint(0, len(TEXTURES)-1)]

    def draw(self, screen):
        screen.blit(self.image, (0, 0))


