import numpy as np

color_number = [
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


class Game:
    def __init__(self, off_x=0, off_y=0):
        self.balls = [Ball(i) for i in color_number]

    def make_shot(self):
        pass


class Ball:
    def __init__(self, id):
        self.id, self.color = id


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
