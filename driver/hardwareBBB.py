import sys
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time
#pwmarray = ["P9_14","P9_21", "P9_42"]
GPIOinArray = ["P9_12","P9_14","P9_16","P9_15","P9_21","P9_23","P9_27","P9_30","P9_41","P9_42","P8_15","P8_16","P8_17","P8_18","P9_22","P8_26","P8_12","P8_14","P8_13","P8_19"]
GPIOoutArray = ["P8_7","P8_8","P8_9","P8_10","P8_11",]
AINarray = ["AIN0","AIN1","AIN2","AIN3","AIN4"]
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
		GPIO.output(GPIOoutArray[num],GPIO.HIGH)

def getGpio(num):
	return GPIO.input(GPIOinArray[num])

def getAio(num):
	return ADC.read(AINarray[num])

def onFail():
	#for failz in pwmarray:
	#	PWM.set_duty_cycle(failz, 15)
	pass
