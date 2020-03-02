from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parrentdir = os.path.dirname(currentdir)
sys.path.insert(0, parrentdir)

import classes
# import frontend.gui as gui

HOST = "127.0.0.1"
PORT = 5500
ADDR = (HOST, PORT)
BUFSIZ = 512

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

players = []
turn = True

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


class Player:
	def __init__(self, addr, client, first):
		self.addr = addr
		self.client = client
		self.first = first


def client_communication(player, balls):
	client = player.client
	while True:
		shot = client.recv(BUFSIZ)
		pl_id = 1 if player.first else 2
		for ball in balls:
			if ball.number == '0':
				# ball.move(shot)
				print(f'Player {pl_id}: {shot}')
		turn = not turn


def wait_for_connection():
	while len(players)<2:
		try:
			client, addr = SERVER.accept()
			player = Player(addr, client, first=True if len(players) < 1 else False)
			players.append(player)

			print(f'{addr} connected')
		except Exception as e:
			print('Exception', e)
			break

def update_board(balls, game):
	pass
	#gui.render(balls, turn)


def start_game():
	game = classes.Game(1, 1)
	balls = [game.white_ball]
	while True:
		update_board(balls, game)
		for player in players:
			client_communication(player, balls)


if __name__ == "__main__":
	SERVER.listen(2)
	print('waiting for 2 players ...')
	wait_for_connection()
	start_game()
	SERVER.close()
