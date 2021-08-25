import scrapy
import logging

# logger = logging.getLogger(__name__)

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']    # 允许爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        for i in range(10):
            item = {}
            item["i"] = i
            logging.getLogger(__name__).warning(item)
        # 处理start_urls地址对应的相应内容
        # names = response.xpath('//div[@class="maincon"]//li/div[2]/h2/text()').extract()
        # names1 = response.xpath('//div[@class="maincon"]//li/div[2]/h2').extract()
        # print(names)
        # print(names1)

        # 先分组，再取值
        # li_list = response.xpath('//div[@class="maincon"]//li')
        # for li in li_list:
        #     item = {}
        #     # item["image"] = li.xpath('./div[1]/img/@src')
        #     item["name"] = li.xpath('./div[2]/h2/text()').extract()
        #     item["label"] = li.xpath('./div[2]/h3/span/text()').extract()
        #     item["achievement"] = li.xpath('./div[2]/p/span/text()').extract()
        #     item["hiredate"] = li.xpath('./div[3]/h3/text()').extract()
        #     item["introduce"] = li.xpath('./div[3]/p/text()').extract()
        #     # print(item)
        #     yield item
        #     print("**************************************************************")
