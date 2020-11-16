import cv2
import numpy as np

w = 800; h = 600; 
background = np.zeros((h,w,3), np.uint8)

x1,y1 = 50,50
w1,h1 = 150,150
cv2.rectangle(background, (x1, y1), (x1+w1,y1+h1), (0,0,255), 2)

x,y = x1,y1
squares = 3
#sx = (int) (w1/squares); sy=(int) (h1/squares);
sx =  (w1/squares); sy= (h1/squares);

for i in range(squares):  
    for j in range(squares):
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

