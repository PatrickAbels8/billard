from numpy import sqrt

s2 = sqrt(2)
scale = 5
color_number = [
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


class Game:
    def __init__(self, off_x=0, off_y=0):
        self.balls = [Ball(i, off_x, off_y) for i in color_number]
        self.off_x, self.off_y = off_x, off_y

    def make_shot(self):
        pass


class Ball:
    def __init__(self, id, off_x, off_y):
        self.id, self.color, self.position = id
        self.off_x, self.off_y = off_x, off_y

        x, y = self.position

        self.position = [(x + self.off_x) * scale, (y + self.off_y) * scale]


class Player:
    def __init__(self):
        pass


class vec(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vec(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return vec(self.x * other, self.y * other)
        else:
            return self.x * other.x + self.y * other.y

    def __str__(self):
        return f"{[self.x, self.y]}"


G = Game(10, 10)
"""
from p5 import *


def setup():
    size(640, 360)
    no_stroke()
    background(204)


def draw():
    for i in G.balls:
        circle(tuple(i.position), 5)


run()
"""

from p5 import *


def setup():
    size(640, 360)
    no_stroke()
    background(204)


def draw():
    if mouse_is_pressed:
        fill(random_uniform(255), random_uniform(127), random_uniform(51), 127)
    else:
        fill(255, 15)

    circle_size = random_uniform(low=10, high=80)

    circle((mouse_x, mouse_y), circle_size)


def key_pressed(event):
    background(204)


run()
