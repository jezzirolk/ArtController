import sys
import time
import socket
class Connection(object):
	def __init__(self):
		self.s = 0
		self.ip = 0
	
	def openConnection(self, ips):
		self.ip = ips
		port = 1857
		self.s = socket.socket()
		con = (self.ip, port)
		while 1:
			try:
				self.s.connect(con)
				print 'robot connected'
				break
			except:
				print 'waiting for connection'
				time.sleep(2)

	def sendClose(self):
		msg = 'cls'
		self.send(msg)
		self.cls()

	def sendAnalog(self, num, val):
		if num > 9:
			num = 9
		if num < 1:
			num = 1
		if val > 255:
			val = 255
		if val < 0:
			val = 0
		msg = 'ana%d%03d' % (num, val)
		self.send(msg)

	def sendIck(self):
		msg = 'ick'
		self.send(msg)

	def cls(self):
		self.s.close()
	
	def send(self, msg):
		done = False
		while not done:
			print "sending", msg
			try:
				self.s.sendall(msg)
				done = True
			except:
				print 'lost connection trying again'
				self.openConnection(self.ip)
