import os
import pygame
from elements import Bar, Number, Text
from snake import Snake
from level import Level, LevelPng

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
SCREEN = pygame.Surface((WIDTH, HEIGHT))


body = []
snake = Snake()

bar = Bar(0, 0, WIDTH, 120, 0, os.path.join('graphics', 'bar.png'))
scores_in_game = Number(WIDTH - 250, 10, WIDTH - 170, 10, WIDTH - 90, 10)
text_scores = Text(WIDTH - 800, 10, os.path.join('graphics', 'numb', 'scor.png'))

life = [Bar(80, 20, 40, 80, 0, os.path.join('graphics', 'heart.png')),
        Bar(150, 20, 40, 80, 0, os.path.join('graphics', 'heart.png')),
        Bar(220, 20, 40, 80, 0, os.path.join('graphics', 'heart.png')),
        ]


title = Bar(0, 0, 0, 0, 0, os.path.join('graphics', 'title.png'))
arrow_l = Bar(100, 700, 0, 0, 0, os.path.join('graphics', 'arr_l.png'))
arrow_r = Bar(1400, 700, 0, 0, 0, os.path.join('graphics', 'arr_r.png'))
menu_level = LevelPng()

go = Bar(0, 0, 0, 0, 0, os.path.join('graphics', 'go.png'))

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hungry Snake')

level = Level()
