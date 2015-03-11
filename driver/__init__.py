import sys
import os
if __name__ == '__main__':
	if __package__ is None:
		sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
		from common.sends import Connection
		from common.timer import Timer
		from common import evtype
	else:
		from ..common.sends import Connection

import socket
import time
import pygame
import string
import driverCode
#os.environ["SDL_VIDEODRIVER"] = 'dummy'
#init the pygame and display setup
pygame.init()
pygame.display.init()
screen = pygame.display.set_mode([800,600])
#init the queue
pygame.fastevent.init()
#init the joystick
js = pygame.joystick.Joystick(0)
js.init()
#start the connection
con = Connection()
con.openConnection('localhost')
#start the timer
t=Timer()
t.startTimer()
#run the user init code
driverCode.onInit()
#queue processing loop
while True:
	#let the queue do what it needs
	pygame.fastevent.pump()
	#pull the next event
	ev = pygame.fastevent.poll()
	if ev.type == pygame.NOEVENT:
		#on an empty queue wait
		print 'wait'
		time.sleep(.2)
	elif ev.type == evtype.USRICK:
		#if an ick event respond to it
		print 'ick'
		con.sendIck()
	elif ev.type == evtype.USR10HZ:
		#on the 10Hz timer send ick and then run user code
		con.sendIck()
		driverCode.on10hz()
		print '10hz'
	elif ev.type == evtype.USR1HZ:
		#on the 1Hz timer run user code
		driverCode.on1hz()
		print '1hz'
	elif ev.type == evtype.USRDIGITAL:
		#on a digital reciever run user code passing the num and val
		driverCode.onDigital(ev.num, ev.val)
		print 'digital signal recieved'
	elif ev.type == evtype.USRANALOG:
		#on a analog reciever run user code passing the num and val
		driverCode.onAnalog(ev.num, ev.val)
		print 'analog signal recieved'
	elif ev.type == pygame.JOYBUTTONDOWN:
		#run user code to process the joystick events
		driverCode.onJoyButtonDown(ev.button)
	elif ev.type == pygame.JOYBUTTONUP:
		#run user code to process joystick events
		driverCode.onJoyButtonUp(ev.button)
		print 'joystick buttons'
	elif ev.type == pygame.JOYAXISMOTION:
		#run user code to process axis motion
		print ev.axis
		print ev.value
		driverCode.onJoyAxisMove(ev.axis, ev.value)
	else:
		print 'something Else'
