import pygame
from objects import *

BACKGROUND_COLOR = (34, 139, 34)


def Intersect(obj1, obj2):
    s1_x, s1_y = obj1.xpos, obj1.ypos
    s2_x, s2_y = obj2.xpos, obj2.ypos
    if (s1_x > s2_x - 40) and (s1_x < s2_x + 40) and (s1_y > s2_y - 40) and (s1_y < s2_y + 40):
        return 1
    else:
        return 0


def move():
    if key[pygame.K_DOWN]:
        head.go_down()
    if key[pygame.K_UP]:
        head.go_up()
    if key[pygame.K_LEFT]:
        head.go_left()
    if key[pygame.K_RIGHT]:
        head.go_right()

pygame.init()

window = pygame.display.set_mode((1024, 768), 0, 32)
pygame.display.set_caption('Hungry Snake')
key = pygame.key.get_pressed()

head = Head(500, 300)
game = True

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    move()

    SCREEN.fill(BACKGROUND_COLOR)
    head.render()
    window.blit(SCREEN, (0, 0))
    pygame.display.flip()
