from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

SAMPLE_RATE = 2000

n = 17

f1 = 50
f2 = 200

# Here there are two ve


b, a = signal.iirfilter(n, [2*np.pi*f1, 2*np.pi*f2], rs=60,
                        btype='band', analog=True, ftype='cheby2')
w, h = signal.freqs(b, a, 1000)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.semilogx(w / (2*np.pi), 20 * np.log10(np.maximum(abs(h), 1e-5)))
ax.set_title('Chebyshev Type II bandpass frequency response')
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Amplitude [dB]')
ax.axis((10, 1000, -100, 10))
ax.grid(which='both', axis='both')

sos = signal.iirfilter(n, [f1, f2], rs=60, btype='band',
                       analog=False, ftype='cheby2', fs=SAMPLE_RATE,
                       output='sos')

w, h = signal.sosfreqz(sos, 2000, fs=SAMPLE_RATE)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.semilogx(w, 20 * np.log10(np.maximum(abs(h), 1e-5)))
ax.set_title('Chebyshev Type II bandpass frequency response')
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Amplitude [dB]')
ax.axis((10, 1000, -100, 10))
ax.grid(which='both', axis='both')

print(sos)

plt.show()




