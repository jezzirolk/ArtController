import socket
import sys
import time

driver_ip = socket.gethostname()
port = 1857
s = socket.socket()
robot_connection = (driver_ip, port)

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
    val = input('Enter a signal value: ')
    msg = 'pwm%d%5d' % (num, val)
    print("Sending %s", msg)
    s.sendall(msg)

s.close()
