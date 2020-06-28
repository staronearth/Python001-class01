# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanPipeline:
    # def process_item(self, item, spider):
    #     return item
    def process_item(self, item, spider):
        filmname = item['filmname']
        filmtype = item['filmtype']
        filmtime = item['filmtime']
        output=f'{filmname}\t{filmtype}\t{filmtime}\r\n'
        with open('./maoyan.csv','a+',encoding='utf-8') as f:
            f.write(output)
        return item