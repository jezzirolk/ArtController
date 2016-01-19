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
		hardware.init()
		self.radioSw1 = -1
		self.radioSw2 = -1
		self.radioPot1 = -1
		self.radioPot2 = -1
		self.con = c

	#clocking timer actions
	def on10hz(self):
		Rsw11 = hardware.getGpio(0)
		Rsw12 = hardware.getGpio(1)
		Rsw13 = hardware.getGpio(2)
		if (Rsw11 == 1) & (Rsw12 == 1) & (Rsw13 == 0) & (self.radioSw1 != 0):
			self.radioSw1 = 0
			print 0
		elif (Rsw11 == 0) & (Rsw12 == 1) & (Rsw13 == 0) & (self.radioSw1 != 1):
			self.radioSw1 = 1
			print 1
		elif (Rsw11 == 0) & (Rsw12 == 0) & (Rsw13 == 0) & (self.radioSw1 != 2):
			self.radioSw1 = 2
			print 2

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
