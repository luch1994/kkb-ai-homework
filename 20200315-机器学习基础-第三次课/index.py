"""

同学们大家好，本次作业是考察学生对线性回归的理解与SKLearn的使用，以及pandas的使用。

本次作业的数据集：data.csv 这份数据代表了一个循环发电厂，每个数据有5列，分别是:AT（温度）, V（压力）, AP（湿度）, RH（压强）, PE（输出电力)

问题是得到一个线性的关系，对应PE是样本输出，而AT/V/AP/RH这4个是样本特征， 机器学习的目的就是得到一个线性回归模型，即: PE=W0+W1∗AT+W2∗V+W3∗AP+W4∗RH 而需要学习的，就是W0,W1,W2,W3,W4这5个参数。

"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv('./data.csv')

# 总数据量
NUM_ROWS = df.shape[0]

# 生成全为1的常数项
col0 = pd.Series([1 for x in range(NUM_ROWS)])

# 添加常数项
df['constant'] = col0

# 将数据拆分成x和y
x = df[['constant', 'AT', 'V', 'AP', 'RH']]
y = df['PE']

# 将数据拆分为训练和测试数据集
# 取前九千个为训练数据，后面的数据为验证数据
train_x = x[:9000]
train_y = y[:9000]
test_x = x[9000:]
test_y = y[9000:]

# 创建模型
lr = LinearRegression()
# 训练模型
lr.fit(train_x, train_y)

# 得到参数
w0, w1, w2, w3, w4 = lr.coef_
print(w0, w1, w2, w3, w4)

# 预测测试集结果
pred_y = lr.predict(test_x)

# 计算均方误差
mse = (np.square(test_y - pred_y).sum()) / test_x.shape[0]
# 计算均方根误差
rmse = np.sqrt(mse)

print('均方误差：' + str(mse))
print('均方根误差：' + str(rmse))

# 画图
plt.scatter(pred_y, test_y)
plt.show()

# 根据图可以看出，大部分点都在y=x这条直线的附近


# 计算R2，验证数据，越接近1说明越好
# R2 = lr.score(test_x, test_y)
# print('R2:' + str(R2))
