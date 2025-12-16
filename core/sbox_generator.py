import numpy as np
from core.gf256 import gf_inverse
from core.affine import affine_transform
from data.constants import CAES

def generate_sbox(K):
    C = np.array(CAES)
    sbox = []

    for x in range(256):
        x_inv = gf_inverse(x)
        sbox.append(affine_transform(x_inv, K, C))

    return sbox
