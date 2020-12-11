#t62.py
#html 

import sys

def imgs(template,connect, start,end,extension):
	i = (int)(start)
	k = (int) (end)
	while i<=k:
		print("<img src=\"" + template +connect+str(i) + "." + extension+"\"><br>")
		i=i+1
		
#while i<272:
   #print("<a href=\"#"+str(i)+"\">" + str(i) + "</a>" + "nbsp; ")
   #i=i+1
   
if __name__ == '__main__':
	if (len(sys.argv)<5):	print('Usage: template,connect, start,end,extension -- e.g: \'snimka\'\t\'-\'\t1\t 5\tjpg\t<br>\n\n==> <img src="snimka-1.jpg", ... \nsnimka-2.jpg\n ..., snimka-5.jpg\n')
	else:	imgs(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]);
	
	#sys.argv[6]);
  #if (sys.argv[1]=='-c'):
  #  copyseg(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
  #elif (sys.argv[1]=='-i'): inputtest()  
  #else: print('Usage: -c src dst start size - copies a segment of file')   
  
   
   

   