import cv2
import numpy as np
#16-6-2017+

def help(): print("<->Q,W| A,S| ESC")

def loadImage():
  pass
  
def grid1():
  w = 800; h = 600; 
  background = np.zeros((h,w,3), np.uint8)

  x1,y1 = 50,50
  w1,h1 = 400,300
  cv2.rectangle(background, (x1, y1), (x1+w1,y1+h1), (0,0,255), 2)

  x,y = x1,y1
  cells = (40,30)
  #sx = (int) (w1/squares); sy=(int) (h1/squares);
  sx =  (w1/cells[0]); sy= (h1/cells[1]);

  for j in range(cells[1]):  
    for i in range(cells[0]):
      xi = x + (int)(sx); yi = y + (int) (sy)	  
      cv2.rectangle(background, (x, y), (xi, yi), (0,0,255), 1)
	  #push rectangle ... Arrea ...
      x=x+(int)(sx)
    x = (int)(x1)
    y = (int)(y + sy)
	
  # x,y = 1,1 .. -1, ...
  
  cv2.imshow("Le1", background)

  cv2.waitKey(0)
  cv2.destroyAllWindows()


#def drawText(image, x1, y1, cx, cy, col=(255,255,255),scale=0.5, 1width=1):
   #font = cv2.FONT_HERSHEY_SIMPLEX
 #  cv2.putText(image,str(cx)+', '+str(cy),(x1,y1), cv2.FONT_HERSHEY_SIMPLEX, scale,col,width,cv2.LINE_AA) 
   
def drawIndications(image, x1, y1, cx, cy, col=(255,255,255),scale=0.5,width=1):
   #font = cv2.FONT_HERSHEY_SIMPLEX
   cv2.putText(image,str(cx)+', '+str(cy),(x1,y1), cv2.FONT_HERSHEY_SIMPLEX, scale,col,width,cv2.LINE_AA) 
#also remember the last values,class, state, ...! 

def grid2(image, wi=600,hi=450,cx=20,cy=15,c=(255,255,255)):  
  step = 36 #under the grid
  x1,y1 = 20,20
  w1,h1 = wi,hi
  pad = 3
  cv2.rectangle(image, (x1, y1), (x1+w1,y1+h1), c, 3)

  x,y = x1,y1
  cells = (cx,cy)
  #sx = (int) (w1/squares); sy=(int) (h1/squares);
  sx =  (w1/cells[0]); sy= (h1/cells[1]);
  xi = x; yi = y;
  halfsx = int(sx/2); halfsy = int(sy/2)
  
  for j in range(cells[1]):  
    for i in range(cells[0]):      
      xi = x + (int)(sx); yi = y + (int)(sy)	  
      cv2.rectangle(image, (x, y), (xi, yi), (0,0,255), 1)     
      cv2.putText(image,str(i)+','+str(j),(xi+pad+int(halfsx-sx),yi+pad+int(halfsy-sy)), cv2.FONT_HERSHEY_SIMPLEX,0.4,(200,200,200),1,cv2.LINE_AA) 
      #push rectangle ... Arrea ...
      x=x+(int)(sx)
    x = (int)(x1)

    y = (int)(y + sy)	
  # x,y = 1,1 .. -1, ...
  drawIndications(image, x1, y1+h1+step, cx, cy)
    
#def clearImage(image):
  #image = np.zeros(image.shape, np.uint8);
  #return image
  
def createImage(w=800, h=600):
  global image;
  image =  background = np.zeros((h,w,3), np.uint8);
  return image  
  
def createWindow(title, image):
  return cv2.imshow(title, image)
  
  
def v2():
  help()
  title="grid"
  image = createImage()
  window = createWindow(title, image)
  
  gain_step=1
  
  cx = 30; cy = 20 #cells
  while(True):  
    image = np.zeros(image.shape, np.uint8); #clearImage(image)
    k = cv2.waitKey(30) & 0xFF    
    #if(k==ord('q')): break
    if (k==27): break
    elif (k==ord('w')): cx += gain_step
    elif (k==ord('q')): cx -= gain_step    
    elif (k==ord('s')): cy +=gain_step # = 0.1
    elif (k==ord('a')): cy -= gain_step # gain_step = -0.1 	
    elif (k==ord('1')): loadImage()
    elif (k==ord('h')): help()
    #elif (k==ord('x')): gain = gain + gain_step # = 0.1
    #elif (k==ord('z')): gain = gain - gain_step # gain_step = -0.1
    if (cx<1): cx=1 
    if (cy<1): cy=1
    grid2(image,cx=cx, cy=cy)
    cv2.imshow(title, image)
	
	
 #cv2.waitKey(0)
  cv2.destroyAllWindows() 
'''	
    elif (k==ord('x')): gain = gain + gain_step # = 0.1
    elif (k==ord('z')): gain = gain - gain_step # gain_step = -0.1
    elif (k==ord('v')): sat = sat + gain_step # = 0.1
    elif (k==ord('c')): sat = sat - gain_step # gain_step = -0.1 
    elif (k==ord('n')): fps = fps + 1; cap.set(5,fps) # = 0.1
    elif (k==ord('b')): fps = fps - 1; cap.set(5,fps)  # gain_step = -0.1 
    elif (k==ord('r')): x = 0.0;
    elif (k==ord('z')): change_gain = False
'''
   
#grid1()
v2()

