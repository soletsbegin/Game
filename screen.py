from pygame import *
from elements import *

BACKGROUND_COLOR = (34, 139, 34)
COLORS = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'red': (255, 0, 0),
    'grey': (96, 96, 96),
    'red_num': (255, 0, 48)
}
WIDTH = 1600
HEIGHT = 1000
SCREEN = Surface((WIDTH, HEIGHT))
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hungry Snake')


