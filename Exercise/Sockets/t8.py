#t8.py
#https://docs.python.org/release/2.5.2/lib/socket-example.html
#+ Edits: Todor Arnaudov
# Echo client program
import socket

print("***CLIENT***")
HOST = 'localhost'    # The remote host
PORT = 50007          # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
#s.send('Hello, world')
s.send(bytes('Hello, world', 'utf-8'))
data = s.recv(1024)
s.close()
print('Received', repr(data))
