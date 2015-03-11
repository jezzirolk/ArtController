import sys
#for running the robot code off of the robot

#for init of the hardware system
def init():
	print 'doing some init stuff'

#for setting a PWM output
def setPwm(num, val):
	print 'PWM', num, val

#for setting a GPIO output
def setGpio(num, val):
	print 'GPIO', num, val

#for when the driver disconnects it sets things to a safe value
def onFail():
	print 'maikng shit safe on breaking'
