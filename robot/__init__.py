import socket
#import Adafruit_BBIO.PWM as PWM
import sys
import robotCode
import cPickle

# Set IO values for future use
# TODO: GPIO, I2C, UART
pwm = ["P9_14", "P9_16", "P9_21", "P9_22", "P9_42", "P8_13", "P8_19"]
ain = ["P9_33", "P9_35", "P9_36", "P9_37", "P9_38", "P9_39", "P9_40"]
packetLoss = 5  # Optimizing 

ldrive = 0
rdrive = 1

host = ''
port = 1857

# Setup data socket
s = socket.socket()
s.bind((host, port))
print 'Bound at port', port
s.listen(1)

connection, client_address = s.accept()
print 'Connected to', client_address

# Start PWM values at pseudo-zero
#for st in pwm:
#    PWM.start(st, 50)

# Handle Driver Input
while True:
	msg = connection.recv(3)
	if msg == 'dig':
		#if it is a digital message
		leng = int(connection.recv(5))
		msg = connection.recv(leng)
		data = cPickle.loads(msg)
		robotCode.onDigital(data[0], data[1])
	elif msg == 'ana':
		#if it is an analog message
		leng = int(connection.recv(5))
		msg = connection.recv(leng)
		data = cPickle.loads(msg)
		robotCode.onAnalog(data[0], data[1])
        
	elif msg == 'cls':
        # Received the disconnect command
		print 'Driver disconnected, cleaning up...'
		connection.sendall('GG')
		break
	elif msg == 'ick':
		connection.sendall('ack')
		print 'ick, Ack'
	elif msg == '':
		print 'its dead jim'	
		break
	else:
		print msg
		print 'was sent'
	

# Clean up PWMs
#PWM.cleanup()

# Clean up connection object
connection.close()

s.close()
