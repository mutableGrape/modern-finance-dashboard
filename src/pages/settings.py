import time
import streamlit as st
import pandas as pd
import os

def load_data(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path, encoding='utf-8')
    elif file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format")

def file_stuff():
    
    # Pre-loaded datasets
    if "known_datasets" not in st.session_state:
        st.session_state.known_datasets = [f for f in os.listdir("src\\data") if os.path.isfile(os.path.join("src\\data", f)) and f.endswith((".csv", ".xlsx"))]

    selected_option = st.selectbox(
        "Choose a dataset",
        st.session_state.known_datasets + ["Upload your own"],
        key="dataset_choice"
    )

    # Create an empty container for the success message
    message_container = st.empty()
    
    # Check if the selection has changed
    if "previous_selection" not in st.session_state:
        st.session_state.previous_selection = None
    
    if selected_option != st.session_state.previous_selection:
        # Clear any existing message
        message_container.empty()
        
        if not selected_option == "Upload your own":
            # Load the selected dataset
            file_path = os.path.join("src", "data", selected_option)
            print(file_path)
            data = load_data(file_path)
            st.write(data)
            message_container.success(f"Successfully loaded: {selected_option}")
        else:
            # Upload a new dataset
            uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "xlsx"])
            if uploaded_file is not None:
                data = load_data(uploaded_file)
                st.write(data)
                st.session_state.known_datasets.append(uploaded_file.name)
                message_container.success("File uploaded successfully!")
                
        # Update the previous selection
        st.session_state.previous_selection = selected_option


# LLM model names
llm_models = ["Model A", "Model B", "Model C"]

st.title("Settings")

# Dataset selection
st.header("Select Dataset")
file_stuff()
# if "placeholder" not in st.session_state:
#     st.session_state.placeholder = st.empty()  # Create a placeholder for the new widgets
# placeholder = st.session_state.placeholder
# st.selectbox("Choose a dataset", datasets + ["Upload your own"], key="dataset_choice", on_change=on_dataset_change)

# LLM model selection
st.header("Select LLM Model")
llm_model_choice = st.selectbox("Choose a model", llm_models)
st.success(f"Selected model: {llm_model_choice}")