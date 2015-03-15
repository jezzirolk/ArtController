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
con.openConnection('192.168.0.100')
#start the timer
t=Timer()
t.startTimer()
#run the user init code
dc = driverCode.DriverCode(con)
#queue processing loop
while True:
	#let the queue do what it needs
	pygame.fastevent.pump()
	#pull the next event
	ev = pygame.fastevent.poll()
	if ev.type == pygame.NOEVENT:
		#on an empty queue wait
		time.sleep(.2)
	elif ev.type == evtype.USRICK:
		#if an ick event respond to it
		pass
	elif ev.type == evtype.USR10HZ:
		#on the 10Hz timer send ick and then run user code
		con.sendIck()
		dc.on10hz()
	elif ev.type == evtype.USR1HZ:
		#on the 1Hz timer run user code
		dc.on1hz()
	elif ev.type == evtype.USRDIGITAL:
		#on a digital reciever run user code passing the num and val
		dc.onDigital(ev.num, ev.val)
	elif ev.type == evtype.USRANALOG:
		#on a analog reciever run user code passing the num and val
		dc.onAnalog(ev.num, ev.val)
	elif ev.type == pygame.JOYBUTTONDOWN:
		#run user code to process the joystick events
		dc.onJoyButtonDown(ev.button)
	elif ev.type == pygame.JOYBUTTONUP:
		#run user code to process joystick events
		dc.onJoyButtonUp(ev.button)
	elif ev.type == pygame.JOYAXISMOTION:
		#run user code to process axis motion
		print ev.axis
		print ev.value
#		axis = [0,0,0,0,0,0]
#		axis[ev.axis] = ev.value
#		evlist = pygame.fastevent.get(pygame.JOYAXISMOTION)
#		for ev in evlist:
#			axis[ev.axis] = ev.value
##		dc.onJoyAxisMove(0, axis[0])
#		dc.onJoyAxisMove(1, axis[1])
#		dc.onJoyAxisMove(2, axis[2])
#		dc.onJoyAxisMove(3, axis[3])
#		dc.onJoyAxisMove(4, axis[4])
		dc.onJoyAxisMove(ev.axis, ev.value)
	else:
		print 'something Else'
