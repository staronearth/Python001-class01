# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from maoyan.items import MaoyanItem


class MaoyanmovieSpider(scrapy.Spider):
    name = 'maoyanmovie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=10']

    # def parse(self, response):
    #     pass
    
    def start_request(self):
        for page in range(2):
            url=f'https://maoyan.com/films?showType=10?offset={page*30}'
            yield scrapy.Requeset(url,callback=self.parse,dont_filter=False)
    
    def parse(self,response):
        # print(response.text)
        maoyanfilms = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')
        for maoyanfilm in maoyanfilms:
            # print(maoyanfilm.xpath('./a/@href'))
            maoyanfilmlink = 'https://maoyan.com'+ maoyanfilm.xpath('./a/@href').extract_first().strip()
            # print(maoyanfilmlink)
            yield scrapy.Request(maoyanfilmlink,callback=self.parse2)
    
    def parse2(self,response):
        item = MaoyanItem()
        film_info = Selector(response=response).xpath('//div[@class="movie-brief-container"]')

        filmname = film_info.xpath('./h1/text()').extract_first()
        filmtype = film_info.xpath('./ul/li[1]/a[@class="text-link"]/text()').extract()
        filmtime = film_info.xpath('./ul/li[3]/text()').extract_first()

        print(filmname)
        print(filmtype)
        print(filmtime)
        item['filmname']=filmname
        item['filmtype']=filmtype
        item['filmtime']=filmtime
        yield item
