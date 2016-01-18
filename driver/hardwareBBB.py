import sys
import Adafruit_BBIO.PWM as PWM
import time
pwmarray = ["P9_14","P9_21", "P9_42"]
def init():
 	for starter in pwmarray:
		print starter
		PWM.start(starter,15,100,0)

def setPwm(num, val):
	val = val*5+15
	if val >14 and val <16:
		val = 15
	PWM.set_duty_cycle(pwmarray[num], val)

def setGpio(num, val):
	print 'GPIO stuff'

def onFail():
	for failz in pwmarray:
		PWM.set_duty_cycle(failz, 15)
