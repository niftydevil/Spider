import requests
import re

from bs4 import BeautifulSoup
from lxml import etree


class Forecast(object):
    def forecast(self):
        url = "https://weather.com/zh-CN/weather/today/l/7f14186934f484d567841e8646abc61b81cce4d88470d519beeb5e115c9b425a"
        response = requests.get(url)
        # print(response.text)

        # bs = BeautifulSoup(response.text, 'html.parser')
        # title = bs.find('h1', attrs={'classs': 'CurrentConditions--location--kyTeL'}).string
        # print(title)
        tree = etree.HTML(response.text)
        # 天气概况
        location = tree.xpath('//*[@id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034"]/div/section/div/div[1]/h1/text()')
        deadline = tree.xpath('//*[@id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034"]/div/section/div/div[1]/div/text()')
        temperature = tree.xpath('//*[@id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034"]/div/section/div/div[2]/div[1]/span/text()')
        weather = tree.xpath('//*[@id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034"]/div/section/div/div[2]/div[1]/div/text()')
        location_str = str(location).strip("[' ']")# .replace(' ', '')
        deadline_str = str(deadline).strip("[' ']")# .replace(' ', '')
        temperature_str = str(temperature).strip("['']")
        weather_str = str(weather).strip("['']")
        # print(location_str)
        summary = location_str + '\n' + deadline_str + '\n' + temperature_str + '  ' + weather_str
        print(summary)
        print('******************************')

        # 天气详细描述
        d_title = str(tree.xpath('//*[@id="todayDetails"]/section/header/h2/text()')).strip("[' ']")
        d_temperature = str(tree.xpath('//*[@id="todayDetails"]/section/div[1]/div[1]/span[1]/text()')).strip("[' ']")
        d_description = str(tree.xpath('//*[@id="todayDetails"]/section/div[1]/div[1]/span[2]/text()')).strip("[' ']")
        d_sunrise = str(tree.xpath('//*[@id="SunriseSunsetContainer-fd88de85-7aa1-455f-832a-eacb037c140a"]/div/div/div/div[1]/p/text()')).strip("[' ']")
        d_sunset = str(tree.xpath('//*[@id="SunriseSunsetContainer-fd88de85-7aa1-455f-832a-eacb037c140a"]/div/div/div/div[2]/p/text()')).strip("[' ']")
        d1 = d_title + '\n' + d_description + ':' + d_temperature + '\n🌅️：' + d_sunrise + '  🌇：' + d_sunset
        print(d1)
        d_highAndLow = str(tree.xpath('//*[@id="todayDetails"]/section/div[2]/div[1]/div[1]/text()')).strip("[' ']")
        d_highTemperature = str(tree.xpath('//*[@id="todayDetails"]/section/div[2]/div[1]/div[2]/span[1]/text()')).strip("[' ']")
        d_lowTemperature = str(tree.xpath('//*[@id="todayDetails"]/section/div[2]/div[1]/div[2]/span[2]/text()')).strip("[' ']")
        d2 = d_highAndLow + ': ' + d_highTemperature + ' / ' + d_lowTemperature
        print(d2)

        d_wind = str(tree.xpath('//*[@id="todayDetails"]/section/div[2]/div[2]/div[1]/text()')).strip("[' ']")
        d_windSpeed = str(tree.xpath('//*[@id="todayDetails"]/section/div[2]/div[2]/div[2]/span/text()')).strip("[' ']")
        d3 = d_wind + ': ' + d_windSpeed
        print(d3)

        d_humidity = str(tree.xpath('//*[@id="todayDetails"]/section/div[2]/div[3]/div[1]/text()')).strip("[' ']")
        d_humidityValue = str(tree.xpath('//*[@id="todayDetails"]/section/div[2]/div[3]/div[2]/span/text()')).strip("[' ']")
        d4 = d_humidity + '：' + d_humidityValue
        print(d4)

        d_dewPoint = str(tree.xpath('//*[@id="todayDetails"]/section/div[2]/div[4]/div[1]/text()')).strip("[' ']")
        d_dewPointValue = str(tree.xpath('//*[@id="todayDetails"]/section/div[2]/div[4]/div[2]/span/text()')).strip("[' ']")
        d5 = d_dewPoint + '：' + d_dewPointValue
        print(d5)

        d_airPressure = str(tree.xpath('//*[@id="todayDetails"]/section/div[2]/div[5]/div[1]/text()')).strip("[' ']")
        d_airPressureValue = str(tree.xpath('//*[@id="todayDetails"]/section/div[2]/div[5]/div[2]/span/text()')).strip("[' ']")
        d6 = d_airPressure + '：' + d_airPressureValue
        print(d6)

        d_Ultraviolet = str(tree.xpath('//*[@id="todayDetails"]/section/div[2]/div[6]/div[1]/text()')).strip("[' ']")
        d_UltravioletValue = str(tree.xpath('//*[@id="todayDetails"]/section/div[2]/div[6]/div[2]/span/text()')).strip("[' ']")
        d7 = d_Ultraviolet + '：' + d_UltravioletValue
        print(d7)

        d_visibility = str(tree.xpath('//*[@id="todayDetails"]/section/div[2]/div[7]/div[1]/text()')).strip("[' ']")
        d_visibilityValue = str(tree.xpath('//*[@id="todayDetails"]/section/div[2]/div[7]/div[2]/span/text()')).strip("[' ']")
        d8 = d_visibility + '：' + d_visibilityValue
        print(d8)

        d_moon = str(tree.xpath('//*[@id="todayDetails"]/section/div[2]/div[8]/div[1]/text()')).strip("[' ']")
        d_moonValue = str(tree.xpath('//*[@id="todayDetails"]/section/div[2]/div[8]/div[2]/text()')).strip("[' ']")
        d9 = d_moon + '：' + d_moonValue
        print(d9)

        # 最近5天的概况
        li_list = tree.xpath('//*[@id="WxuDailyWeatherCard-main-bb1a17e7-dc20-421a-b1b8-c117308c6626"]/section/div/ul/li')
        # print(li_list)
        for li in li_list:
            date = str(li.xpath('./a/h3/span/text()')).strip("[' ']")
            # print(date)
            highTemp = str(li.xpath('./a/div[1]/span/text()')).strip("[' ']")
            # print(highTemp)
            lowTemp = str(li.xpath('./a/div[2]/span/text()')).strip("[' ']")
            # print(lowTemp)
            weather = str(li.xpath('./a/div[3]/svg/title/text()')).strip("[' ']")
            # print(weather)
            rainPercent = str(li.xpath('./a/div[4]/span/span/text()')).strip("[' ']")
            # print(rainPercent)
            rainPercentValue = str(li.xpath('./a/div[4]/span/text()')).strip("[' ']")
            # print(rainPercentValue)
            d10 = date + '  最高温：' + highTemp + '  最低温：' + lowTemp + '  天气：' + weather + '  ' + rainPercent + '：' + rainPercentValue
            print(d10)



