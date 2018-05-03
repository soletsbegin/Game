import os.path

import pygame

LEVEL_FILES = [
    os.path.join('levels', '1.txt'),
    os.path.join('levels', '2.txt'),
    os.path.join('levels', '3.txt'),
    os.path.join('levels', '4.txt'),
    os.path.join('levels', '5.txt'),
    os.path.join('levels', '6.txt'),
]

LEVEL_PNG = [
    os.path.join('graphics', 'levels', '1.png'),
    os.path.join('graphics', 'levels', '2.png'),
    os.path.join('graphics', 'levels', '3.png'),
    os.path.join('graphics', 'levels', '4.png'),
    os.path.join('graphics', 'levels', '5.png'),
    os.path.join('graphics', 'levels', '6.png'),

]
class LevelPng:
    def __init__(self):
        self.xpos = 520
        self.ypos = 600
        self.current_l = 0
        self.image = pygame.image.load(LEVEL_PNG[self.current_l])

    def next_level(self):
        try:
            self.current_l += 1
            self.image = pygame.image.load(LEVEL_PNG[self.current_l])
        except IndexError:
            pass

    def prev_level(self):
        try:
            self.current_l -= 1
            self.image = pygame.image.load(LEVEL_PNG[self.current_l])
        except IndexError:
            pass

    def draw(self, screen):
        screen.blit(self.image, (self.xpos, self.ypos))


class Block:
    def __init__(self, x, y, png):
        self.xpos = x
        self.ypos = y
        self.image = pygame.image.load(png)

    def draw(self, screen):
        screen.blit(self.image, (self.xpos, self.ypos))


class Level:
    def __init__(self):
        self.path = os.path.join('levels', '1.txt')
        self.file = self.open_file()
        self.blocks = self.generate()

    def choose_level(self, cur_level):
        self.path = os.path.join('levels', str(cur_level) + '.txt')
        self.file = self.open_file()
        self.blocks = self.generate()

    def open_file(self):
        file = []
        with open(self.path) as text:
            for l in text:
                file.append(l.rstrip())
        return file

    def generate(self):
        blocks = []
        for line in range(len(self.file)):
            for row in range(len(self.file[line])):
                if self.file[line][row] == '*':
                    blocks.append(Block(row*40, line*40, os.path.join('graphics', 'block.png')))
        return blocks

    def draw(self, screen):
        for block in self.blocks:
            block.draw(screen)


if __name__ == '__main__':
    level = Level('2.txt')
    level.open_file()
    for l in level.file:
        print(l)
    for b in level.blocks:
        print(b.xpos, b.ypos)