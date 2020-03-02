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