# src/data_fetch.py

import yfinance as yf

def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetches historical stock data from Yahoo Finance.
    
    Parameters:
        ticker (str): Stock ticker symbol (e.g., 'AAPL').
        start_date (str): Start date for data in 'YYYY-MM-DD' format.
        end_date (str): End date for data in 'YYYY-MM-DD' format.
    
    Returns:
        pandas.DataFrame: Historical stock data.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    if data.empty:
        raise ValueError(f"No data found for {ticker} in the specified range.")
    return data
