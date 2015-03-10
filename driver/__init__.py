import socket
import sys
import time
import pygame
import string
import os
from sends import Connection
from timer import Timer
import evtype
#os.environ["SDL_VIDEODRIVER"] = 'dummy'
pygame.init()
pygame.display.init()
screen = pygame.display.set_mode([800,600])
pygame.fastevent.init()
js = pygame.joystick.Joystick(0)
js.init()

con = Connection()
t=Timer()
#joystick.init()
con.openConnection('localhost')
t.startTimer()
while True:
	pygame.fastevent.pump()
	ev = pygame.fastevent.poll()
	if ev.type == pygame.NOEVENT:
		print 'wait'
		time.sleep(.2)
	elif ev.type == evtype.USRICK:
		print 'ick'
		con.sendIck()
	elif ev.type == evtype.USR10HZ:
		print '10hz'
	elif ev.type == evtype.USR1HZ:
		print '1hz'
	elif ev.type == evtype.USRDIGITAL
		print 'digital signal recieved'
	elif ev.type == evtype.USRANALOG
		print 'analog signal recieved'`
	elif ev.type == pygame.JOYBUTTONDOWN:
		con.sendDigital(ev.button, True)
	elif ev.type == pygame.JOYBUTTONUP:
		con.sendDigital(ev.button, False)
		print 'joystick buttons'
	elif ev.type == pygame.JOYAXISMOTION:
		print ev.axis
		print ev.value
		con.sendAnalog(ev.axis,ev.value)
	elif ev.type == pygame.USEREVENT +5:
		print 'It Works!'
	else:
		print 'something Else'

	# Temporarily does basic PWM input for testing purposes
#	typ = raw_input('Enter a Command: ')
#	if typ == 'cls':
#		con.sendClose()
#		break
#	elif typ == 'dig':
#		#msg = sendDig()
#		print 'dig'
#	elif typ == 'ana':
#		con.sendAnalog(1, 128)
#	elif typ == 'ick':
#		#msg = sendIck()
#		print 'ick'
#	else:
#		print 'huh'
#
	#val = input('Enter a signal value: ')
    #nu = int(num)
    #msg = 'ana%d%05d' % (nu, val)
