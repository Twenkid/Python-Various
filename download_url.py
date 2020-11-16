# save-webpage.py
# 4-8-2018
'''import urllib2

def download(url, savePath=None):
 url = 'https://docs.opencv.org/3.1.0/d6/d6e/group__imgproc__draw.html#ga5126f47f883d730f633d74f07456c576'

 response = urllib2.urlopen(url)
 webContent = response.read()

 if (save!=None): f = open(save, 'w'); f.write(webContent); f.close
 
 return webContent
 '''

import urllib.request
import urllib.parse
 
def download(url, save=None):  
   r = urllib.request.urlopen(url)
   c = str(r.read())
   if (save!=None): f = open(save, 'w'); f.write(c); f.close
 
   return c
 

import re

TAG_RE = re.compile(r'<[^>]+>')
def removeTags(text):
    return TAG_RE.sub('', text)
	
#def removeTags(text): #https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
  #import xml
  #return ''.join(xml.etree.ElementTree.fromstring(text).itertext())
def getcv():
 #u = "https://docs.opencv.org/3.1.0/d6/d6e/group__imgproc__draw.html#ga5126f47f883d730f633d74f07456c576"
 u = "http://research.twenkid.com"
 p = "url2.html"
 s = download(u, p) #"url1.html")
 s2 = open(p, "rt").read()
 #s3 = bytearray.fromhex(s2)
 s3 = removeTags(s2)
 print(s3)
 #no! must keep the tags, formatting etc. - but must understand them!


getcv()
 
 


