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

# Setup data socket
s = socket.socket()
driver_address = (socket.gethostname(), 1857)  # Change from localhost eventually
s.bind(driver_address)
s.listen(1)

while True:
    try:
        print 'Waiting for Driver connection...'
        connection, client_address = s.accept()
        print 'Got a connection from', client_address
        
        # Start PWM values at pseudo-zero
        for st in pwm:
            PWM.start(st, 50)
        
        # Handle Driver Input
        while True:
            msg = connection.recv(3)
            
            if msg == 'drv':
                # Drive command was sent
                PWM.set_duty_cycle(pwm[ldrive], float(connection.recv(5)))
                PWM.set_duty_cycle(pwm[rdrive], float(connection.recv(5)))
                
            elif msg == 'pwm':
                # PWM signal command was sent
                PWM.set_duty_cycle(pwm[connection.recv(1)], float(connection.recv(5)))
                
            elif msg == 'cls':
                # Received the disconnect command
                print 'Driver disconnected, cleaning up...'
                connection.sendall('GG')
                break
            
    finally:
        # Stop PWM signals and clean up
        for st in pwm:
            PWM.stop(st)
        PWM.cleanup()
        
        # Clean up connection object
        connection.close()
s.close()
