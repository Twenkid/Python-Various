# coding=<'utf-8'> #not recognized
# -*- coding: utf-8	#ok
# Educational Code
# Author (Exercising from samples, books, variations on): Todor Arnaudov, 2014-2015

import sys
import string

print(sys.platform)

sarr = [];
sarr.append(dir([]))
sarr.append(dir(''))

s = 'Котка куче яде'
print(s)

i=0
for s1 in sarr: 
	print(i)
	print(s1)
	i=i+1

print(s[:-3])

sli = []
sli.append(s)

sli.append(s.replace('у', 'жих'))

print(sli[1])

keys = []
vals = []
keys.append("бяга");
keys.append("скача");
keys.append("мяука");
keys.append("хвърля");
keys.append( "души")
keys.append("ближе")

vals.append("леопард")
vals.append("куче")
vals.append("котка")
vals.append("човек")
vals.append("таралеж")
vals.append("език") 
dict = {}

for (a,b) in zip(keys, vals):
     dict[a] = b;
 
#print(dict.keys().len)
#del dict['мяука']  #doesn't support item deletion

#print(dict.keys().len)
#dir(fi)

print(len(dict))
print( dict['мяука'])
del dict['скача']
print(len(dict))

t = (1, 'ходи', 45)
li = list(t)
tp = tuple(keys)
print(tp)
print(li)

f = open('data\data.txt', 'r')
sli.append(f.read())
f.seek(0)
#print(sli[2])

slines = f.readlines()
#for l in slines: print(l)

print(slines[5]) #, slines[7], slines[12])

L = ['a', [(1,2), ([3], 4)], 5]
print(L[1][1][0])
print(L[1][1][0][0])

# copying section
print("copying section ABC {")

A = slines[:] #copy

import copy 
B = L.copy()  #shallow copy
C = copy.deepcopy(L)
print(A is slines)
print(A == slines)
print(B is C)
print(B == C)
print(B < C)
print(B > C)
print("copying section ABC }")

L1 = [1, ('a', 3, 6, 2, 'c')]
L2 = [1, ('a', 1, 145, 'd', 3)]

print("copying section L1L2 {")
print(L1 is L2)
print(L1 == L2)
print(L1 < L2)
print(L1 > L2)
print("copying section L1L2}")

Y = L1*4
print(Y)

t = sys.stdout

sys.stdout.write(str(L1) + '\n')

sys.stdout = open('l.txt', 'a')
print(slines)
sys.stdout = t
print(s)

log = open('l.txt', 'a')
#print(log, s)  no

s3 = 'kaka'

x = 1; y=2; print(x+y)
if x: print(b)

if 1: print('true')
if not a: print('false')
	
s3 = 'kiki'

if s3 == 'kaka': print('Golyama')
elif s3 == 'baba': print('baba')
else: print ('Nishto')

x = 56
while x:
   if x == 10: break
   x = x - 1
else: print("break not called")

for x in ["a", "b", "c"]: print(x)

t = ["a", "b", "c", "d"]
itm = ["d", "x", "z", "a"]

smatch = ''
for key in t:
	for item in itm: #print('item')
		if item==key: smatch = smatch + item
	#	else: print(key + "!=" + itm)
	# res.append(key) ... intersect
	
print('matching: [' + smatch + ']')

s5 = ''
for i in range(0, 124, 6): s5 = s5 + str(i) + ", "
print(s5)

L4 = [1,2,3]
L5 = [5,6,7]

L6 = list(zip(L4,L5)) #OK!
print(L6[0])

L8 = map(L4, L5)
#L8 = list(L8)
print("map = " + str(L8))

#tuples cycle
L7 = [(1,2, 'kaka'), (5, 124, 'batka')]
for (a,b,c) in L7: print(a, b, c)
	
#//for x in L5
 
#s6 = help(sys)  //goes to stdout!
#f2 = open('help.txt', 'w')
#f2.write(s6)
#f2.close()

z = 135
def times(x,y): return x*y

print(times(3,z))

def fun1(z=467): 
	global gx		
	gx = z
	y = z*gx
	gx = gx+y
	return y

fun1(213)
print(gx)
gx = gx + 567
print(gx)

D3 = {}
for (k,v) in zip(keys, vals): D3[k] = v

#D4 = dict(zip(keys,vals))  dict object is not callable

#import docstrings.__doc__
#print(doscstrings.__square.__doc__)
#documentation
print(sys.__doc__)

#help(sys.getrefcount) #to stdout
#help(dict)


def intersect(sq1, sq2):
	res=[]				#започва празна
	for x in sq1:		#обхожда sq1
		if x in sq2:	#общ елемент
			res.append(x)	#добавя към края на резултата
	return res			#връща резултата
	
print(intersect("Krokodil"," Hipopotam"))

#26-5-2014, 16:00
def fmany1():
	dir(__builtin__)

def changer(x,y):
	x = 2
	y[0] = 'new'

kk=99	
changer(kk, L1)
print(kk, L1)

changer(kk, L2[:])	#L2[:] copy the list - doesn't change it
print(kk,L2)


def f(a,b,c): print (a,b,c)

print(f(c=3, b=2, a=1))
print(f(1, c=3, b=2))

def fparam(name='Rib', h=640, w ='Qsg2'): print(name, h, w)

fparam('Kaaa')

  
def fmany2(*args): print(args)  # list,array args[0], args[1] ...

def fmany3(**args): print(args)	#hash

def fmany4(a, *pargs, **kargs): print (a, pargs, kargs)

fmany4(1, 2,3, x=1, y=2)
  

  
def intersectA(*args):	#Common in all
	res=[]				#започва празна
	for x in args[0]:		#обхожда sq1
		for other in args[1:] :	#общ елемент
			if x not in other: break	#добавя към края на резултата
		else:
			res.append(x)
	return res			#връща резултата
	
def unionA(*args):
	res = []
	for seq in args:
		for x in seq:
			if not x in res:
				res.append(x)
	return res
	
s1, s2, s3 = "Aba", "raba", "libi"
#s4 = ["errereb", "ssssssb"]
s4 = "errereb"
print(intersectA(s1, s2, s3, s4))
print(unionA(s1, s2, s3, s4))

#26-5-2014, 19:23
#lambda

f = lambda x,y, z: x+y+z
print(f(2,3,4))

L = [(lambda x: x**2), (lambda x: x**3), (lambda x: x**4)]
for f in L: print(f(2))

print(L[0](3))

dd = {'a': (lambda: 2+2),
 'g': (lambda: 2*4),
 'o': (lambda: 2**6)
 }
 
print(dd['g']())
 
 #function pointers
 
 
ds = { 'a': fmany1, 'b': fmany2, 'c': fmany3, 'd':fmany4}

ds['b']('asasaasa')
 
 
def ifelse(a,b,c): return ((a and [b]) or [c])[0]
def ifelse2(a,b,c):
	if a: return b
	else: return c
	
	
#def saver(x=None):
#		if x is None:
#			x=[]
#		x.append(1)
#		print(x)
		

		
counters = [1, 2, 5, 10]	
def inc(x): return x+10

countersPlus = map(inc, counters)
print(list(countersPlus))	

countersPlusLambda = map((lambda x:x+3), counters)
print(list(countersPlusLambda))
		
pargs = ((1,2), (1,8))
#res = apply(unionA, pargs)  #deprecated since 2.3!
res = unionA(*pargs)
print(res)

#map, filter, reduce

print(list(filter((lambda x:x>0), range(-5,5))))	#a1


res = []											#a2
for x in range(-5,5):
	if x > 0:
		res.append(x)
print(res)

#print(s8)

#r1 = reduce((lambda x,y: x+y), [1,2,3,4])	#reduce dropped from 3.0
#r2 = reduce((lambda x,y: x*y), [1,2,3,4])	
#print(list(r1))
#print(list(r2))

print(ord('а'))
#print(o('а'))
res = list(map(ord, 'абвгдежзАБВ'))	
print(res)
#1072, 1073, 1074 ... 1040, 1041, ...

#Some combinations etc... generate
res = []
for x in range(5):
	if x%2 == 0:
		for y in range(5):
				if y%2 == 1:
						res.append((x,y))
print(res)







