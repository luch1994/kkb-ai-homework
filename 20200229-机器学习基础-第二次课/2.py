"""

securities.csv包含了这些股票的基本信息

请列举出各个sector中的加入时间最早的股票名称（10分）
请列举出每一个州中加入时间最晚的股票名称（10分）

"""
import pandas as pd

# 读取csv文件
df = pd.read_csv('./securities.csv')

# 将加入时间列转换成时间，因为Date first added有空的列，使用fillna把空格替换成1970-01-01
df['Date first added'] = pd.to_datetime(df['Date first added'].fillna('1970-01-01'))

# 第一问
print('请列举出各个sector中的加入时间最早的股票名称', '*' * 20)
# 按GICS Sector分组，取Date first added列的最小值
print(df.groupby('GICS Sector')['Date first added'].min())

# 第二问
print('请列举出每一个州中加入时间最晚的股票名称', '*' * 20)
# 按州（Address of Headquarters）分组，取出时间最小的分组的行号下标
min_index = df.groupby('Address of Headquarters')['Date first added'].idxmin()
# 打印对应下标的股票代码
print(df.loc[min_index, 'Ticker symbol'])
