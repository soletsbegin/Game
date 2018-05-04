import pygame
import sys
import mainvars as m
from mainvars import SCREEN
from food import food


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
    if key[pygame.K_RETURN]:
        m.title.get_start()
    if key[pygame.K_LEFT]:
        m.menu_level.prev_level()
    if key[pygame.K_RIGHT]:
        m.menu_level.next_level()
    if key[pygame.K_ESCAPE]:
        sys.exit()


def g_o_action():
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        return True
    if key[pygame.K_ESCAPE]:
        sys.exit()


def game_update():
    SCREEN.fill(m.COLORS['black'])
    m.bar.draw(SCREEN)
    m.scores_in_game.draw(SCREEN)
    m.text_scores.draw(SCREEN)
    for f in food:
        f.draw(SCREEN)
    m.snake.draw(SCREEN)
    m.snake.head.draw(SCREEN)

    m.life.draw(SCREEN)

    m.level.draw(SCREEN)
    m.window.blit(SCREEN, (0, 0))
    pygame.display.update()


def menu_update():
    SCREEN.fill(m.COLORS['black'])
    m.bar.draw(SCREEN)
    m.scores_in_game.draw(SCREEN)
    m.text_scores.draw(SCREEN)
    m.life.draw(SCREEN)
    m.title.draw(SCREEN)
    m.arrow_l.draw(SCREEN)
    m.arrow_r.draw(SCREEN)
    m.menu_level.draw(SCREEN)
    m.window.blit(SCREEN, (0, 0))
    pygame.display.update()


def g_o_update():
    SCREEN.fill(m.COLORS['black'])
    m.bar.draw(SCREEN)
    m.text_scores.draw(SCREEN)
    m.level.draw(SCREEN)
    m.snake.draw(SCREEN)
    m.life.draw(SCREEN)
    m.go.draw(SCREEN)
    # m.scores_in_game.show_final()
    m.scores_in_game.draw(SCREEN)

    m.window.blit(SCREEN, (0, 0))
    pygame.display.update()


def level_update():
    SCREEN.fill(m.COLORS['black'])
    m.bar.draw(SCREEN)
    m.level.draw(SCREEN)

    m.window.blit(SCREEN, (0, 0))
    pygame.display.update()
