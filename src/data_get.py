import pandas as pd


def Df_get () -> pd.DataFrame:
    """Get data from Yahoo Finance for Microsoft, Apple, and Nvidia."""
    import yfinance as yf
    try:
        all_ticker = yf.download('MSFT AAPL NVDA', period="10y", group_by='ticker')  #download data
    except ConnectionError:
        print("Connection error. Please check your internet connection.")
        return pd.DataFrame()  # Return an empty DataFrame if download fails
    try:
        with open('data/raw_data.csv', 'w') as f:
            all_ticker.to_csv(f)
    except PermissionError:
        print("Permission error. Please check if the file is open or if you have write permissions.")
        return pd.DataFrame()
    return all_ticker

Df_get()