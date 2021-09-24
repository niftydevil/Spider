import requests
import re

domain = "https://dytt8.net/"
res = requests.get(domain)  # verify=False  去掉安全验证（现在可以不加，但是有这么一个功能）
res.encoding = 'gb2312'  # 指定字符集，网页采用的gb2312编码，这边也需要指定编码为gb2312
# print(res.text)
page_content = res.text

obj1 = re.compile(r"2021新片精品.*?<ul>(?P<info>.*?)</ul>", re.S)
# 获取链接
obj2 = re.compile(r">最新电影下载.*?<a href='(?P<url>.*?)'>(?P<name>.*?)</a>", re.S)
results1 = obj1.finditer(page_content)
results2 = obj2.finditer(page_content)
child_href_list = []
# print(results1)
# for result1 in results1:
# print(result1.group("info"))
for result2 in results2:
    # print(result2.group("url"))
    # print(result2.group("name"))
    # 拼接子页面的url
    child_href = domain + result2.group("url").strip("/")
    # print(child_href)
    child_href_list.append(child_href)
    # print(child_href_list)

for child_href in child_href_list:
    child_resp = requests.get(child_href)
    child_resp.encoding = 'gb2312'
    child_page_content = child_resp.text
    # 下面开始写正则，提取需要的东西
    child_obj = re.compile(r"<div>◎译　　名　(?P<film_name>.*?)</div>", re.S)
    child_results = child_obj.finditer(child_page_content)
    for child_result in child_results:
        print(child_result.group("film_name"))
