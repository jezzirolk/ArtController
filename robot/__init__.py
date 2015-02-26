import socket
import Adafruit_BBIO.PWM as PWM
import sys

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
for st in pwm:
    PWM.start(st, 50)

# Handle Driver Input
while True:
    msg = connection.recv(3)
    
    if msg == 'drv':
        # Drive command was sent
        lval = float(connection.recv(5))
        rval = float(connection.recv(5))
        PWM.set_duty_cycle(pwm[ldrive], lval)
        PWM.set_duty_cycle(pwm[rdrive], rval)
        
    elif msg == 'pwm':
        # PWM signal command was sent
        num = int(connection.recv(1))
        val = float(connection.recv(5))
        print 'PWM', id, val
        PWM.set_duty_cycle(pwm[id], val)
        
    elif msg == 'cls':
        # Received the disconnect command
        print 'Driver disconnected, cleaning up...'
        connection.sendall('GG')
        break

# Clean up PWMs
PWM.cleanup()

# Clean up connection object
connection.close()

s.close()
