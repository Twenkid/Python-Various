#t82.py
#Call sessions
#ObObr ... start!
#Todor Arnaudov
#14-4-2016

import os, sys
import subprocess
import time


pmt = {}

class Sessions():
  
  def __init__(self,path=None):
    if (path!=None):  self.path = path
    else:  self.path = os.getcwd()
    print(self.path)
    addr = ["c:\\windows\\system32\\", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    volya = ["cmd", "dir"]
    volya_nagled = {}
	
  def open(this, what):
    #subprocess.call([r"C:\Incept\FusenReceiver2\ffmpeg\fb1.bat", " "], cwd="C:\\Incept\\FusenReceiver2\\ffmpeg\\")
						#time.sleep(tPause)
    p1 = addr[0]+volya[0]
    from subprocess import Popen, PIPE, STDOUT	
    try:
		####subprocess.call([п1, tlsk[1], tlsk[2]]) # ... more flexible -- tlsk[1] ... parameters 	
		#cmd = 'ls /etc/fstab /etc/non-existent-file'		
        p = Popen(p1, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=False)
        print("Popen(" + p1 + "...") # + str(p))
        print('======== STDOUT =========')
        for line in p.stdout:
          line = line.rstrip()			
			#s = line.decode(encoding='utf-8')#str(line)
          p5 = line.decode(encoding='windows-1251')#str(line)
			#print(p.stdout.decode('utf-8'))
          print(p5)
          p4 = p4 + p5 + "\n"
			#в6([line,'utf-8'])
          volya_nagled[p1] = p4	#натрупва всички редове, ако има
    except:
            import sys
            print('?Тт = н')
            print(sys.exc_info())
    print('?Тт = д')	#must capture the stdio ... get the output of the process...
	
def redirectStdout():
  from subprocess import Popen, PIPE, STDOUT
  s = 'dir'
  inp = s.encode('windows-1251')
  p = Popen(['c:/windows/system32/cmd.exe'], stdout=PIPE, stdin=PIPE, stderr=PIPE)  
  #p = Popen(['c:/windows/system32/systeminfo.exe'], stdout=STDOUT, stdin=PIPE, stderr=PIPE)  
  
  while p.poll() is None:          # check if the process is still alive
    out = p.stdout.readline()    # if it is still alive, grab the output
	
  #opens and it disappears?
  #doesn't show output and for systeminfo

    
  #for line in p.stdout: print(line)
  #stdout_data = p.communicate(input=inp)[0]	
  #print(str(stdout_data))
  #for line in p.stdout: print(line)
  
  #rd = p.stdout.read()
  # print(rd)
    
	
#open()

  
def obobr(nagled):
  import numpy
  data = []
  will = ["sum(b)", "numpy.average(b)"]
  nagled_volya = {}
  
  #b = bytes(nagled)  #should be bytearray - otherways sum doesn't work
  b = bytearray(nagled)
  print(b[0:100])
  #b2 = 
  data.append(sum(b))
  data.append( numpy.average(b))

  print(nagled)  
  print(str(len(b)) + " bytes")
  i = 0
  for w,d in will, data: print(str(w) + " : " + str(data[i])); i=i+1

  
def obobr16(nagled):
  import numpy
  from array import *
  data = []
  will = ["sum(b)", "numpy.average(b)"]
  nagled_volya = {}
  
  print(nagled)
 # bt = bytearray(nagled)  #should be bytearray - otherways sum doesn't work
  sh = array('i', nagled) #bt) #nagled)
  print(sh)
  #b = numpy.int16(nagled[44:])
  #b = numpy.array(bt[44:], dtype=numpy.int16)
  
  #b = numpy.array(bt, dtype=numpy.int16)
  b = numpy.array(sh, dtype=numpy.int16)
  s = " "
  #for i in range(0,99): s = s + str(b) + ", "
  for i in b: print(str(i))
  print(str(s))
  
 # print(b[0:100])
  #b2 = 
  data.append(numpy.sum(b))
  data.append(numpy.average(b))

  print(nagled)  
  print(str(len(b)) + " bytes")
  i = 0
  for w,d in will, data: print(str(w) + " : " + str(data[i])); i=i+1
  
def openwav(path, name=None):
  import array
  
  print(path); print(name);
  if (name!=None): fullpath = path + "\\" + name; print(fullpath);
  else: fullpath = path
  
  print(dir(open))
 # f = open("b:\\tor\\1.wav", "rb") #name, 'rb')   
  #f = open(name, "rb")
#  f = open(name, 'rb')
  f = open(fullpath, 'r')
  raw = array.array('i')
  raw = f.read()
  f.close()
  print(raw[0:100])
  return raw
  
def read_data(mode='d', path=None): #d = dir, f = file
  raw = None
  if (mode=='d'):
    if (path==None): r = os.getcwd() 
    else: r = path
  else: r = path	#mode = f
  
  if (mode == 'd'):
    pmt['os.getcwd()'] = r
    pmt['os.listdir()'] = os.listdir(r)
    keys = pmt['os.listdir()']
    print(pmt) 
    for n in keys:
      if (n.endswith('wav')): raw = openwav(path, n); break #the first file; path is directory, n is name of file
  else:  raw = openwav(path, None);	#mode = f, path is fullpath  
  return raw
  
def test():
  #print("arg: f ""path to dir with wav""")
  print("arg: f ""path to wav-file""")
  if (len(sys.argv)>1):
    if (sys.argv[1]=='f'): raw = read_data('f', sys.argv[2])  
    else: raw = read_data('d', sys.argv[2])
  else: raw = read_data('d')
  
  obobr(raw)
  obobr16(raw)

if __name__ == '__main__':	  
  test()
  