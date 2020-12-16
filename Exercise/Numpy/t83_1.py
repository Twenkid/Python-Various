#t83_1.py
#numpy Tutorial 
#15-4-2016

import numpy as np

time = np.linspace(20, 145, 5)                 # time scale  #+ generates series from 20 to 145 in 5 steps, double
data = np.sin(np.arange(20)).reshape(5,4)      # 4 time-dependent series

#20 elements, 5 rows x 4 columns ... sinus of 0, 1, 2, 3, ... 19  -- sin(0), sin(1) ...


print(time)
print(data)


ind = data.argmax(axis=0)                   # index of the maxima for each series
# ahaaa ... vertical ...
print("axis=0")
print(ind)
#print(data[ind])

ind2 = data.argmax(axis=1)                   # index of the maxima for each series
# ahaaa ... vertical ...
print("axis=1")
print(ind2)

#Брои индексите ВЕРТИКАЛНО на това което показва с печатането!


#ind
#array([2, 0, 3, 1])
print("time_max... ind")
time_max = time[ ind]                       # times corresponding to the maxima
print(time_max)
data_max = data[ind, xrange(data.shape[1])] # => data[ind[0],0], data[ind[1],1]...
print(data_max)


print(type(data_max))
print(type(data))
# no -- errors
#print("time_max... ind2")
#time_max2 = time[ ind2]                       # times corresponding to the maxima
#print(time_max2)
#data_max2 = data[ind2, xrange(data.shape[1])] # => data[ind[0],0], data[ind[1],1]...
#print(data_max2)


#time_max
#array([  82.5 ,   20.  ,  113.75,   51.25])
# data_max
#array([ 0.98935825,  0.84147098,  0.99060736,  0.6569866 ])
#
# np.all(data_max == data.max(axis=0))
#True


import numpy as np
import matplotlib.pyplot as plt
# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
mu, sigma = 2, 0.5
v = np.random.normal(mu,sigma,100)
# Plot a normalized histogram with 50 bins
plt.hist(v, bins=10, normed=1)       # matplotlib version (plot)
plt.show()

#v2 = np.linspace(20, 145, 0.35)
#v3 = np.linspace(10, 100, 1)
#v4 = np.ndarray(v2, 3)
mu, sigma = 4, 0.2
#v4 = np.random.
v4 = np.random.poisson(size=1000)
plt.hist(data, bins=2, normed=1.0)       # matplotlib version (plot)
plt.show()

