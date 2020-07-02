# -*- coding:utf-8 -*-

import scrapy
import sys
sys.path.append('.')
from csdn.items import CsdnItem


class CsdnSpider(scrapy.Spider):
    name = "csdn"
    allowed_domains = ["csdn.net"]
    start_urls = [
        "https://blog.csdn.net/zxcvbbnn/article/details/106985485",
        "https://blog.csdn.net/CUFEECR/article/details/105566733"
    ]

    def parse(self, response):
        for sel in response.xpath('//*[@id="asideProfile"]'):
            # author = sel.xpath('div[1]/div[2]/div[1]/a/text()').extract()
            # fans = sel.xpath('div[2]/dl[2]/dt/span/text()').extract()
            # like = sel.xpath('div[2]/dl[3]/dt/span/text()').extract()
            # comment = sel.xpath('div[2]/dl[4]/dt/span/text()').extract()
            # print(author, fans, like, comment)
            item = CsdnItem()
            item['author'] = sel.xpath('div[1]/div[2]/div[1]/a/span/text()').extract()#.strip()
            item['fans'] = sel.xpath('div[2]/dl[2]/dt/span/text()').extract()
            item['like'] = sel.xpath('div[2]/dl[3]/dt/span/text()').extract()
            item['comment'] = sel.xpath('div[2]/dl[4]/dt/span/text()').extract()
            yield item