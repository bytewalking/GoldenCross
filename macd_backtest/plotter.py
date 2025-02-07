import matplotlib.pyplot as plt

"""
绘制 MACD
"""


def plot_macd(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["MACD"], label="MACD", color="blue")
    plt.plot(df.index, df["Signal"], label="Signal", color="red")
    plt.bar(df.index, df["MACD_Hist"], label="MACD Histogram", color="gray", alpha=0.5)
    plt.legend()
    plt.title("MACD Indicator")
    plt.show(block=False)
