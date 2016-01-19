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

	#clocking timer actions
	def on10hz(self):
        pass

	#clocking timer actions
	def on1hz(self):
	    test = hardware.getGpio(0)
        print test
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
