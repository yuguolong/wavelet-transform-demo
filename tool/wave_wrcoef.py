import pywt
from wrcoef import wavedec, wrcoef
import numpy as np


def wave_wrcoef(signal, wavelet_type, wavelet_level):
    C, L = wavedec(signal, wavelet=wavelet_type, level=wavelet_level)
    return C, L


if __name__ == "__main__":
    signal = np.array([0, 1, 2, 3, 1, 0, 2, 4, 3, 1, 0, 3, 4, 2, 1, 0])
    wavelet_type = pywt.Wavelet('dmey')
    wavelet_level = 4
    C, L = wave_wrcoef(signal, wavelet_type, wavelet_level)

    # 重建多个信号
    for n in range(len(L)-2):
        D = wrcoef(C, L, wavelet=wavelet_type, level=n+1)
        print(n+1, D)
