import threading
import time
import pygame
import signal
import evtype
class Timer(object):
#	tid = 0
#	stopped = 0
	def __init__(self):
#		self.tid=0
#		self.stopped = threading.Event()
		self.ticks = 0
		signal.signal(signal.SIGALRM, self.worker)
	def startTimer(self):
		signal.setitimer(signal.ITIMER_REAL,1,1)
		signal.pause()
#		self.tid = threading.Thread(target=worker, args=[self.stopped])
#		self.tid.start()
	def stopTimer(self):
		signal.setitimer(signal.ITIMER_PROF, 0,0)
		print '4'
#		self.stopped.set()

	def worker(self, signum, framstack):
		self.ticks=self.ticks+1
		ev = pygame.event.Event(evtype.USRICK, x=0)
		pygame.fastevent.post(ev)
		ev = pygame.event.Event(evtype.USR10HZ, x=0)
		pygame.fastevent.post(ev)
		if self.ticks==10:
			ev = pygame.event.Event(evtype.USR1HZ, x=0)
			pygame.fastevent.post(ev)
			self.ticks=0
		return
#	while not stop.isSet():
#		# add a timer event to the queue for 10 hz
#		#print 'sleep 10hz'
#		ev = pygame.event.Event(USRICK, x=1)
#		pygame.fastevent.post(ev)
#		time.sleep(.1)
#		i = i + 1
#		if i == 10:
#			#add a timer to the queue for 1 hz
#			print 'sleep 1hz'
#			i = 0
	#return
