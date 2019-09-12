# -*- coding: utf-8 -*-
import pymongo
from  csdn_scrapy.settings import mongo_host,mongo_port,mongo_db_name,mongo_db_collection
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class CsdnScrapyPipeline(object):
    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        sheetname = mongo_db_collection
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]  # 得到它到数据库
        self.post = mydb[sheetname]  # 得到它的表

    def process_item(self, item, spider):
        # 去除已经收录过到作者
        count = self.post.find({'uid':item['uid']}).count()
        if(count == 0):
            data = dict(item)   #将sipider中yield过来的item转换成字典形式
            self.post.insert(data)  #保存到mongodb中
        return item
