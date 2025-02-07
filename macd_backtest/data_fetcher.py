import yfinance as yf
import os
import pandas as pd

"""
获取数据
"""


def get_stock_data(ticker, start="2019-01-01", end="2024-01-01", save_dir="../data"):
    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, f"{ticker}.csv")

    df = yf.download(ticker, start=start, end=end)
    df.to_csv(file_path)

    return df
