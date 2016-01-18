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
		self.port = 1857
		self.rcv = 0
		self.sender = 'default'
		self.rcvrun = threading.Event()
	def openConnection(self, ips):
		#sets the object up as a connector
		#setup all the variable
		self.sender = 'driver'
		self.ip = ips
		self.s = socket.socket()
		con = (self.ip, self.port)
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
	
	def openConnectionPort(self, ips, port):
		self.port = port
		self.openConnection(ips)

	def openListen(self):
		#sets the object up as a listener
		#start listening
		self.sender = 'robot'
		self.s2 = socket.socket()
		self.s2.bind(('', self.port))
		self.s2.listen(1)
		print 'waiting for a connection'
		self.s, client_address = self.s2.accept()
		print 'connected'
		#start the reciever thread
		self.rcv = threading.Thread(target=rcv, args=[self.rcvrun, self.s])
		self.rcv.setDaemon(True)
		self.rcv.start()

	def openListenPort(self, port):
		self.port = port
		self.openListen()
	
	def sendAnalog(self, num, val):
		#All Old send code
		#sends an indexed float
		#serilaizes it
		#mg = cPickle.dumps((int(num),float(val)))
		#gets the size
		#m = '%05d' % sys.getsizeof(mg)
		# adds the header, followed by the size as 5 digits, and then the message
		#msg = 'ana' + m + mg
		#self.send(msg)
		nu = '%02d' % num
		print nu
		pn = '2'
		if val < 1 :
			pn = '1'
		else:
			pn = '0'
		print pn
		vl = '%.6f' % abs(val)
		print vl
		msg = 'ana' + nu + pn + vl
		print msg
		self.send(msg)

	def sendDigital(self, num, val):
		#sends an indexed boolean
		#searilaizes the data
		#mg = cPickle.dumps((int(num), bool(val)))
		#get the size of the message
		#m = '%05d' % sys.getsizeof(mg)
		#adds the header, followed by the size, then adds the message
		nu = '%02d' % num
		print nu
		pn = '2'
		if val < 1 :
			pn = '1'
		else:
			pn = '0'
		print pn
		vl = '%08d' % abs(val)
		print vl
		msg = 'dig' + nu + pn + vl
		self.send(msg)

	def sendIck(self):
		#sends an ick message
		msg = 'ick'
		self.send(msg)
	
	def sendAck(self):
		#sends an ack message
		msg = 'ack'
		self.send(msg)

	def cls(self):
		#gracefully closes the socket, though never used
		self.s.close()
	
	def send(self, msg):
		done = False
		while not done:
			#tries to send the message
			try:
				self.s.sendall(msg)
				done = True
			except:
				#if it cant it will tell the hardware to make things safe then try again
				print 'connection lost'
				hardware.onFail()
				#so the hardware can make sure to redo what it already was doing before it died
				if self.sender == 'driver':
					self.openConnection(self.ip)
				elif self.sender == 'robot':
					self.openListen()

def rcv(rcvrun, s):
	#reciever worker thread
	rcvrun.set()
	done = False
	while not done:
		msg = s.recv(3)
		if msg == 'ack':
			#stuff for if an ack shows up
			pass
		elif msg == 'dig':
			# on digital message
			#pull the size
			#leng = int(s.recv(5))
			#Pull the message
			#msg = s.recv(leng)
			#unsearilaize it
			#data = cPickle.loads(msg)
			nm = int(s.recv(2))
			print nm
			pn = int(s.recv(1))
			print pn
			vlu = float(s.recv(8))
			print vlu
			if pn == 1:
				vlu = vlu * -1
			print vlu
			#
			#make and post the event
			ev = pygame.event.Event(evtype.USRDIGITAL, num=nm, val=vlu)
			pygame.fastevent.post(ev)
		elif msg == 'ana':
			#on an analog message
			#get the size of the data
			#leng = int(s.recv(5))
			#get the data
			#msg = s.recv(leng)
			#unsearilaize it
			#data = cPickle.loads(msg)
			nm = int(s.recv(2))
			print nm
			pn = int(s.recv(1))
			print pn
			vlu = float(s.recv(8))
			print vlu
			if pn == 1:
				vlu = vlu * -1
			print vlu
			#make and post the event
			ev = pygame.event.Event(evtype.USRANALOG, num = nm, val = vlu)
			pygame.fastevent.post(ev)
		elif msg == 'ick':
			#on an ick message
			ev = pygame.event.Event(evtype.USRICK, x=0)
		elif msg == '':
			#on a disconnect remotely
			print 'its dead jim'
			done = True
		else:
			print msg
			print 'was sent'
	rcvrun.clear()
	return
