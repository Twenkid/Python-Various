# Client-Server Sockets example, spawning the processes automatically
# Author: Todor Arnaudov, 7.12.2020
import os

client = "t8.py"
server = "t7.py"
#spawnvp - uses PATH
#py = "python"
#for spawnv - full path

py = r"C:\Program Files\Python38\python.exe"

#p =  os.getcwd() + "\\"
p = py # + " " + server
print(p)
import time

def ClientServer():
  from subprocess import Popen
  pid1 = Popen([py, server]).pid
  time.sleep(1)
  pid2 = Popen([py, client]).pid
  exit(0)

def Sub():
  import subprocess
  subprocess.call([py, server], cwd=os.getcwd()) #Blocks, waits for return and the server waits for data
  time.sleep(1)
  subprocess.call([py, client], cwd=os.getcwd())	
  exit(0)
 
def StdInOut(): #doesn't work?
    print("StdInOut")
    from subprocess import Popen, PIPE, STDOUT
    try:
        #subprocess.call([p, server]) # ... more flexible -- tlsk[1] ... parameters 	
        pid1 = Popen([p, server], shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=False)
        print(pid)
        time.sleep(2)
        pid2 = Popen([p, client], shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=False)                                        
    except: pass                                 
      
ClientServer()

#StdInOut()

# https://docs.python.org/3/library/subprocess.html
#ids = os.spawnl(os.P_WAIT, p, server) #, os.environ)
#idc = os.spawnl(os.P_WAIT, p, client)# os.environ)						
# Not available on Windows:
#ids = os.spawnv(os.P_DETACH, p, [server, ' '])
#idc = os.spawnv(os.P_WAIT, p, [client, ' '])						
#ids = os.spawnve(os.P_DETACH, p, [server, ' '], os.environ)  
#idc = os.spawnve(os.P_WAIT, p, [client, ' '], os.environ)						

#os.system(p+server) # BLOCKS!
#os.system(p+client)