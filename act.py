import pygame
import sys
import mainvars as m
from mainvars import SCREEN


def game_action():
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]:
        m.snake.turn('down')
    if key[pygame.K_UP]:
        m.snake.turn('up')
    if key[pygame.K_LEFT]:
        m.snake.turn('left')
    if key[pygame.K_RIGHT]:
        m.snake.turn('right')
    if key[pygame.K_ESCAPE]:
        sys.exit()
    if key[pygame.K_DELETE]:
        m.snake.add_sect()


def menu_action():
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        m.title.get_start()
    if key[pygame.K_ESCAPE]:
        sys.exit()


def game_update():
    SCREEN.fill(m.COLORS['black'])
    m.bar.draw(SCREEN)
    m.scores_in_game.draw(SCREEN)
    m.text_scores.draw(SCREEN)
    m.snake.draw(SCREEN)
    for f in m.food:
        f.draw(SCREEN)
    m.snake.head.draw(SCREEN)
    for l in m.life:
        l.draw(SCREEN)
    m.window.blit(SCREEN, (0, 0))
    pygame.display.update()


def menu_update():
    SCREEN.fill(m.COLORS['black'])
    m.bar.draw(SCREEN)
    m.scores_in_game.draw(SCREEN)
    m.text_scores.draw(SCREEN)
    m.snake.draw(SCREEN)
    for l in m.life:
        l.draw(SCREEN)

    m.title.draw(SCREEN)

    m.window.blit(SCREEN, (0, 0))
    pygame.display.update()


def g_o_update():
    SCREEN.fill(m.COLORS['black'])
    m.bar.draw(SCREEN)
    m.text_scores.draw(SCREEN)
    m.snake.draw(SCREEN)
    for l in m.life:
        l.draw(SCREEN)

    m.go.draw(SCREEN)
    m.scores_in_game.show_final()
    m.scores_in_game.draw(SCREEN)

    m.window.blit(SCREEN, (0, 0))
    pygame.display.update()

