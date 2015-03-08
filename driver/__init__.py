import socket
import sys
import time
import pygame
import string
import os
from sends import Connection
from timer import Timer
USRICK = pygame.USEREVENT
USR10HZ = pygame.USEREVENT + 1
USR1HZ = pygame.USEREVENT + 2
os.environ["SDL_VIDEODRIVER"] = 'dummy'
pygame.init()
pygame.display.init()
screen = pygame.display.set_mode([1,1])
pygame.fastevent.init()

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
	elif ev.type == USRICK:
		print 'ick'
		con.sendIck()
	elif ev.type == USR10HZ:
		print '10hz'
	elif ev.type == USR1HZ:
		print '1hz'
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
