"""
生成交易信号
"""


def generate_signals(df):
    df["Buy_Signal"] = (df["MACD"] > df["Signal"]) & (df["MACD"].shift(1) <= df["Signal"].shift(1))
    df["Sell_Signal"] = (df["MACD"] < df["Signal"]) & (df["MACD"].shift(1) >= df["Signal"].shift(1))
    return df
