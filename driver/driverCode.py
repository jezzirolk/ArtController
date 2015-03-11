import sys

def onInit():
	print 'init'

def on10hz():
	print '10hz'

def on1hz():
	print '1hz'

def onDigital(num, val):
	print '%d%d' % (num, val)

def onAnalog(num, val):
	print '%d%d' % (num, val)

def onJoyButtonDown(num):
	print 'button down'

def onJoyButtonUp(num):
	print 'button up'

def onJoyAxisMove(axis, val):
	print 'axis move'
