import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

scope = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("/home/rpi/shared/expense_trackerapp/app/plenary-utility-444815-g1-08f401bc6c68.json", scopes=scope)
client = gspread.authorize(creds)
spreadsheet = client.open_by_key("1AccUH_X1SSLCtIFv9pUHxfq4CQhTpsumIokUZfL87bY")
sheet = spreadsheet.worksheet("Expenses")

def fetch_data():
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Year-Month'] = df['Date'].dt.to_period('M').astype(str)
    return df

def refresh_sheet_data():
    global formatted_data, monthly_data, category_monthly_data, yearly_data, daily_total_data
    formatted_data = fetch_data()
    monthly_data = formatted_data.groupby('Year-Month')['Amount'].sum().reset_index()
    category_monthly_data = formatted_data.groupby(['Year-Month', 'Category'])['Amount'].sum().reset_index()
    yearly_data = formatted_data.groupby('Year')['Amount'].sum().reset_index()
    daily_total_data = formatted_data.groupby('Date')['Amount'].sum().reset_index()

def fetch_investment_data():
    investment_data = spreadsheet.worksheet("Mutual Funds and Investments").get_all_records()
    df = pd.DataFrame(investment_data)
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Year'] = df['Date'].dt.year
    df['Year-Month'] = df['Date'].dt.to_period('M').astype(str)
    return df

# Initialize on module load
refresh_sheet_data()