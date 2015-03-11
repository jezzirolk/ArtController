import threading
import time
import pygame
import signal
import evtype
class Timer(object):
	def __init__(self):
		#prep the object
		self.tid=0
		self.stopped = threading.Event()
	def startTimer(self):
		#make the thread, set it to die with the program, and start it
		self.tid = threading.Thread(target=worker, args=[self.stopped])
		self.tid.setDaemon(True)
		self.tid.start()
	def stopTimer(self):
		#tell the thread to stop
		self.stopped.set()

def worker(stop):
	i = 0
	while not stop.isSet():
		# add a timer event to the queue for 10 hz
		ev = pygame.event.Event(evtype.USR10HZ, x=0)
		pygame.fastevent.post(ev)
		time.sleep(.1)
		i = i + 1
		if i == 10:
			#add a timer to the queue for 1 hz
			ev = pygame.event.Event(evtype.USR1HZ, x=0)
			pygame.fastevent.post(ev)
			i = 0
	return
