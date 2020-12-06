# 26-5-2014, 20:41
# Python
# Generators and iterators
# Educational Code. Author: Todor Arnaudov

import imp

def gen2(n):	
	s = ''
	for i in range(n):
		yield i**2			

		
def gen(n):	
	s = ''
	for i in range(n):
		s = s + str(i) + ': '
	return s	

def gen3(n):	
	s = ''
	for i in gen2(n):
		s = s + str(i) + ': '
	return s
	
#gen(20)
s1 = gen(20)
print(s1)
s2 = gen3(5)
print(s2)


x = gen2(10)	# generator

D = { 'a': 124, 'b': 19465, 'c': 6733, 'd':9555}
x = iter(D)
s = dir(x)
print("Iterator?... __next__")
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(s)
for key in D:
	print (key, D[key])
	
#Python

#PYTHONPATH
#.pth

import t3	#all
#from t3 import *

t3.pipi('Kur')

from t4 import kaka
#from t4 import *

kaka(236)

t3.pix = 999

pix = 111

print(t3.pix)
print(pix)
#t3.pix != pix

#окачествяванее X.Y

# X = 1
# import mod2
# print X
# print mod2.X
# print mod2.mod3.X
#
#

imp.reload(t3)  #import before importing the other module t3! 

print(t3.pix)

#26-5-2014, 21:26

#package import ... пакетно импортиране 

#import dir1.dir2.mod  # == dir1/dir2/mod.py

#6. Modules — Python v2.7.7rc1 documentation
#https://docs.python.org/2/tutorial/modules
#When importing the package, Python searches through the directories on sys.path looking for the ... Users of the package can import individual modules from the ...

#26-5-2014, 23:36

#content of:
#sound/effects/__init__.py 
#__all__ = ["echo", "surround", "reverse"]
#import sound.effects.echo
#import sound.effects.surround
#from sound.effects import *

print("Class stuff...")

class Home:
	def __init__(self, val=0):
		self.data = val
	def setdata(self, val):	#self -- the instance
		self.data = val;
	def show(self):
		print(self.data)
		
h = Home()
h.setdata(100)
h.show()

h.newitem = "Barakuda"

print(h.newitem)

h2 = Home()
h2.setdata("Karikatura")
h2.show()
		

#__X__
#redefine operators		-- предефиниране на оператори
#__init__				-- конструктор, ctor, constructor
	
class BigHome(Home):
	def __init__(self, val=0):
		self.data = val
	def	__add__(self, other):
		return BigHome(self.data + other)
	def __mul__(self, other):
		self.data = self.data * other
		return self.data
	
b = BigHome("Shibka")
b.show()
b = b + " kakavida"
b.show()

bi = BigHome(9999)
scalar = bi * 146
print(scalar)
bi.show()

class BiggerHome(BigHome):
	varofclass = 2014		#class variable (not instance)
	def __init__(self, val=0):
		BigHome.__init__(self, val)
  
bigger = BiggerHome(456)
print(bigger.varofclass)

if __name__ == '__main__':
	for klass in (Home, BigHome, BiggerHome):
		print(klass.__name__ + '...')
		klass().show()

#print(x.next())

#for i in range(0,10):

# __init__
# __del__
# __add__
# __or__
# __repr__
# __str__
# __call__
# __getattr__

predef = ['init', 'del', 'add', 'or', 'repr', 'str', 'call', 'getattr', 'setattr', 'setitem', 'len', 'cmp', 'lt', 'eq', 'radd', 'iadd', 'iter']
sout = []
for s in predef:
	sout.append("__" + s + "__")
print(sout)
   
class Miger():
	"""
	Does nothing but :P
	"""
	def __init__(self, start=0, end=10):
		self.val = start
		self.end = end
	def __getitem__(self,index):
		"""
		getitem help?
		"""
		return index**2
	def __iter__(self):
		return self
	def	next(self):
		if self.val == self.stop:
			raise StopIteration
			self.data +=1
			return self.value**2
				
x = Miger(1, 9)
# print([n for n in x]) #?

# list(Miger(1,6)) #?

# __dict__
# __class__
# __bases__

print(BiggerHome.__dict__)
print(BiggerHome.__bases__)
print(BiggerHome.__class__)
print("BiggerHome.__bases__[0].__dict__")
print(BiggerHome.__bases__[0].__dict__)
print("BiggerHome.__bases__[0].__bases__[0].__dict__")
print(BiggerHome.__bases__[0].__bases__[0].__dict__)
print("\nBiggerHome.__bases__[0].__bases__[0].__dict__.keys()\n")
print(BiggerHome.__bases__[0].__bases__[0].__dict__.keys())
print(BiggerHome.__bases__[0].__bases__[0].__dict__.values())

#instance
print(bigger.__dict__.keys())
print(bigger.__dict__.values())

#instance
bigger.__dict__['data'] = 9999
print(bigger.__dict__.values())

def classtree(cls, indent):
	print ('.'*indent, cls.__name__)
	for supercls in cls.__bases__:
		classtree(supercls, indent+3)
		
def instancetree(inst):
	print('Tree of', inst)
	classtree(inst.__class__, 3)

def selftest():
	class A: pass
	class B(A): pass
	class C(A): pass
	class D(B,C): pass
	class E: pass
	class F(D,E): pass
	instancetree(B())
	instancetree(F())
	
if __name__ == '__main__': selftest()
	
#27-5-2014, 14:25

print(Miger.__doc__)
print(Miger.__getitem__.__doc__)
		
class Set(list):

	def __init__(self, value = []):
		list.__init__([])		#override list
		self.concat(value)
	def intersect(self, other):	#Common in all
		res=[]				#започва празна
		for x in self:		#обхожда sq1			
			if x in other: 
				res.append(x)
		return Set(res)			#връща резултата
	
	def union(self, other):		
		res = Set(self)
		self.concat(other)
		#for x in other:			
		#		if not x in self: self.append(x)		
		return res
	
	def concat(self, value):
		for x in value:
			if not x in self:	self.append(x)
	def __and__(self, other): return self.intersect(other)
	def __or__(self, other): return self.union(other)
	def __repr__(self): return 'Set:' + list.__repr__(self)
		
if __name__=='__main__':
			x = Set(['a', 'b', 'kur'])
			y = Set(['h', 'koko', 'qhfdifs', 'kur'])
			z = ['h', 'kur']
			print(x,y,len(x))
			z = x.intersect(y)
			print('z = ' + str(z))
			#q = (x | y)#z # | z # don't use | for or!!!... doesn't work? #27-5-2014
			#q1 = (x and y)			
			#q1 = x			
			#print('(x and y) = ' + str(q1))			
			q1 = x.intersect(y)
			print('x.intersect(y) = ' + str(q1))			
			q =	q1 or z
			print('(x and y) or z = ', q)
			#print('x or y: ' + str(x or y))
		
# differences between intersect and the operator!!!...		
#print(st)

#list, str, tuple, dict

class Private():
  def __init__(self, v):
     self.__x = v

p = Private(15)
print(p._Private__x)

class Obj(object):	#new classes ... diamond inheritance ...
  __slots__ = ['type', 'name', 'date', '__x'] #limit available attributes
  def __init__(self, v):
     self.__x = v
	 
o = Obj(567)
o.type = 'human'

class Objslot(object):	#new classes ... diamond inheritance ...
  __slots__ = ['type', 'name', 'date', '__x'] #limit available attributes
  def __init__(self, v):
     self.__x = v
	 
os = Objslot(999)

class Static:
	num = 0
	def __init__(self):
		Static.num += 1
	def __repr__(self): return "Instances: " + str(Static.num)
   
sta = Static()
print(sta)
sta2 = Static()
print(sta)
#age = property(getage, None, None, None) 
#property

#old classes:
#__getattr__
#__setattr__

#new classes:
#__getattribute__	#captures all  ...
#
#o.mype = 'asasa'


def fetcher(obj,i):
	return obj[i]

x = []
x.append([1, 2, 3])
	
def catcher():
	try:
		fetcher(x,4)
	except IndexError:
		print('except! index')
	print("continue")

catcher()

class bad(BaseException): pass	

#TypeError: catching classes that do not inherit from BaseException is not allowe

#bad(
 #= 'bbb'
try:
	raise bad
except bad:
	print('got bad')

	
	


	 

#
#
#
#
#
#
#
#
#
#
#

	#print (x.next())	next is probably deprecated
	
#for i in gen2(10):
#	p
