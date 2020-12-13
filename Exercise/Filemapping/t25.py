import mmap
import sys
import array

#27-3-2015
#f = open('cppcsh.bin', 'br')
#has to know the path!... not only the name... Discover, init folder ...
f = open('S:\\Code\\Cpp\\2014\\Release\\cppcsh.bin', 'rb+')
m = mmap.mmap(f.fileno(), 60000)

m.seek(0);
s = m.read(3000);

print(s[1040:1072]);
print();
print(s[1100:1200]);

#bytes
s1 = s[1100:1200]

#s3 = [:]

#for i in s1: 
s2 = []

index = 0
for i1 in s1:      
   if i1 != 0: s2.append(i1); #s1[i1]); index=index+1
       #if s1[i1] != 0: s2.append(i1); #s1[i1]); index=index+1
	   	  
#bytes = s2.encode(s2)

#a = array.array('B', s2)
#print(a)
#print(a.tostring())

print(s2)


  
#s1 = s2
  #if (s1 == 0) s1.remove(i1)
#for i in range(0, 559): print(s[i])

#for i in range(1040, 1072): print(s[i])

#for i in range(1100, 1200): print(s[i])
#print(s1.decode('cp1251')) #"utf_8"))
#print(s1.decode("utf_16"))
#print(s1.decode("utf_16_be"))
#print(s1.decode("utf_16_le"))

s2 = " "
for i in range(1100,1200,2): k = s1[i:i+1]; s2 = s2 + k.decode("utf-8"); print(k.decode("utf-8"))

print(s2)

print(s1.decode())
print(s1.decode("cp1251"))
print(s1.decode("utf_16"))  #Success!!...  -- No spaces redundant... OK, 6:34

#print(s.decode("utf-8"))

#print(s1.decode("utf-8")) #"utf_8"))

m.close()
f.close()
