#open images, subprocess, irfan view
#Author: Todor
import os
print (os.curdir)
f = open("termlist.txt", 'rt')
list = f.readlines()
f.close()

print(list)

import subprocess
cwdNow = r"S:\Code\Python\\";

for n in list: subprocess.call([r"C:\Program Files\IrfanView\i_view32.exe", n.strip()], cwd=cwdNow)	
#for n in list: print(n);print(n.strip())

#C:\Program Files\IrfanView441\i_view32.exe

