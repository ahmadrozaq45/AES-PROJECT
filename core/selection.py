from core.sbox_validation import is_balanced, is_bijective

def valid_sbox(sbox):
    return is_balanced(sbox) and is_bijective(sbox)
