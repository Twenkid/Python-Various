#t9.py
#28-5-2014
# OS functions, file sizes, exec, walk directory (not recursive, see also t9_3b)
import os
import os.path
import sys

out = []

def callit(func, param, num):
	#if num==1: exec('import os; import os.path; os.' + func + '(' + '\'' + param + '\'' +')')	
	#if num==0: exec('import os; import os.path; os.' + func + '()')	
	if num==1: exec('import os; import os.path; out.append(' + 'os.' + func + '(' + '\'' + param + '\'' +')' + ')')	
	if num==0: exec('import os;import os.path; out.append(' + 'os.' + func + '()'  + ')')

ssa = ['getcwd', 'listdir', 'system']
#ssb = ['', 'S:\\code', 'pause']
ssb = ['', 'D:\\code', 'pause']
ssc = [0, 1, 1]
i = 0
#for s1,s2 in ssa, ssb: callit(s1, s2)

def testfunc():
		i = 0
	#try:
		for s1 in ssa: callit(s1, ssb[i], ssc[i]); i=i+1		
	#except: pass
	
	
testfunc()
for s2 in out: print(s2)

print(dir(os.path))

print(os.path.getsize("t9.py"))
print(os.path.getmtime("t9.py"))
print(os.path.getctime("t9.py"))

import time

tm = os.path.getmtime("t9.py")
tm2 = time.localtime(tm)
print(tm2)


di = { 4545.43:'file', 124:'home', 42:'mome'}
print(di)
#di.values().sort()
#print(di)

#d2 = sortedDictValues1(di)

#print(d2)

for key in sorted(di):
    print("%s: %s" % (key, di[key]))

#2-6-2014 list directories, sort by time etc.
import sys, stat
#O'reilly 

def describedir(start): 
	def helper(arg, dirname, files):
		print("%s has files:", dirname)
	for file in files:
		fullname = os.path.join(dirname, file)
		if (os.path.isdir(fullname)):
			print(file + '[dir]')
		else:
			size = os.stat(fullname)[stat.ST_ZIE]
			print(file + '==' + str(size))
			
			
		
#def sortbytime(rootpath):
def scandir(rootpath):
	s1 = listdir(rootpath)
	print(s1)
	
print('os.path...');
#os.path.walk(r's:\code\python', scandir, None) #no .path
#os.walk(r's:\code\python', scandir, None)

#os.walk(r'b:\tor\', scandir, None)

def walkExample(path):	#22-3-2016 from ...
	import os
	for root, dirs, files in os.walk(path, topdown=False):
		print("FILES============")
		for name in files:
			s = os.path.join(root, name);
			print(s.encode(encoding='utf-8'))
		for name in dirs:
			print("DIRS============")
			j = os.path.join(root, name)
			#print(j.encode(encoding='utf-8'))
			print(j.encode(encoding='windows-1251'))
			k = " ";
			k = str(j.encode(encoding='windows-1251'))			
			#print(k[1:])
			print(k[2:]) #remove the:  b'
			#print(k[3:])
					
			
walkExample('b:\\tor\\')

print(sys.getdefaultencoding())
			



	
	
	