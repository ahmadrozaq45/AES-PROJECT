import streamlit as st

def sidebar():
    st.sidebar.title("AES S-box Project")
    return st.sidebar.radio(
        "Menu",
        ["Generate S-box", "Strength Testing", "Export / Import"]
    )
