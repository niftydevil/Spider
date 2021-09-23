import requests
import re
import csv

from datetime import datetime

# 把结果存储到csv文件中
dt = datetime.now()
dt_format = dt.strftime('%Y%m%d%H%M')
f = open(dt_format + "douban.csv", mode="w")
csv_write = csv.writer(f)

for i in range(0, 41, 20):
    # 访问页面，获取页面源代码
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        "type": "5",
        "interval_id": "100:90",
        "action": "",
        "start": i,
        "limit": 20
    }
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    response = requests.get(url=url, params=param, headers=header)
    print(response.url)
    page_content = response.text
    # print(page_content)

    # 解析数据，在获取的页面源代码中解析数据
    # 预加载正则表达式
    com = re.compile(r'"title":"(?P<title>.*?)".*?"url":"(?P<url>.*?)".*?"release_date":"(?P<release_date>.*?)".*?'
                     r'"score":"(?P<score>.*?)"', re.S)
    # 开始在获取的源代码中匹配正则，把匹配到的结果都放到results中
    results = com.finditer(page_content)

    # print(results)
    for result in results:
        # print(result.group("title"))
        # print(result.group("url"))
        # print(result.group("release_date"))
        # print(result.group("score"))
        # 把结果存储在一个字典中
        # print(result)
        dic = result.groupdict()
        # print(dic)
        # 写入csv文件中
        csv_write.writerow(dic.values())


f.close()
print("over!")
