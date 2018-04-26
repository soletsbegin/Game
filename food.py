from random import randint
from screen import *

food = []
pics = ['1.png',
        '2.png',
        '3.png']


class Food(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.xpos, self.ypos = self.rand_pos()
        self.image = pygame.image.load(os.path.join('graphics', 'food', '111.png'))

    def rand_pos(self):
        while True:
            x = randint(40, WIDTH-40)
            y = randint(160, HEIGHT-40)
            if x % 40 == 0 and y % 40 == 0:
                return (x, y)

    def draw(self, screen):
        screen.blit(self.image, (self.xpos, self.ypos))