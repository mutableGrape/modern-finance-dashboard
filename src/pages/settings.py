import streamlit as st
import pandas as pd
from langchain.llms.ollama import Ollama
from entity.pot_entity import Account

def load_data(file):
    if file.name.endswith(".csv"):
        df = pd.read_csv(file, encoding='utf-8')
    elif file.name.endswith(".xlsx"):
        df = pd.read_excel(file)
    else:
        return st.error("Invalid file format. Please upload a CSV or Excel file.")
    
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    return df

def file_stuff():
    def handle_upload():
        uploaded_files = st.file_uploader("Upload your datasets", type=["csv", "xlsx"], accept_multiple_files=True)
        if uploaded_files:
            datasets = []
            for uploaded_file in uploaded_files:
                data = load_data(uploaded_file)
                account = Account(name=uploaded_file.name, data=data)
                datasets.append(account)
            st.session_state.finance_data += datasets
        else:
            st.warning("No files uploaded")

    st.header("Upload Datasets")
    handle_upload()
    display_uploaded_files()

def display_uploaded_files():
    st.subheader("Uploaded Files")
    for uploaded_file in st.session_state.finance_data:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(uploaded_file.name)
        with col2:
            if st.button('x', key=uploaded_file.name):
                st.session_state.finance_data.remove(uploaded_file)
                st.rerun()

def llm_stuff():
    # LLM model selection
    st.header("Select LLM Model")
    llm_models = ["llama3"]
    llm_model_choice = st.selectbox("Choose a model", llm_models)
    message_container = st.empty()

    def set_llm():
        if "chat_llm" not in st.session_state:
            st.session_state.chat_llm = Ollama(model="llama3")
        else:
            st.session_state.chat_llm = Ollama(model=llm_model_choice)
        message_container.success(f"Selected model: {llm_model_choice}")
    
    set_llm()

file_stuff()
llm_stuff()
