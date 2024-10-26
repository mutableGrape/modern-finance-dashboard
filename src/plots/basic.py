import plotly.express as px
import plotly.graph_objs as go
import pandas as pd

def balance_plot(data: pd.DataFrame) -> go.Figure:    
    # Create the line plot
    fig = px.line(data, x='Date', y='Balance', labels={'value': 'Balance'}, title='Balance')
    
    # Update x-axis to show whole months
    fig.update_xaxes(dtick='M1', tickformat='%b %Y')
    
    # Update y-axis to show GBP units
    fig.update_yaxes(tickprefix='£')
        
    return fig

def monthly_income_breakdown(data: pd.DataFrame) -> go.Figure:
    # Calculate monthly income and expenditure
    monthly_data = data.groupby('Month').agg({'Paid in': 'sum', 'Paid out': 'sum'}).reset_index()
    monthly_data['Month'] = monthly_data['Month'].astype(str)  # Convert Period to string
    monthly_data['Savings'] = monthly_data['Paid in'] - monthly_data['Paid out']

    # Calculate averages
    avg_paid_out = monthly_data['Paid out'].mean()
    avg_savings = monthly_data['Savings'].mean()

    # Plot average monthly income, expenditure, and savings using Plotly
    fig_combined = px.bar(monthly_data, x='Month', y=['Savings', 'Paid out'], 
                            labels={'value': 'Amount', 'variable': 'Category'}, 
                            title='Average Monthly Income, Expenditure, and Savings',
                            )
    fig_combined.update_layout(barmode='stack')

    # Add horizontal lines for average 'Paid out' and 'Savings'
    fig_combined.add_shape(
        type='line',
        x0=monthly_data['Month'].min(),
        y0=avg_paid_out,
        x1=monthly_data['Month'].max(),
        y1=avg_paid_out,
        line=dict(dash='dash'),
        xref='x',
        yref='y'
    )
    fig_combined.add_annotation(
        x=monthly_data['Month'].max(),
        y=avg_paid_out,
        text=f'Avg Paid Out: £{avg_paid_out:.2f}',
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=-20,
        bgcolor='rgba(255, 255, 255, 0.3)'
    )
    fig_combined.add_shape(
        type='line',
        x0=monthly_data['Month'].min(),
        y0=avg_savings,
        x1=monthly_data['Month'].max(),
        y1=avg_savings,
        line=dict(dash='dash'),
        xref='x',
        yref='y'
    )
    fig_combined.add_annotation(
        x=monthly_data['Month'].max(),
        y=avg_savings,
        text=f'Avg Savings: £{avg_savings:.2f}',
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=-20,
        bgcolor='rgba(255, 255, 255, 0.3)'
    )

    return fig_combined

def plot_balance_distribution(data):
    fig = px.histogram(data, x='Balance', nbins=20, title='Balance Distribution')
    return fig

def plot_monthly_average_balance(data):
    monthly_avg_balance = data.groupby('Month')['Balance'].mean().reset_index()
    monthly_avg_balance['Month'] = monthly_avg_balance['Month'].astype(str)
    fig = px.bar(monthly_avg_balance, x='Month', y='Balance', title='Monthly Average Balance')
    return fig