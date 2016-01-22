import sys,os
import hardware
	
class DriverCode(object):
	# If anyting needs to get send to the  side use either
	#	self.con.sendAnalog(int, float)
	#	self.con.sendDigital(int, Boolean)
	# These functions are not used internally and are for user use only.
	# The first arguement is which signal you are refering to
	# The second argument is the value of the specified signal
	# The analog and digital signals use a different set of numbers

	#anthing that needs to be done at the robot startup
	def __init__(self, c):
		self.con = c
		hardware.init()
		self.f1 = -1
		self.f2 = -1
		self.enter = -1
		self.toy1 = -1
		self.toy2 = -1
		self.toy3 = -1
		self.proxsense = -1
	#clocking timer actions
	def on10hz(self):
		fridge1 = hardware.getGpio(0)
		fridge2 = hardware.getGpio(3)
		pir = hardware.getGpio(4)
		toy1 = hardware.getGpio(5)
		toy2 = hardware.getGpio(6)
		toy3 = hardware.getGpio(8)
		prox = hardware.getAio(0)
		if fridge1 != self.f1:
			self.f1 = fridge1	
			print fridge1
		if fridge2 != self.f2:
			self.f2 = fridge2	
			print fridge2
		if pir != self.enter:
			self.enter = pir	
			print pir
		if toy1 != self.toy1:
			self.toy1 = toy1	
			print toy1
		if toy2 != self.toy2:
			self.toy2 = toy2
			print toy2
		if toy3 != self.toy3:
			self.toy3 = toy3	
			print toy3

	#clocking timer actions
	def on1hz(self):
		pass
			
	#on a recive of of a true false variable
	def onDigital(self, num, val):
		pass

	#on a revieve of a number float variable
	def onAnalog(self, num, val):
		pass

	#on a joystick button being pressed
	def onJoyButtonDown(self, num):
		pass

	#on a joystick axis moving
	def onJoyAxisMove(self, axis, val):
		pass
