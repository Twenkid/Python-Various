
f = open("all.txt")
s = f.readlines();


f.close()

fout = open("allout1.txt", 'w')

o = []
outPath = 'S:\\BACKUP!!!\\WD\\L\\Canon\\All\\'
quote = "\""
for x in s:
  #x.replace('\\', '\\\\')  
  #print(x)
  #if x.rfind('MVI') > -1: ix = x.rindex('MVI');  
  x = x.strip();
  if x.rfind('MVI') > -1: ix = x.rindex('MVI');    
  else: ix = -1
  if x.rfind('THM') > -1: ix = -1
  
  fn = x[ix:]
  #if ix != None: fn = x[ix:]
  #else: fn = "NONE"
  
  #if (x.rfind("avi")): o = o + ["VirtualDub.Open(" + x + "); " + "VirtualDub.SaveAVI(" + outPath + fn + ");\n" ]
  
  if ix != -1:
    
	#if (x.rfind("avi")): so = "VirtualDub.Open(\"" + x + "\"" + "); VirtualDub.SaveAVI(" + quote + outPath + fn + quote + ");"
	
    if (x.rfind("avi")): so = "VirtualDub.Open(" + quote + x + quote + "); VirtualDub.SaveAVI(" + quote + outPath + fn + quote + ");" + "\r\n";
	
    print(so)
    fout.write(so)
	
fout.close();
 
#print(o)
 
   
 