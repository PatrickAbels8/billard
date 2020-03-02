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


a = vec(1, 2)
b = vec(5, 5)
print(a + b)
print(a - b)
print(a * b)
print(a * 5)

from p5 import *


def setup():
    size(640, 360)
    no_stroke()
    background(204)


def draw():
    circle((mouse_x, mouse_y), 5)


run()
