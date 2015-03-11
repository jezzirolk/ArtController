import sys,os
import hardware
class RobotCode(object):
	# If anyting needs to get send to the Driver side use either
	#	self.con.sendAnalog(int, float)
	#	self.con.sendDigital(int, Boolean)
	# These functions are not used internally and are for user use only.
	# The first arguement is which signal you are refering to
	# The second argument is the value of the specified signal
	# The analog and digital signals use a different set of numbers

	# anything that needs to be done when the robot is started up
	def __init__(self,c):
		self.con = c

	#when an analog variable is recieved
	def onAnalog(self, num, val):
		hardware.setPwm(num, val)

	#when a digital variable is recieved
	def onDigital(self, num, val):
		pass

	#actions that happen at specific fequencies
	def on10hz(self):
		pass

	#actions that happen at specific freqencies
	def on1hz(self):
		pass
