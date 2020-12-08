import re
text = """ Metadata:
   major_brand     : isom
   minor_version   : 512
   compatible_brands: isomiso2avc1mp41
   encoder         : Lavf55.0.100
 Duration: 00:01:10.01, start: 0.013991, bitrate: 4751 kb/s
   Stream #0:0(und): Video: h264 (Constrained Baseline) (avc1 / 0x31637661), yu
420p, 1920x1080 [SAR 1:1 DAR 16:9], 4625 kb/s, 59.94 fps, 59.94 tbr, 60k tbn, 1
9.88 tbc
   Metadata:
     handler_name    : VideoHandler"""
	 
#pattern = 'Duration.(\d\d).(\d\d).(\d\d).(\d\d)'
pattern = 'Duration:\s(\d\d):(\d\d):(\d\d)\.(\d\d)'
pattern = '(\d\d):(\d\d):(\d\d)\.(\d\d)'
#pattern = '.' #uration.(\d\d)'

m = re.search(pattern, text)#, re.UNICODE) #re.MULTILINE)
#print(m)
#print(str(m))
#print(str(m.group(0)))
print(m.group(0))

#m1 = re.search('(?<=-)\w+', 'spam-egg') #, re.UNICODE)
#m1 = re.search('a', 'bdefaghee')
#print(m1.group(0))	#OK

m1 = re.search(pattern, text) #, re.UNICODE)
#print(m1.group(0))
print(m1.group(1))
print(m1.group(2))
print(m1.group(3))
print(m1.group(4))

seconds = 1 + int(m1.group(3)) + int(m1.group(2))*60

half = seconds/2

back = 60
if (half<60): back = 30

else: back=60

print("Seconds = " + str(seconds) + ", Half = " + str(seconds/2))

start = half - back
if (start < 0): start = 0

print("One minute (or half) earlier than the middle = ", str(start)) #str(half - back))

