import sys,os
	
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
		self.gearmode = 'low'
		self.axis0 = 0.0
		self.axis1 = 0.0
		self.axis2 = 0.0
	#clocking timer actions
	def on10hz(self):
		#self.con.sendAnalog(0, self.axis0)
		#self.con.sendAnalog(1, self.axis1)
		#self.con.sendAnalog(2, self.axis2)
		pass

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
		if num == 0:
			# A button, spinup
			print 'spinup'
			self.con.sendAnalog(2,  1.0)
			pass
		if num == 1:
			# B button, stop wheel
			print 'off'
			self.con.sendAnalog(2,  0.0)
			pass
		if num == 2:
			# X button, spinbacka
			print 'spinback'
			self.con.sendAnalog(2, -1.0)
			pass
		if num == 5:
			# R bump, switch speed modes
			if self.gearmode == 'low':
				self.gearmode = 'high'
			else:
				self.gearmode = 'low'
		pass

	#on a joystick button being released
	def onJoyButtonUp(self, num):
		pass

	#on a joystick axis moving
	def onJoyAxisMove(self, axis, val):
		#tank Drive
		if axis == 4:
			if self.gearmode == 'low':
				self.con.sendAnalog(0, val/4)
			else:
				self.con.sendAnalog(0, val/2)
		elif axis == 1:
			if self.gearmode == 'low':
				self.con.sendAnalog(1, -val/4)
			else:
				self.con.sendAnalog(1, -val/2)
