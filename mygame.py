import time
import os

from act import *
from mainvars import snake, scores_in_game, title, life, level, menu_level
from snake import intersect
from food import food
from food import Food

scores = 0


def save_res(score):
    if not'results.txt' in os.listdir('.'):
        open('results.txt', 'w', encoding='utf-8').close()
    with open('results.txt', 'w') as file:
        text = file.readlines()
    t = time.ctime().split(' ')
    text.append('{} ({})\n'.format(score, ' '.join(t)))
    file.write(''.join(reversed(sorted(text, key=lambda x: x.split()[0]))))


def eat():
    for f in range(len(food)):
        if intersect(m.snake.head, food[f]):
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
            save_res(scores)
            break
        if snake.intersect1():
            life.life_pop()
            if len(life) < 1:
                save_res(scores)
                break
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


def g_o_loop():
    while True:
        if g_o_action():
            return True
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
        g_o_update()


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
        game_loop(0)
        if g_o_loop():
            snake.reset()
            scores_in_game.reset()
            life.reset()
            title.reset()


if __name__ == '__main__':
    main()