import yfinance as yf
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt




# 获取股票数据
stock_symbol = '002956.sz'
data = yf.download(stock_symbol, start='2020-01-01', end='2025-01-27')

pd.set_option('display.float_format', '{:.2f}'.format)


# 打印数据框
print(data)


data.to_excel(f'{stock_symbol}_stock_data.xlsx', index=True)


#data.to_excel('data.xlsx', index=True)
