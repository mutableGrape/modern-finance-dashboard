import streamlit as st
import pandas as pd
import plotly.express as px
from utils.kalman import apply_kalman_filter

st.title("Analysis")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # Apply Kalman filter to the 'Balance' column
    data['Filtered_Balance'] = apply_kalman_filter(data['Balance'].values)

    # Display the original and filtered data using Plotly
    fig = px.line(data, x='Date', y=['Balance', 'Filtered_Balance'], labels={'value': 'Balance'}, title='Original and Filtered Balance')
    st.plotly_chart(fig)