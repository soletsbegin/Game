import pygame
from snake import *
from screen import *
from food import *
import sys

body = []
scores = 0
snake = Snake()


def intersect(obj1, obj2):
    s1_x, s1_y = obj1.xpos, obj1.ypos
    s2_x, s2_y = obj2.xpos, obj2.ypos
    if (s1_x > s2_x - 40) and (s1_x < s2_x + 40) and (s1_y > s2_y - 40) and (s1_y < s2_y + 40):
        return True
    else:
        return False


def eat():
    if len(food):
        for f in range(len(food)):
            if intersect(snake.head, food[f]):
                food.remove(food[f])
                return True


def action():
    if key[pygame.K_DOWN]:
        snake.change_condition('down')
    if key[pygame.K_UP]:
        snake.change_condition('up')
    if key[pygame.K_LEFT]:
        snake.change_condition('left')
    if key[pygame.K_RIGHT]:
        snake.change_condition('right')
    if key[pygame.K_ESCAPE]:
        print(scores)
        sys.exit()


pygame.init()
game = True
count = 0

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    key = pygame.key.get_pressed()

    action()
    snake.move()

    count += 1
    if count % 500 == 0:
        food.append(Food())
    if eat():
        scores += 1

    SCREEN.fill(BACKGROUND_COLOR)
    snake.draw(SCREEN)
    for f in food:
        f.draw()
    window.blit(SCREEN, (0, 0))
    pygame.display.update()
