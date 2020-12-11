"""
    This script is a benchmark to test different FIR filter on real time implementation (sample by sample)
    Author. Gabriel Galeote Checa
    email: gabriel@imse-cnm.csic.es
    GNU license
"""
import matplotlib.pylab as plt
import numpy as np
from scipy import signal

SAMPLE_RATE = 2000  # Hertz
DURATION = 5  # Seconds
NTAPS = 1000
SAMPLES = DURATION * SAMPLE_RATE
fs = SAMPLE_RATE

def generate_sine_wave(freq, sample_rate, duration, magnitude):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    y = magnitude * np.sin((2 * np.pi) * frequencies)
    return x, y

class IIR2Filter(object):
    """
    given a set of coefficients for the IIR filter this class creates an object that keeps the variables needed for the
    IIR filtering as well as creating the function "filter(x)" with filters the input data.
    Attributes:
        @:param coefficients: input coefficients of the IIR filter as an array of 6 elements where the first three
        coefficients are for the FIR filter part of the IIR filter and the last three coefficients are for the IIR part
        of the IIR filter.
    """

    def __init__(self, coefficients):
        self.myCoefficients = coefficients
        self.IIRcoeff = self.myCoefficients[3:6]
        self.FIRcoeff = self.myCoefficients[0:3]
        self.acc_input = 0
        self.acc_output = 0
        self.buffer1 = 0
        self.buffer2 = 0
        self.input = 0
        self.output = 0

    def filter(self, input):
        """
        :param input: input value to be processed.
        :return: processed value.
        """

        self.input = input
        self.output = 0

        """
        IIR Part of the filter:
            The accumulated input are the values of the IIR coefficients multiplied by the variables of the filter: 
            the input and the delay lines.
        """
        self.acc_input = (self.input + self.buffer1
                          * -self.IIRcoeff[1] + self.buffer2 * -self.IIRcoeff[2])

        """
        FIR Part of the filter:     
            The accumulated output are the values of the FIR coefficients multiplied by the variables of the filter: 
            the input and the delay lines. 
        
        """

        self.acc_output = (self.acc_input * self.FIRcoeff[0]
                           + self.buffer1 * self.FIRcoeff[1] + self.buffer2
                           * self.FIRcoeff[2])

        # Shifting the values on the delay line: acc_input->buffer1->buffer2
        self.buffer2 = self.buffer1
        self.buffer1 = self.acc_input
        self.input = self.acc_output
        self.output = self.acc_output
        return self.output
    
f1 = 1
f2 = 50
magnitude_1 = 1
magnitude_2 = 0.5
x, sine1 = generate_sine_wave(f1, SAMPLE_RATE, DURATION, magnitude_1)
_, noise = generate_sine_wave(f2, SAMPLE_RATE, DURATION, magnitude_2)
mysignal = sine1 + noise
plt.figure(1)
plt.plot(mysignal)

# ----------- IIR filter -------------- 
cutoff = [0.5, 45]
order = 20
fs =  2000
for i in range(len(cutoff)):
    cutoff[i] = cutoff[i]/(fs * 2)

cutoff =[0.000125, 0.01125] 
coeff = signal.butter(order, cutoff, 'bandpass', output='sos')

# If the order of the filter is 1, is one IIR 2nd order filter otherwise, it is a chain of IIR filters.

myFilter = IIR2Filter(coeff[0])

y = np.zeros(SAMPLES)
for i in range(SAMPLES):
    y[i] = myFilter.filter(mysignal[i])

# np.savetxt('coefficients.dat', b, fmt='%f', delimiter='')

plt.figure(2)
plt.subplot(211)
plt.plot(mysignal)
# plt.ylim((-150, 300))
plt.subplot(212)
plt.plot(y)
# plt.ylim((-150, 300))

unfilteredfft = np.fft.fft(mysignal)
IIRfilteredfft = np.fft.fft(y)

T = 1/SAMPLE_RATE

# 1/T = frequency
f = np.linspace(0, SAMPLE_RATE, SAMPLES)

plt.figure(3)
plt.subplot(211)
plt.plot(f[:SAMPLES // 2], np.abs(unfilteredfft)[:SAMPLES // 2] * 1 / SAMPLES)  # 1 / N is a normalization factor
# plt.plot(20.0*np.log10(unfilteredfft))
plt.subplot(212)
plt.plot(f[:SAMPLES // 2], np.abs(IIRfilteredfft)[:SAMPLES // 2] * 1 / SAMPLES)  # 1 / N is a normalization factor

print(coeff)
plt.show()