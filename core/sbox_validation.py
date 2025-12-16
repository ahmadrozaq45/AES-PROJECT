def is_bijective(sbox):
    return len(set(sbox)) == 256 and min(sbox) >= 0 and max(sbox) <= 255

def is_balanced(sbox):
    for bit in range(8):
        ones = sum((v >> bit) & 1 for v in sbox)
        if ones != 128:
            return False
    return True
