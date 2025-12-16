def sac(sbox):
    total = 0
    for x in range(256):
        for i in range(8):
            diff = sbox[x] ^ sbox[x ^ (1 << i)]
            total += bin(diff).count("1")
    return total / (256 * 8 * 8)
