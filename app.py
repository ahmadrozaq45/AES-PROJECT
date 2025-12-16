import streamlit as st
import numpy as np

from ui.sidebar import sidebar
from core.affine_space import random_affine_matrix
from core.sbox_generator import generate_sbox
from core.selection import valid_sbox

from analysis.nonlinearity import nonlinearity
from analysis.sac import sac
from analysis.bic import bic_nl, bic_sac
from analysis.lap import lap
from analysis.dap import dap
from analysis.ideal_score import ideal_score

from utils.excel_io import export_excel

st.set_page_config(layout="wide")

menu = sidebar()

K = random_affine_matrix()
sbox = generate_sbox(K)

if menu == "Generate S-box":
    st.title("AES S-box Modification")

    st.write("Affine Matrix (8×8)")
    st.write(K)

    st.write("Valid S-box:", valid_sbox(sbox))
    st.dataframe(np.array(sbox).reshape(16,16))

elif menu == "Strength Testing":
    st.title("S-box Strength Testing")

    results = {
        "NL": nonlinearity(sbox),
        "SAC": sac(sbox),
        "BIC-NL": bic_nl(sbox),
        "BIC-SAC": bic_sac(sbox),
        "LAP": lap(sbox),
        "DAP": dap(sbox)
    }
    results["IDEAL"] = ideal_score(results["SAC"], results["BIC-SAC"])

    st.json(results)

elif menu == "Export / Import":
    st.title("Export Result")

    data = [{
        "NL": nonlinearity(sbox),
        "SAC": sac(sbox),
        "BIC-NL": bic_nl(sbox),
        "BIC-SAC": bic_sac(sbox),
        "LAP": lap(sbox),
        "DAP": dap(sbox),
        "IDEAL": ideal_score(sac(sbox), bic_sac(sbox))
    }]

    if st.button("Download Excel"):
        export_excel(data, "sbox_results.xlsx")
        st.success("File saved: sbox_results.xlsx")
