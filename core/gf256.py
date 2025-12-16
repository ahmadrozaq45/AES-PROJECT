IRREDUCIBLE = 0x11B

def gf_mult(a, b):
    res = 0
    for _ in range(8):
        if b & 1:
            res ^= a
        hi = a & 0x80
        a <<= 1
        if hi:
            a ^= IRREDUCIBLE
        a &= 0xFF
        b >>= 1
    return res

def gf_inverse(a):
    if a == 0:
        return 0
    for i in range(1, 256):
        if gf_mult(a, i) == 1:
            return i
    return 0
