#python t81.py
#"Toshko 2" POST server. Receives speech requests, returns mp3 records.
#Target: Python 2.7 
#Author: Todor Arnaudov, thanks to general sample code from Python's core site and other sources
#2-4-2016
#-*-


import sys			
from sys import version as python_version
if python_version.startswith('3'):
    print("Please, use Python 2 (e.g. 2.7)! http://python.org")
    sys.exit(0)
	
import time
import BaseHTTPServer
import CGIHTTPServer 
import t80_3	#WM_COPYDATA .. wmcopydataB

from cgi import parse_header, parse_multipart
from urlparse import parse_qs
from BaseHTTPServer import BaseHTTPRequestHandler

import random
	

#if python_version.startswith('3'):   
    #from urllib.parse import parse_qs
    #from http.server import BaseHTTPRequestHandler
#else:
    #from urlparse import parse_qs
    #from BaseHTTPServer import BaseHTTPRequestHandler
	
HOST_NAME = 'localhost' #example.net ... Set the proper address and port
PORT_NUMBER = 8079

mp3 = []
mp3.append("S:\\Code\\Cpp\\2014\\UTF8-Test\\Debug\\mp3\\") #Set the path to the mp3 output folder of Toshko 2

#mp3.append("toshko2_glas_2_3_4_2016_10-10-20-444.wav.mp3")
mp3.append("pythonSay")		#[0] path, [1] file

mp3Path = "S:\\Code\\Cpp\\2014\\UTF8-Test\\Debug\\mp3\\"
mp3File = "pythonSay"
mp3Ext = ".mp3"
wavExt = ".wav"

#list directory ... get the latest file or ...

#busy = False

class PostHandler(CGIHTTPServer.CGIHTTPRequestHandler ):

	#def __Init__(self):
	#	busy = False
	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
	def do_GET(s):
		"""Respond to a GET request."""
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		s.wfile.write("<html><head><title>Title goes here.</title></head>")
		s.wfile.write("<body><p>This is a test.</p>")
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
		s.wfile.write("<p>You accessed path: %s</p>" % s.path)
		s.wfile.write("</body></html>")
		
	def parse_POST(self):
		ctype, pdict = parse_header(self.headers['content-type'])
		if ctype == 'multipart/form-data':
			postvars = parse_multipart(self.rfile, pdict)
		elif ctype == 'application/x-www-form-urlencoded':
			length = int(self.headers['content-length'])
			postvars = parse_qs(
					self.rfile.read(length), 
					keep_blank_values=1)
		else:
			postvars = {}
		return postvars
		
	def do_POST(self):	#s = self		
		try:
			#if (self.busy): return
			
			#self.busy=True
			
			print("called do_POST?")
			self.send_response(200)
			self.send_header("CAANANAAA", "text/html")
			self.end_headers()
			
			postvars = self.parse_POST()
			print(postvars)
			#print("==== self.rfile ====")
			#print(str(self.rfile))
			#rd = self.rfile.read()
			#print(rd)
			#print(dir(self.rfile))
			#print(dir(self))
			#self.wfile.write("POST RESPONSE?")
			
			#t80_3.wmcopydataB(postvars["@say"])
			print(postvars["@say"])
			print(postvars["@say"][0])
			
			say = postvars["@say"][0]
			
			#command = "f,17" + str(postvars["@vowels"][0]) + ",7" + str(postvars["@consonants"][0]) + ";"
			
			#command = ":::f,17," + postvars["@vowels"][0] + ",14," + postvars["@consonants"][0] + ",7," + postvars["@speed"][0] + ";\n"; # + ",9" + postvars["@speed"][0] + ";\n"  #9-4-2016
			#f,17,1.0,14,1.5  
			#7, ... -Zabavyane
			
			#no 17 -- range?
			
			command = ":::f,14," + postvars["@consonants"][0] + ",7," + postvars["@vowels"][0] +";"; # + ";\n"; # + ",9" + postvars["@speed"][0] + ";\n"  #9-4-2016
			
			#mp3File += str(random.randint(1000000,999999))
			
			random.seed(int(time.time()))
			nn = random.randint(1000000,9999909)
			
			mp3File = "pythonSay" + str(nn)
			print(mp3File)
			
			
			#command += "$$$"+mp3File + ";\n" #12-4-2016
			command += "$$$"+mp3File + ";\n" #12-4-2016
			
			print("Before say1251 = ...")
			#say1251 = say.decode('utf-8') #encoding='windows-1251')

			print("BUSY... Communicating with Toshko...")
			
			#print(postvars["@say"][0](encoding='windows-1251'))
			print(command)
			say = command + say; ###### 9-4-2016
			#ii = input('\nenter...')
			
			#print(say)
			
			#t80_3.wmcopydataB(postvars['@say'][0])
			
			s = say.decode(encoding='utf-8') #windows-1251')
			say = s.encode('windows-1251')
			t80_3.wmcopydataB(say) #1251) #postvars['@say'][0])
						
			time.sleep(0.250)
			#А... Защото изговорът е в нишка и е изговорило частично!!!... 13-4-2016, 0:21
			#Ако няма синхронизация, няма как! Трябва да стробира, може FM модул, през 1/100 напр.
			import base64
			
			
			#f = open(mp3[0] + mp3[1], 'rb')  #with a list
			#pythonSay.wav.mp3
			print(mp3File)
			print(mp3Path + mp3File + wavExt + mp3Ext)
			f = open(mp3Path + mp3File + wavExt + mp3Ext , 'rb')  #with vars
			#print(mp3File)
			#print(mp3Path + mp3File + wavExt + mp3Ext)
			d = f.read()
			encoded = base64.b64encode(d)			
			f.close()		
			self.wfile.write(encoded)
			
			print("OK! READY for new requests");
		except:			
			print(sys.exc_info())

def cgiServer():
	server_class = BaseHTTPServer.HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), PostHandler)	
	print(time.asctime(), "Toshko POST Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
	print(time.asctime(), "Toshko POST Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))

	
if __name__ == '__main__':	
	cgiServer()

#Т:Бележка: Защо обработва POST по два пъти??
	