def dap(sbox):
    max_p = 0
    for dx in range(1, 256):
        table = {}
        for x in range(256):
            dy = sbox[x] ^ sbox[x ^ dx]
            table[dy] = table.get(dy, 0) + 1
        max_p = max(max_p, max(table.values()) / 256)
    return max_p
