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
		self.position = -1
		self.con = c

	#clocking timer actions
	def on10hz(self):
		test = hardware.getAio(0)
		if (test < .25) & (self.position != 0):
			self.position = 0
			self.con.sendDigital(2,0)
		elif (test > .25) & (test < .5) & (self.position != 1):
			self.position = 1
			self.con.sendDigital(2,1)
		elif (test > .5) & (test < .75) & (self.position != 2):
			self.position = 2
			self.con.sendDigital(2,2)
		elif (test > .75) & (self.position != 3):
			self.position = 3
			self.con.sendDigital(2,3)
		
		print test

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
