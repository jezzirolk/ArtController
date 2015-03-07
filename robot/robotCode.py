import sys
import hardwareDummy as hardware

def onAnalog(num, val):
	hardware.setPwm(num, val)

def onDigital(num, val):
	hardware.setGpio(num, val)
