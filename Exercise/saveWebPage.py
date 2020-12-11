import os, sys
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import re
# https://stackoverflow.com/questions/1825438/download-html-page-and-its-content
# cmd Admin ...
# python -m pip install BeautifulSoup4
# python -m pip install lxml (could, parser)

def savePage(url, pagefilename='page'):
    def soupfindnSave(pagefolder, tag2find='img', inner='src'):
        """saves on specified `pagefolder` all tag2find objects"""
        if not os.path.exists(pagefolder): # create only once
            os.mkdir(pagefolder)
        for res in soup.findAll(tag2find):   # images, css, etc..
            try:         
                if not res.has_attr(inner): # check if inner tag (file object) exists
                    continue # may or may not exist
                filename = re.sub('\W+', '', os.path.basename(res[inner])) # clean special chars
                fileurl = urljoin(url, res.get(inner))
                filepath = os.path.join(pagefolder, filename)
                # rename html ref so can move html and folder of files anywhere
                res[inner] = os.path.join(os.path.basename(pagefolder), filename)
                if not os.path.isfile(filepath): # was not downloaded
                    with open(filepath, 'wb') as file:
                        filebin = session.get(fileurl)
                        file.write(filebin.content)
            except Exception as exc:
                print(exc, file=sys.stderr)
        return soup
    
    session = requests.Session()
    #... whatever other requests config you need here
    response = session.get(url)
    #soup = BeautifulSoup(response.text, features="lxml")
    soup = BeautifulSoup(response.text,  "html.parser")
    pagefolder = pagefilename+'_files' # page contents
    soup = soupfindnSave(pagefolder, 'img', 'src')
    soup = soupfindnSave(pagefolder, 'link', 'href')
    soup = soupfindnSave(pagefolder, 'script', 'src')
    with open(pagefilename+'.html', 'wb') as file:
        file.write(soup.prettify('utf-8'))
    return soup
    
#soup = savePage('https://www.twenkid.com', 'google') #cyr bad
soup = savePage('https://www.abv.bg', 'abv') #OK

#extenstions - missing . 

