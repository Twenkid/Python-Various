try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
	
#import webCrawl
#import urllib2
import razumir1

#a = 'http://erabg.com';
a = 'http://twenkid.com';

f = urllib2.urlopen(a)

data = f.read(999999)
encoding = 'utf-8'

   #razumir1.findEncoding(

try:
  text = data.decode('utf-8')    
except UnicodeDecodeError: text = data.decode('windows-1251'); encoding = 'windows-1251';

print(text)

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
                                        
fo = open('webRead2.txt', 'ab')

fo.write(bytes(text, encoding))
fo.close()

#  text = data.decode('windows-1251') #'utf-8') #should scan, try -- catch exceptions etc.!
#fo = open('webRead.txt', 'a+')
#b = bytes(mystring, 'utf-8')
#b = mystring.encode('utf-8')
#fo.write(a)
#fo.write(bytes(text, 'utf-8'))
#fo.write(bytes(text, 'windows-1251'))