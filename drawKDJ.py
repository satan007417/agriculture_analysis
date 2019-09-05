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

# 當KD指標的K值由下往上突破D值，建議買進、做多
# 當KD指標的K值由上往下跌破D值時，建議賣出、做空
# 反轉點：K>90, D>80=高檔超買，K<10, D<20=低檔超賣
# KD鈍化：就是指K值在高檔(K>80)或低檔(K<20)區
# 連續5天以上J值(J=3D-2K)大於100，股價至少會形成短期頭部，反之J值小於0時，股價至少會形成短期底部。
# fastk_period, slowk_period, slowd_period參數為9,3,3，是依據台灣常用的參數搭配方式。J線我沒找到對應function，則是自己計算。

K,D = talib.STOCH(high = np.array(df.high), 
                low = np.array(df.low), 
                close = np.array(df.close),
                fastk_period=9,
                slowk_period=3,
                slowk_matype=0,
                slowd_period=3,
                slowd_matype=0)

K_df = pd.DataFrame(K, columns = ['K'])
D_df = pd.DataFrame(D, columns = ['D'])
J_df = pd.merge(K_df, D_df, left_index=True, right_index=True).apply(lambda x: (3*x.K) - (2*x.D), axis = 1)
fig,ax = plt.subplots()
ax.set_title('甘藍KDJ')

ax.plot(df.index,K_df,label ='K',color='blue')
ax.plot(df.index,D_df,label ='D',color='orange')
ax.plot(df.index,J_df,label ='J',color='green',linestyle='--')
# 參考網址https://binda.blog/2018/04/28/py_talib/
ax.set_xticks(df.index[::400])
ax.set_xticklabels(df.index[::400], rotation=45)
plt.grid(True)
plt.legend(loc='lower left')
plt.plot()
plt.show()