# 西瓜数据保存和读取
"""
添加编号列，并将数据集写入到machine_learning.csv文件，使用pandas读取验证文件是否有效(无错即可)。
添加一条记录，青绿 硬挺 浊响 稍糊 平坦 硬滑 0.666 0.111 好
再使用普通文件读取将数据集读取出来，列名读取到columns，数据(带编号)读取到datalist
在所有数据中过滤出色泽='浅白'的数据
在所有数据中过滤出密度大于0.5的数据
"""

import pandas as pd

dataset = \
"""色泽 根蒂 敲声 纹理 脐部 触感 密度 含糖率 好瓜
青绿 蜷缩 浊响 清晰 凹陷 硬滑 0.697 0.460 是
乌黑 蜷缩 沉闷 清晰 凹陷 硬滑 0.774 0.376 是
乌黑 蜷缩 浊响 清晰 凹陷 硬滑 0.634 0.264 是
青绿 蜷缩 沉闷 清晰 凹陷 硬滑 0.608 0.318 是
浅白 蜷缩 浊响 清晰 凹陷 硬滑 0.556 0.215 是
青绿 稍蜷 浊响 清晰 稍凹 软粘 0.403 0.237 是
乌黑 稍蜷 浊响 稍糊 稍凹 软粘 0.481 0.149 是
乌黑 稍蜷 浊响 清晰 稍凹 硬滑 0.437 0.211 是
乌黑 稍蜷 沉闷 稍糊 稍凹 硬滑 0.666 0.091 否
青绿 硬挺 清脆 清晰 平坦 软粘 0.243 0.267 否
浅白 硬挺 清脆 模糊 平坦 硬滑 0.245 0.057 否
浅白 蜷缩 浊响 模糊 平坦 软粘 0.343 0.099 否
青绿 稍蜷 浊响 稍糊 凹陷 硬滑 0.639 0.161 否
浅白 稍蜷 沉闷 稍糊 凹陷 硬滑 0.657 0.198 否
乌黑 稍蜷 浊响 清晰 稍凹 软粘 0.360 0.370 否
浅白 蜷缩 浊响 模糊 平坦 硬滑 0.593 0.042 否
青绿 蜷缩 沉闷 稍糊 稍凹 硬滑 0.719 0.103 否"""

# 将数据写入csv文件
# your code here 
file = r'machine_learning.csv' # 文件名称，学员可修改或不修改
# 将数据转化为列表
dataset = list(map(lambda item: item.split(' '), dataset.split('\n')))
# 循环列表，添加上编号列
for i in range(len(dataset)):
    if i == 0:
        dataset[i].insert(0, '编号')
    else:
        dataset[i].insert(0, '{}'.format(i))
# 将新加入的数据转换为字符串
txtdata = '\n'.join([','.join(item) for item in dataset])
# 写入数据
with open(file, 'w', encoding='utf-8') as f:
    f.write(txtdata)


# 向csv文件中加入一条新的数据（数据已给出）
# your code here
# 注意每一行数据的间隔符号是什么
inser_data = '18 青绿 硬挺 浊响 稍糊 平坦 硬滑 0.666 0.111 是'
# 使用a，表示追加数据，不改变原有数据
with open(file, 'a', encoding='utf-8') as f:
    f.write('\n' + ','.join(inser_data.split(' ')))



"""
使用pandas读取和过滤数据
"""
# 查看全体数据
df = pd.read_csv(file, dtype=str)
print(df.head())


# 读取文件存储的数据
# your code here
# columns是指列标签
# datalist指全体数据内容，每一行数据应为一个列表
columns = df.columns.values
datalist = df.values

# print(columns)
# print(datalist)

# 验证数据信息是否相符
print(columns==['编号', '色泽', '根蒂', '敲声', '纹理', '脐部', '触感', '密度', '含糖率', '好瓜'])
print(datalist[-1]==['18', '青绿', '硬挺', '浊响', '稍糊', '平坦', '硬滑', '0.666', '0.111', '是'])

# # 在所有数据中过滤出色泽='浅白'的数据
# # 在所有数据中过滤出密度大于0.5的数据
datalist1 = datalist[datalist[:, 1] == '浅白']
datalist2 = datalist[datalist[:, 7].astype('float') > 0.5]

print('过滤浅白数据', '*' * 20)
print(datalist1)
print('过滤密度大于0.5的数据', '*' * 20)
print(datalist2)


"""
使用open函数读取，和filter过滤数据的方法
"""

# with open(file, 'r', encoding='utf-8') as f:
#     txtdata = f.read()
#     datas = list(map(lambda row: row.split(','), txtdata.split('\n')))
#     columns = datas[0]
#     datalist = datas[1:]

# print('验证数据是否相符', '*' * 20)
# # 验证数据信息是否相符
# print(columns==['编号', '色泽', '根蒂', '敲声', '纹理', '脐部', '触感', '密度', '含糖率', '好瓜'])
# print(datalist[-1]==['18', '青绿', '硬挺', '浊响', '稍糊', '平坦', '硬滑', '0.666', '0.111', '是'])

# # 在所有数据中过滤出色泽='浅白'的数据
# # 在所有数据中过滤出密度大于0.5的数据
# # your code here
# datalist1 = list(filter(lambda row: row[1] == '浅白', datalist))
# datalist2 = list(filter(lambda row: float(row[7]) > 0.5, datalist))

# print('过滤浅白数据', '*' * 20)
# print(datalist1)
# print('过滤密度大于0.5的数据', '*' * 20)
# print(datalist2)
