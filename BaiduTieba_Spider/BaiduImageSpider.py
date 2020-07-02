# -*- coding:utf-8 -*-

import requests
from lxml import etree
from urllib import parse

class BaiduImageSpider(object):
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url = "http://tieba.baidu.com/f?kw={}&ie=utf-8&pn=0"
        self.headers = {
                        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'
                        }
    
    def write_image(self, t_link):
        xpath = "//div[@class='d_post_content j_d_post_content clearfix']/img[@class='BDE_Image']/@src | //div[@class='video_src_wrapper']/embed/@data-video"
        img_list = self.get_parse_page(t_link, xpath)       
        for img_link in img_list:  
            html = requests.get(url=img_link, headers=self.headers).content
            filename = "baidu/"+img_link[-10:]
         
            with open(filename, 'wb') as f:
                f.write(html)
                print("%s下载成功" % filename)

    def get_parse_page(self, url, xpath):
        html = requests.get(url=url, headers=self.headers.content.decode('utf-8'))
        parse_html = etree.HTML(html)
        r_list = parse_html.xpath(xpath)
        return r_list

    def get_tlink(self, url):
        print('-----------------------------')
        xpath = '//div[@class="threadlist_lz clearfix"]/div/a/@href'
        t_list = self.get_parse_page(url, xpath)
        for t in t_list:
            t_link = "http://www.tieba.com" + t
            self.write_image(t_link)
    

    def main(self):
        url = self.url.format(self.tieba_name)


if __name__ == '__main__':
    input_word = input("请输入你要查询的信息：")
    key_word = parse.quote(input_word)
    spider= BaiduImageSpider(key_word)
    spider.main()