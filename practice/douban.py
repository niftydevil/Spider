import requests
import re

# 访问页面，获取页面源代码
url = 'https://movie.douban.com/j/chart/top_list'
param = {
    "type": "5",
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20
}
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}
response = requests.get(url=url, params=param, headers=header)
page_content = response.text
# print(res.json())

# 解析数据，在获取的页面源代码中解析数据
# <div class="movie-content">.*?
# 预加载正则表达式
com = re.compile(r'<a href="https://movie.douban.com/subject/1303408/" target="_blank">(?P<name>.*?)</a>', re.S)
# 开始在获取的源代码中匹配正则
results = com.finditer(page_content)
print(results)
for result in results:
    print(result.group("name"))

