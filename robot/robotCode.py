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
	def __init__(self,c):
		self.con1 = c
		self.osc = OSC.OSCClient()
		self.osc.connect(('192.168.1.150',53000 ))
		self.radioOn = -1

	#when an analog variable is recieved
	def onAnalog(self, num, val):
		pass

	#when a digital variable is recieved
	def onDigital(self, num, val):
		print num
		if num == 1:
			if val == 0:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/1/start")
				self.osc.send(oscmsg)
			if val == 1:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/1.5/start")
				self.osc.send(oscmsg)
			print val
		if num == 2:
			if val == 1:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/3/start")
				self.osc.send(oscmsg)
			if val == 0:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/3.5/start")
				self.osc.send(oscmsg)
			print val
		if num == 15:
			if val == 1:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/22/start")
				self.osc.send(oscmsg)
		if num == 16:
			if val == 1:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/23/start")
				self.osc.send(oscmsg)
		if num == 17:
			if val == 1:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/24/start")
				self.osc.send(oscmsg)
		if num == 10:
			if val == 0:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/4/start")
				self.osc.send(oscmsg)
			if val == 1:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/5/start")
				self.osc.send(oscmsg)
		if num == 11:
			if val == 1:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/9/start")
				self.osc.send(oscmsg)
			if val == 0:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/9.5/start")
				self.osc.send(oscmsg)
		if num == 20:
			if val == 1:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/6/start")
				self.osc.send(oscmsg)
		if num == 21:
			if val == 1:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/10/start")
				self.osc.send(oscmsg)
		if num == 22:
			if val == 0:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/11/start")
				self.osc.send(oscmsg)
		if num == 4:
			if val == 1:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/19/start")
				self.osc.send(oscmsg)
		if num == 5:
			if val == 1:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/20/start")
				self.osc.send(oscmsg)
		if num == 6:
			if val == 1:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/49/start")
				self.osc.send(oscmsg)
		if num == 7:
			if val == 1:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/21/start")
				self.osc.send(oscmsg)
		if num == 8:
			if val == 1:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/17/start")
				self.osc.send(oscmsg)
		if num == 11:
			if val == 0:
				self.radioOn = 0
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/13.5/start")
				self.osc.send(oscmsg)
			if val == 1:
				self.radioOn = 1
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/12/start")
				self.osc.send(oscmsg)
		if num == 12:
			if val == 1 and self.radioOn == 1:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/13/start")
				self.osc.send(oscmsg)





	#actions that happen at specific fequencies
	def on10hz(self):
		pass

	#actions that happen at specific freqencies
	def on1hz(self):
		pass
