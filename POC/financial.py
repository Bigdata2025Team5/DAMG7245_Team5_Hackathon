import yfinance as yf
import pandas as pd

# Define the tickers for Apple (AAPL) and Meta (META)
tickers = ["AAPL", "META"]

# Function to fetch and save data
def fetch_and_save_data(ticker):
    stock = yf.Ticker(ticker)

    # Get stock price history for the past 2 years
    stock_history = stock.history(period="2y")

    
    # Get financial data
    financials = stock.financials
    balance_sheet = stock.balance_sheet
    cash_flow = stock.cashflow
    income_statement = stock.income_stmt

    # Save stock history to CSV
    stock_history.to_csv(f"{ticker}_stock_history_2years.csv")

    # Save financial data to CSV
    financials.to_csv(f"{ticker}_financials.csv")
    balance_sheet.to_csv(f"{ticker}_balance_sheet.csv")
    cash_flow.to_csv(f"{ticker}_cash_flow.csv")
    income_statement.to_csv(f"{ticker}_income_statement.csv")

    # Save news as CSV


# Fetch and save data for both Apple & Meta
for ticker in tickers:
    fetch_and_save_data(ticker)

print("✅ All data saved successfully!") 