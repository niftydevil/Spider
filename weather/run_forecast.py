# https://oapi.dingtalk.com/robot/send?access_token=784a5c665be03151834af87b768b46346b195c9b6d44e0f9fca91b4967b5a29d
import requests
import json
import time
import schedule

from bs4 import BeautifulSoup
from lxml import etree
from forecast import Forecast


def job():
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=784a5c665be03151834af87b768b46346b195c9b6d44e0f9fca91b4967b5a29d'

    header = {
        "content-type": "application/json",
        "charset": "utf-8"
    }

    # def func():
    # 天气
    forecast = Forecast()
    # forecast.forecast()

    data = {
        "msgtype": "text",
        "text": {
            "content": "天气预报：" + forecast.forecast()
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
