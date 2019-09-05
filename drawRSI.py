import talib
import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np
# 本python 是畫RSI，和KDtest是一樣的功能，目前應該還有bug，但不確定是不是RSI

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
# 標題顯示中文請參照https://ppt.cc/fTbrPx

with open('./after_Integrate_forRSI.json') as f:
    data = json.load(f)


df = pd.DataFrame(data).transpose()
df.columns = ['avg', 'top', 'btm', 'tn']

fig,ax = plt.subplots()
ax.set_title('甘藍RSI')

plt.grid(True)
rsi=talib.RSI(np.array(df.avg), timeperiod = 6)
# rsi=talib.RSI(np.array(df.tail(120).avg), timeperiod = 6)
# plt.plot(df.tail(120).index,rsi)
rsi_df = pd.DataFrame(rsi,columns = ['RSI'])
ax.plot(df.index,rsi_df)
ax.set_xticks(df.index[::400])
ax.set_xticklabels(df.index[::400], rotation=45)

plt.plot()
plt.show()