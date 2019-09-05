requirements.txt ==> 內含有套件名稱及版本

排序好資料 --> 附近點平均法 (Mean of nearby points,MEAN)補零

--->

預計會去除資料集的第一天(101.01.01) 因為無法定出101.01.01的開盤價

開盤價 ==> 前一天均價 最高價 ==> 上價 最低價 ==> 下價 收盤價 ==> 當天均價 成交量(volume) ==> 交易量

--->

整理成:

after_Integration_forKLine.json ==> 資料格式 {date:[open,high,low,close,volume],...}

after_Integration_forRSI.json ==> 資料格式 {日期：[均價,上價,下價,交易量],...}

--->

畫圖:

drawRSI.py、drawKLine.py、drawKDJ、drawMA 畫圖日期座標：https://stackoverflow.com/questions/50128668/change-the-tick-frequency-when-value-of-x-axis-is-string