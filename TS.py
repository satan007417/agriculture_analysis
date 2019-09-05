import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
# 標題顯示中文請參照https://ppt.cc/fTbrPx

with open('./arma106107.json') as f:
    data = json.load(f)

df = pd.DataFrame(data).transpose()
df.columns = ['avg', 'top', 'btm', 'tn']
dfa = df.avg
print(dfa.head(10))
# dataset = np.array(dfa).reshape(1, -1)
# dataset = dataset.astype('float32')
# print(dataset)
# fig,ax = plt.subplots()
# ax.plot(df.index,df.avg)
# ax.set_xticks(df.index[::400])
# ax.set_xticklabels(df.index[::400], rotation=45)

# plt.plot()
# plt.show()

# # 畫出 ACF 12 期的效應
# sm.graphics.tsa.plot_acf(df.avg, lags=12)
# plt.show()
# # 畫出 PACF 12 期的效應
# sm.graphics.tsa.plot_pacf(df.avg, lags=12)
# plt.show()