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

    # Income Outcome Analysis
    st.header("Income Outcome Analysis")

    # Calculate average monthly income and expenditure
    data['Date'] = pd.to_datetime(data['Date'])
    data['Month'] = data['Date'].dt.to_period('M')
    monthly_data = data.groupby('Month').agg({'Paid in': 'sum', 'Paid out': 'sum'}).reset_index()
    monthly_data['Average Monthly Income'] = monthly_data['Paid in'] / monthly_data['Month'].dt.days_in_month
    monthly_data['Average Monthly Outcome'] = monthly_data['Paid out'] / monthly_data['Month'].dt.days_in_month
    monthly_data['Average Savings'] = monthly_data['Average Monthly Income'] - monthly_data['Average Monthly Outcome']

    # Plot average monthly income, expenditure, and savings using Plotly
    fig_income = px.line(monthly_data, x='Month', y='Average Monthly Income', labels={'Average Monthly Income': 'Average Monthly Income'}, title='Average Monthly Income')
    st.plotly_chart(fig_income)

    fig_expenditure = px.line(monthly_data, x='Month', y='Average Monthly Outcome', labels={'Average Monthly Outcome': 'Average Monthly Outcome'}, title='Average Monthly Outcome')
    st.plotly_chart(fig_expenditure)

    fig_savings = px.line(monthly_data, x='Month', y='Average Savings', labels={'Average Savings': 'Average Savings'}, title='Average Savings')
    st.plotly_chart(fig_savings)
