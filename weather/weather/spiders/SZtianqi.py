# -*- coding: utf-8 -*-
import scrapy


class SztianqiSpider(scrapy.Spider):
    name = 'SZtianqi'
    allowed_domains = ['www.tianqi.com/suzhou/']
    start_urls = ['http://www.tianqi.com/suzhou//']

    def parse(self, response):
        pass
