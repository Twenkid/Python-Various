#t15.py
#urlib + nltk ...
#python 2.7+

#import urllib.request#, urllib.parse, urllib.error  #later version!
#import urllib
import nltk
from urllib import urlopen
import sys

def basicclean():
  page = urlopen("http://news.bbc.co.uk/").read()
  cl = nltk.clean_html(page)
  print(cl)

def listclean():
  #li = ["http://dnes.bg/", "http://news.bbc.co.uk/", "http://www.atpworldtour.com/", "http://www.tennis24.bg"]
  li = ["http://abv.bg", "http://www.tennis24.bg"]
  pages = []
  cl = []
  
  for a in li: 
    print(a)
    page = urlopen(a).read()
    pages.append(page)
    cl.append(nltk.clean_html(page))
  for s in cl: 
    print(s)
	#print(s.encode('utf8'))
	#print(unicode(s))

    #sys.stdout.buffer.write(s.encode('utf8'))  #python 3?
  
#if __name__ == '__main__':
 
listclean()


  