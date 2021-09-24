import requests

from bs4 import BeautifulSoup

url = "https://www.youmeitu.com/weimeitupian/"

response = requests.get(url)
# print(response.text)
page_content = response.text

bs = BeautifulSoup(page_content, "html.parser")
divs = bs.find_all("div", class_="TypeList")
# print(divs)
for div in divs:
    lis = div.find_all("li")
    # print(lis)
    for li in lis:
        a = li.a["href"]      # 获取属性的值，直接"标签.属性"  若是获取标签中文本的值，需要.text
        print(a)


