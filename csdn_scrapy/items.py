# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CsdnScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 文章模块
    module = scrapy.Field()
    # 文章名
    title = scrapy.Field()
    # 文章链接
    url = scrapy.Field()
    # 文章内容
    text = scrapy.Field()
    # 用户名称
    uir = scrapy.Field()
    # 用户id
    uid = scrapy.Field()
    原创 = scrapy.Field()
    粉丝 = scrapy.Field()
    喜欢 = scrapy.Field()
    评论 = scrapy.Field()
    # 等级
    grade = scrapy.Field()
    # 访问
    visitor = scrapy.Field()
    # 积分
    integral = scrapy.Field()
    # 排名
    sort = scrapy.Field()