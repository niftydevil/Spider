import scrapy

from wzsun.items import WzsunItem


class WzSpider(scrapy.Spider):
    name = 'wz'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']

    def parse(self, response):
        item = WzsunItem()
