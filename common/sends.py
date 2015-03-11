import sys
import time
import socket
import threading
import pygame
import cPickle
import evtype
import hardware
class Connection(object):
	def __init__(self):
		self.s = 0
		self.s2 = 0
		self.ip = 0
		self.rcv = 0
		self.sender = ''
		self.rcvrun = threading.Event()
	
	def openConnection(self, ips):
		self.sender = 'driver'
		self.ip = ips
		port = 1857
		self.s = socket.socket()
		con = (self.ip, port)
		done = False
		#keep trying to conect
		while not done:
			try:
				self.s.connect(con)
				print 'robot connected'
				done = True
				break
			except:
				print 'waiting for connection'
				time.sleep(2)
		#start the reciever thread
		self.rcv = threading.Thread(target=rcv, args=[self.rcvrun,self.s])
		self.rcv.setDaemon(True)	
		self.rcv.start()

	def openListen(self):
		#start listening
		self.sender = 'robot'
		self.s2 = socket.socket()
		self.s2.bind(('', 1857))
		self.s2.listen(1)
		print 'waiting for a connection'
		self.s, client_address = self.s2.accept()
		print 'connected'
		#start the reciever thread
		self.rcv = threading.Thread(target=rcv, args=[self.rcvrun, self.s])
		self.rcv.setDaemon(True)
		self.rcv.start()
	
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
	
	def sendAck(self):
		msg = 'ack'
		self.send(msg)

	def cls(self):
		self.s.close()
	
	def send(self, msg):
		done = False
		while not done:
			try:
				self.s.sendall(msg)
				done = True
			except:
				print 'connection lost'
				hardware.onFail()
				if self.sender == 'driver':
					self.openConnection(self.ip)
				elif self.sender == 'robot':
					self.openListen()

def rcv(rcvrun, s):
	rcvrun.set()
	done = False
	while not done:
		msg = s.recv(3)
		if msg == 'ack':
			#stuff for if an ack shows up
			pass
		elif msg == 'dig':
			leng = int(s.recv(5))
			msg = s.recv(leng)
			data = cPickle.loads(msg)
			ev = pygame.event.Event(evtype.USRDIGITAL, num=data[0], val=data[1])
			pygame.fastevent.post(ev)
		elif msg == 'ana':
			leng = int(s.recv(5))
			msg = s.recv(leng)
			data = cPickle.loads(msg)
			ev = pygame.event.Event(evtype.USRANALOG, num = data[0], val = data[1])
			pygame.fastevent.post(ev)
		elif msg == 'ick':
			ev = pygame.event.Event(evtype.USRICK, x=0)
		elif msg == '':
			print 'its dead jim'
			done = True
		else:
			print msg
			print 'was sent'
	rcvrun.clear()
	return


