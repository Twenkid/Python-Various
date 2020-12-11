try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
	
#import webCrawl
import razumir1

#import urllib2

#a = 'http://erabg.com';
#a = 'http://twenkid.com';
a = 'http://research.twenkid.com/';
f = urllib2.urlopen(a)

data = f.read(999999)


u = urllib.request.urlopen(url)
web = response.read()
print(web)

#razumir1.findEncoding(

try:
  text = data.decode('utf-8')
#  text = data.decode('windows-1251') #'utf-8') #should scan, try -- catch exceptions etc.!
except UnicodeDecodeError: text = data.decode('windows-1251')

text2 = text.encode('windows-1251')

#print(text)
print(text2)
import re

p = re.compile('[\w\s]+креативен[\w,!.?\s]+')

#found = re.match(text)
found = p.findall(text)
print('REGEX... \n')
print(found)
print('\n\n')

for item in found: print(item) #.span())  //string

iterator = p.finditer(text)
for item in iterator: print(item.span())




#fo = open('webRead.txt', 'a+')
fo = open('webRead2.txt', 'ab')

#fo.write(a)
#fo.write(bytes(text, 'utf-8'))
fo.write(bytes(text, 'windows-1251'))
fo.close()


#b = bytes(mystring, 'utf-8')
#b = mystring.encode('utf-8')
