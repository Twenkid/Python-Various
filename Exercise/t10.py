#t10.py
#python 3.3 print('...')
#O'Reilly ... p.510 others
# Count words in text and timing ...
# Author: Todor Arnaudov

#timing

def lots_of_appends():
	vals = []
	for i in range(10000): vals.append(i)
	
def one_multiply(): zaros = [0] * 10000

import time

def do_timing(num, *funcsin):
	totals = {}
	funcs = list(funcsin)
	for func in funcs:
		totals[func] = 0.0
		start = time.clock()
		for x in range(num):
			for func2 in funcs:
				func2()
		stop = time.clock()
		elapsed = stop - start
		totals[func] = totals[func] + elapsed
	for func in funcs:
		print("Running %s %d times took %.3f sec" % (func.__name__, num, totals[func]))
		
#do_timing(100, (lots_of_appends, one_multiply))

do_timing(100, lots_of_appends, one_multiply)

#from timings import *

#import profile
#profile.run(do_timing(100, (lots_of_appends, one_multiply)))

import cProfile
import re
#cProfile.run('re.compile("foo|bar")')
cProfile.run('do_timing(100, lots_of_appends, one_multiply)')

#Error checking, debug, interactive
#import pdb
#pdb.run('do_timing(100, lots_of_appends)')

#unittest

import random

#random.shuffle(list1)

def AdaTextTest(pathAnsi):

	#t = open(r'R:\ngramtool-20040527-mingw32-static\ada2008ansi.txt', 'r').read()
	t = open(pathAnsi).read()
	 
	s = t.split()
	d = {}
	sunique = []

	out = open(r'words1.txt', 'w')

	for s1 in s: 
		if s1 not in sunique: sunique.append(s1)
		#t = open(r'R:\ngramtool-20040527-mingw32-static\ada2008ansi.txt', 'r').read()
	print(sunique.__len__())

	out.write(str(sunique))
	out.close()

	out2 = open(r'words2.txt', 'w')

	sunique.sort()
	n = 0
	m = 10
	for s2 in sunique: 	
		out2.write(s2 + '\t')
		n=n+1
		if n%10 == 0: out2.write('\n')
	out2.close()
		
AdaTextTest(r'R:\ngramtool-20040527-mingw32-static\ada2008ansi.txt')



#import ctypes
#print(dir(ctypes))



