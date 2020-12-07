#t9_4.py ... Copy segments of mp4 or whatever videos or media files or apply other processing
#Set path to ffmpeg etc. ...
#print(s.encode(encoding='utf-8'));  #print(j.encode(encoding='utf-8')); 	#print(j.encode(encoding='windows-1251')); #print(k[2:]) #remove the:  b'
#>>>python t9_4.py > ff.bat   ...   >>>ff.bat
#ffmpeg ... copy generate commands ... crop ...
#Author: (C) Todor Arnaudov, 2014?, 2016, 7.12.2020 (recursive iteration)

videos = []
commands = []
commands2 = []
ffmpeg_path = "C:\\Incept\\FusenReceiver\\ffmpeg\\ffmpeg.exe"
bPrintDirs = False
#ffplay_path_dir = "C:\\Incept\\FusenReceiver\\ffmpeg\\";
ffplay_path_dir = "C:\\Incept\\FusenReceiver\\ffmpeg\\ffplay.exe";
#ffplay.exe

import re

def findDuration(text):
	#pattern = 'Duration:\s(\d\d):(\d\d):(\d\d)\.(\d\d)'
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

	try:
		m1 = re.search(pattern, text) #, re.UNICODE)
		#print(m1.group(0))
		print(m1.group(1))
		print(m1.group(2))
		print(m1.group(3))
		print(m1.group(4))
	except:
			return 0	#not found

	seconds = 1 + int(m1.group(3)) + int(m1.group(2))*60

	half = seconds/2

	back = 60
	if (half<60): back = 30

	else: back=60

	print("Seconds = " + str(seconds) + ", Half = " + str(seconds/2))

	start = half - back
	if (start < 0): start = 0

	print("One minute (or half) earlier than the middle = ", str(start)) #str(half - back))
	return start

def printDirs(dirs):
	for name in dirs:
			print("DIRS============")
			j = os.path.join(root, name)						
			k = " ";
			k = str(j.encode(encoding='windows-1251'))	
			print(k[2:]) #removes the:  b'
		
def walkExample(path, list, ext='mp4'):	#22-3-2016 from ...
	import os
	for root, dirs, files in os.walk(path, topdown=False):
		#print("FILES============")
		for name in files:
			s = os.path.join(root, name);						
			if (s.endswith(ext)):	list.append(s);	print(s)	#collect the files ending with extension "ext"
			if (bPrintDirs):	printDirs(dirs)
        for name in dirs: #RECURSIVE 7-12-2020
			print("DIRS============["+name+"]")
			#j = os.path.join(root, name)
			walkExample(os.path.join(path,name), list, ext)        
					
def ffmpeg(paths, ext):								
				import os, time, re
				#pattern = re.compile('Duration.(\dd):(\dd):(\dd):(\dd)')
				
				for p in paths:
								new = p[:-4] + "_cut" + "." + ext; #".mp4"
								c = ffmpeg_path + " -i " + "\"" + p + "\"" + " -ss 600 -c copy -t3600 ";
								c = c + new;
								print(c)
								commands.append(c)
								#fullPath = fullPath.replace("\\\\", "\\") #no
								#print('FULLPATH = ' + fullPath)
								##os.execl(fullPath, " ") #no  
								
								#os.startfile(fullPath)  -- no information for the state
								print(ffplay_path_dir)
								
								#os.spawnv(os.P_WAIT, ffplay_path_dir, ['-i', p, '  '])
								
								#os.spawnv(os.P_NOWAIT, ffplay_path_dir, ['-i', p, '  '])
								
								from subprocess import Popen, PIPE, STDOUT
								try:
									####subprocess.call([п1, tlsk[1], tlsk[2]]) # ... more flexible -- tlsk[1] ... parameters 	
									#cmd = 'ls /etc/fstab /etc/non-existent-file'		
									pid = Popen(ffplay_path_dir + " -i " + p, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=False)
									print("Popen(" + ffplay_path_dir + "..." + str(p) + ", PID = " + str(pid))
									time.sleep(6)
									
									
									print('======== STDOUT =========')
									text = " "
									for line in pid.stdout:
										line2 = line.rstrip()			
										#s = line.decode(encoding='utf-8')#str(line)
										line3 = line2.decode(encoding='windows-1251')#str(line)
										text = text + line3
										#print(p.stdout.decode('utf-8'))
										print(line3)
										#п4 = п4 + п5 + "\n"
										#в6([line,'utf-8'])
									#воля_наглед[п1] = п4	#натрупва всички редове, ако има
									
									
									#regex
									
									#found = re.search(pattern, text)
									
									print(text)
									start = findDuration(text)
									print("================")
									print("START FROM: " + str(start))
									print("================")
									
															
									new = p[:-4] + "_cut" + "." + ext; #".mp4"
									c = ffmpeg_path + " -i " + "\"" + p + "\"" + " -ss ";
									c = c + str(start) + " -c copy -t5400 ";
									c = c + new;
									print(c)
									commands2.append(c)
								
									#m = re.match('Duration.(\dd):(\dd):(\dd):(\dd)', text)
																		
									#try:
										#print(found.group(0), found.group(1),found.group(2),found.group(3), found.group(4))
									#except:
									#		print(found.group(0) + '\nNot found 4 groups')
									
									
									
									pid.kill()

								except:
									import sys
									print('EXCEPTION')
									print(sys.exc_info())
									
									#new = p[:-4] + "_cut" + "." + ext; #".mp4"
									#c = ffmpeg_path + " -i " + "\"" + p + "\"" + " -ss ";
									#c = c + str(start) + " -c copy -t5400 ";
									#c = c + new;
									#print(c)
									
									#commands2.append(c)
									
									pid.kill()
									
			
								
								#time.sleep(6)
								
								
								#read output ... Duration ... re
								
								
								
								
				#c = C:\ffmpeg\ffmpeg.exe -i "C:\video\edi_koe_si_v_guza_hd.mp4" -ss 600 -c copy -t 60 otryazanoVideoKopirano.mp4
				#c = "C:\\Incept\\FusenReceiver\\ffmpeg\\ffmpeg.exe" + " -i " + "\"" + p + "\"" + " -ss 600 -c copy -t3600 ";
																										
import sys
root = '.'	#current dir if no input given
ext = 'mp4';
if (len(sys.argv)>1):	root = sys.argv[1]
if (len(sys.argv)>2):	ext = sys.argv[2]
#if (len(sys.argv)==1):	
print("REM: Usage: path extension. If none (or one) given, using default path:  . (current dir) and extension: " + ext + ".\n" + sys.argv[0] +"\n");
print("REM: Now using: " + root + "\n" + ext + "\n")
#walkExample('b:\\tor\\', videos, 'mp4')

walkExample(root, videos, ext)
ffmpeg(videos, ext)

print("======================")
for s in commands2:	print(s)


