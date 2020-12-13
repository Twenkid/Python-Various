import mmap
import sys
import array
#Author: (C) Todor Arnaudov, Interprocess communication, for ACS etc.
#27-3-2015
#f = open('cppcsh.bin', 'br')
#has to know the path!... not only the name... Discover, init folder ...
class FMOne():

	def fm_open(self, path):
		#f = open('S:\\Code\\Cpp\\2014\\Release\\cppcsh.bin', 'rb+')
		self.f = open(path, 'rb+')
		self.m = mmap.mmap(self.f.fileno(), 60000)
		self.m.seek(0);
 
	def fm_read(self ):
		self.s = self.m.read(3000);
		print(self.s[1040:1072]);
		print();
		print(self.s[1100:1200]);
		self.s1 = self.s[1100:1200]  #bytes
  
	def removeZeros(self ):
			self.s2 = []
			index = 0
			for i1 in s1:      
				if i1 != 0: self.s2.append(i1); #s1[i1]); index=index+1       	   	  
			print(self.s2)
			self.s2 = " "
			for i in range(1100,1200,2): k = s1[i:i+1]; s2 = s2 + k.decode("utf-8"); print(k.decode("utf-8"))
			print(s2)

	def mpExchange(self):  
		print(self.s1.decode())
		print(self.s1.decode("cp1251"))
		print(self.s1.decode("utf_16"))  #Success!!...  -- No spaces redundant... OK, 6:34
		#print(s.decode("utf-8")) #"utf_8"))

	def close(self):
		self.m.close()
		self.f.close()
		
	def __init__(self):
		print("FM Class")
		
def test_main():
	fm = FMOne()
	fm.fm_open('S:\\Code\\Cpp\\2014\\Release\\cppcsh.bin')
	fm.fm_read()
	fm.mpExchange()
	fm.close()
	s4 = dir(fm)
	print(s4)
	print()
	print(s4[12])

	
if __name__ == '__main__':
    test_main()
	
