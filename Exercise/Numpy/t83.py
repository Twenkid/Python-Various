#t83.py

#f = open("b:\\wav\\1.wav", "rb") 
#r = f.read()
import numpy as np
import array
r = np.array ([124, 546, 12312, 32465, 234, 123, 645654,234, 0, 1232, 566])
print(r)


#r1 = bytes(r)
a = np.average(r)

print("========================")
print("Average=" + str(a))


f = open('b:\\wav\\3.wav', "rb") 
f.seek(44);
r1 = f.read()
#r1.append(0)
#if (len(r1)%2 != 0): r1.append(0)
print("LEN = ", len(r1))
f.close()


print(r1)


from scipy.io.numpyio import fwrite, fread

#data.tofile('myfile.dat')
fd = open('b:\\wav\\3.wav', "rb")
read_data = np.fromfile(file=fd, dtype=numpy.int16).reshape(shape)

print(str(read_data))


#r2 = array.array('i', r1)
r2 = array.array('b', r1)
r3 = array.array('i', r2)
r4 = np.array(r3)
b = np.average(r4)

# dtype = np.float64 ..

print("========================")
print("Average=" + str(b))