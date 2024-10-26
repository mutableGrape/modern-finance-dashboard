import streamlit as st
import pandas as pd
from plots.basic import balance_plot, monthly_income_breakdown, plot_balance_distribution, plot_monthly_average_balance

st.set_page_config(layout="wide", page_icon=":material/query_stats:")
st.title("Analysis")
if "finance_data" not in st.session_state:
    st.error("Please load a dataset first.")
else:

    data = st.session_state.finance_data

    # Convert 'Date' column to datetime
    data['Date'] = pd.to_datetime(data['Date'])

    # Date range selector
    min_date = data['Date'].min()
    max_date = data['Date'].max()
    date_range = st.date_input(
        "Select date range",
        value=[min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

    if len(date_range) == 2:
        start_date, end_date = date_range
    else:
        start_date, end_date = min_date, max_date

    # Filter data based on selected date range
    mask = (data['Date'] >= pd.to_datetime(start_date)) & (data['Date'] <= pd.to_datetime(end_date))
    filtered_data = data.loc[mask]

    col1, col2 = st.columns(2)

    with col1:
        # Display the original and filtered data using Plotly
        st.plotly_chart(balance_plot(filtered_data))
        st.plotly_chart(plot_monthly_average_balance(filtered_data))

    with col2:
        # Income Outcome Analysis
        fig_combined = monthly_income_breakdown(filtered_data)
        st.plotly_chart(fig_combined)
        st.plotly_chart(plot_balance_distribution(filtered_data))

