import pygame
from twisted.internet import reactor

win = None
FPS = 30
HEIGHT = 600
WIDTH = 1200

MARGIN = 40
BORDER = 5
BOARD_HEIGHT = HEIGHT - 2 * MARGIN
BOARD_WIDTH = WIDTH - 2 * MARGIN
BALL_RADIUS = 10
BACK_COL = 0.8
BACK_ROW = 0.5

rect_table = pygame.Rect(MARGIN, MARGIN, BOARD_WIDTH, BOARD_HEIGHT)
rect_border = pygame.Rect(MARGIN-BORDER, MARGIN-BORDER, BOARD_WIDTH+2*BORDER, BOARD_HEIGHT+2*BORDER)

Balls = [
	(0, (255, 255, 255), (0.2, 0.5)),
	(1, (204, 214, 39), (4, 2)),
	(2, (27, 78, 213), (0, 4)),
	(3, (213, 35, 27), (2, 1)),
	(4, (153, 24, 176), (4, -2)),
	(5, (226, 137, 37), (0, -4)),
	(6, (58, 150, 19), (8, 0)),
	(7, (131, 4, 4), (0, 0)),
	(8, (0, 0, 0), (4, 0)),
	(9, (204, 214, 39), (2, -1)),
	(10, (27, 78, 213), (6, 1)),
	(11, (213, 35, 27), (0, 2)),
	(12, (153, 24, 176), (0, -2)),
	(13, (226, 137, 37), (6, -1)),
	(14, (58, 150, 19), (2, -3)),
	(15, (131, 4, 4), (2, 3))
]

class Ball:
	def __init__(self, pos, vel, color, number):
		self.pos = pos
		self.vel = vel
		self.color = color
		self.number = number

	# def move(self):
 #        # self.pos[0] += (ttm() - self.t) * self.vel[0]
 #        # self.pos[1] += (ttm() - self.t) * self.vel[1]
 #        self.vel[0] *= gamma
 #        self.vel[1] *= gamma

 #        print(self.pos)
 #        return self.pos

 #    def shot(self):
 #        x, y = self.pos
 #        self.pos = [x+0.03, y]


BALLS = [Ball(number=str(num), color=col, pos=[BACK_COL-x*BALL_RADIUS/BOARD_WIDTH, BACK_ROW-y*BALL_RADIUS/BOARD_HEIGHT], vel=[0, 0]) 
	if num != 0 else Ball(number=str(num), color=col, pos=[x, y], vel=[0, 0]) for (num, col, (x, y)) in Balls]

def init():
	global win
	win = pygame.display.set_mode((WIDTH, HEIGHT))
	win.fill((0, 0, 0))


def redraw():
	global win, rect_border, rect_table, BALLS, MARGIN, BALL_RADIUS, BOARD_WIDTH, BOARD_HEIGHT
	pygame.draw.rect(win, (238, 118, 33), rect_border)
	pygame.draw.rect(win, (0, 255, 0), rect_table)
	[pygame.draw.circle(win, (238, 118, 33), (hole_x, hole_y), BALL_RADIUS) for hole_x, hole_y in [
		(MARGIN+int(0.5*BALL_RADIUS), MARGIN+int(0.5*BALL_RADIUS)),
		(MARGIN+int(0.5*BOARD_WIDTH), MARGIN+int(0.5*BALL_RADIUS)),
		(MARGIN+BOARD_WIDTH-int(0.5*BALL_RADIUS), MARGIN+int(0.5*BALL_RADIUS)),
		(MARGIN+BOARD_WIDTH-int(0.5*BALL_RADIUS), MARGIN+BOARD_HEIGHT-int(0.5*BALL_RADIUS)),
		(MARGIN+int(0.5*BOARD_WIDTH), MARGIN+BOARD_HEIGHT-int(0.5*BALL_RADIUS)),
		(MARGIN+int(0.5*BALL_RADIUS), MARGIN+BOARD_HEIGHT-int(0.5*BALL_RADIUS)),
	]]
	for ball in BALLS:
		x, y = ball.pos
		x = int(x*BOARD_WIDTH+MARGIN)
		y = int(y*BOARD_HEIGHT+MARGIN)
		if int(ball.number) > 8:
			pygame.draw.circle(win, ball.color, (x, y), BALL_RADIUS)
			pygame.draw.circle(win, (255, 255, 255), (x, y), BALL_RADIUS-4)
		else:
			pygame.draw.circle(win, ball.color, (x, y), BALL_RADIUS)


	pygame.display.update()


'''
function to call every FPS seconds
:param shots: list of shots made so far
'''
def game_tick(shots):
	pygame.init()
	pygame.display.set_caption('Billard')
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			reactor.stop()
	redraw()
	return True
