import time

import pygame
import sys

from check_win import check_win
from computer_move import battle, computer_win
from computer_vs import comp_vs


pygame.init()
size_block = 50
margin = 1
width = heigth = size_block * 10 + margin * 12

size_window=(width, heigth)
screen=pygame.display.set_mode(size_window)
pygame.display.set_caption("@Обратные крестики нолики@")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

mas = [[0] * 10 for i in range(10)]
queue = 0
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if mas[row][col] == 0:
                if queue % 2 ==0:
                    mas[row][col] = 'x'
                queue += 1
        elif not game_over:
            for row in range(10):
                for col in range(10):
                    if mas[row][col] == 0:
                        if queue % 2 ==1:
                            computer_win(mas,'o')
                            queue += 1
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        game_over = False
                        mas = [[0] * 10 for i in range(10)]
                        queue = 0
                        screen.fill(BLACK)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 10 for i in range(10)]
            queue = 0
            screen.fill(BLACK)
    if not game_over:
        for row in range(10):
            for col in range(10):
                if mas[row][col] == 'x':
                    color = GREEN
                elif mas[row][col] == 'o':
                    color = BLUE
                else:
                    color = WHITE
                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == GREEN:
                    pygame.draw.line(screen, BLACK, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 7)
                    pygame.draw.line(screen, BLACK, (x + size_block -5, y + 5), (x + 5, y + size_block - 5), 7)
                elif color == BLUE:
                    pygame.draw.circle(screen, RED, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3, 7)

    if (queue - 1) % 2 == 0:
        game_over = check_win(mas, 'x')
    else:
        game_over = check_win(mas, 'o')

    if game_over:
        screen.fill(BLACK)
        font1 = pygame.font.SysFont('stxingkai', 80)
        font2 = pygame.font.SysFont('stxingkai', 20)
        text1 = font1.render(game_over, True, WHITE)
        text2 = font2.render("(Нажмите пробел)", True, WHITE)
        text_rect = text1.get_rect()
        test_x = screen.get_width() / 2 - text_rect.width / 2
        test_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [test_x, test_y])
        screen.blit(text2, [test_x-45, test_y+50])

    pygame.display.update()
