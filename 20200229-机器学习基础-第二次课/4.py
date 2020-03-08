"""

请导入price.csv，然后结合你的聪明才智回答以下问题（附加题，40分）

假设你是某基金公司的老板，现在对于每只股票，你都专门安排了一位负责它的交易员。
公司规定每一位交易员手中的资金要么全部买入要么全部卖出（空仓，转化为现金）。
假设2016年每一位交易员手中都有10000美元，
假设他们都能够看到2016年全年的数据，
假设他们都能抓住每一次机会，
那么请问2016年底时，赚钱最多的股票是哪一只，赚了多少钱？

"""

import pandas as pd

# 读取prices.csv
df = pd.read_csv('./prices.csv')

# 将日期列转换为日期格式
df['date'] = pd.to_datetime(df['date'])

# 2016年的开始和结束时间
start_2016 = pd.Timestamp(2016, 1, 1)
end_2016 = pd.Timestamp(2016, 12, 12)

# 过滤出2016年的数据
data_2016 = df[(df['date'] >= start_2016) & (df['date'] <= end_2016)]

# 根据名称分组
rate_data = df.groupby('symbol')

ret = []

# 遍历分组
for name, group in rate_data:
    # 计算方式是，在最低价买入，再最高价卖出，本次获利的倍数就是最高价比上最低价
    rate_data = group['high'] / group['low']
    rate = 1
    # 计算累计最低价
    for i, v in rate_data.items():
        rate *= v
    ret.append((name, rate))

# 根据倍数排序
ret.sort(key=lambda x: x[1])
# 最大的数据
max_data = ret[-1]
print("最大的股票是{}，赚了{}钱".format(max_data[0], (max_data[1] - 1) * 10000))