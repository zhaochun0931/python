import yfinance as yf
import mplfinance as mpf
import pandas as pd
import matplotlib.pyplot as plt


# 获取股票数据，例如：Apple (AAPL)
stock_symbol = 'AAPL'








# stock_symbol = '002956.sz'
data = yf.download(stock_symbol, start='2025-01-01', end='2025-01-27')

pd.set_option('display.float_format', '{:.2f}'.format)

# 检查数据结构
print(data.head())


# 打印数据框
print(data)
