# 畫均線
import talib
import pandas as pd
import mpl_finance as mpf
import json
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
# 標題顯示中文請參照https://ppt.cc/fTbrPx

with open('./after_Integrate_forKLine.json') as f:  
    all_data = json.load(f)

df = pd.DataFrame(all_data).transpose()
df.columns = ['open', 'high','low','close','volume']

# 簡單平均線(SMA)：n天收盤價的平均。
# 指數移動平均(EMA)：權重考量，以指數方式遞減加權的移動平均。
# 加權移動平均(WMA)：權重考量，最近的日期乘n，次近的乘n-1，依此類推到零。
# 兩倍的EMA(DEMA)
# 三倍的EMA(TEMA)

SMA = talib.MA(np.array(df.close), 30, matype=0)
EMA = talib.MA(np.array(df.close), 30, matype=1)
WMA = talib.MA(np.array(df.close), 30, matype=2)
DEMA = talib.MA(np.array(df.close), 30, matype=3)
TEMA = talib.MA(np.array(df.close), 30, matype=4)

SMA_df = pd.DataFrame(SMA, columns = ['SMA'])
EMA_df = pd.DataFrame(EMA, columns = ['EMA'])
WMA_df = pd.DataFrame(WMA, columns = ['WMA'])
DEMA_df = pd.DataFrame(DEMA, columns = ['DEMA'])
TEMA_df = pd.DataFrame(TEMA, columns = ['TEMA'])

fig,ax = plt.subplots(figsize=(20,5))
ax.set_title('甘藍均線')


ax.plot(df.index,SMA_df, color='#DE5B49', label='SMA', alpha=0.8, linewidth=3)
ax.plot(df.index,EMA_df, color='#46B29D', label='EMA', alpha=0.8, linewidth=3)
ax.plot(df.index,WMA_df, color='#324D5C', label='WMA', alpha=0.8, linewidth=3)
ax.plot(df.index,DEMA_df, color='#F0CA4D', label='DEMA', alpha=0.8, linewidth=3)
ax.plot(df.index,TEMA_df, color='#9C4368', label='TEMA', alpha=0.8, linewidth=3)
plt.legend(loc='upper left')
plt.grid(True)
ax.set_xticks(df.index[::400])
ax.set_xticklabels(df.index[::400], rotation=45)
plt.plot()
plt.show()