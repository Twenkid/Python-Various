# WM_COPYDATA, python ... try with py27 first - ASCII
#-*-
# Author: Todor Arnaudov 4.2016
import win32api
import win32gui
import win32con
import struct
import array


def wmcopydataTest():
	#char_buffer = array.array('B', b'012345678')
	#char_buffer = array.array('B', [191, 192, 193, 66, 12, 67, 25, 68, 69, 70, 71, 80, 75, 72, 94])

	abv = []
	#for i in range(128,255):	abv.append(i)
	#for i in range(0,100):	abv.append(0)
	k = 0
	#for i in range(1,4096):	abv.append(k%128+32); k=k+1;
	for i in range(1,60):	abv.append(k%60+190); k=k+1;

	#abv.append("абвгед"); k=k+1;

	#char_buffer = array.array('B', abv)
	#char_buffer = array.array('b', abv)

	char_buffer = array.array('B', abv)

	#char_buffer = array.array('s', abv)
	#print(abv)

	char_buffer_address, char_buffer_size = char_buffer.buffer_info()
	copy_struct = struct.pack("PLP", 2, char_buffer_size, char_buffer_address) #GLAS_CMDS_SPEAK=1, ..SIMPLE=2
	print(char_buffer_size)
	print(char_buffer_address)
	hwnd = win32gui.FindWindow(None, "WM_COPYDATA_GLAS")
	win32gui.SendMessage(hwnd, win32con.WM_COPYDATA, None, copy_struct)

def wmcopydataB(say):	
	print("wmcopydataB(say)")
	import binascii
	s = "abcdef"
	d = binascii.a2b_qp(s)
	#print(d)
#b'abcdef'

	#k = 0	
	#for i in range(1,60):	abv.append(k%60+190); k=k+1;

	#char_buffer = array.array('B', abv)
	print('before: char_buffer = array.array('B', binascii.a2b_qp(say))')
	
	#char_buffer = array.array('B', binascii.a2b_qp(say))
	#sayUTF = say.decode('utf-8') #windows-1251') 
	#say1251 = sayUTF.encode("windows-1251", "ignore")

	char_buffer = array.array('B', binascii.a2b_qp(say)) #1251))
	
	
	print('before: char_buffer')
	print(char_buffer)

	char_buffer_address, char_buffer_size = char_buffer.buffer_info()
	copy_struct = struct.pack("PLP", 2, char_buffer_size, char_buffer_address) #GLAS_CMDS_SPEAK=1, ..SIMPLE=2
	print(char_buffer_size)
	print(char_buffer_address)
	hwnd = win32gui.FindWindow(None, "WM_COPYDATA_GLAS")
	win32gui.SendMessage(hwnd, win32con.WM_COPYDATA, None, copy_struct)

