import sys
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time
pwmarray = ["P9_14","P9_21", "P9_42"]
GPIOinArray = ["P9_12"]
GPIOoutArray = []
AINarray = []
def init():
 	#for starter in pwmarray:
	#	print starter
	#	PWM.start(starter,15,100,0)
	for starter in GPIOinArray:
		print starter
		GPIO.setup(starter, GPIO.IN)
	for starter in GPIOoutArray:
		print starter
		GPIO.setup(starter, GPIO.OUT)
	ADC.setup()	
	
def setPwm(num, val):
	#val = val*5+15
	#if val >14 and val <16:
	#	val = 15
	#PWM.set_duty_cycle(pwmarray[num], val)
    pass

def setGpio(num, val):
	if val == 0:
		GPIO.output(GPIOoutArray[num],GPIO.LOW)
	else:
		GPIO.output(GPIOoutArrau[num],GPIO.HIGH)

def getGpio(num):
	return GPIO.input(GPIOinArray[num])

def getAio(num)
	return ADC.read(AINarray[num])

def onFail():
	for failz in pwmarray:
		PWM.set_duty_cycle(failz, 15)
