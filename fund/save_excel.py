import datetime
import os

from openpyxl import Workbook
from fund.fund_information import fund_information

fund_information = fund_information()


def save_excel():
    # 把数据保存到Excel文件
    wb = Workbook()
    # ws = wb.active
    fund_sheet = wb.create_sheet('fund_sheet', 0)
    fund_sheet['A1'] = '基金链接'
    fund_sheet['B1'] = '基金名称'
    fund_sheet['C1'] = '基金代码'
    fund_sheet['D1'] = '基金类型'
    fund_sheet['E1'] = '净值'
    fund_sheet['F1'] = '日增长率'
    fund_sheet['G1'] = '日期'
    fund_sheet['H1'] = '近1周'
    fund_sheet['I1'] = '近1月'
    fund_sheet['J1'] = '近3月'
    fund_sheet['K1'] = '近6月'
    fund_sheet['L1'] = '今年来'
    fund_sheet['M1'] = '近1年'
    fund_sheet['N1'] = '近2年'
    fund_sheet['O1'] = '近3年'
    fund_sheet['P1'] = '手续费链接'
    fund_sheet['Q1'] = '手续费'
    fund_sheet['R1'] = '购买起点'

    def save():
        # 循环写入Excel，把这个页面的20条数据都写入Excel
        row = [fund_information.fund_link, fund_information.fund_name, fund_information.fund_code,
               fund_information.fund_type, fund_information.fund_net_worth, fund_information.fund_daily_growth_rate,
               fund_information.fund_date, fund_information.fund_one_week, fund_information.fund_one_month,
               fund_information.fund_three_month, fund_information.fund_six_month, fund_information.fund_this_year,
               fund_information.fund_one_year, fund_information.fund_two_year, fund_information.fund_three_year,
               fund_information.fund_rate_link, fund_information.fund_rate, fund_information.fund_min_purchase_money]
        # append()方法可以直接在Excel中添加一行，不覆盖原有的数据
        fund_sheet.append(row)

        # 保存excel
        dt = datetime.now()
        dt_format = dt.strftime('%Y%m%d%H%M')
        path = os.getcwd()
        # print(path)
        wb.save(path + '/' + dt_format + '.xlsx')
