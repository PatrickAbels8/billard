from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time




class Client:
	HOST = '127.0.0.1'
	PORT = 5500
	ADDR = (HOST, PORT)
	BUFSIZ = 512

	def __init__(self):
		self.client_socket = socket(AF_INET, SOCK_STREAM)
		self.client_socket.connect(self.ADDR)


	def receive_msg(self):
		while True:
			try:
				balls = self.client_socket.rcv(self.BUFSIZ).decode()
				shot = self.make_move(balls)

			except Exception as e:
				print('Exeption', e)
				break

	def make_move(self, balls):
		vel_x = 2
		vel_y = 1
		send_msg((vel_x, vel_y))

	def send_msg(self, shot):
		try:
			self.client_socket.send(bytes(shot, 'utf8'))
		except Exception as e:
			self.client_socket = socket(AF_INET, SOCK_STREAM)
			self.client_socket.connect(self.ADDR)
			print(e)
