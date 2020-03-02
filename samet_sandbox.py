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

import matplotlib.pyplot as plt
import numpy as np

ti = np.linspace(0, 100, 101)


def model(iv):
    return np.exp(-iv * 0.05)  # + 10 * np.exp(-iv * 0.04)


plt.plot(ti, model(ti))
plt.show()
