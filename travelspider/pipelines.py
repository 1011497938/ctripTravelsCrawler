# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import pymongo
import json
import traceback
# import file


class TravelspiderPipeline(object):
    def __init__(self):
        # conn = pymongo.MongoClient()
        # self.col = conn['travel']['doc2']
        self.count = 0
        return

    '''处理采集资讯, 存储至Mongodb数据库'''
    def process_item(self, item, spider):
        # try:
        item = dict(item)
        item_id = hash(tuple(item.values()))


        # item['title'] =  item['title'].decode('unicode_escape')
        # # .encode('utf-8').decode('unicode_escape')
        # item['content'] =  str(item['content'])
        # .encode('utf-8').decode('unicode_escape')

        item_path = 'travelspider/data/{}.json'.format(item_id)
        f = open(item_path, 'w', encoding='utf')
        
        # , encoding='utf'
        f.write(json.dumps(item, ensure_ascii=False))
        f.close()
        # spider.crawler.engine.close_spider(spider, '没有新数据关闭爬虫')
            # print('\n\n\n\nout',item)
            # exit()
            # self.col.insert(dict(item))
        # except (pymongo.errors.WriteError, KeyError) as err:
        # except Exception as e:
            # traceback.print_exc()
        #     raise DropItem("Duplicated Item: {}".format(item['name']))
        return item
