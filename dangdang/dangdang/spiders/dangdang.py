# -*- coding: utf-8 -*-

import scrapy
from dangdang.items import DangdangItem
from scrapy.http import Request

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4004279.html']

    def parse(self, response):       

        for i in range(1, 66):
            url = "http://category.dangdang.com/pg" + str(i) + "-cid4004279.html"
            print(url)
            #print('3333333333333333333')
            yield Request(url, callback=self.get_info)
            #print('4444444444444444444444')

    def get_info(self, response):
        item = DangdangItem()
        item['name'] = response.xpath('//a[@class="pic"]/@title').extract()
        item['price'] = response.xpath('//p[@class="price"]/span/text()').extract()
        item["link"] = response.xpath("//a[@class='pic']/@href").extract()
        item["comnum"] = response.xpath("//a[@name='itemlist-review']/text()").extract()
        #print('11111111111111111111')
        yield item
        #print('22222222222222222222')