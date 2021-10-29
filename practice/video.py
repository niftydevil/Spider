# 抓取一个视频的一般步骤
# 1：找到m3u8文件（网站用来存放视频的文件，视频会被切片成一个个ts）
# 2：通过m3u8找到ts文件，并下载
# 3：把下载的ts文件合并为一个mp4文件


# 不能直接使用该url，因为该url中的note后面的值是变量（反爬机制）
# url = "https://m3api.awenhao.com/index.php?note=kkRns1ampqczh8xw94gek&raw=1&n.m3u8"

import requests
import re       # 从JS中提取内容，用re

url = "http://91kanju2.com/vod-play/60826-1-1.html"
url = "http://91kanju2.com/vod-play/60991-1-1.html"
response = requests.get(url)
# print(response.text)
com = re.compile(r"url: '(?P<url>.*?)',", re.S)   # 用来提取m3u8的地址
m3u8_url = com.search(response.text).group("url")            # 拿到m3u8的地址
# print(m3u8_url)
# 下载m3u8
m3u8_response = requests.get(m3u8_url)
# 保存m3u8
with open("video/长津湖.m3u8", mode="wb") as f:
    f.write(m3u8_response.content)



# 解析m3u8文件
n = 1
with open("video/长津湖.m3u8", mode="r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line.startswith("#"):
            continue

        video_response = requests.get(line)
        with open(f"video/{n}.mp4", mode="wb") as f:
            f.write(video_response.content)
        f.close()
        video_response.close()
        n += 1
        print(f"完成第{n}个")