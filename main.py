import time
import os
import sys

import pygame

from act import g_o_action, game_action, menu_action
from act import menu_update, game_update, g_o_update, level_update
from mainvars import snake, scores_in_game, title, life, level, menu_level, COLORS, SCREEN, window
from snake import intersect
from fonts import list_scores_title_font, list_scores_font
from food import food
from food import Food

scores = 0


def save_res(score):
    if 'results.txt' in os.listdir(os.getcwd()):
        file = open('results.txt')
        text = []
        for line in file:
            text.append(line.strip() + '\n')
        file.close()
    else:
        text = []
    file = open('results.txt', 'w')
    t = time.ctime().split(' ')
    text.append('{} ({})'.format(score, ' '.join(t)))
    for line in text:
        file.write(line)
    file.close()
    return sorted(text, reverse=True)


def eat():
    for f in range(len(food)):
        if intersect(snake.head, food[f]):
            food.remove(food[f])
            return True


def snake_on_block():
    for b in level.blocks:
        if intersect(snake.head, b):
            return True


def check_food():
    for b in level.blocks:
        for f in food:
            if intersect(b,f):
                food.remove(f)


def add_food():
    if len(food) < 3:
        f = Food()
        food.append(f)


def show_text():
    pass


def game_loop(score):
    timer = pygame.time.Clock()
    scores = score
    speed = 5
    count = 0
    level.choose_level(menu_level.current_l+1)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
        game_action()
        snake.change_condition()
        count += 1
        add_food()
        check_food()
        if eat():
            if len(snake.body) % 10 == 0:
                speed += 1
            snake.add_sect()
            scores += round((len(snake.body))/5)
        scores_in_game.change_num(scores/100)
        if snake_on_block():
            return save_res(scores), scores
        if snake.intersect1():
            life.life_pop()
            if len(life) < 1:
                return save_res(scores), scores
        game_update()
        timer.tick(speed)
        game_action()


def menu_loop():
    timer = pygame.time.Clock()
    speed = 7
    while True:
        timer.tick(speed)
        menu_action()
        if title.move(speed):
            speed += 5
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
        if title.ypos > 1600:
            break
        menu_update()


def g_o_loop(all_scores):

    #
    if len(all_scores[0]) >= 3:
        scores_list = [all_scores[0][res].split()[0] for res in range(3)]
    else:
        scores_list = [all_scores[0][res].split()[0] for res in range(len(all_scores)-1)]
    print(scores_list)
    rec_nums = list()
    for rec in range(3):
        try:
            rec_nums.append(list_scores_font.render('{}:  {}'.format(rec+1, scores_list[rec]), True, COLORS['black']))
        except IndexError:
            rec_nums.append(list_scores_font.render('{}:  {}'.format(rec+1, 0), True, COLORS['black']))

    show_title = list_scores_title_font.render('Bests:', True, COLORS['black'])

    scores_in_game.show_final()

    while True:
        if g_o_action():
            return True
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
        g_o_update()
        SCREEN.blit(show_title, (1200, 480))
        SCREEN.blit(rec_nums[0], (1250, 600))
        SCREEN.blit(rec_nums[1], (1250, 670))
        SCREEN.blit(rec_nums[2], (1250, 740))

        window.blit(SCREEN, (0, 0))


def test_level_loop():
    while True:
        menu_action()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
        level_update()


def main():

    while True:
        pygame.init()
        menu_loop()
        list_scores = game_loop(0)
        if g_o_loop(list_scores):
            snake.reset()
            scores_in_game.reset()
            life.reset()
            title.reset()
        time.sleep(2)


if __name__ == '__main__':
    main()