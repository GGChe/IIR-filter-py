from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams.update({'font.size': 18})
wc = 1000

order = 4
# Butterworth filter
b, a = signal.butter(order, wc, 'low', analog=True)
w, h = signal.freqs(b, a)

plt.figure(1)
plt.subplot(321)
plt.semilogx(w, 20 * np.log10(np.abs(h)))
plt.title('Butterworth')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(wc, color='green')  # cutoff frequency
plt.figure(2)
plt.subplot(321)
plt.semilogx(w, np.unwrap(np.angle(h)))
plt.axvline(wc, color='green')  # cutoff frequency
plt.title('Butterworth')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Phase [radians]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')


# Bessel filter

b, a = signal.bessel(order, wc, 'low', analog=True, norm='phase')
w, h = signal.freqs(b, a)

plt.figure(1)
plt.subplot(322)
plt.semilogx(w, 20 * np.log10(np.abs(h)))
plt.title('Bessel')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(wc, color='green')  # cutoff frequency
plt.figure(2)
plt.subplot(322)
plt.semilogx(w, np.unwrap(np.angle(h)))
plt.axvline(wc, color='green')  # cutoff frequency
plt.title('Bessel')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Phase [radians]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')

# Chebyshev 1
# rp : maximum ripple allowed below the unity gain
b, a = signal.cheby1(order, 10, wc, 'low', analog=True)
w, h = signal.freqs(b, a)

plt.figure(1)
plt.subplot(323)
plt.semilogx(w, 20 * np.log10(abs(h)))
plt.title('Chebyshev Type I')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(wc, color='green') # cutoff frequency
plt.figure(2)
plt.subplot(323)
plt.semilogx(w, np.unwrap(np.angle(h)))
plt.axvline(wc, color='green')  # cutoff frequency
plt.title('Chebyshev Type I')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Phase [radians]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')

# Chebyshev 2 or inverse of chebyshev 1
b, a = signal.cheby2(order, 10, wc, 'low', analog=True)
w, h = signal.freqs(b, a)

plt.figure(1)
plt.subplot(324)
plt.semilogx(w, 20 * np.log10(abs(h)))
plt.title('Chebyshev Type II')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(wc, color='green') # cutoff frequency
plt.figure(2)
plt.subplot(324)
plt.semilogx(w, np.unwrap(np.angle(h)))
plt.axvline(wc, color='green')  # cutoff frequency
plt.title('Chebyshev Type II')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Phase [radians]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')

# Elliptic or Cauer
b, a = signal.ellip(order, 10, 10, wc, 'low', analog=True)
w, h = signal.freqs(b, a)

plt.figure(1)
plt.subplot(325)
plt.semilogx(w, 20 * np.log10(abs(h)))
plt.title('Elliptic')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(wc, color='green') # cutoff frequency
plt.figure(2)
plt.subplot(325)
plt.semilogx(w, np.unwrap(np.angle(h)))
plt.axvline(wc, color='green')  # cutoff frequency
plt.title('Elliptic')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Phase [radians]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')

plt.tight_layout()
plt.show()

