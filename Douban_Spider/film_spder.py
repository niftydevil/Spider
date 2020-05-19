# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from lxml import html
import xml
import requests
import os

# 想要爬取数据页面的url
url = "https://movie.douban.com/chart"
# 豆瓣的反爬机制，需要加上headers，否则不会返回任何数据，固定从网站copy
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
            }
# 获取返回对象
r = requests.get(url, headers=headers)
# 创建soup对象，获取网页内容，解析对象抓取数据
soup = BeautifulSoup(r.text, "lxml")
# print(soup)
# print(soup.contents)
# 查找所有class=pl2的div元素
for k in soup.find_all('div',class_='pl2'):
    # 查找所有div中的span标签
    a = k.find_all('span')
    # 保存文件的路径
    filename = os.path.abspath('.') + '/电影排行.txt'
    # print(filename)
    # 保存文件
    with open(filename, 'a+', encoding='utf-8') as f:
        # 把span标签下第一个a标签的内容返回，输出到文件
        r = a[0].string
        if r != None:
            f.write(r + '\n')
        else:
            f.write('空' + '\n')