#t7.py
# SERVER from Socket client-server exchange
# Sample from somewhere + edit: Todor
#s = socket()
#import socket
#h = gethostname()
#print(h)

# Echo server program
import time
import socket
#import keyboard #requires root in Linux also it is a third-party lib
#import msvcrt #Windows

h = socket.gethostname()
print(h)

HOST = ''                 # Symbolic name meaning the local host
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ('### Server Connected by ###', addr)
while 1:
    data = conn.recv(1024)
    #print("Waits?")
    if not data: break
    print(data)
    conn.send(data)
           
conn.close()
