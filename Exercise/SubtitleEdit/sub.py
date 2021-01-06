# Update FontSize for BlueRay Sup export with SubEdit
# Automatically substitute the setting in the XML config file
# Author: Todor Arnaudov, 19.12.2020
# Solution for the question of L42 for scaling Blueray sup->dvbsub subtitles with command line tools only:
# https://stackoverflow.com/questions/65038906/how-to-go-from-srt-subtitles-and-a-ts-video-to-a-ts-video-with-dvb-subtitles/65329763#65329763 
# It is applied for version 3.5.18: https://www.nikse.dk/SubtitleEdit
# The target file is Settings.xml in the root folder after installation where SubtitleEdit.exe is located (I used the portable version)
# Sample Usage: python sub.py Z:\SE3518\Settings.xml 33
# Sets the font size to 33 in the dialog for the next time Export dialog is opened (I couldn't test whether it reads from this file for the command line version but I guess so,
# the sample command doesn't produce anything without giving an error:
# SubtitleEdit.exe /convert 'test_subtitles.srt' Blu-raysup /resolution:1920x1080 /overwrite

import re, sys

# Test a regex: OK
def SubstituteTest(size):

    s = """<ExportVobSubFontSize>0</ExportVobSubFontSize>
        <ExportVobSubVideoResolution />
        <ExportVobSubLanguage />
        <ExportVobSubSimpleRendering>False</ExportVobSubSimpleRendering>
        <ExportVobAntiAliasingWithTransparency>True</ExportVobAntiAliasingWithTransparency>
        <ExportBluRayFontName>Arial</ExportBluRayFontName>
        <ExportBluRayFontSize>40</ExportBluRayFontSize>
        <ExportFcpFontName />
        <ExportFontNameOther>Arial</ExportFontNameOther>
        <ExportFcpFontSize>20</ExportFcpFontSize>
        <ExportFcpImageType>Bmp</ExportFcpImageType>
        <ExportFcpPalNtsc>PAL</ExportFcpPalNtsc>
        <ExportBdnXmlImageType>Png 32-bit</ExportBdnXmlImageType>
        <ExportLastFontSize>30</ExportLastFontSize>
        <ExportLastLineHeight>28</ExportLastLineHeight>
        <ExportLastBorderWidth>4</ExportLastBorderWidth>
        <ExportLastFontBold>False</ExportLastFontBold>
        <ExportBluRayVideoResolution>2048x858</ExportBluRayVideoResolution>
        <ExportFcpVideoResolution />"""

    fontSize = size
    print(s)
    p1 = "<ExportBluRayFontSize>(.+)</ExportBluRayFontSize>"
    p2 = "<ExportBluRayFontSize>"+str(fontSize)+"</ExportBluRayFontSize>"
    res = re.search(p1, s, re.MULTILINE)
    print(res)
    print(res.group(0))
    print(res.group(1))
    res = re.sub(p1,p2,s) #re.MULTILINE)
    print(res)

# Adjust nonsense errors with the encoding and the console
#https://stackoverflow.com/questions/31469707/changing-the-locale-preferred-encoding-in-python-3-in-windows
def getpreferredencoding(do_setlocale = True):
    return "utf-8"

# The nonsense console encoding issues
def Encoding():    
    import sys, locale, os
    print(sys.stdout.encoding)
    print(sys.stdout.isatty())
    print(locale.getpreferredencoding())
    print(sys.getfilesystemencoding())
    #print(os.environ["PYTHONIOENCODING"]) # not found
    #print(locale.setpreferredencoding('utf-8')) # no such function - a hack, see above
    print(locale.getpreferredencoding())
    #print(chr(246), chr(9786), chr(9787)) # error sometimes if cp1252 as default encoding
    
# Test replace on another file
def SubstituteToFileTest(path, size):   
    Encoding()
    #import sys
    #sys.setdefaultencoding('utf8')
    with open (path, "rb") as f:
      b = f.read()
    s = b.decode(encoding='utf-8')       
    print(s)
    fontSize = size   
    p1 = "<ExportBluRayFontSize>(.+)</ExportBluRayFontSize>"
    p2 = "<ExportBluRayFontSize>"+str(fontSize)+"</ExportBluRayFontSize>"
    res = re.search(p1, s, re.MULTILINE)
    print(res)
    print(res.group(0))
    print(res.group(1))
    res = re.sub(p1,p2,s) 
    print(res)
    f = open("out.xml", "wb") # Adjust paths etc. 
    f.write(bytes(res, encoding="utf-8"))
    f.close()
   
# Write to the file
def SubstituteXML(path, size):   
    Encoding()
    #import sys
    #sys.setdefaultencoding('utf8')
    with open (path, "rb") as f:
      b = f.read()
    s = b.decode(encoding='utf-8')       
    print(s)
    fontSize = size
    p1 = "<ExportBluRayFontSize>(.+)</ExportBluRayFontSize>"
    p2 = "<ExportBluRayFontSize>"+str(fontSize)+"</ExportBluRayFontSize>"
    res = re.search(p1, s, re.MULTILINE)
    print(res)
    print(res.group(0))
    print(res.group(1))
    res = re.sub(p1,p2,s)
    print(res)
    f = open(path, "wb") 
    f.write(bytes(res, encoding="utf-8"))
    f.close()
    
def Sub():    
  Substitute(r"Z:\SE3518\Settings.xml", 33)
  
if __name__ == '__main__':	
  print(sys.argv)
  if len(sys.argv)!=3:
      print("Parameters: Path-to-SE-XML(3.518)  Font_Size")
      exit(0)
  SubstituteXML(sys.argv[1], sys.argv[2])
  
