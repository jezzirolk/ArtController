import threading
import time
import pygame
USRICK=pygame.USEREVENT+2
class Timer(object):
	tid = 0
	stopped = 0
	def __init__(self):
		self.tid=0
		self.stopped = threading.Event()
	def startTimer(self):
		self.tid = threading.Thread(target=worker, args=[self.stopped])
		self.tid.start()
	def stopTimer(self):
		self.stopped.set()
def worker(stop):
	i = 0
	while not stop.isSet():
		# add a timer event to the queue for 10 hz
		#print 'sleep 10hz'
		ev = pygame.event.Event(USRICK, x=1)
		pygame.fastevent.post(ev)
		time.sleep(.1)
		i = i + 1
		if i == 10:
			#add a timer to the queue for 1 hz
			print 'sleep 1hz'
			i = 0
	return
