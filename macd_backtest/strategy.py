import backtrader as bt

"""
Backtrader 策略
"""


class MACDStrategy(bt.Strategy):
    params = dict(fast=12, slow=26, signal=9)

    def __init__(self):
        macd = bt.indicators.MACD(period_me1=self.params.fast, period_me2=self.params.slow,
                                  period_signal=self.params.signal)
        self.crossover = bt.indicators.CrossOver(macd.macd, macd.signal)  # 金叉 & 死叉

    def notify_trade(self, trade):
        if trade.isclosed:
            print(f"交易收益: {trade.pnl}, 总收益: {trade.pnlcomm}")

    def next(self):
        if self.crossover > 0:  # 金叉买入
            cash = self.broker.get_cash()
            price = self.datas[0].close[0]
            size = int(cash * 0.9 / price)  # 90% 资金买入

            if size > 0:
                self.buy(size=size)
        elif self.crossover < 0:  # 死叉卖出
            self.sell(size=self.position.size)
