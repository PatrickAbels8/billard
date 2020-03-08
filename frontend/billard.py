import pygame
import random
from numpy import sqrt


s2 = sqrt(2)
gamma = 0.5

TURN = True


pygame.display.set_caption("Billard")
pygame.font.init()

HEIGHT = 600
WIDTH = 1200
FPS = 50

MARGIN = 40
BORDER = 5
BOARD_HEIGHT = HEIGHT - 2 * MARGIN
BOARD_WIDTH = WIDTH - 2 * MARGIN
BALL_RADIUS = 10
BACK_COL = 0.8
BACK_ROW = 0.5

FONT = pygame.font.SysFont("arial", 20)

# bals = [
#     [1, (204, 214, 39), [0, 0]],
#     [9, (204, 214, 39), [2, 0]],
#     [2, (27, 78, 213), [4, 0]],
#     [10, (27, 78, 213), [6, 0]],
#     [3, (213, 35, 27), [8, 0]],
#     [11, (213, 35, 27), [1, s2 * 2]],
#     [4, (153, 24, 176), [3, s2 * 2]],
#     [12, (153, 24, 176), [5, s2 * 2]],
#     [5, (226, 137, 37), [7, s2 * 2]],
#     [13, (226, 137, 37), [2, s2 * 4]],
#     [6, (58, 201, 19), [4, s2 * 4]],
#     [14, (58, 201, 19), [6, s2 * 4]],
#     [7, (131, 4, 4), [3, s2 * 6]],
#     [15, (131, 4, 4), [5, s2 * 6]],
#     [8, (0, 0, 0), [4, s2 * 8]],
# ]


class Ball:
    def __init__(self, pos, vel, color=None, number=None, *args):
        # self.t = ttm()
        self.pos = pos
        self.vel = vel
        self.color = color
        self.number = number

    def move(self):
        # self.pos[0] += (ttm() - self.t) * self.vel[0]
        # self.pos[1] += (ttm() - self.t) * self.vel[1]
        self.vel[0] *= gamma
        self.vel[1] *= gamma

        print(self.pos)
        return self.pos

    def shot(self):
        x, y = self.pos
        self.pos = [x+0.03, y]


class Board:
    rect_table = pygame.Rect(MARGIN, MARGIN, BOARD_WIDTH, BOARD_HEIGHT)
    rect_border = pygame.Rect(MARGIN-BORDER, MARGIN-BORDER, BOARD_WIDTH+2*BORDER, BOARD_HEIGHT+2*BORDER)

    BALLS = [
        Ball(pos=[0.2, 0.5], vel=[0, 0], color=(255, 255, 255), number="0"),
        Ball(pos=[BACK_COL-4*BALL_RADIUS/BOARD_WIDTH, BACK_ROW-2*(BALL_RADIUS/BOARD_HEIGHT)], vel=[0, 0], color=(204, 214, 39), number="1"),
        Ball(pos=[BACK_COL, BACK_ROW-4*(BALL_RADIUS/BOARD_HEIGHT)], vel=[0, 0], color=(27, 78, 213), number="2"),
        Ball(pos=[BACK_COL-2*BALL_RADIUS/BOARD_WIDTH, BACK_ROW-1*(BALL_RADIUS/BOARD_HEIGHT)], vel=[0, 0], color=(213, 35, 27), number="3"),
        Ball(pos=[BACK_COL-4*(BALL_RADIUS/BOARD_WIDTH), BACK_ROW+2*(BALL_RADIUS/BOARD_HEIGHT)], vel=[0, 0], color=(153, 24, 176), number="4"),
        Ball(pos=[BACK_COL, BACK_ROW+4*(BALL_RADIUS/BOARD_HEIGHT)], vel=[0, 0], color=(226, 137, 37), number="5"),
        Ball(pos=[BACK_COL-8*(BALL_RADIUS/BOARD_WIDTH), BACK_ROW], vel=[0, 0], color=(58, 150, 19), number="6"),
        Ball(pos=[BACK_COL, BACK_ROW], vel=[0, 0], color=(131, 4, 4), number="7"),
        Ball(pos=[BACK_COL-4*(BALL_RADIUS/BOARD_WIDTH), BACK_ROW], vel=[0, 0], color=(0, 0, 0), number="8"),
        Ball(pos=[BACK_COL-2*(BALL_RADIUS/BOARD_WIDTH), BACK_ROW+1*(BALL_RADIUS/BOARD_HEIGHT)], vel=[0, 0], color=(204, 214, 39), number="9"),
        Ball(pos=[BACK_COL-6*(BALL_RADIUS/BOARD_WIDTH), BACK_ROW-1*(BALL_RADIUS/BOARD_HEIGHT)], vel=[0, 0], color=(27, 78, 213), number="10"),
        Ball(pos=[BACK_COL, BACK_ROW-2*(BALL_RADIUS/BOARD_HEIGHT)], vel=[0, 0], color=(213, 35, 27), number="11"),
        Ball(pos=[BACK_COL, BACK_ROW+2*(BALL_RADIUS/BOARD_HEIGHT)], vel=[0, 0], color=(153, 24, 176), number="12"),
        Ball(pos=[BACK_COL-6*(BALL_RADIUS/BOARD_WIDTH), BACK_ROW+1*(BALL_RADIUS/BOARD_HEIGHT)], vel=[0, 0], color=(226, 137, 37), number="13"),
        Ball(pos=[BACK_COL-2*(BALL_RADIUS/BOARD_WIDTH), BACK_ROW+3*(BALL_RADIUS/BOARD_HEIGHT)], vel=[0, 0], color=(58, 150, 19), number="14"),
        Ball(pos=[BACK_COL-2*(BALL_RADIUS/BOARD_WIDTH), BACK_ROW-3*(BALL_RADIUS/BOARD_HEIGHT)], vel=[0, 0], color=(131, 4, 4), number="15"),
    ]

    def __init__(self):
        self.turn = True
        self.winner = None

    def draw(self, win):
        win.fill((0, 0, 0))
        pygame.draw.rect(win, (238, 118, 33), self.rect_border)
        pygame.draw.rect(win, (0, 255, 0), self.rect_table)
        [pygame.draw.circle(win, (238, 118, 33), (hole_x, hole_y), BALL_RADIUS) for hole_x, hole_y in [
            (MARGIN+int(0.5*BALL_RADIUS), MARGIN+int(0.5*BALL_RADIUS)),
            (MARGIN+int(0.5*BOARD_WIDTH), MARGIN+int(0.5*BALL_RADIUS)),
            (MARGIN+BOARD_WIDTH-int(0.5*BALL_RADIUS), MARGIN+int(0.5*BALL_RADIUS)),
            (MARGIN+BOARD_WIDTH-int(0.5*BALL_RADIUS), MARGIN+BOARD_HEIGHT-int(0.5*BALL_RADIUS)),
            (MARGIN+int(0.5*BOARD_WIDTH), MARGIN+BOARD_HEIGHT-int(0.5*BALL_RADIUS)),
            (MARGIN+int(0.5*BALL_RADIUS), MARGIN+BOARD_HEIGHT-int(0.5*BALL_RADIUS)),
        ]]
        player = "2" if self.turn else "1"
        player = FONT.render(f"Player {player}'s turn!", 1, (255, 255, 255))
        win.blit(player, (int(WIDTH / 2) - player.get_width(), 5))

        for ball in self.BALLS:
            x, y = ball.pos
            x = int(x*BOARD_WIDTH+MARGIN)
            y = int(y*BOARD_HEIGHT+MARGIN)
            if int(ball.number) > 8:
                pygame.draw.circle(win, ball.color, (x, y), BALL_RADIUS)
                pygame.draw.circle(win, (255, 255, 255), (x, y), BALL_RADIUS-4)

            else:
                pygame.draw.circle(win, ball.color, (x, y), BALL_RADIUS)

        pygame.display.update()

    def move(self):
        [ball.shot() for ball in self.BALLS if ball.number == '0']
        self.turn = not self.turn

def main():
    game = Board()
    clock = pygame.time.Clock()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    run = True
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    move()

        game.draw(win)

if __name__ == '__main__':
    main()



# def render(balls, turn):
#     draw_window(balls, turn)


# def close():
#     pygame.quit()
