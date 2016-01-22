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
		self.gearPos = -1
		self.gearDeb = 0
		self.lampsw1 = -1
		self.lampsw2 = -1
		self.lampsw3 = -1
		self.lampsw4 = -1
		self.lampsw5 = -1
		self.lamprl1 = -1
		self.lamprl2 = -1
		self.lamprl3 = -1
		self.lamprl4 = -1
		self.lamprl5 = -1
		self.pirAway = -1
		self.turnA = -1
		self.turnB = -1
		self.ignition = -1
		self.wiper = -1
		self.radiopot1 = -1
		self.carGas = -1
		self.con = c

	#clocking timer actions
	def on10hz(self):
		Rsw11 = hardware.getGpio(0)
		Rsw12 = hardware.getGpio(3)
		Rsw21 = hardware.getGpio(1)
		Rsw22 = hardware.getGpio(2)
		Rpot1 = self.test(hardware.getAio(0))
		#Rpot2 = self.test(hardware.getAio(1))
		pir = hardware.getGpio(4)
		lsw1 = hardware.getGpio(5)
		lsw2 = hardware.getGpio(6)	
		lsw3 = hardware.getGpio(7)
		lsw4 = hardware.getGpio(8)
		lsw5 = hardware.getGpio(9)
		tura = hardware.getGpio(10)
		turb = hardware.getGpio(11)
		ignit = hardware.getGpio(12)
		wipe = hardware.getGpio(13)

		cargearpos = hardware.getAio(2)
		if (Rsw11 == 1) & (Rsw12 == 1) & (self.radioSw1 != 0):
			self.radioSw1 = 0
t
			print 'Radio SW1 - 0'
		elif (Rsw11 == 0) & (Rsw12 == 0) & (self.radioSw1 != 1):
			self.radioSw1 = 1
			print 'Radio SW1 - 1'
		elif (Rsw11 == 0) & (Rsw12 == 1) & (self.radioSw1 != 2):
			self.radioSw1 = 2
			print 'Radio SW1 - 2'
		if (Rsw21 == 1) & (Rsw22 == 0) & (self.radioSw2 != 0):
			self.radioSw2 = 0
			print 'Radio SW2 - 0'
		elif (Rsw21 == 0) & (Rsw22 == 1) & (self.radioSw2 != 1):
			self.radioSw2 = 1
			print 'Radio SW2 - 1'
		elif (Rsw21 == 0) & (Rsw22 == 0) & (self.radioSw2 != 2):
			self.radioSw2 = 2
			print 'Radio SW2 - 2'
		if Rpot1 != self.radioPot1:
			self.radioPot1 = Rpot1
			print 'Radio Pot 1 - %s' % (Rpot1)
		#if Rpot2 != self.radioPot2:
		#	self.radioPot2 = Rpot2
		#	print 'Radio Pot 2 - %s' % (Rpot2)
		if (cargearpos > (self.gearPos + .05)) or (cargearpos < (self.gearPos - .05)):
			self.gearPos = cargearpos
			print cargearpos
			if self.gearDeb < .1:
				self.gearDeb = 10
				print 'gearChanged'
		if self.gearDeb > 0:
			self.gearDeb = self.gearDeb - .1
		if pir != self.pirAway:
			self.pirAway = pir
			print "PIR"
		if lsw1:
			hardware.setGpio(0,1)
		else:
			hardware.setGpio(0,0)
		if lsw2:
			hardware.setGpio(1,1)
		else:
			hardware.setGpio(1,0)

	def test(self, test):
		if (test > 0) & (test < .1):
			return 0
		if (test > .1) & (test < .2):
			return 1
		if (test > .2) & (test < .3):
			return 2
		if (test > .3) & (test < .4):
			return 3
		if (test > .4) & (test < .5):
			return 4
		if (test > .5) & (test < .6):
			return 5
		if (test > .6) & (test < .7):
			return 6
		if (test > .7) & (test < .8):
			return 7
		if (test > .8) & (test < .9):
			return 8
		if (test > .9) & (test < 1):
			return 9


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
