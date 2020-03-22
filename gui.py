import pygame
from twisted.internet import reactor
from math import sqrt, acos, cos, sin
import numpy as np

win = None
FPS = 10
FPS_SHOT = 30
HEIGHT = 600
WIDTH = 1200

MARGIN = 0 # 40
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

		self.direction = (0, 0)

	def move(self):
		# shot_direction, shot_power = shot
		dir_x, dir_y = self.direction
		x, y = self.pos
		self.pos = [x+self.vel*(dir_x*0.01), y-self.vel*(dir_y*0.01)]
		self.vel -= 1 # todo smaller to be realistic

	'''
	if it bounces on a wall it inverses its direction, else nothing happens
	'''
	def bounce(self): # todo take ball radius into count / maybe <= and >=
		pos_x, pos_y = self.pos
		dir_x, dir_y = self.direction

		# new_dir_x, new_dir_y = self.direction
		if pos_x < 0 and dir_x < 0: # left border
			dir_x *= -1
			print('left')
		if pos_y < 0 and dir_y > 0: # top border
			dir_y *= -1
			print('top')
		if pos_x > 1 and dir_x > 0: # right border
			dir_x *= -1
			print('right')
		if pos_y > 1 and dir_y < 0: # down border
			dir_y *= -1
			print('down')
		self.direction = (dir_x, dir_y)

	'''
	collide is called on self with every other ball
	todo: every collision is tested 2 times, only do that once
	'''
	def crash(self, balls, index):
		for i in range(len(balls)):
			if i != index:
				self.collide(balls[i])

	'''
	if self and ball collide they bounce, else nothing happens
	'''
	def collide(self, ball):
		global BALL_RADIUS, BOARD_WIDTH, BOARD_HEIGHT

		dx = self.pos[0]-ball.pos[0]
		dy = self.pos[1]-ball.pos[1]
		distance = sqrt(pow(BOARD_WIDTH*dx, 2) + pow(BOARD_HEIGHT*dy, 2))

		if distance <= 2*BALL_RADIUS:
			if self.vel > 0 or ball.vel > 0:
				# 1. angle mirrors
				# 2. energy decreases
				# 3. angle out factor depending on angle in
				# 4. all depending on angle of other ball
				(dir_x, dir_y) = self.direction
				denominator = np.abs(np.dot((dir_x, dir_y), (dx, dy)))
				nominator = np.linalg.norm((dir_x, dir_y))*np.linalg.norm((dx, dy))
				beta_in = acos(denominator/nominator)
				beta_out = 2*beta_in
				R_beta = [[cos(beta_out), sin(beta_out)], [-sin(beta_out), cos(beta_out)]]
				new_dir_x, new_dir_y = np.dot((dir_x, dir_y), R_beta)
				print(denominator)
				print(nominator)
				print(beta_in)
				print(beta_out)
				print(R_beta)
				print(new_dir_x)
				print(new_dir_y)
				self.direction = (int(new_dir_x), int(new_dir_y))

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

DEFAULT_BALLS = [Ball(number=str(num), color=col, pos=[BACK_COL-x*BALL_RADIUS/BOARD_WIDTH, BACK_ROW-y*BALL_RADIUS/BOARD_HEIGHT], vel=0) 
	if num != 0 else Ball(number=str(num), color=col, pos=[x, y], vel=0) for (num, col, (x, y)) in Balls]

BALLS = [Ball(number=str(num), color=col, pos=[BACK_COL-x*BALL_RADIUS/BOARD_WIDTH, BACK_ROW-y*BALL_RADIUS/BOARD_HEIGHT], vel=0) 
	if num != 0 else Ball(number=str(num), color=col, pos=[x, y], vel=0) for (num, col, (x, y)) in Balls]

def init():
	global win, BALLS, shots_made, DEFAULT_BALLS
	win = pygame.display.set_mode((WIDTH, HEIGHT))
	win.fill((0, 0, 0))

	shots_made= []
	BALLS = DEFAULT_BALLS # todo balls dont reset visually

	redraw(BALLS)
	save_balls(BALLS)
	print(shots_made)


def redraw(balls):
	global win, rect_border, rect_table, MARGIN, BALL_RADIUS, BOARD_WIDTH, BOARD_HEIGHT
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
	for ball in balls:
		x, y = ball.pos
		x = int(x*BOARD_WIDTH+MARGIN)
		y = int(y*BOARD_HEIGHT+MARGIN)
		if int(ball.number) > 8:
			pygame.draw.circle(win, ball.color, (x, y), BALL_RADIUS)
			pygame.draw.circle(win, (255, 255, 255), (x, y), BALL_RADIUS-4)
		else:
			pygame.draw.circle(win, ball.color, (x, y), BALL_RADIUS)


	pygame.display.update()


def save_balls(balls):
	return_string = ''
	for ball in balls:
		return_string += ball.number
		return_string += ','
		return_string += str(ball.pos[0])
		return_string += ','
		return_string += str(ball.pos[1])
		return_string += ';'

	with open('board.txt', 'w') as f:
		f.write(return_string)
		# print('written balls.')


def quiet_board(balls):
	for ball in balls:
		# print('vel: ', ball.vel)
		if ball.vel > 0:
			return False
	return True

'''
shot loop, change positions (call move on balls recursively) and redraw until board is quit
:param dir: for dir[0] in x go dir[1] in y
:param power: factor of 0.01 in x and y
'''
def shoot(direction ,power):
	# print('dir: %i, pow: %i' %(direction, power))
	global BALLS, FPS_SHOT
	clock = pygame.time.Clock()

	BALLS[0].vel = power
	BALLS[0].direction = direction

	while(not quiet_board(BALLS)):
		clock.tick(FPS_SHOT)

		# call move on BALLS[0]
		# check for collisions with other balls
		# for each collision, reduce power and call move on them as well, and so on
		for i in range(len(BALLS)):
			BALLS[i].move()
			BALLS[i].bounce()
			# BALLS[i].crash(BALLS, i)


		redraw(BALLS)
	# print('move done.')


'''
function to call every FPS seconds
:param shots: list of shots made so far, shot = "dir_power"
... dir: -1/-3 means x=-1 y=-3
'''
shots_made = []
def game_tick(shots):
	pygame.init()
	pygame.display.set_caption('Billard')
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			reactor.stop()

	global shots_made, BALLS
	if len(shots) > len(shots_made):
		cur_shot = shots[-1]
		cur_dir = int(cur_shot.split('_')[0].split('/')[0]), int(cur_shot.split('_')[0].split('/')[1])		
		cur_pow = int(cur_shot.split('_')[1])
		shoot(cur_dir, cur_pow)
		# BALLS[0].vel = cur_pow
		# BALLS[0].move(cur_dir, cur_pow)
		save_balls(BALLS)
		shots_made.append(cur_shot)
		print(shots_made)

	# redraw(BALLS)
	return True
