#t80_2.py ... Python 2.7
#Web POST client
#Here is an example session that shows how to POST requests:
#2-4-2016
#t80_4.py	7-4-2016
#OK, works! :)
# Author: Todor Arnaudov

from sys import version

if version.startswith('3'):
	from urllib.parse import parse_qs
	import urllib.request, urllib.parse, urllib.error
	#from http.server import BaseHTTPRequestHandler
	import http.client
else:
	from urlparse import parse_qs	
	#from BaseHTTPServer import BaseHTTPRequestHandler
	import httplib, urllib
	
#import httplib, urllib



def py2():	#say=None):

	params = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})

#	params = urllib.urlencode({'@say': '123456787', '@type': 'issue', '@action': 'show'})
#	params = urllib.urlencode({'@say': "\xd0\xd1\xd2\xd3\xd4\xd5\xd6", '@type': 'issue', '@action': 'show', '@encoding':'utf-8'})
	
	params = urllib.urlencode({'@say': "Проба Проба 1, 2, 3", '@type': 'issue', '@action': 'show', '@encoding':'utf-8'}) #, '@vowels':'1.0', '@consonants':'1.5', '@speed':'0.5'})
	
	
	#if say==None:
	params = urllib.urlencode({'@say': "Говоря ли бързо 1, 2, 3", '@type': 'issue', '@action': 'show', '@encoding':'utf-8', '@consonants':'0.6', '@vowels':'2.0'})
	#else: params = urllib.urlencode(say)
	#'@vowels':'2.0', -- lenght of vowels > = longer
	
	
	#FloatVars[17] = 0.  #speed

   #Glas.Zabavyane = Glas.FloatVars[7];
   #FloatVars[14] = consonants
	#f,17,1.0,7,2.0;  //float ... index, value
	

	
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = httplib.HTTPConnection("localhost:8079")
	#conn = httplib.HTTPConnection("77.77.164.35:8079")

	conn.request("POST", "", params, headers)
	response = conn.getresponse()
	print(response.status, response.reason)
	#302 Found
	data = response.read()
	print(data)

#  UNCOMMENT FINALLY - save file ...	
#	import base64
#	decoded = base64.b64decode(data)
#	f = open("resp12345678.mp3", "wb")
#	f.write(decoded)
#	f.close()

	#>>> data
	#'Redirecting to <a href="http://bugs.python.org/issue12524">http://bugs.python.org/issue12524</a>'

	conn.close()
	
	
	#########################
	#params = urllib.urlencode({'@say': "По-различно сега. Изговор. ", '@type': 'issue', '@action': 'show', '@encoding':'utf-8', '@vowels':'2.5', '@consonants':'2.0', '@speed':'0.6'})
	#headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	#conn = httplib.HTTPConnection("localhost:8079")	
	#conn.request("POST", "", params, headers)
	#response = conn.getresponse()
	#print(response.status, response.reason)
	##302 Found
	#data = response.read()
	#print(data)

def pycall():
	py2({"'@say': 'Проба Проба 1, 2, 3', '@type': 'issue', '@action': 'show', '@encoding':'utf-8', '@vowels':'1.0', '@consonants':'0.5', '@speed':'0.8'"})
	py2({'@say': "Сега по-забавено", '@type': 'issue', '@action': 'show', '@encoding':'utf-8', '@vowels':'1.5', '@consonants':'1.5', '@speed':'0.8'})
def py3():
	print('not defined yet')
	
if version.startswith('2'): py2()
else: py3()
	
	
