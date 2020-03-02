from numpy import sqrt
from time import sleep
from time import time as ttm

s2 = sqrt(2)
scale = 5

gamma = 0.5


class Game:
    def __init__(self, *args):
        self.white_ball = Ball(
            pos=[0.5, 0.5], vel=[0, 0], color=(255, 255, 255), number="0"
        )


class Ball:
    def __init__(self, pos, vel, color=None, number=None, *args):
        self.t = ttm()
        self.pos = pos
        self.vel = vel
        self.color = color
        self.number = number

    def move(self):
        self.pos[0] += (ttm() - self.t) * self.vel[0]
        self.pos[1] += (ttm() - self.t) * self.vel[1]
        self.vel[0] *= gamma
        self.vel[1] *= gamma

        print(self.pos)
        return self.pos


if __name__ == "__main__":
    from p5 import *

    HEIGHT = 600
    WIDTH = 1200
    FPS = 50

    MARGIN = 40
    BOARD_HEIGHT = HEIGHT - 2 * MARGIN
    BOARD_WIDTH = WIDTH - 2 * MARGIN

    B = Ball([200, 200], [10, 10])

    def setup():
        size(WIDTH, HEIGHT)
        background(204)

    def draw():
        k = B.move()
        circle(k, 40)

        clear()

    run()

