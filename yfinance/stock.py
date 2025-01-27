import yfinance as yf
import mplfinance as mpf
import pandas as pd

# 获取股票数据，例如：Apple (AAPL)
stock_symbol = 'AAPL'
data = yf.download(stock_symbol, start='2020-01-01', end='2021-01-01')

# 检查数据结构
print(data.head())
