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

	#clocking timer actions
	def on10hz(self):
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
			self.con.sendAnalog(4, 1.0)
			pass
		if num == 1:
			# B button, stop wheel
			self.con.sendAnalog(4, 0.0)
			pass
		if num == 2:
			# X button, spinback
			self.con.sendAnalog(4, -1.0)
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
		if axis == 2:
			if self.gearmode == 'low':
				self.con.sendAnalog(2, val/2)
			else:
				self.con.sendAnalog(2, val)
		elif axis == 5:
			if self.gearmode == 'low':
				self.con.sendAnalog(3, val/2)
			else:
				self.con.sendAnalog(3, val)
