import streamlit as st

if "finance_data" not in st.session_state:
    st.session_state.finance_data = []
