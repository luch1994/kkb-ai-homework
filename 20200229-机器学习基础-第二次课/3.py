"""

现在你需要同时处理来自两个表中的信息了

请思考，合并两个表的信息的时候，我们应该用什么样的准则对其它们（10分）
请列举每个sector在2013-2016年累计Research&Development的总投入（10分）
请列举出每个sector中，在2013-2016年累计Research&development投入最大的3家公司的名称以及投入的数值（20分）

"""

# 第一问思考
"""

在合并两个表格的时候，需要先根据实际业务
是需要直接上下拼接到一起，还是需要根据什么条件进行数据连接

如果是上下直接拼接的话，使用concat方法即可
如果两个表列名完全一样，则没有问题
如果列名不一样，会产生NaN，要考虑NaN用什么替换

如果是需要对数据进行左右合并的话
要考虑一下他们是否相同的列
还有合并的条件是什么，是哪种合并方式（inner，left，right，outer）

"""

import pandas as pd
fundamentals = pd.read_csv('./fundamentals.csv')
securities = pd.read_csv('./securities.csv')

# 将列名转化成小写再重新赋值，以便合并的时候可以合并
fundamentals.columns = fundamentals.columns.str.lower()
securities.columns = securities.columns.str.lower()

# 使用inner的方式合并
df = pd.merge(fundamentals, securities, how='inner')

# 将日期列转换成日期类型
df['period ending'] = pd.to_datetime(df['period ending'])

# 开始和结束时间
start_2013 = pd.Timestamp(2013, 1, 1)
end_2016 = pd.Timestamp(2016, 12, 31)

# 根据时间过滤数据
filter_data = df[(df['period ending'] >= start_2013) & (df['period ending'] <= end_2016)]

# 第二问
# 过滤得到的数据选取research and development列进行求和，根据gics sector分组
res = filter_data['research and development'].groupby(filter_data['gics sector']).sum()
print('每个sector在2013-2016年累计Research&Development的总投入为：')
print(res)

def top(df, n=3, column='research and development'):
    return df.sort_values(by=column)[-n:]

# 根据时间过滤的数据，先根据gics sector分组，再根据research and development进行组内排序取最后三个数据，即最大的三个
res1 = filter_data.groupby('gics sector').apply(top)
# 第三问
# 显示公司的名称以及投入的数值
print(res1[['ticker symbol', 'research and development']])
