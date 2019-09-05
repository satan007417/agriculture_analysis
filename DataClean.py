import json
import collections
from decimal import *

def decimal_default_proc(obj):
# https://qiita.com/ekzemplaro/items/5fa8900212252ab554a3 ==>浮點數解法
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

def getNext(data,index):
	# 獲得下個不為零的位置
	if index==len(data):
		return len(data)-1
	elif data[index][1] == 0.0:
		return getNext(data,index+1)
	else:
		return index



def MeanTrap(data,deviation):
	# deviation ==> 上下範圍
	# 補漏:附近點平均法
	
	everyday = list(data.items())
	# 轉為tuple的list
	nof_day = len(everyday)
	# 獲取list的長度，即data的總天數
	new_data = {}
	#最後回傳的dictionary

	for day in range(nof_day):
		if everyday[day][1] == 0.0:
			start = day - deviation

			# 需擴展start到上一個不為零的位置
			while(everyday[start][1]==0.0):
				start = start -1

			end = day + deviation
			# 尋求鄰近範圍
			if start < 0:
				start = 0


			# 需擴展end到下一個非零之位置
			end = getNext(everyday,end)

			if end > nof_day:
				end = nof_day
			elif end < nof_day:
				end = end + 1
			# 如果超出list範圍，則縮減範圍
			s = Decimal(str(0.0))
			i = 0
			for n in range(start,end):
				# 計算範圍之總和以及筆數，若為0.0則忽略不計算
				if everyday[n][1] != 0.0:
					s = s + Decimal(str(everyday[n][1]))
					i = i + 1

			if i == 0:
				i = 1
				#若筆數為0，則為了計算平均時分母不為0，而賦予其值為1
			# 計算該區間的平均

			# 補值

			#----
			# 若要多一個空值只有一個的狀況
			# if end-start == 2:
			# 	
			#----
			avg = Decimal(str(s/i))
			# new_data[everyday[day][0]] = s/i
			for tr in range(start,end):
				if everyday[tr][1] != 0.0:
					new_data[everyday[tr][0]] = Decimal(str(everyday[tr][1]))
					# print(Decimal(str(everyday[tr][1])))
				else:
					new_data[everyday[tr][0]] = Decimal(str(avg))
					# print(Decimal(str(avg)))
					
		else:
			new_data[everyday[day][0]] = everyday[day][1]
		
	return new_data

def rsi_integration(PriceAvg, TopPrice, BtmPrice, Turnover):
	pa = list(PriceAvg.items())
	top = list(TopPrice.items())
	btm = list(BtmPrice.items())
	tn = list(Turnover.items())
	# 轉為tuple的list
	nof_day = len(PriceAvg)
	# 獲取list的長度，即data的總天數
	new_data = {}
	# 最後回傳的dictionary

	for day in range(nof_day):
		new_data[pa[day][0]] = [pa[day][1], top[day][1], btm[day][1], tn[day][1]]
	
	return new_data

def KLine_Integrate(PriceAvg, TopPrice, BtmPrice, Turnover):
	# open ==> 前一天均價
	# close ==> 當天均價
	# high ==> 上價
	# low ==> 下價
	pa = list(PriceAvg.items())
	top = list(TopPrice.items())
	btm = list(BtmPrice.items())
	tn = list(Turnover.items())
	# 轉為tuple的list
	nof_day = len(PriceAvg)
	# 獲取list的長度，即data的總天數
	re_data = {}
	#最後回傳的dictionary


	for day in range(1,nof_day):
	# 去除資料集的第一天(101.01.01)，因為無法定出101.01.01的開盤價
		re_data[pa[day][0]] = [pa[day-1][1], top[day][1], btm[day][1], pa[day][1],tn[day][1]]

	return re_data 

# -----主程式----
data = []

try:
	# 起始年
	load_year = 101

	while True:
		with open('./OriginData/球莖甘藍'+str(load_year)+'.json') as f:
			data.append(json.load(f))

		load_year =load_year + 1
except FileNotFoundError:
	print('讀取結束')

# 交易量,均價,上價,中價,下價
Turnover,PriceAvg,TopPrice,MidPrice,BtmPrice={},{},{},{},{}
for year in data:
	length = len(year)

	for n in range(0,length):
		# 預設為0
		Turnover[year[n]['交易日期']] = 0.0
		PriceAvg[year[n]['交易日期']] = 0.0
		TopPrice[year[n]['交易日期']] = 0.0
		MidPrice[year[n]['交易日期']] = 0.0
		BtmPrice[year[n]['交易日期']] = 0.0

	for i in range(0,length):
		# 只擷取台北一市場的資料
		if year[i]['市場名稱'] == '台北一':
			Turnover[year[i]['交易日期']] = year[i]['交易量']
			PriceAvg[year[i]['交易日期']] = year[i]['平均價']
			TopPrice[year[i]['交易日期']] = year[i]['上價']
			MidPrice[year[i]['交易日期']] = year[i]['中價']
			BtmPrice[year[i]['交易日期']] = year[i]['下價']
# Dictionary 按照交易日期排序
OrderTurnover = collections.OrderedDict(sorted(Turnover.items()))
OrderPriceAvg = collections.OrderedDict(sorted(PriceAvg.items()))
OrderTopPrice = collections.OrderedDict(sorted(TopPrice.items()))
OrderMidPrice = collections.OrderedDict(sorted(MidPrice.items()))
OrderBtmPrice = collections.OrderedDict(sorted(BtmPrice.items()))

Turnover,PriceAvg,TopPrice,MidPrice,BtmPrice=dict(OrderTurnover),dict(OrderPriceAvg),dict(OrderTopPrice),dict(OrderMidPrice),dict(OrderBtmPrice)


M_PriceAvg = MeanTrap(PriceAvg,1)
M_Turnover = MeanTrap(Turnover,1)
M_TopPrice = MeanTrap(TopPrice,1)
M_MidPrice = MeanTrap(MidPrice,1)
M_BtmPrice = MeanTrap(BtmPrice,1)

for_rsi_data = rsi_integration(M_PriceAvg, M_TopPrice, M_BtmPrice, M_Turnover)

for_kline_data = KLine_Integrate(M_PriceAvg, M_TopPrice, M_BtmPrice, M_Turnover)

with open('./after_Integrate_forRSI.json', 'w') as outfile:  
	# 資料格式 {日期：[均價,上價,下價,交易量],...}
    json.dump(for_rsi_data, outfile,default=decimal_default_proc)

with open('./after_Integrate_forKLine.json','w') as outfile:
	# 資料格式 {date:[open,high,low,close,volume],...}
	json.dump(for_kline_data, outfile,default=decimal_default_proc)






