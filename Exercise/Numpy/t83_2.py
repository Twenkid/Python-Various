#t83_1.py
#numpy Tutorial 
#15-4-2016

import numpy as np

np.fft.fft(np.exp(2j * np.pi * np.arange(8) / 8))

import matplotlib.pyplot as plt
t = np.arange(256)
sp = np.fft.fft(np.sin(t))
freq = np.fft.fftfreq(t.shape[-1])
plt.plot(freq, sp.real, freq, sp.imag)

plt.show()