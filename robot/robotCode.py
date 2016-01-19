import sys,os
import hardware
import OSC
class RobotCode(object):
	# If anyting needs to get send to the Driver side use either
	#	self.con.sendAnalog(int, float)
	#	self.con.sendDigital(int, Boolean)
	# These functions are not used internally and are for user use only.
	# The first arguement is which signal you are refering to
	# The second argument is the value of the specified signal
	# The analog and digital signals use a different set of numbers

	# anything that needs to be done when the robot is started up
	def __init__(self,c,d):
		self.con1 = c
		self.con2 = d
		self.osc = OSC.OSCClient()
		self.osc.connect(('127.0.0.1',53000 ))

	#when an analog variable is recieved
	def onAnalog(self, num, val):
		pass

	#when a digital variable is recieved
	def onDigital(self, num, val):
		if num == 1:
			if val == 1:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/test")
				oscmsg.append('1')
				self.osc.send(oscmsg)
			print val
		pass

	#actions that happen at specific fequencies
	def on10hz(self):
		pass

	#actions that happen at specific freqencies
	def on1hz(self):
		pass
