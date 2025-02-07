import backtrader as bt
import pandas as pd
import os

from macd_backtest.strategy import MACDStrategy

"""
回测执行
"""


def run_backtest(ticker, data_dir="../data"):
    file_path = os.path.join(data_dir, f"{ticker}.csv")
    df = pd.read_csv(file_path)
    # 删除第 2 和第 3 行（索引 1 和 2）
    df = df.drop(index=[0, 1])
    # 重置索引
    df = df.reset_index(drop=True)

    # 保存修改后的 CSV 文件
    file_path = os.path.join(data_dir, f"{ticker}_clean.csv")
    df.to_csv(file_path, index=False)

    # 载入数据
    data = bt.feeds.GenericCSVData(
        dataname=file_path,
        dtformat="%Y-%m-%d",
        timeframe=bt.TimeFrame.Days,
        compression=1,
        openinterest=-1,
        headers=True
    )

    # 运行回测
    cerebro = bt.Cerebro()
    cerebro.addstrategy(MACDStrategy)
    cerebro.adddata(data)
    cerebro.broker.set_cash(10000)
    cerebro.broker.setcommission(commission=0.001)

    print("初始资金:", cerebro.broker.getvalue())
    cerebro.run()
    print("回测后资金:", cerebro.broker.getvalue())

    cerebro.plot()
