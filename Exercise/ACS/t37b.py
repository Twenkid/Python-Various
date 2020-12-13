#t37.py
#6-5-2015
#Parse ACS logs
#Author: Todor Arnaudov

import os
import sys

#cnt = list.count(sys.argv); # count counts elements equal to something!!!
#sys.argv.__len__
cnt = len(sys.argv)
print(cnt)
prn = " "
curdir = os.curdir;

print("sys.argv:")
for s in sys.argv: prn = prn + s + "\n"

path = " "
#if cnt > 0:  
if cnt > 0:  path = sys.argv[1]
 

#print(sys.argv[0], sys.argv[1]) #, argv[2])
print(prn)
print(curdir)
print(os.defpath)
cwd = os.getcwd()
print(cwd)		#ok


#list1 = os.listdir()
list1 = os.listdir(path)

#print(list1)

list2 = []

#clip-...
for s in list1: 
  #if s.find('clip-') > 0: list2.append(s)
  if s.find('clip') >= 0: list2.append(s)

for s in list2: print(s)

os.chdir(path)

#f = open(list2[0])
#lines = f.readlines(105)
#f.close()

import codecs
f = codecs.open(list2[0], "r", "utf-8")
list3 = f.readlines(105)
f.close()

f = codecs.open(list2[0], "r", "utf-8")
data1 = f.read() #all

#for i in range(1, 100): print(list3[i])  #ok

list4 = data1.split("<#>")

print(str(len(list4) - 2) + "data items in " + path + os.sep + list2[0])
print("Average size: ")
print(os.path.getsize(list2[0]) / len(list4))

f.close()

print("Number of files: " + str(len(list4)))

import math

#before 11/2013 or ? -- there's no <#> for a delimiter, just the time/date!
#after ... there's a list of HWND, title ... -- exclude the last item from max
#number of items is ... - 2 ==> because  first two delimiters ... str(len(list5) - 2)
for s in list2:
  f = codecs.open(s, "r", "utf-8")
  data2 = f.read() #all
  list5 = data2.split("<#>")
  max = 0
  last = len(list5)
  #for k in list5: 
    #if (len(k) > max): max = len(k)  
  for k in range(0, last-1):
    if (len(list5[k]) > max): max = len(list5[k])
  prn2 = str(len(list5) - 2) + "\t\t" + s + "\t\t" + str(math.floor(os.path.getsize(s) / len(list5))) + "\t\t" + str(max);
  print(prn2)
  










