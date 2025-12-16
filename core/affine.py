import numpy as np

def affine_transform(x_inv, K, C):
    x_bin = np.array([(x_inv >> i) & 1 for i in range(7, -1, -1)])
    result = (K @ x_bin) % 2
    result = (result + C) % 2

    out = 0
    for bit in result:
        out = (out << 1) | int(bit)
    return out
