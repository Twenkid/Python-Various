#python t80.py
#Web server ... POST Server ... tests ...
#2-4-2016
#from http.server import BaseHTTPServer.HTTPServer#, BaseHTTPServer.BaseHTTPRequestHandler

#import http.server	
#import socketserver

import time
import BaseHTTPServer
import CGIHTTPServer 

HOST_NAME = 'localhost' #example.net' # !!!REMEMBER TO CHANGE THIS!!!
HOST_NAME = "tosh-PC" # invalid -? http://77.77.164.35"
PORT_NUMBER = 8079 # 62000 #8079 #8079 # Maybe set this to 9000.

mp3 = []
mp3.append("S:\\Code\\Cpp\\2014\\UTF8-Test\\Debug\\mp3\\")
mp3.append("toshko2_glas_2_3_4_2016_10-10-20-444.wav.mp3")
#list directory ... get the latest file or ...

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
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
	def do_POST(s):
		s.send_response(200)
		s.send_header("CAANANAAA", "text/html")
		s.end_headers()
        s.wfile.write("<html><head><title>Title goes here.</title></head>")
        s.wfile.write("<body><p>This is a test.</p>")

class PostHandler(CGIHTTPServer.CGIHTTPRequestHandler ):
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
	def do_POST(self):	#s = self
		self.send_response(200)
		self.send_header("CAANANAAA", "text/html")
		self.end_headers()
		#self.wfile.write("POST RESPONSE?")
		
		import base64
		f = open(mp3[0] + mp3[1], 'rb')
		d = f.read()
		encoded = base64.b64encode(d)			
		f.close()
		
		self.wfile.write(encoded)
		
        #self.wfile.write("<html><head><title>Title goes here.</title></head>")
        #self.wfile.write("<body><p>This is a test.</p>")
		
				
def baseHttpServer():
    server_class = CGIHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))

def cgiServer():
	server_class = BaseHTTPServer.HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), PostHandler)
	print(time.asctime(), "POST Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
	print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))

	
if __name__ == '__main__':
	#baseHttpServer()
	cgiServer()

#Responding with URL Redirection

	
#server1()