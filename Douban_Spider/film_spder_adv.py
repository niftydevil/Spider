# -*- coding:utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import html
import xml
import requests
import os

# selenium自动打开豆瓣电影首页
driver = webdriver.Chrome()
driver.get('https://movie.douban.com/')
driver.maximize_window()

# 爬取数据，写入csv文件
# 1. 爬取热门电影，获取热门电影的图片，电影名称，分数，保存到CSV文件中
url = 'https://movie.douban.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, "lxml")   # 因为保存的内容有图片，所以以content获取内容
# 创建soup对象，获取网页内容之后，开始查找所需爬取的数据
divs = soup.find_all('div', class_='')

# 2. 爬取最新电影，

# 3. 爬取豆瓣高分电影，

# 邮箱发送，文件作为附件一起发送

# 定时爬取数据，发送邮件