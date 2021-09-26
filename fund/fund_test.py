# coding=utf-8
import json
import re
import ssl
import urllib.error
import urllib.request
import time

import pymysql
import xlwt
from bs4 import BeautifulSoup
from multiprocessing import Process


def main():
    baseurl = "http://fund.eastmoney.com/js/fundcode_search.js"
    # datalist = get_data()
    savepath = "fundscore.xls"
    # html = ask_url(baseurl)
    f = open('demo.json', 'r', encoding="utf-8")
    content = f.read()
    if content.startswith(u'\ufeff'):
        content = content.encode('utf8')[3:].decode('utf8')
    con = json.loads(content)
    datalist = get_data(con[0:20])
    save_data(datalist, savepath)
    # save_fund_info_to_mysql()


# 得到所有的基金信息，存储在json文件或数据库中
def get_all_fund_info(save_type):
    funder = "http://fund.eastmoney.com/js/fundcode_search.js"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
    req = urllib.request.Request(url=funder, headers=header)
    res = urllib.request.urlopen(req)
    # print(type(res.read().decode('utf-8')))
    if save_type == 'json':
        save_fund_info_to_json(res)
    elif save_type == 'mysql':
        save_fund_info_to_mysql(res)


# 存储到json
def save_fund_info_to_json(res):
    str_fund = res.read().decode('utf-8')
    str_fund = str_fund.replace('var r = ', '')
    str_fund = str_fund.replace(';', '')
    f = open('demo.json', 'w')
    f.write(str_fund)
    f.close()


# 存储到mysql
def save_fund_info_to_mysql():
    f = open('demo.json', 'r', encoding="utf-8")
    content = f.read()
    if content.startswith(u'\ufeff'):
        content = content.encode('utf8')[3:].decode('utf8')
    datalist = json.loads(content)
    conn = pymysql.connect(host='127.0.0.1', user='root', password='12345678', database='test')
    cursor = conn.cursor()
    for data in datalist:
        for index in range(0, len(data)):
            # if index == 1 or index == 4:
            #     continue
            data[index] = '"' + data[index] + '"'
        sql = '''insert into fund_info (
                        fund_num, fund_ename, fund_cname, fund_type, fund_c)
                        values (%s)''' % ",".join(data)
        print(sql)
        cursor.execute(sql)
        conn.commit()
    cursor.close()
    conn.close()


# 得到基金的业绩信息，存储在字典里边
def get_data(con):
    datalist = []
    findmoney = re.compile(r'<td><a href=".*">基金规模</a>：(.*?)</td>', re.S)
    find_manager = re.compile(r'<td>基金经理：<a href="http://fundf10.eastmoney.com/jjjl_(\d*).html">(.*)</a>(等?)</td></tr>')
    for item in con:
        url = 'http://fund.eastmoney.com/' + item[0] + '.html'
        html = ask_url(url)
        soup = BeautifulSoup(html, 'html.parser')
        # 得到业绩元素
        eldiv = soup.find_all('dd', class_=False)
        info_fund = soup.find("div", class_="infoOfFund-line")
        if info_fund is not None:
            obj = {
                'cname': item[2],
                'ename': item[0],
                'fundtype': item[3],
                'onemonth': '',
                'threemonth': '',
                'sixmonth': '',
                'oneyear': '',
                'threeyear': '',
                'fundnum': '',
                'fundmanager': ''
            }
            div_fund = soup.find("div", class_="infoOfFund-line").next_element
            # print(div_fund)
            # moneydiv = soup.find_all(href=re.compile("http://fundf10.eastmoney.com/gmbd_"))
            money_num = re.findall(findmoney, str(div_fund))[0]
            obj['fundnum'] = money_num
            manager_name = re.findall(find_manager, str(div_fund))
            if len(manager_name) != 0:
                obj['fundmanager'] = manager_name[0][1]
            if len(eldiv) != 0:  # 某些有前端，后端代码的基金拿不到业绩信息，if判断过滤
                for el in eldiv:
                    score = el.text.split('：')
                    for des in score:
                        if des == '近1月':
                            obj['onemonth'] = score[1]
                        elif des == '近3月':
                            obj['threemonth'] = score[1]
                        elif des == '近6月':
                            obj['sixmonth'] = score[1]
                        elif des == '近1年':
                            obj['oneyear'] = score[1]
                        elif des == '近3年':
                            obj['threeyear'] = score[1]
                datalist.append(obj)
    print(datalist)
    return datalist


def ask_url(url):
    headers = {
        "User-Agent": "Mozilla / 5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    }
    request = urllib.request.Request(url, headers=headers)
    html = ""
    try:
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(request, context=context)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 保存到本地excel文件中
def save_data(datalist, savepath):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('基金全部代码', cell_overwrite_ok=True)
    dict_table = [
        {
            'name': '基金名称',
            'key': 'cname'
        },
        {
            'name': '基金类型',
            'key': 'fundtype'
        },
        {
            'name': '基金代码',
            'key': 'ename'
        },
        {
            'name': '基金经理',
            'key': 'fundmanager'
        },
        {
            'name': '基金规模',
            'key': 'fundnum'
        },
        {
            'name': '近一月',
            'key': 'onemonth'
        },
        {
            'name': '近三月',
            'key': 'threemonth'
        },
        {
            'name': '近半年',
            'key': 'sixmonth'
        },
        {
            'name': '近一年',
            'key': 'oneyear'
        },
        {
            'name': '近三年',
            'key': 'threeyear'
        }
    ]
    col = ("基金名称", '基金类型', '基金代码', '基金经理', '基金规模', '近一月', '近三月', '近半年', '近一年', '近三年')
    for i in range(0, 10):
        worksheet.write(0, i, col[i])
    for i in range(0, len(datalist)):
        # print('第%d条' % i)
        data = datalist[i]
        # print(data)
        for j in range(0, 10):
            key = dict_table[int(j)]['key']
            print(key)
            worksheet.write(i + 1, j, data[key])
    workbook.save(savepath)


if __name__ == '__main__':
    main()



('fund_link', 'fund_name', 'fund_code', 'fund_type', 'fund_net_worth',
                                'fund_daily_growth_rate','fund_date', 'fund_one_week', 'fund_one_month',
                                'fund_three_month', 'fund_six_month', 'fund_this_year','fund_one_year',
                                'fund_two_year', 'fund_three_year', 'fund_rate_link', 'fund_rate',
                                'fund_min_purchase_money')
