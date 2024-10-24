import streamlit as st
import pandas as pd
import os
from langchain_community.llms.ollama import Ollama

def load_data(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path, encoding='utf-8')
    elif file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)
    else:
        st.error("Invalid file format. Please upload a CSV or Excel file.")

def file_stuff():
    def handle_select():
        print("run")
        # Clear any existing message
        message_container.empty()
        
        if not selected_option == "Upload your own":
            # Load the selected dataset
            file_path = os.path.join("src", "data", selected_option)
            print(file_path)
            data = load_data(file_path)
            st.write(data)
            st.session_state.finance_data = data
            message_container.success(f"Successfully loaded: {selected_option}")
        else:
            # Upload a new dataset
            uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "xlsx"])
            if uploaded_file is not None:
                # Read the uploaded file into a pandas dataframe (load_data won't work here)
                data = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
                st.write(data)
                st.session_state.finance_data = data
                st.session_state.known_datasets.append(uploaded_file.name)
                message_container.success("File uploaded successfully!")
            else:
                message_container.warning("An error occured")

    # Dataset selection
    st.header("Select Dataset")
    
    # Pre-loaded datasets
    if "known_datasets" not in st.session_state:
        st.session_state.known_datasets = [f for f in os.listdir("src\\data") if os.path.isfile(os.path.join("src\\data", f)) and f.endswith((".csv", ".xlsx"))]

    selected_option = st.selectbox(
        "Choose a dataset",
        st.session_state.known_datasets + ["Upload your own"],
        key="dataset_choice",
        placeholder="Select a dataset...",
        on_change=handle_select,
    )

    # Create an empty container for the success message
    message_container = st.empty()
    
    handle_select()

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
