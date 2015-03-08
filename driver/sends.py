import sys
import time
import socket
import threading
import pygame
USRFUCKIT = pygame.USEREVENT + 5
class Connection(object):
	def __init__(self):
		self.s = 0
		self.ip = 0
		self.rcv = 0
		self.rcvrun = threading.Event()
	
	def openConnection(self, ips):
		self.ip = ips
		port = 1857
		self.s = socket.socket()
		con = (self.ip, port)
		done = False
		while not done:
			try:
				self.s.connect(con)
				print 'robot connected'
				done = True
				break
			except:
				print 'waiting for connection'
				time.sleep(2)
		self.rcv = threading.Thread(target=rcv, args=[self.rcvrun,self.s])
		self.rcv.setDaemon(True)	
		self.rcv.start()
	
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

def rcv(rcvrun, s):
	print '1'
	rcvrun.set()
	done = False
	print '2'
	ev = pygame.event.Event(pygame.USEREVENT + 5, x=0)
	pygame.fastevent.post(ev)
	while not done:
		msg = s.recv(3)
		if msg == 'ack':
			print 'ack'
		elif msg == '':
			print 'its dead jim'
			done = True
		else:
			print msg
			print 'was sent'
	rcvrun.clear()
	return


