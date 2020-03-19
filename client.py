import sys
from time import sleep
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory, connectWS

# player = '0'

class ClientProtocol(WebSocketClientProtocol):

	player_id = '0'

	def makeShot(self, board):
		return input('shot? ')

	def onOpen(self):
		print('CONNECTED TO SERVER')

	def onMessage(self, payload, isBinary):
		if not isBinary:
			msg = payload.decode('utf8')
			if 'HELLO' in msg:
				self.player_id = msg.split()[1]
			else:
				if msg[0] == self.player_id:
					print(msg)
					board = msg.split(':')[1]
					shot = self.makeShot(board)
					self.sendMessage(shot.encode('utf8'))


	# def onMessage(self, data):
	# 	data = data.decode('utf-8')
	# 	if('CONNECTED' in data):
	# 		player = data.split()[1]
	# 		print('I am Player ', player)
	# 	if(player == data[0]):
	# 		print('Current Board: ', data.split()[1])
	# 		shot = input('My Shot: ')
	# 		self.transport.write(str.encode(shot))
		# self.transport.loseConnection()


factory = WebSocketClientFactory('ws://127.0.0.1:9000')
factory.protocol = ClientProtocol
connectWS(factory)
reactor.run()