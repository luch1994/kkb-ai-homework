from bs4 import BeautifulSoup
import requests
import os

# 获取a标签的href属性里的城市拼音和a标签的内容
def get_city_and_coding(aTag):
    href = aTag.attrs['href']
    coding = href[5:href.index('.')]
    city = aTag.string.strip()
    return (city, coding)

# 获取城市中文和对应拼音的字典
def get_city_coding(file='./city_coding'):
    # your code
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), features='html.parser')
        aList = soup.findAll('a')
        coding_list = list(map(get_city_and_coding, aList))
        return dict(coding_list)

#输入城市 年 月 输出 url地址
def build_url(city_coding, year=None, month=None):
    base_url = ' http://www.tianqihoubao.com/aqi/'
    if year is not None and month is not None:
        return base_url + '{}-{}{:0>2d}.html'.format(city_coding, year, month)
    else:
        return base_url + '{}.html'.format(city_coding)


def parse(url, city_name):
    # your code
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, features='html.parser')
        content = soup.table.contents
        result = []
        for index, c in enumerate(content[1::2]):
            if index == 0:
                result.append(tuple(['城市'] + c.text.split()))
            else:
                result.append(tuple([city_name] + c.text.split()))
        return result
    else:
        print('request fail with status code {}'.format(response.status_code))

def save_csv(file, data):
    # your code 
    if os.path.exists(file):
        with open(file, 'a', encoding='utf-8') as f:
            for d in data[1:]:
                f.write(','.join(d))
                f.write('\n')
    else:
        with open(file, 'w', encoding='utf-8') as f:
            for d in data:
                f.write(','.join(d))
                f.write('\n')

# 主函数
def crawler_all():
    # 保存的文件名
    file = './data/allcity_2019.csv'
    
    city_codings = get_city_coding()
    allcities = list(city_codings.keys())
    # result = parse('http://www.tianqihoubao.com/aqi/hangzhou-202001.html', '杭州')
    # save_csv(file, result)
    for city in allcities:
        city_code = city_codings[city]
        for year in range(2019,2012,-1):
            for month in range(1,13):
                url = build_url(city_code, year, month)
                result = parse(url, city_code) # city
                print(f'\r{city} {year}-{month} {len(result)}', end='')
                save_csv(file, result)
                time.sleep(1)

if __name__ == '__main__':
    crawler_all()