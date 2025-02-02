# src/visualization.py

import matplotlib.pyplot as plt

def plot_stock_data(data, ticker):
    """
    Plots stock closing prices and moving averages.
    
    Parameters:
        data (pandas.DataFrame): Stock data with 'Close' and 'Moving Average'.
        ticker (str): Stock ticker symbol.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Closing Price', color='blue')
    if 'Moving Average' in data.columns:
        plt.plot(data.index, data['Moving Average'], label='Moving Average', color='orange')
    plt.title(f'{ticker} Stock Prices and Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid()
    plt.show()
