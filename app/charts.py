import plotly.express as px
from .data_handler import monthly_data, category_monthly_data, yearly_data, daily_total_data, fetch_investment_data

def create_expenses_chart():
    fig = px.bar(monthly_data, x="Year-Month", y="Amount", title="Monthly Expenses")
    return fig.to_html(full_html=False)

def create_category_chart():
    fig = px.bar(category_monthly_data, x="Year-Month", y="Amount", color="Category", title="Category-wise Monthly Spending")
    return fig.to_html(full_html=False)

def create_yearly_expenses_chart():
    fig = px.bar(yearly_data, x="Year", y="Amount", title="Yearly Expenses")
    return fig.to_html(full_html=False)

def create_daily_total_chart():
    fig = px.bar(daily_total_data, x="Date", y="Amount", title="Daily Total Spending")
    return fig.to_html(full_html=False)

def create_monthly_investment_chart():
    df = fetch_investment_data()
    df = df.groupby(['Year-Month', 'Investment Type'])['Amount'].sum().reset_index()
    fig = px.bar(df, x="Year-Month", y="Amount", color="Investment Type", title="Monthly Investments")
    return fig.to_html(full_html=False)

def create_yearly_investment_chart():
    df = fetch_investment_data()
    df = df.groupby(['Year', 'Investment Type'])['Amount'].sum().reset_index()
    fig = px.bar(df, x="Year", y="Amount", color="Investment Type", title="Yearly Investments")
    return fig.to_html(full_html=False)