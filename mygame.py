import pygame
from snake import *
from screen import *
from food import *
import sys

body = []
scores = 0
snake = Snake()
screen = Screen()


def eat():
    for f in range(len(food)):
        if intersect(snake.head, food[f]):
            food.remove(food[f])
            return True


def action():
    if key[pygame.K_DOWN]:
        snake.turn('down')
    if key[pygame.K_UP]:
        snake.turn('up')
    if key[pygame.K_LEFT]:
        snake.turn('left')
    if key[pygame.K_RIGHT]:
        snake.turn('right')
    if key[pygame.K_ESCAPE]:
        print(scores)
        sys.exit()


pygame.init()
game = True
speed = 8
count = 0
timer = pygame.time.Clock()

while game:
    timer.tick(speed)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    key = pygame.key.get_pressed()

    action()
    snake.change_condition()
    count += 1

    if len(food) < 3:
        food.append(Food())
    if eat():
        if len(snake.body) % 10 == 0:
            speed += 1
        snake.add_sect()
        scores += 1

    # if count > 10:
    #     if snake.intersect(): sys.exit()

    SCREEN.fill(BACKGROUND_COLOR)
    screen.draw(SCREEN)
    snake.draw(SCREEN)
    for f in food:
        f.draw()

    window.blit(SCREEN, (0, 0))
    pygame.display.update()
