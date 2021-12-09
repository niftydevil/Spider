# https://oapi.dingtalk.com/robot/send?access_token=784a5c665be03151834af87b768b46346b195c9b6d44e0f9fca91b4967b5a29d
import requests
import json
import time
import schedule

from bs4 import BeautifulSoup
from lxml import etree


def job():
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=784a5c665be03151834af87b768b46346b195c9b6d44e0f9fca91b4967b5a29d'

    header = {
        "content-type": "application/json",
        "charset": "utf-8"
    }

    # def func():
    weather_url = "http://www.weather.com.cn/weather1d/101020100.shtml"
    weather_header = {
        # "content-type": "application/json",
        # "charset": "utf-8",
        "Cookie": "userNewsPort0=1; defaultCty=101020700; defaultCtyName=%u91D1%u5C71; f_city=%E9%87%91%E5%B1%B1%7C101020700%7C; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1636100367,1636100383; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1636100472",
        "Referer": "http://www.weather.com.cn/weather/101020100.shtml",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    weather_response = requests.get(url=weather_url, headers=weather_header)
    # bs = BeautifulSoup(weather_response.text, "html.parser")
    weather_response.encoding = 'utf-8'
    tree = etree.HTML(weather_response.text)
    # print(weather_response.text)
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    temperature = str(tree.xpath('//*[@id="hidden_title"]/@value')).strip('['']')

    print(temperature)

    data = {
        "msgtype": "text",
        "text": {
            "content": "天气预报：" + temperature
        },
        "isAtAll": False
    }

    data_json = json.dumps(data)

    info = requests.post(url=webhook, data=data_json, headers=header)
    print(info.text)


schedule.every().minutes.do(job)
# schedule.every().day.at("8:30").do(job)         # 每天在 8:30 时间点运行 job 函数

while True:
    schedule.run_pending()  # 运行所有可以运行的任务
    time.sleep(1)
