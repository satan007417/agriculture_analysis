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
ax.set_title('甘藍BB')

plt.grid(True)
# rsi=talib.RSI(np.array(df.avg), timeperiod = 6)
upper,middle,lower=talib.BBANDS(df.avg ,timeperiod=20, matype=talib.MA_Type.SMA)


ax.plot(upper,label ='upper',color='blue')
ax.plot(middle,label ='middle',color='green')
ax.plot(lower,label ='lower',color='orange')
ax.plot(df.avg,label = 'avg',color='red') #紅線

diff1=upper-middle
diff2=middle-lower
print(diff1)
print(diff2) 
ax.fill_between(df.index,upper, lower, color='grey')
ax.set_xticks(df.index[::3])
ax.set_xticklabels(df.index[::3], rotation=45)
plt.legend(loc='upper right')
plt.plot()
plt.show()