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
import robotCode
import hardware
#makes it so no screen opens
os.environ["SDL_VIDEODRIVER"] = 'dummy'
#init the pygame and display setup
pygame.init()
pygame.display.init()
screen = pygame.display.set_mode([1,1])
#init the queue
pygame.fastevent.init()
#init the joystick
#js = pygame.joystick.Joystick(0)
#js.init()
#start the connection
hardware.init()
con1 = Connection()
con2 = Connection()
con1.openListenPort(2000)
con2.openListenPort(2001)
#start the timer
t=Timer()
t.startTimer()
#run the user init code
rc = robotCode.RobotCode(con1,con2)
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
		rc.on10hz()
	elif ev.type == evtype.USR1HZ:
		#on the 1Hz timer run user code
		rc.on1hz()
	elif ev.type == evtype.USRDIGITAL:
		#on a digital reciever run user code passing the num and val
		rc.onDigital(ev.num, ev.val)
	elif ev.type == evtype.USRANALOG:
		#on a analog reciever run user code passing the num and val
		rc.onAnalog(ev.num, ev.val)
	else:
		print 'something Else'
