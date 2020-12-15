#t15.py
#urlib + nltk ...
#python 2.7+

#import urllib.request#, urllib.parse, urllib.error  #later version!
#import urllib
import nltk
from urllib import urlopen
import sys

def cleanpage(url):
  page = urlopen(url).read()
  cl = nltk.clean_html(page)
  print(cl)
  
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
 
import re

def readcomix():
  txt = r"""<div id="info"><img src="komiksi/img8290b662b6532b5e1635fb338d152a4e.jpg"  width="550px"/></div><br />""" 
  s1 = "src=\"komiksi/([\w\d.]+)\s+width=\"550" #no
  s1 = "src=\"komiksi/([\w\d.]+)\s+" #no
  s1 = "src=\"komiksi/([a-zA-Z0-9]+)\s*" #OK
  s1 = "src=\"komiksi/([a-zA-Z0-9]+[.]jpg)\s*"
  
  
  li = ["http://stoinews24.com/komiksi.php?id=2352"]
  page = urlopen(li[0]).read()
  
  #print s1
  res = re.search(s1, page, re.MULTILINE)
  print res
  print res.group(0)
  print res.group(1)
  
  path = "http://stoinews24.com/" + "komiksi" + "/" + res.group(1)
  
  print path
  
  #unbalanced parenthesis!!! careful with \)  !!!
  
#listclean() //t20.py

#readcomix()

#listclean()

if __name__ == '__main__':
  if (len(sys.argv) > 1):
                         cleanpage(sys.argv[1])
  #else: listclean()
  