from analysis.nonlinearity import nonlinearity
from analysis.sac import sac

def bic_nl(sbox):
    return nonlinearity(sbox)

def bic_sac(sbox):
    return sac(sbox)
