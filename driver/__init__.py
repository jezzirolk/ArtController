import socket
import sys
import time
from pygame import joystick

driver_ip = '192.168.1.101'
port = 1857
s = socket.socket()
robot_connection = (driver_ip, port)

joystick.init()

while 1:
    try:
        s.connect(robot_connection)
        print 'Robot connected'
        break
    except:
        print('Waiting for connection...')
        time.sleep(2)

while True:
    # Temporarily does basic PWM input for testing purposes
    num = input('Enter a PWM number: ')
    if num == 'cls':
        print 'Exiting...'
        break
    val = input('Enter a signal value: ')
    msg = 'pwm%d%05d' % (num, val)
    print "Sending", msg
    s.sendall(msg)

s.close()
