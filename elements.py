import pygame


class Bar():
    def __init__(self, x, y, w, h, color):
            self.xpos = x
            self.ypos = y
            self.color = color
            self.image = pygame.Surface((w, h))

    def draw(self, screen):
        self.image.fill(self.color)
        screen.blit(self.image, (self.xpos, self.ypos))