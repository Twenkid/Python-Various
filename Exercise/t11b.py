#t11.py
#python 3.3 print('...')
#2-6-2014, 9:00 AM
#see t15.py

#indent: space

import sys

#I want: to print without new line
#test 1. from O'reilly
print('aaaaa',)
print('bbbbb',)
#didn't work

#test 2. from  http://codingrecipes.com/print-without-a-new-line-or-space-in-python
sys.stdout.write("xxx")
sys.stdout.write("iii")
#OK!

import os, os.path#, urllib#, urllib2
import shutil, tempfile, fileinput
import struct
#import cgi
import urllib#, urlparse

ref = []
ref.append(dir(os))
ref.append(dir(os.path))
ref.append(dir(shutil))
ref.append(dir(tempfile))
ref.append(dir(fileinput))
ref.append(dir(struct))
#ref.append(dir(urllib2))
#ref.append(dir(urlparse))

#ref.append(dir(urllib))
#ref.append(dir(urllib2))

for s in ref:
  print('\n\n===================\n')
  for s1 in s:
    print(s1)
		
for s in dir(os):
  #for s1 in s:
    #print(s1 + '\n\n' + help()+ '\n\n')
    s2 = ''
    print('\n\n' + 'os.' + s + '.__doc__'  + '\n\n') # + ')' + '\n\n')
    exec('s2 = os.' + s + '.__doc__')# + ')')
    print(s2)
	#exec('doc(' + 'os.' + s + ')')
	
for s in dir(os.path):
  #for s1 in s:
    #print(s1 + '\n\n' + help()+ '\n\n')
    s2 = ''
    print('\n\n' + 'os.path.' + s + '.__doc__'  + '\n\n') # + ')' + '\n\n')
    exec('s2 = os.path.' + s + '.__doc__')# + ')')
    print(s2)
	
import urllib.request, urllib.parse, urllib.error

for s in dir(urllib.request):
    s2 = ''
    print('\n\n' + 'urllib.request.' + s + '.__doc__'  + '\n\n') # + ')' + '\n\n')
    exec('s2 = urllib.request.' + s + '.__doc__')# + ')')
    print(s2)
	
for s in dir(urllib.parse):
    s2 = ''
    print('\n\n' + 'urllib.parse.' + s + '.__doc__'  + '\n\n') # + ')' + '\n\n')
    exec('s2 = urllib.parse.' + s + '.__doc__')# + ')')
    print(s2)
	
for s in dir(urllib.error):
    s2 = ''
    print('\n\n' + 'urllib.error.' + s + '.__doc__'  + '\n\n') # + ')' + '\n\n')
    exec('s2 = urllib.error.' + s + '.__doc__')# + ')')
    print(s2)

	
#NO --- this takes the first char of the ident!
	
  
#def PrintDoc(moduleName):   
 #scode = 'for s in dir(' + moduleName + '):'
  ####scode = scode + '\n'
  ####scode = scode + 's2 = \'\''
  ####scode += '\n  s2 = ' + moduleName + '.' + s + '.__doc__' + '\n' #' + s + '.__doc__' 
 # scode += '\n  s2 = ' + moduleName + '.' + 'eval(s)' + '.__doc__' + '\n' #' + s + '.__doc__' 
  ####scode = scode + '\n'
 # scode += "\n  print(s2)"
 # print(scode)  
 # exec(scode)
  
 
  #for s in dir(moduleId): #moduleName):  
   # s2 = ''
    #print('\n\n' + moduleName + '.' + s + '.__doc__'  + '\n\n') # + ')' + '\n\n')
    #exec('s2 = ' + moduleName +'.' + s + '.__doc__') # + ')')
    #print(s2)	
  
#PrintDoc(os.path, 'os.path')
#PrintDoc(sys, 'sys')
#PrintDoc('os.path')
#PrintDoc('os')


#Continue -- problems with one solid exec ... more granularity... later  #10:00


#10:06
#Copy files etc.

import shutil

for s in dir(shutil):
    s2 = ''
    print('\n\n' + 'shutil.' + s + '.__doc__'  + '\n\n') # + ')' + '\n\n')
    exec('s2 = shutil.' + s + '.__doc__')# + ')')
    print(s2)

path = 'R:'
print('Usage of Path')
gb = 2**30
try:
  u1 = list(shutil.disk_usage('R:'))
  umb = []
  ugb = []
  for x in u1: umb.append(x/1048576)  #better, lambdas, check in MB
  for x in u1: ugb.append(x/gb)  #better, lambdas, check in MB
  print(umb)
  print(ugb)
except: pass

#indent: tab

def DrivesUsage(path='C:'):
	#path = 'R:'
	print('Usage of [' + path + ']')
	gb = 2**30
	u1 = list(shutil.disk_usage(path))
	umb = []
	ugb = []
	for x in u1: umb.append(x/1048576)  #better, lambdas, check in MB
	for x in u1: ugb.append(x/gb)  #better, lambdas, check in MB
	print(umb)
	print(ugb)

try:
  DrivesUsage('R:')
except: pass
try:
  DrivesUsage('C:')
except: pass
try:
  DrivesUsage('S:')
except: pass

import base64

#import mimetypes, mimetools, multifile, binascii, mailboc, mail
#no module htmllib
#import xml.parsers.expat, xml.dom, xml.dom.minidom, ...



