import pygame
import os


pygame.font.init()

font_gameover = os.path.join('fonts', 'game_over.ttf')
font_title = os.path.join('fonts', 'ka1.ttf')

font_size = {
    '1': 10,
    '2': 20,
    '3': 180,
    '4': 250,
}

last_scores_font = pygame.font.Font(font_gameover, font_size['4'])
list_scores_font = pygame.font.Font(font_gameover, font_size['3'])
list_scores_title_font = pygame.font.Font(font_gameover, font_size['4'])

if __name__ == '__main__':
    print(pygame.font.get_fonts())
