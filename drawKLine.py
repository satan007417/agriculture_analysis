#原先是import matplotlib.finance 但現在要用下面的方法
import mpl_finance as mpf
# 先 pip install https://github.com/matplotlib/mpl_finance/archive/master.zip
# 參考：https://stackoverflow.com/questions/42373104/since-matplotlib-finance-has-been-deprecated-how-can-i-use-the-new-mpl-finance
import json
import talib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
# 標題顯示中文請參照https://ppt.cc/fTbrPx


with open('./after_Integrate_forKLine.json') as f:  
    all_data = json.load(f)

df = pd.DataFrame(all_data).transpose()
df.columns = ['open', 'high','low','close','volume']


fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)
mpf.candlestick2_ochl(ax, df.tail(10).open, df.tail(10).close, df.tail(10).high, df.tail(10).low, 
                      width=0.5, colorup='r', colordown='green', alpha=0.6)

plt.setp(ax,xticks=[0,1,2,3,4,5,6,7,8,9],xticklabels=df.tail(10).index)
fig.tight_layout()
plt.title('甘藍KLine')
plt.show()
