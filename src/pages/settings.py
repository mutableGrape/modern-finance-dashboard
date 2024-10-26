import streamlit as st
import pandas as pd
from langchain.llms.ollama import Ollama
from entity.account_entity import Account

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

def handle_upload(files):
    datasets = []
    for i, uploaded_file in enumerate(files):
        data = load_data(uploaded_file)
        account = Account(name=f"Account {i+1}", fn=uploaded_file.name, data=data)
        datasets.append(account)

    st.session_state.finance_data += datasets

def get_files_to_upload():
    """This function is a streamlit button that opens a modal to upload files"""

    with st.popover("Upload Files"):
        uploaded_files = st.file_uploader("Upload your datasets", type=["csv", "xlsx"], accept_multiple_files=True)

    if uploaded_files:
        files = uploaded_files.copy()
        del uploaded_files
        handle_upload(files)

def display_uploaded_files():
    st.subheader("Uploaded Files")

    # Display column headers
    header_cols = st.columns([3, 3, 1])
    header_titles = ["Account name", "Filename", "Remove"]
    for col, title in zip(header_cols, header_titles):
        with col:
            st.write("**" + title + "**")

    # Display uploaded files
    for account in st.session_state.finance_data:
        col1, col2, col3 = st.columns([3, 3, 1], vertical_alignment="center")
        with col1:
            new_name = st.text_input("Edit Account Name", value=account.acc_name, key=str(id(account))+"_name", label_visibility="collapsed")
            if new_name != account.acc_name:
                account.acc_name = new_name
        with col2:
            st.write(account.filename)
        with col3:
            if st.button('x', key=str(id(account))+"_remove"):
                st.session_state.finance_data.remove(account)
                st.rerun()

def account_options(): 
    col1, col2 = st.columns([6,1], vertical_alignment="bottom")
    col1.header("Upload Account Data")
    with col2: get_files_to_upload()
    display_uploaded_files()

def llm_options():
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

llm_options()

account_options()
