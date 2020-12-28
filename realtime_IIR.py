"""
    This script is a benchmark to test different FIR filter on real time implementation (sample by sample)
    Author. Gabriel Galeote Checa
    email: gabriel@imse-cnm.csic.es
    GNU license
"""
import matplotlib.pylab as plt
import numpy as np
from scipy import signal
import iir

fs = 2000  # Hertz

def generate_sine_wave(freq, sample_rate, duration, magnitude):
    x = np.linspace(0, duration, fs * duration, endpoint=False)
    frequencies = x * freq
    y = magnitude * np.sin((2 * np.pi) * frequencies)
    return x, y
    
# Generate 2 sinusoidal waves with a frequencies of 1 and 50 Hz for test
f1 = 1
f2 = 50
magnitude_1 = 1
magnitude_2 = 0.5
DURATION = 5  # Seconds
x, sine1 = generate_sine_wave(f1, fs, DURATION, magnitude_1)
_, noise = generate_sine_wave(f2, fs, DURATION, magnitude_2)
mysignal = sine1 + noise

plt.figure(1)
plt.plot(mysignal)

# ----------- IIR filter -------------- 
order = 20
fs =  2000
f1 = 0.5 /(fs * 2)
f2 = 45 /(fs * 2)

cutoff =[0.000125, 0.01125] 

coeff = signal.butter(order, cutoff, 'bandpass', output='sos')

# If the order of the filter is 1, is one IIR 2nd order filter otherwise, it is a chain of IIR filters.
SAMPLES = DURATION * fs

myFilter = iir.IIR_filter(coeff)
y = np.zeros(SAMPLES)
for i in range(SAMPLES):
    y[i] = myFilter.filter(mysignal[i])

# Now plot original and filtered signal
plt.figure(2)
plt.subplot(211)
plt.plot(mysignal)
# plt.ylim((-150, 300))
plt.subplot(212)
plt.plot(y)
# plt.ylim((-150, 300))

# Calculate the fourier trasnform 
unfilteredfft = np.fft.fft(mysignal)
IIRfilteredfft = np.fft.fft(y)

T = 1/fs
f = np.linspace(0, fs, SAMPLES)

plt.figure(3)
plt.subplot(211)
plt.plot(f[:SAMPLES // 2], np.abs(unfilteredfft)[:SAMPLES // 2] * 1 / SAMPLES)  
plt.subplot(212)
plt.plot(f[:SAMPLES // 2], np.abs(IIRfilteredfft)[:SAMPLES // 2] * 1 / SAMPLES) # 1 / N is a normalization factor

np.savetxt('coefficients.dat', b, fmt='%f', delimiter='')

plt.show()