#  爬虫数据集筛选及保存

import requests
from bs4 import BeautifulSoup

# 以前遇到过的函数

def build_url(city_coding, year=None, month=None):
    """
    创建网页链接
    paramters:
        city_coding: 城市名称(英文)
        year: 年份
        month: 月份
    return:
        url: 可访问的链接
    """
    BASE = 'http://www.tianqihoubao.com/aqi/'
    city_base_url = BASE + '{}.html'
    city_date_base_url = BASE + '{}-{}{}.html'
    
    if year is not None and month is not None:
        month = str(month) if month >= 10 else '0' + str(month)
        return city_date_base_url.format(city_coding, year, month)
    else:
        return city_base_url.format(city_coding)


def parse(url, city_name):
    """
    抓取网页信息
    parameters:
        url: 需要抓取的网页链接
        city_name: 城市名称(用于数据标识)
    returns:
        result: 抓取的信息
    """
    response = requests.get(url)
    if response.ok:
        html = response.text
        
        soup = BeautifulSoup(html, features='html.parser')
        data_table = soup.table
        
        content = data_table.contents
        
        result = []
        for index, c in enumerate(content[1::2]):
                if index == 0:
                    result.append(tuple(['城市'] + c.text.split()))
                else:
                    result.append(tuple([city_name] + c.text.split()))
        return result
    
    else:
        if response.status_code == 403:
            print('403 Forbidden! 抓取太快你被拉黑啦~')

            
def save(data, file):
    # 完成数据保存到文件
    # 使用open函数打开文件，w表示写文件并覆盖原文件内容，设置字符编码utf-8防止中文乱码
    with open(file, 'w', encoding='utf-8') as f:
        # 将数据分割成，每个月份的数据占一行，每一行的数据使用,隔开的字符串
        txtdata = '\n'.join(list(map(lambda item: ','.join(item), data)))
        # 将数据写入文件
        f.write(txtdata)
    print('data saved in ', file)
    

if __name__ == '__main__':
    datas = []
    for i in range(1, 2):
        url = build_url('hangzhou', 2019, i)
        data = parse(url, '杭州')
        datas.extend(data)
    
    # 只保留质量等级优 良 数据
    
    datas = [datas[0]] + list(filter(lambda item: item[2] == '优' or item[2] == '良', datas[1:]))

    # 提示：用什么方法对数据进行筛选？
    
    # 保存数据
    save(datas, './data.txt')