import sys
import os
from time import sleep
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File
from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory, listenWS

from gui import game_tick, FPS, init
from twisted.internet.task import LoopingCall

def new_game():
	print('--- NEW GAME ---')
	factory.shots = []
	init()
	tick = LoopingCall(game_tick, factory.shots)
	tick.start(1.0/FPS)

class ServerProtocol(WebSocketServerProtocol):

	def read_balls(self): # todo alwas one shot behind
		if os.path.exists('board.txt'):
			with open('board.txt', 'r') as f:
				return f.read()
		else:
			return ''

	def render(self, shot):
		self.factory.shots.append(shot)

	def broadcastBoard(self):
		self.factory.broadcast(self.factory.turn + "'s Turn:" + self.read_balls())

	def onOpen(self):
		self.factory.register(self)
		if len(self.factory.clients) == 2:
			new_game()
			self.broadcastBoard()
			

	def onMessage(self, payload, isBinary):
		if not isBinary:
			shot = payload.decode('utf8')
			print(self.factory.turn + ': ' + shot)
			self.render(shot)
			self.factory.turn = '1' if self.factory.turn == '0' else '0'
			self.broadcastBoard()

	def connectionLost(self, reason): # todo deconnect clients if server crashes
		WebSocketServerProtocol.connectionLost(self, reason)
		self.factory.unregister(self)


class ServerFactory(WebSocketServerFactory):

	def __init__(self, url):
		WebSocketServerFactory.__init__(self, url)
		self.clients = []
		self.turn = '0'
		self.shots = []

	def register(self, client):
		if client not in self.clients:
			if len(self.clients) == 0: # todo if player 0 reconnects both are player 1
				client.sendMessage('HELLO 0'.encode('utf8'))
			else:
				client.sendMessage('HELLO 1'.encode('utf8'))
			self.clients.append(client)
			print('CONNECT')

	def unregister(self, client):
		if client in self.clients:
			self.clients.remove(client)
			print('DECONNECT')

	def broadcast(self, msg):
		for c in self.clients:
			c.sendMessage(msg.encode('utf8'))


server_factory = ServerFactory
factory = server_factory('ws://127.0.0.1:9000')
factory.protocol = ServerProtocol
listenWS(factory)
reactor.listenTCP(8000, Site(File(".")))

reactor.run()