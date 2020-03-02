from numpy import sqrt

s2 = sqrt(2)
scale = 5

gamma = 0.5


class Game:
    def __init__(self):
        pass


class Ball:
    def __init__(self, pos, vel, other=None):
        self.pos = pos
        self.vel = vel
        self.other = other

    def move(self):
        self.pos[0] *= gamma
        self.pos[1] *= gamma
        self.vel = self.vel * gamma

        return self.pos


from p5 import *

HEIGHT = 600
WIDTH = 1200
FPS = 50

MARGIN = 40
BOARD_HEIGHT = HEIGHT - 2 * MARGIN
BOARD_WIDTH = WIDTH - 2 * MARGIN


B = Ball([200, 200], [5, 5])


def setup():
    size(640, 360)
    no_stroke()
    background(204)


def draw():
    print(B.pos)
    B.move()
    print(B.pos)
    circle(B.pos, 20)

    clear()


run()

