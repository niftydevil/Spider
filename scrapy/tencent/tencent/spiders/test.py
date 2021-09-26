# from selenium import webdriver
import requests
from bs4 import BeautifulSoup
# driver = webdriver.Chrome()

url = 'https://careers.tencent.com/search.html?index=1'

myHeaders = {"accept": "application/json, text/plain, */*",
             "accept-encoding": "gzip, deflate, br",
             "accept-language": "zh-CN,zh;q=0.9",
             "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/92.0.4515.107 Safari/537.36",
             "referer": "https://careers.tencent.com/search.html?index=1",
             "cookie": "_ga=GA1.2.873545319.1629882468; "
                       "sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217b7c90c56c249-06e600bc0723b3-35627203"
                       "-1296000-17b7c90c56dcd2%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22"
                       "%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F"
                       "%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22"
                       "%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com.hk%2F%22%7D%2C%22%24device_id%22%3A"
                       "%2217b7c90c56c249-06e600bc0723b3-35627203-1296000-17b7c90c56dcd2%22%7D; "
                       "_gcl_au=1.1.1206556651.1629882491; loading=agree"
             }

response = requests.get(url, headers=myHeaders)
# file = open('', 'rb')
html = response.text
bs = BeautifulSoup(html, "html.parser")

print(bs.div)


