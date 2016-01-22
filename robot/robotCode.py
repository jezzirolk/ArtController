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
		self.radioVol = -57
		self.lamp1 = -1
		self.lamp2 = -1
		self.lamp3 = -1
		self.lamp4 = -1
		self.toy1 = -1
		self.carGas = -1
		self.ignition = -1
		self.fridgeOpen = -1
		self.popaDeb = 0
		self.thunderDeb = 0
		self.bassDeb = 0
		self.ratsDeb = 0
		self.missleDeb = 0

	#when an analog variable is recieved
	def onAnalog(self, num, val):
		pass

	#when a digital variable is recieved
	def onDigital(self, num, val):
		print num
		if num == 1:
			if val == 0:
				self.fridgeOpen = 1
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/1/start")
				self.osc.send(oscmsg)
			if val == 1:
				self.fridgeOpen = 0
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
			self.toy1 = val
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
			self.ignition = val
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
			self.carGas = val
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
			self.lamp1 = val
			if val == 1:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/19/start")
				self.osc.send(oscmsg)
		if num == 5:
			self.lamp2 = val
			if val == 1:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/20/start")
				self.osc.send(oscmsg)
		if num == 6:
			self.lamp3 = val
			if val == 1:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/49/start")
				self.osc.send(oscmsg)
		if num == 7:
			self.lamp4 = val
			if val == 1:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/21/start")
				self.osc.send(oscmsg)
		if num == 8:
			if val == 1:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/17/start")
				self.osc.send(oscmsg)
		if num == 12:
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
		if num == 13:
			if val == 1 and self.radioOn == 1:
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress("/cue/13/start")
				self.osc.send(oscmsg)
		if num == 18:
			print val
			if val == 0:
				self.vol = -45
			if val == 1:
				self.vol = -39.5
			if val == 2:
				self.vol = -34
			if val == 3:
				self.vol = -28.5
			if val == 4:
				self.vol = -23
			if val == 5:
				self.vol = -17.5
			if val == 6:
				self.vol = -12
			if val == 7:
				self.vol = -5.5
			if val == 8:
				self.vol = -1
			if val == 9:
				self.vol = 4.5
			stations = ["100","101","102","103","104","105","106","107","108","109","110","111","112","113","114","115","116","117","118"]
			for current in stations:
				command = "/cue/%s/sliderLevel/0" % current
				print command
				print self.vol
				oscmsg = OSC.OSCMessage()
				oscmsg.setAddress(command)
				oscmsg.append(self.vol)
				self.osc.send(oscmsg)

		#	if val == 1 and self.radioOn == 1:
		#		oscmsg = OSC.OSCMessage()
		#		oscmsg.setAddress("/cue/13/start")
		#		self.osc.send(oscmsg)
		if (self.lamp2 == 1) and (self.ignition == 0) and (self.popaDeb < .1):
			self.popaDeb = 60
			oscmsg = OSC.OSCMessage()
			oscmsg.setAddress("/cue/33/start")
			self.osc.send(oscmsg)
		if (self.fridgeOpen == 1) and (self.ignition == 0) and (self.radioOn == 1) and (self.thunderDeb < .1):
			self.popaDeb = 300
			oscmsg = OSC.OSCMessage()
			oscmsg.setAddress("/cue/34/start")
			self.osc.send(oscmsg)
		if (self.fridgeOpen == 1) and (self.lamp3 == 1) and (self.radioOn == 1) and (num == 20) and (self.bassDeb < .1):
			self.BassDeb = 600
			oscmsg = OSC.OSCMessage()
			oscmsg.setAddress("/cue/36/start")
			self.osc.send(oscmsg)
		if (self.lamp1 == 1) and (self.lamp3 == 1) and (num == 15) and (self.ratsDeb < .1):
			self.BassDeb = 300
			oscmsg = OSC.OSCMessage()
			oscmsg.setAddress("/cue/16/start")
			self.osc.send(oscmsg)
		if (self.lamp4 == 1) and (self.radioOn == 1) and (self.toy1 == 1) and (self.carGas == 1) and (self.fridgeOpen == 1) and (self.missleDeb < .1):
			self.missleDeb = 1200
			oscmsg = OSC.OSCMessage()
			oscmsg.setAddress("/cue/37/start")
			self.osc.send(oscmsg)
	
		


	#actions that happen at specific fequencies
	def on1hz(self):
		if self.popaDeb > 0:
			self.popaDeb = self.popaDeb - 1
		if self.thunderDeb > 0:
			self.thunderDeb = self.thunderDeb - 1
		if self.bassDeb > 0:
			self.bassDeb = self.bassDeb - 1
		if self.ratsDeb > 0:
			self.ratsDeb = self.ratsDeb - 1
		if self.missleDeb > 0:
			self.missleDeb = self.missleDeb - 1


	#actions that happen at specific freqencies
	def on10hz(self):
		pass
