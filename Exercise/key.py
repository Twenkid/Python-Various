import msvcrt
import time
# Windows Get key, example from Stackoverflow+;
# time.sleep is in seconds! (not millisec! as usual thread sleep!)
# Todor

while True:
  if msvcrt.kbhit():
           key = msvcrt.getch()
           print(key)
           if key=='q': break #doesn't detect it?
           #if key==ord('q'): break
           else: print("not Q?")
           time.sleep(0.033)		             