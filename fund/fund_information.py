import requests
import re

from bs4 import BeautifulSoup

url = "http://fund.eastmoney.com/daogou"
# response = requests.get(url)
# print(response.url)
html = requests.get(url).content
soup = BeautifulSoup(html, 'lxml')
fund_infos = soup.find_all('tr', id=re.compile('^tr'))


def fund_information():
    for fund_info in fund_infos:
        # 基金链接
        fund_link = fund_info.a['href']
        # print(fund_link)
        # 基金名称
        fund_name = fund_info.a.string
        # print(fund_name)
        # 基金代码
        fund_code = fund_info.span.string
        # print(fund_code)
        # 基金类型
        fund_type = fund_info.find('td', class_='fname').next_sibling.string
        # print(fund_type)
        # 基金净值
        fund_net_worth = fund_info.find('span', class_='ping').string
        # print(fund_net_worth)
        # 基金日增长率
        fund_daily_growth_rate = fund_info.find('span', class_='zhang').string
        # print(fund_daily_growth_rate)
        # 日期
        fund_date = fund_info.find('span', class_='gray').string
        # print(fund_date)
        # 近1周增长率
        fund_one_week = fund_info.contents[4].string
        # print(fund_one_week)
        # 近1月增长率
        fund_one_month = fund_info.contents[5].string
        # 近3月增长率
        fund_three_month = fund_info.contents[6].string
        # 近6月增长率
        fund_six_month = fund_info.contents[7].string
        # 今年来增长率
        fund_this_year = fund_info.contents[8].string
        # 近1年增长率
        fund_one_year = fund_info.contents[9].string
        # 近2年增长率
        fund_two_year = fund_info.contents[10].string
        # 近3年增长率
        fund_three_year = fund_info.contents[11].string
        # 手续费
        fund_rate_link = fund_info.find('div', class_='l').a['href']
        fund_rate = fund_info.find('div', class_='l').a.string
        # 购买起点
        fund_min_purchase_money = fund_info.find('div', class_='r').string
