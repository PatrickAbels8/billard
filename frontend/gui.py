import pygame
import random

pygame.display.set_caption("Billard")
pygame.font.init()

HEIGHT = 600
WIDTH = 1200
FPS = 50

MARGIN = 40
BOARD_HEIGHT = HEIGHT-2*MARGIN
BOARD_WIDTH = WIDTH-2*MARGIN
FONT = pygame.font.SysFont("arial", 20)

win = pygame.display.set_mode((WIDTH, HEIGHT))

bals = [
    [1, (204, 214, 39)],
    [9, (204, 214, 39)],
    [2, (27, 78, 213)],
    [10, (27, 78, 213)],
    [3, (213, 35, 27)],
    [11, (213, 35, 27)],
    [4, (153, 24, 176)],
    [12, (153, 24, 176)],
    [5, (226, 137, 37)],
    [13, (226, 137, 37)],
    [6, (58, 201, 19)],
    [14, (58, 201, 19)],
    [7, (131, 4, 4)],
    [15, (131, 4, 4)],
    [8, (0, 0, 0)],
]



def draw_window(balls, turn):
	win.fill((0, 0, 0))
	rect = pygame.Rect(MARGIN, MARGIN, BOARD_WIDTH, BOARD_HEIGHT)
	pygame.draw.rect(win, (0, 255, 0), rect)
	player = '2' if turn else '1'
	player = FONT.render(f'Player {player} ...', 1, (255, 255, 255))
	win.blit(player, (int(WIDTH/2)-player.get_width(), 5))

	for ind, color in balls:
		pygame.draw.circle(win, color, (random.randint(MARGIN, BOARD_WIDTH), random.randint(MARGIN, BOARD_HEIGHT)), 10)

	pygame.display.update()

'''
balls: list of Ball
turn: 0 for player 1, 1 for player 2
'''
def render(balls, turn):
	draw_window(balls, turn)

def close():
	pygame.quit()