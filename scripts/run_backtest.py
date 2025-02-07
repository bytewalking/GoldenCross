import argparse
from macd_backtest.data_fetcher import get_stock_data
from macd_backtest.indicators import compute_macd
from macd_backtest.signals import generate_signals
from macd_backtest.plotter import plot_macd
from macd_backtest.backtest import run_backtest


def main():
    parser = argparse.ArgumentParser(description="运行 MACD 交易策略回测")
    parser.add_argument("--ticker", type=str, default="NVDA", help="股票代码")
    args = parser.parse_args()

    print("获取数据...")
    df = get_stock_data(args.ticker)

    print("计算 MACD...")
    df = compute_macd(df)

    print("生成交易信号...")
    df = generate_signals(df)

    print("绘制 MACD 指标...")
    plot_macd(df)

    print("运行回测...")
    run_backtest(args.ticker)


if __name__ == "__main__":
    main()
