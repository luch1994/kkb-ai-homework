"""

fundemantals.csv 是这些股票的年报数据

请用数据回答以下问题：

S&P500股票在2015年net income的均值是多少？最大值比最小值多多少？（每问10分，共计20分）
S&P500股票在2016年的固定资产（fixed assets）占总资产(total assets)比例的均值是多少？固定资产占总资产比例最小的股票是的代码（ticker symbol）是什么？（每问10分，共计20分）

"""
import pandas as pd

fundamentals = pd.read_csv('./fundamentals.csv')

# 将日期列转换成日期类型
fundamentals['Period Ending'] = pd.to_datetime(fundamentals['Period Ending'])

# 2015开始和结束时间
start_2015 = pd.Timestamp(2015, 1, 1)
end_2015 = pd.Timestamp(2015, 12, 31)

# 获取指定2015年的数据
data2015 = fundamentals[(fundamentals['Period Ending'] >= start_2015) & (
    fundamentals['Period Ending'] <= end_2015)]['Net Income']

# 得到第一题的结果
print("2015年的平均数是{}".format(data2015.mean()))
print("2015年的最大值比最小值多{}".format(data2015.max() - data2015.min()))

# 获取2016年的开始和结束时间
start_2016 = pd.Timestamp(2016, 1, 1)
end_2016 = pd.Timestamp(2016, 12, 31)

# 选取2016年的数据
data2016 = fundamentals[(fundamentals['Period Ending'] >= start_2016) & (
    fundamentals['Period Ending'] <= end_2016)]

# 计算2016年的固定资产和总资产的比例
rate2016 = data2016['Fixed Assets']/ data2016['Total Assets']
# 得到2016年比例最小的行的下标
rate2016_min_index = rate2016.idxmin()

# 得到第二问的答案
print('2016年这只股票固定资产占总资产的比例的均值是{}'.format( rate2016.mean()))
print('固定资产占总资产比例最小的股票是的代码是{}'.format(fundamentals.loc[rate2016_min_index, 'Ticker Symbol']))
