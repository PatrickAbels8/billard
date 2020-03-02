from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time


HOST = "127.0.0.1"
PORT = 5500
ADDR = (HOST, PORT)
BUFSIZ = 512

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

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
    def __init__(self):

        self.balls = [Ball(i) for i in color_number]

    def make_shot(self):
        pass


class Ball:
    def __init__(self, id):
        self.id, self.color = id


class Player:
    def __init__(self):
        pass


def start_game():
    pass


if __name__ == "__main__":
    start_game()
