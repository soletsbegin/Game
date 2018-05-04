import os

import pygame


NUMBERS = {
    '0': pygame.image.load(os.path.join('graphics', 'numb', '0.png')),
    '1': pygame.image.load(os.path.join('graphics', 'numb', '1.png')),
    '2': pygame.image.load(os.path.join('graphics', 'numb', '2.png')),
    '3': pygame.image.load(os.path.join('graphics', 'numb', '3.png')),
    '4': pygame.image.load(os.path.join('graphics', 'numb', '4.png')),
    '5': pygame.image.load(os.path.join('graphics', 'numb', '5.png')),
    '6': pygame.image.load(os.path.join('graphics', 'numb', '6.png')),
    '7': pygame.image.load(os.path.join('graphics', 'numb', '7.png')),
    '8': pygame.image.load(os.path.join('graphics', 'numb', '8.png')),
    '9': pygame.image.load(os.path.join('graphics', 'numb', '9.png')),
}


class Bar:
    def __init__(self, x, y, w, h, color, path=None):
            self.xpos = x
            self.ypos = y
            self.color = color
            self._start = False
            if path is None:
                self.path = False
                self.image = pygame.Surface((w, h))
            elif path is not None:
                self.path = True
                self.image = pygame.image.load(path)

    def draw(self, screen):
        if self.path:
            screen.blit(self.image, (self.xpos, self.ypos))
        else:
            self.image.fill(self.color)
            screen.blit(self.image, (self.xpos, self.ypos))

    def get_start(self):
        self._start = True

    def reset(self):
        self.xpos, self.ypos = 0, 0
        self._start = False

    def move(self, speed):
        if self._start:
            self.ypos += speed
            return True


class Number:
    """
    Цифровая панель.
    """
    def __init__(self, x, y, x2, y2, x3, y3):
        self.pos1 = (x, y)
        self.pos2 = (x2, y2)
        self.pos3 = (x3, y3)
        self.image1 = pygame.image.load(os.path.join('graphics', 'numb', '0.png'))
        self.image2 = pygame.image.load(os.path.join('graphics', 'numb', '0.png'))
        self.image3 = pygame.image.load(os.path.join('graphics', 'numb', '0.png'))
        self.image1.set_colorkey((0, 0, 0))
        self.image2.set_colorkey((0, 0, 0))
        self.image3.set_colorkey((0, 0, 0))

    def change_num(self, scores):
        """

        """
        try:
            first, second, third = str(scores)[0], str(scores)[2], str(scores)[3]
            self.image1 = NUMBERS[first]
            self.image2 = NUMBERS[second]
            self.image3 = NUMBERS[third]
        except IndexError:
            pass

    def show_final(self):
        self.pos1 = (400, 650)
        self.pos2 = (480, 650)
        self.pos3 = (560, 650)

    def reset(self):
        self.image1 = pygame.image.load(os.path.join('graphics', 'numb', '0.png'))
        self.image2 = pygame.image.load(os.path.join('graphics', 'numb', '0.png'))
        self.image3 = pygame.image.load(os.path.join('graphics', 'numb', '0.png'))

    def draw(self, screen):
        screen.blit(self.image1, self.pos1)
        screen.blit(self.image2, self.pos2)
        screen.blit(self.image3, self.pos3)


class Text:
    def __init__(self, x, y, path):
        self._xpos = x
        self._ypos = y
        self.image = pygame.image.load(path)

    def draw(self, screen):
        screen.blit(self.image, (self._xpos, self._ypos))


class Life:
    def __init__(self):
        self._life_bar = [Bar(80, 20, 40, 80, 0, os.path.join('graphics', 'heart.png')),
                          Bar(150, 20, 40, 80, 0, os.path.join('graphics', 'heart.png')),
                          Bar(220, 20, 40, 80, 0, os.path.join('graphics', 'heart.png')),
                          ]

    def __len__(self):
        return len(self._life_bar)

    def reset(self):
        self._life_bar = [Bar(80, 20, 40, 80, 0, os.path.join('graphics', 'heart.png')),
                          Bar(150, 20, 40, 80, 0, os.path.join('graphics', 'heart.png')),
                          Bar(220, 20, 40, 80, 0, os.path.join('graphics', 'heart.png')),
                          ]

    def life_pop(self):
        try:
            self._life_bar.pop()
        except IndexError:
            self.reset()

    def draw(self, screen):
        for l in self._life_bar:
            l.draw(screen)

