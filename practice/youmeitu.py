import requests
import time

from bs4 import BeautifulSoup
from datetime import datetime

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
        a = li.a["href"]      # 获取属性的值，直接"标签.属性"或者a.get("href")  若是获取标签中文本的值，需要.text
        # print(a)
        child_url = url + a.strip("/")
        # print(child_url)
        # 获取子页面中图片的下载链接
        # 获取子页面的源代码
        child_response = requests.get(child_url)
        # 把子页面的源代码格式化
        child_page_content = child_response.text
        # 创建bs对象
        child_bs = BeautifulSoup(child_page_content, "html.parser")
        # 通过bs对象查找需要的内容，先通过id找到div标签
        child_div = child_bs.find("div", id='ArticleId60')
        # 在找到的div标签中查找img标签，通过get()方法，获取img里面src的属性值
        child_src = child_div.find("img").get("src")
        # 下载图片，通过requests.get()方法下载
        img_download = requests.get("https://www.youmeitu.com" + child_src)
        # img_download.content         # 这里拿到的是字节，存储到文件中，就是图片
        # 拿到链接中最后一个/ 后面的内容作为存储图片的名称
        # 保存图片
        # img_name = img_download.split("/").[-1]
        dt = datetime.now()
        img_name = dt.strftime('%Y%m%d%H%M%S')
        with open("img/" + img_name + ".jpg", mode="wb") as f:
            f.write(img_download.content)     # 图片内容写入文件
        print("over!!!" + img_name)
        time.sleep(2)

