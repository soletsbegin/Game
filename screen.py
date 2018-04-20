import pygame
from pygame import *
import os

BACKGROUND_COLOR = (34, 139, 34)
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

window = pygame.display.set_mode((WIDTH, HEIGTH), 0, 32)
pygame.display.set_caption('Hungry Snake')