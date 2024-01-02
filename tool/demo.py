import pywt
from wrcoef import wavedec, wrcoef
import numpy as np
import matplotlib.pyplot as plt


wavelet_type = 'dmey'
wavelet_level = 4

# Generate input data
signal = np.array([0, 1, 2, 3, 1, 0, 2, 4, 3, 1, 0, 3, 4, 2, 1, 0])
# Define wavelet
w = pywt.Wavelet(wavelet_type)
# Decompose input signal
# C, L = wavedec(signal, wavelet=w, level=wavelet_level, mode="periodic")
C, L = wavedec(signal, wavelet=w, level=wavelet_level)


t = [x for x in range(len(signal))]
plt.figure(figsize=(8, 7))
plt.subplot(6, 1, 1)
plt.plot(t, signal)
plt.title('Original Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

# Reconstruct all the coefficients
for n in range(len(L)-2):
    D = wrcoef(C, L, wavelet=w, level=n+1)
    print(n+1, D)
    plt.subplot(6, 1, n+2)
    plt.plot(t, D)
    plt.title(f'Wavelet Coefficients - Level {n+1}')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
