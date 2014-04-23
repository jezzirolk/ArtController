import sys
import Adafruit_BBIO.PWM as PWM
import time
pwmarray = ["P9_14","P9_16","P9_21", "P9_22"]
def initHardware():
	PWM.start("P9_16",15,100,0)
	PWM.start("P9_21",15,100,0)

def setPwm(num, val):
	val = val*5+15
	if val >14 and val <16:
		val = 15
	PWM.set_duty_cycle(pwmarray[num], val)

def setGpio(num, val):
	print 'GPIO stuff'

def onFail():
	for failz in pwmarray
		PWM.set_duty_cycle(pwmarray[failz], val)
