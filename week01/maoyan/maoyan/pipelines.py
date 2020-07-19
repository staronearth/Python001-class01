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
        # print(filmname)
        # print(filmtype)
        # print(filmtime)
        # output=f'{filmname}\t{filmtype}\t{filmtime}\r\n'
        # print('=====================')
        # print(output)
        # print('+++++++++++++++++++++')
        # with open('maoyan.txt',encoding='utf-8') as f:
        #     f.write(output)
        import pymysql
        connection = pymysql.connect(
            host='192.168.222.129',
            port=3306,
            user='root',
            password='yview.cn',
            db='test',
            charset='utf8mb4'
        )
        try:
            with connection.cursor() as cursor:
                #创建一个record
                sql = "INSERT INTO `maoyan` (`flimname`,`filmtype`,`filmtime`) VALUES (%s,%s,%s)"
                cursor.executemany(sql,(filmname,str(filmtype),filmtime))
            connection.commit()

            with connection.cursor() as cursor:
                sql = "select * from `maoyan`"
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
        except Exception as e:
            print(e)
        finally:
            connection.close()
        return item