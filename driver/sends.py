import sys
import time
import socket
import threading
import pygame
import cPickle
import evtype
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
		mg = cPickle.dumps((num,val))
		m = '%05d' % sys.getsizeof(mg)
		msg = 'ana' + m + mg
		self.send(msg)

	def sendDigital(self, num, val):
		mg = cPickle.dumps((num, val))
		m = '%05d' % sys.getsizeof(mg)
		msg = 'dig' + m + mg
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
	rcvrun.set()
	done = False
	while not done:
		msg = s.recv(3)
		if msg == 'ack':
			print 'ack'
		elif msg == 'dig':
			print 'digital'
		elif msg == 'ana':
			print 'analog'
		elif msg == 'ick':
			print 'ick'
		elif msg == '':
			print 'its dead jim'
			done = True
		else:
			print msg
			print 'was sent'
	rcvrun.clear()
	return


