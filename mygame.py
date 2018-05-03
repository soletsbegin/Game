import time

from act import *
from mainvars import snake, scores_in_game, title, life, level, menu_level
from snake import intersect
from food import food
from food import Food


def save_res(scores):
    file = open('results.txt')
    text = file.readlines()
    file.close()
    t = time.ctime().split(' ')
    text.append('{} ({})\n'.format(scores, ' '.join(t)))
    with open('results.txt', 'w') as file:
        file.write(''.join(reversed(sorted(text))))


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


def game_loop():
    timer = pygame.time.Clock()
    scores = 0
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
            g_o_loop()
        if snake.intersect1():
            life.pop()
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
            break
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
        game_loop()


if __name__ == '__main__':
    main()