import pandas as pd

def show_sbox(sbox):
    df = pd.DataFrame(sbox).values.reshape(16,16)
    return df
