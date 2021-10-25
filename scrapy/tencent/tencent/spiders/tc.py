import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['careers.tencent.com']
    start_urls = ['https://careers.tencent.com/search.html']

    def parse(self, response):
        print(response.text)
        job_list = response.xpath('//div[@class="recruit-list"]').extract()
        for job in job_list:
            item = {}
            item["title"] = job.xpath('.//h4/text()').extract()[0]
            item["tips"] = job.xpath('.//p[1]/text()').extract()[0]
            item["text"] = job.xpath('.//p[2]/text()').extract()[0]
            print(item)
            # yield item


