import sys
import os.path
from snake import *
from food import *
from screen import *

body = []
snake = Snake()
bar = Bar(0, 0, WIDTH, 120, COLORS['grey'])
title = Bar(0, 0, 0, 0, 0, os.path.join('graphics', 'title.png'))
scr1 = Bar(0, 120, WIDTH, HEIGHT-120, COLORS['black'])
scr2 = Bar(0, 999, WIDTH, HEIGHT-120, COLORS['black'])
go = Bar(0, 0, 0, 0, 0, os.path.join('graphics', 'go.png'))
fin_scores = Number(WIDTH-250, 1000, WIDTH-170, 1000, WIDTH-90, 1000)
life = [Bar(78, 18, 164, 84, COLORS['black']),
        Bar(80, 20, 40, 80, COLORS['red_num']),
        Bar(140, 20, 40, 80, COLORS['red_num']),
        Bar(200, 20, 40, 80, COLORS['red_num']),]
numb = Number(WIDTH-250, 10, WIDTH-170, 10, WIDTH-90, 10)
t_scores = Text(WIDTH-800, 10, os.path.join('graphics', 'numb', 'scor.png'))
timer = pygame.time.Clock()
game_speed = 20


def eat():
    for f in range(len(food)):
        if intersect(snake.head, food[f]):
            food.remove(food[f])
            return True


def add_food():
    if len(food) < 3:
        while True:
            f = Food()
            for b in snake.body:
                if f.ypos != b.ypos and f.xpos != b.xpos:
                    food.append(f)
                    return True


def action(game = True):
    key = pygame.key.get_pressed()
    if game:
        if key[pygame.K_DOWN]:
            snake.turn('down')
        if key[pygame.K_UP]:
            snake.turn('up')
        if key[pygame.K_LEFT]:
            snake.turn('left')
        if key[pygame.K_RIGHT]:
            snake.turn('right')
        if key[pygame.K_ESCAPE]:
            sys.exit()
        if key[pygame.K_SPACE]:
            game_loop()


def update_all():
    SCREEN.fill(COLORS['black'])
    bar.draw(SCREEN)
    numb.draw(SCREEN)
    t_scores.draw(SCREEN)
    snake.draw(SCREEN)
    for f in food:
        f.draw(SCREEN)
    snake.head.draw(SCREEN)
    for l in life:
        l.draw(SCREEN)
    window.blit(SCREEN, (0, 0))
    pygame.display.update()


def game_loop():

    scores = 0.00
    speed = 7
    count = 0
    while True:
        timer.tick(speed)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
        action(True)
        snake.change_condition()
        count += 1
        add_food()
        if eat():
            if len(snake.body) % 10 == 0:
                speed += 0.5
            snake.add_sect()
            scores += 0.01
        numb.change_num(scores)
        if snake.intersect1():
            life.pop()
            if len(life) == 1:
                game_over(scores)
        update_all()
        action()


def start_loop():
    while True:
        timer.tick(20)
        SCREEN.fill(COLORS['black'])
        bar.draw(SCREEN)
        numb.draw(SCREEN)
        for l in life:
            l.draw(SCREEN)
        scr1.draw(SCREEN)
        title.draw(SCREEN)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
        action()
        window.blit(SCREEN, (0, 0))
        pygame.display.update()


def game_over(scores):
    timer = pygame.time.Clock()
    numb.change_num(0)
    numb.draw(SCREEN)
    fin_scores.change_num(scores)
    while True:
        timer.tick(20)
        go.draw(SCREEN)
        fin_scores.draw(SCREEN)
        numb.draw(SCREEN)
        bar.draw(SCREEN)
        t_scores.draw(SCREEN)
        for l in life:
            l.draw(SCREEN)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            break
        window.blit(SCREEN, (0, 0))
        pygame.display.update()



if __name__ == "__main__":
    pygame.init()
    game_loop()
