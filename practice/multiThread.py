# def func():
#     for i in range(3):
#         print("func", i)
#
#
# if __name__ == '__main__':
#     func()
#     for i in range(5):
#         print("main", i)

# 多线程，需要导入一个包
# from threading import Thread
#
#
# def func():
#     for i in range(3):
#         print("func", i)
#
#
# if __name__ == '__main__':
#     t = Thread(target=func)  # 创建一个线程类对象，并且告诉对象，当前线程要执行的是func
#     t.start()  # 开始执行该线程（可以开始工作状态，具体何时执行，CPU决定）
#     for i in range(5):
#         print("main", i)

# 多线程，方法二
# from threading import Thread
#
#
# class MyThread(Thread):
#     def run(self):  # 固定方法名  当线程被执行的时候，被执行的就是run()
#         for i in range(5):
#             print("子线程", i)
#
#
# if __name__ == '__main__':
#     t = MyThread()   # 创建MyThread对象
#     t.start()  # 开启线程
#     for i in range(5):
#         print("主线程", i)


# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
#
#
# def func(name):
#     print(name)
#
#
# if __name__ == '__main__':
#     # 创建线程池
#     with ThreadPoolExecutor(5) as t:
#         for j in range(100000):
#             t.submit(func, name=f"***{j}***")


# 1. 如何提取单个页面的数据
# 2. 上线程池，多个页面同时抓取
import requests
import time
import csv

from openpyxl import Workbook
from concurrent.futures import ThreadPoolExecutor

# with open("data.csv", mode="w", encoding="utf-8") as f:
#     csvwriter = csv.writer(f)
# 保存到csv文件中，创建csv对象
f = open("data.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)

# 保存到Excel文件中，创建工作簿对象，通过工作簿创建表格对象
wb = Workbook()
products = wb.create_sheet("products", 0)


def download_one_page(response):
    # response = requests.get(url)
    # print(response.text)
    product_lists = response.json()["list"]
    # print(product_lists)
    for product in product_lists:
        # print(product)
        product_id = product["id"]
        product_name = product["prodName"]
        product_Cat = product["prodCat"]
        product_lowPrice = product["lowPrice"]
        product_highPrice = product["highPrice"]
        product_avgPrice = product["avgPrice"]
        product_unitInfo = product["unitInfo"]
        # 日期格式更改，先转换为时间数据，然后转为其他格式
        product_pubDate = time.strptime(product["pubDate"], "%Y-%m-%d %H:%M:%S")
        product_pubDate_ft = time.strftime("%Y-%m-%d", product_pubDate)
        product_info = [product_id, product_name, product_Cat, product_lowPrice,
                        product_highPrice, product_avgPrice, product_unitInfo,
                        product_pubDate_ft]
        # 保存到csv文件中
        csvwriter.writerow(product_info)
        # 保存到Excel文件中
        products.append(product_info)
        wb.save("data.xlsx")
        # print(product_info)


def get_url():
    # 使用线程池，最大一次20个 爬取50个页面 打印时间看耗时
    url = "http://www.xinfadi.com.cn/getPriceData.html"
    with ThreadPoolExecutor(20) as t:
        for i in range(1, 50):
            param = {
                "current": i,
                "limit": 20
            }
            header = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/94.0.4606.71 Safari/537.36 "
            }
            response = requests.get(url, params=param, headers=header)
            # print(response.url)
            t.submit(download_one_page, response)

    # 不使用线程池 爬取50个页面 打印时间看耗时
    # url = "http://www.xinfadi.com.cn/getPriceData.html"
    # for i in range(1, 50):
    #     param = {
    #         "current": i,
    #         "limit": 20
    #     }
    #     header = {
    #         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) "
    #                       "Chrome/94.0.4606.71 Safari/537.36 "
    #     }
    #     response = requests.get(url, params=param, headers=header)
    #     # print(response.url)
    #     download_one_page(response)


if __name__ == '__main__':
    # download_one_page("http://www.xinfadi.com.cn/getPriceData.html")
    print(time.localtime())
    get_url()
    print(time.localtime())
