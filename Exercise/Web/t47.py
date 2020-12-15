#t47.py
#import win32.win32api  #ImportError: No module named win32.win32api   ???

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
	
#print(dir(urllib2))
list = dir(urllib2)
for s in list: print(s)

url = 'http://www.bing.com/images/search?q=%d0%93%d1%80%d1%83%d0%b7%d0%b8%d1%8f&FORM=HDRSC2'
url = 'http://www.bing.com/images/search?q=Imanuel+Kant&view=detailv2&&&id=20C00C8B61AC086C2988CB7172395A3AD1B87A9C&selectedIndex=19&ccid=o1O3XNKY&simid=608053578826975455&thid=JN.INhbeB%2bbzfDQuY0MgDnrNA&ajaxhist=0'
s1 = urllib2.unquote(url)
print(s1)

print(url)

print('splitattr')
x = urllib2.splitattr(url)
print(x)
print('splithost')
x = urllib2.splithost(url)
print(x)
print('splitpasswd')
x = urllib2.splitpasswd(url)
print(x)
print('splitport')
x = urllib2.splitport(url)
print(x)
print('splittype')
x = urllib2.splittype(url)
print(x)
print('splituser')
x = urllib2.splituser(url)
print(x)
print('splitvalue')
x = urllib2.splitvalue(url)
print(x)


from urllib.parse import urlparse

#from urllib.urlparse import urlparse

print('dir(urllib2.urlparse)')
#x = dir(urllib2.urlparse)
x = dir(urllib.parse.urlparse)
print(x)

print('urlparse')
x = urllib2.urlparse.urlparse(url)
print(x)

print('urlparse.parse_qs')
x = urllib2.urlparse.parse_qs(url)
print(x)

print('urlparse.parse_qsl')
x = urllib2.urlparse.parse_qsl(url)
print(x)

print('urlparse.urlsplit')
x = urllib2.urlparse.urlsplit(url)
print(x)

print('eval(urllib2.urlparse.parse_qs(url)')
x = eval('urllib2.urlparse.parse_qs(url)')
print(x)

print('dir(win32.win32api)')

#import win32.win32api

import win32.win32api

res = []
imp = 'win32.win32api'
#win = dir(win32.win32api)
win = eval('dir('+imp+')')
value = 0
params = str(value)
for i in win: 
             if i=='GetComputerNameEx':
                                       exp = 'imp.'+i+'('+params+')'
                                       print(exp) 
                                       r = eval(exp)
                                       res.append(r)
							 
							 