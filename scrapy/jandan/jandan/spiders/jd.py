# -*- coding: utf-8 -*-
import scrapy
from jandan.items import JandanItem


class JdSpider(scrapy.Spider):
    name = "jd"
    #allowed_domains = ["jandan.net/ooxx"]
    allowed_domains = ["http://jandan.net/ooxx"]
    start_urls = (
        'http://www.jandan.net/ooxx/',
        #'http://www.topit.me/',
    )

    def parse(self, response):
        item = JandanItem()
        #item['image_urls'] = response.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/ol/li[1]/div[1]/div/div[2]/p/a[1]').extract()
        #yield  item
        image_urls = response.xpath('//img//@src').extract()#提取图片链接
        image_urls2 = image_urls[2:]
        print 'image_urls', image_urls2
        item['image_urls'] = image_urls2
        # print 'image_urls',item['image_urls']
        #yield item

        # new_url= response.xpath('//a[@class="previous-comment-page"]//@href').extract_first()#翻页
        # # print 'new_url',new_url
        # if new_url:
        #     yield scrapy.Request(new_url,callback=self.parse)