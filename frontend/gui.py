import pygame
import random
from numpy import sqrt

s2 = sqrt(2)


pygame.display.set_caption("Billard")
pygame.font.init()

HEIGHT = 600
WIDTH = 1200
FPS = 50

MARGIN = 40
BOARD_HEIGHT = HEIGHT - 2 * MARGIN
BOARD_WIDTH = WIDTH - 2 * MARGIN
FONT = pygame.font.SysFont("arial", 20)

win = pygame.display.set_mode((WIDTH, HEIGHT))

bals = [
    [1, (204, 214, 39), [0, 0]],
    [9, (204, 214, 39), [2, 0]],
    [2, (27, 78, 213), [4, 0]],
    [10, (27, 78, 213), [6, 0]],
    [3, (213, 35, 27), [8, 0]],
    [11, (213, 35, 27), [1, s2 * 2]],
    [4, (153, 24, 176), [3, s2 * 2]],
    [12, (153, 24, 176), [5, s2 * 2]],
    [5, (226, 137, 37), [7, s2 * 2]],
    [13, (226, 137, 37), [2, s2 * 4]],
    [6, (58, 201, 19), [4, s2 * 4]],
    [14, (58, 201, 19), [6, s2 * 4]],
    [7, (131, 4, 4), [3, s2 * 6]],
    [15, (131, 4, 4), [5, s2 * 6]],
    [8, (0, 0, 0), [4, s2 * 8]],
]


def draw_window(balls, turn):
    win.fill((0, 0, 0))
    rect = pygame.Rect(MARGIN, MARGIN, BOARD_WIDTH, BOARD_HEIGHT)
    pygame.draw.rect(win, (0, 255, 0), rect)
    player = "2" if turn else "1"
    player = FONT.render(f"Player {player} ...", 1, (255, 255, 255))
    win.blit(player, (int(WIDTH / 2) - player.get_width(), 5))

    for ind, color, pos in balls:
        x, y = pos
        x = int(x * 10)
        y = int(y * 10)
        pygame.draw.circle(win, color, (x, y), 10)

    pygame.display.update()


"""
balls: list of Ball
turn: 0 for player 1, 1 for player 2
"""


def render(balls, turn):
    draw_window(balls, turn)


def close():
    pygame.quit()

