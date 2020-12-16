# Computes the number of pixels for different resolutions, for 24-bit color (bitmap)
# Todor
m = 16 #multiplier
p = 3 #per pixel
for i in range(1,129): 
  for j in range(1,129):
    print(str(i*m) +"x" +str(j*m) +"\t" + str(i*m*j*m) + "\t" + str(i*j*m*m*p) + "\n");
	
