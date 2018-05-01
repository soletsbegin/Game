import time
from act import *
# from mainvars import *
from mainvars import snake, scores_in_game, title, bar, text_scores, life, go, window
from mainvars import COLORS
from snake import intersect
from food import food
from food import Food


def save_res(scores):
    file = open('results.txt')
    text = file.readlines()
    file.close()
    t = time.ctime().split(' ')
    text.append('{} ({} {} {})\n'.format(scores, ' '.join(t[3:4]), t[1], t[2]))
    with open('results.txt', 'w') as file:
        file.write(''.join(reversed(sorted(text))))


def eat():
    for f in range(len(food)):
        if intersect(m.snake.head, food[f]):
            food.remove(food[f])
            return True


def add_food():
    if len(food) < 3:
        count = 0
        f = Food()
        for b in snake.body:
            if f.ypos == b.ypos and f.xpos == b.xpos:
                count += 1
        if count == 0:
            food.append(f)


def game_update():
    SCREEN.fill(COLORS['black'])
    bar.draw(SCREEN)
    scores_in_game.draw(SCREEN)
    text_scores.draw(SCREEN)
    snake.draw(SCREEN)
    for f in food:
        f.draw(SCREEN)
    snake.head.draw(SCREEN)
    for l in life:
        l.draw(SCREEN)
    window.blit(SCREEN, (0, 0))
    pygame.display.update()


def game_loop():
    timer = pygame.time.Clock()
    scores = 0
    speed = 5
    count = 0
    while True:
        timer.tick(speed)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
        game_action()
        snake.change_condition()
        count += 1
        add_food()
        if eat():
            if len(snake.body) % 10 == 0:
                speed += 1
            snake.add_sect()
            scores += round((len(snake.body))/5)
        scores_in_game.change_num(scores/100)
        if snake.intersect1():
            life.pop()
            if len(life) < 1:
                save_res(scores)
                g_o_loop()
        game_update()
        game_action()


def menu_loop():
    speed = 20
    while True:
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
        menu_action()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
        g_o_update()


pygame.init()
menu_loop()
game_loop()
