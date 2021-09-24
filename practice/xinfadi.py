import requests
import re

from bs4 import BeautifulSoup

url = "http://www.xinfadi.com.cn/getPriceData.html"
response = requests.post(url)
page_content = response.text
print(page_content)

# 正则获取
com = re.compile(r'.*?"prodName":"(?P<name>.*?)","prodCatid"', re.S)
results = com.finditer(page_content)
for result in results:
    print(result.group("name"))

# 生成bs对象，处理页面源代码
bs = BeautifulSoup(page_content, "html.parser")
name = bs.find_all("prodName")
# print(name)

