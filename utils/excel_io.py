import pandas as pd

def export_excel(data, filename):
    pd.DataFrame(data).to_excel(filename, index=False)

def import_excel(file):
    return pd.read_excel(file)
