import pygame
from snake import *
from screen import *
from food import *
import sys

food = []
body = []
scores = 0
head = Head(500, 300)


def intersect(obj1, obj2):
    s1_x, s1_y = obj1.xpos, obj1.ypos
    s2_x, s2_y = obj2.xpos, obj2.ypos
    if (s1_x > s2_x - 40) and (s1_x < s2_x + 40) and (s1_y > s2_y - 40) and (s1_y < s2_y + 40):
        return 1
    else:
        return 0


def eat():
    if len(food):
        for f in range(len(food)):
            if intersect(head, food[f]):
                food.remove(food[f])
                return True


def action():
    if key[pygame.K_DOWN]:
        head.change_vector('down')
    if key[pygame.K_UP]:
        head.change_vector('up')
    if key[pygame.K_LEFT]:
        head.change_vector('left')
    if key[pygame.K_RIGHT]:
        head.change_vector('right')
    if key[pygame.K_ESCAPE]:
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
    head.move()

    if eat():
        scores += 1
        body.append(Body())

    count += 1
    if count % 1000 == 0:
        food.append(Food())

    SCREEN.fill(BACKGROUND_COLOR)
    head.draw(SCREEN)
    for f in food:
        f.draw()
    window.blit(SCREEN, (0, 0))
    pygame.display.update()


print(scores)