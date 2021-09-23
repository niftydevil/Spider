import requests
import re

domain = "https://dytt8.net/"
res = requests.get(domain)    # verify=False  去掉安全验证（现在可以不加，但是有这么一个功能）
res.encoding = 'gb2312'    # 指定字符集，网页采用的gb2312编码，这边也需要指定编码为gb2312
# print(res.text)
page_content = res.text

obj1 = re.compile(r"2021新片精品<table>(?P<info>.*?)</table>", re.S)
results = obj1.finditer(page_content)
print(results)
for result in results:
    print(result.group("info"))