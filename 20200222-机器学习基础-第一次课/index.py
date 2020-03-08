import math
from collections import Counter
# 坐标
x = [(1, 1), (0.4, 5.2), (-2.8, -1.1), (3.2, 1.4), (-1.3, 3.2), (-3, 3.1)]
# 坐标对应分类
y = [2, 1, 2, 1, 1, 2]

# 需要求解分类的坐标点
x_new = [(-2.6, 6.6), (1.4, 1.6), (-2.5, 1.2)]

k = 1

# 结果数组
res = []

for p in x_new:
    # 每个原始点距需要求解点的距离数组
    distances = []
    for i, item in enumerate(x):
        distance = math.sqrt((item[0] - p[0]) ** 2 + (item[1] - p[1]) ** 2)
        distances.append((distance, y[i]))
    distances.sort(key = lambda x: x[0])
    # print(distances)
    # 找出距离最近的k个点的分类
    shortest = [item[1] for item in distances[:k]]
    # print(shortest)
    # 统计前K个数据里，每个分类出现的次数
    counter = Counter(shortest)
    # print(counter)
    # 找出分类出现次数最多的一个
    # 返回的是数组，得到的每一项是元组，元组的下标，0是key，1的出现的次数
    most = counter.most_common(1)
    # print(most)
    res.append(most[0][0])

print(res)