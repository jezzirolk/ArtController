import socket

s = socket.socket()
host = socket.gethostname()
port = 1857
s.bind((host, port))

s.connect((host, port))
print(s.recv(1024))
s.close()