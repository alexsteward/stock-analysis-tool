# src/analysis.py

def calculate_moving_average(data, window):
    """
    Calculates the moving average of stock closing prices.
    
    Parameters:
        data (pandas.DataFrame): Stock data containing a 'Close' column.
        window (int): The window size for the moving average.
    
    Returns:
        pandas.Series: Moving average values.
    """
    if 'Close' not in data.columns:
        raise KeyError("DataFrame must contain a 'Close' column.")
    return data['Close'].rolling(window=window).mean()
