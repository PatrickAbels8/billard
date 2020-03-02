from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time


HOST = "127.0.0.1"
PORT = 5500
ADDR = (HOST, PORT)
BUFSIZ = 512

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

# comment
def game_loop():
    pass


def render_board():
    pass


def make_shot():
    pass


def call_player():
    pass


if __name__ == "__main__":
    SERVER.listen(2)  # waiting for 2 clients
    print("Waiting for 2 players...")

    SERVER.close()
