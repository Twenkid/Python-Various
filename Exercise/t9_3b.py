#t9_3b.py ... Copy segments of mp4 or whatever videos or media files
# Set path to ffmpeg etc. ...
# Walk directory, recursively, collect paths
# Author: Todor Arnaudov

videos = []
commands = []
ffmpeg_path = "C:\Incept\FusenReceiver\ffmpeg"
import os

def walkExample(path, list, ext='mp4'):	#22-3-2016 from ...
	print("WALK["+path+"]")
	for root, dirs, files in os.walk(path, topdown=False):
		print("FILES============")
		for name in files:
			print("FILE["+name+"]")
			s = os.path.join(root, name);
			#print(s.encode(encoding='utf-8'))
			
			if (s.endswith(ext)):	list.append(s);	print(s)	#collect the files ending with extension "ext"
			
		for name in dirs:
			print("DIRS============["+name+"]")
			j = os.path.join(root, name)
			#print(j.encode(encoding='utf-8'))
			
			#print(j.encode(encoding='windows-1251'))
			k = " ";
			k = str(j.encode(encoding='windows-1251'))	
			walkExample(os.path.join(path,name), list, ext)            
			
			#print(k[2:]) #remove the:  b'
def ffmpeg(paths):
				#c = C:\ffmpeg\ffmpeg.exe -i "C:\video\edi_koe_si_v_guza_hd.mp4" -ss 600 -c copy -t 60 otryazanoVideoKopirano.mp4
				for p in paths:
								new = p[:-4] + "_cut" + ".mp4"
								c = "C:\\Incept\\FusenReceiver\\ffmpeg\\ffmpeg.exe" + " -i " + "\"" + p + "\"" + " -ss 600 -c copy -t3600 ";
								c = c + new;
								print(c)
								commands.append(c)
																										
#walkExample('b:\\tor\\', videos, 'mp4')
walkExample('D:\\Code\\', videos, '*')
#ffmpeg(videos)
