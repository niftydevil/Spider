# -*- coding:utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import html
import xml
import requests
import os
import csv
import time

# selenium自动打开豆瓣电影首页
# driver = webdriver.Chrome()
# driver.get('https://movie.douban.com/')
# driver.maximize_window()

# 爬取数据，写入csv文件
# 1. 爬取热门电影，获取热门电影的图片，电影名称，分数，保存到CSV文件中
url = 'https://movie.douban.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, "lxml")   # 因为保存的内容有图片，所以以content获取内容
# 创建soup对象，获取网页内容之后，开始查找所需爬取的数据
divs = soup.find_all('div', class_='slide-page')
print(divs)
for div in divs:   
    # 获取一个div下的所有img标签
    images = div.find_all('img')
    names = div.find_all('p')
    scores = div.find_all('strong')
    # images是列表，遍历获取每一个图片
    for image in images:
        film_image = image.attr['src']
    # names是列表，遍历获取每一个电影名称
    for name in names:
        film_name = image.find_all('p')
    # scores是列表，遍历获取每一个电影的评分
    for score in scores:
        film_score = image.find_all('strong')

    # 文件路径，名称
    time_now = time.strftime('%Y%m%d%H%M%S', time.localtime())
    filename = os.path.abspath('.') + '/热门电影' + time_now + '.csv'
    # 定义csv文件的表头
    headers = ['电影图片', '电影名称','电影评分']
    # 定义csv文件除了表头之外的内容
    rows = [film_image, film_name, film_score]
    # 创建一个csv文件，将文件对象作为参数传给csv.writer()，最后将表头和每一行的内容写入到csv文件中
    print('=================')
    with open(filename, 'ab+', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)



# 2. 爬取最新电影，

# 3. 爬取豆瓣高分电影，

# 邮箱发送，文件作为附件一起发送

# 定时爬取数据，发送邮件