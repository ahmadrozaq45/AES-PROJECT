def sub_bytes(state, sbox):
    return [sbox[b] for b in state]

def inv_sub_bytes(state, inv_sbox):
    return [inv_sbox[b] for b in state]

def inverse_sbox(sbox):
    inv = [0]*256
    for i, v in enumerate(sbox):
        inv[v] = i
    return inv
