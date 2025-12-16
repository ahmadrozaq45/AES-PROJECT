import numpy as np

def nonlinearity(sbox):
    nls = []
    for bit in range(8):
        f = np.array([(x >> bit) & 1 for x in sbox])
        walsh = np.abs(np.fft.fft(1 - 2*f))
        nls.append(128 - max(walsh)/2)
    return int(min(nls))
