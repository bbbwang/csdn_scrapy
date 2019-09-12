# -*- coding: utf-8 -*-
import scrapy,re
from scrapy import Selector
from csdn_scrapy.items import CsdnScrapyItem
from scrapy.spiders import CrawlSpider, Rule

# 创建一个Spider，必须继承 scrapy.Spider 类
class comicspider(scrapy.Spider):
    # 自己定义的内容，在运行工程的时候需要用到的标识；
    # 用于区别Spider。该名字必须是唯一的，不可以为不同的Spider设定相同的名字。
    name = 'csdn.com'
    # 允许爬虫访问的域名，防止爬虫跑飞
    allowed_domains=['csdn.net']
    # start_urls:包含了Spider在启动时进行爬取的url列表。 第一个被获取到的页面将是其中之一。 后续的URL则从初始的URL获取到的数据中提取。
    start_urls=['https://www.csdn.net']

    def start_requests(self):
        print("start request .....")
        yield scrapy.Request(url=self.start_urls[0],callback=self.parse0)

    # 请求分析的回调函数，如果不定义start_requests(self)，获得的请求直接从这个函数分析
    # parse()是spider的一个方法。 被调用时，每个初始URL完成下载后生成的Response对象将会作为唯一的参数传递给该函数。
    # 该方法负责解析返回的数据(responsedata)，提取数据(生成item) 以及生成需要进一步处理的URL的Request对象。

    def parse0(self, response):
        print("at csdn master page, get module pages .....")
        page = Selector(response)
        # 标签 设置标签和offset
        navs=page.xpath('//div/ul//li/a/@href').extract()
        navs.remove(navs[0])
        # print(navs)
        for nav in navs:
            crawl_url=self.start_urls[0]+nav
            if nav.find("https:") == 0:
                crawl_url = nav
            module = self.dealUrl(nav)
            yield scrapy.Request(url=crawl_url,meta={'module':module}, callback=self.parse1)


    # 解析response 获得文章url
    def parse1(self,response):
        print("at csdn module page, get article pages .....")
        module = response.meta['module']
        items = []
        hxs = Selector(response)
        # 文章名
        titles=hxs.xpath('//h2/a/text()').extract()
        # 文章链接
        urls=hxs.xpath('//h2/a/@href').extract()
        # 保存文章名和链接
        for i in range(len(titles)):
            item=CsdnScrapyItem()
            titles[i]=self.cleanInput(titles[i])
            item['title']=titles[i]
            item['url']=urls[i]
            item['module']=module
            items.append(item)
        for item in items:
            # request的地址和allow_domain里面的冲突，从而被过滤掉。可以停用过滤功能。
            yield scrapy.Request(url=item['url'],meta={'item':item},callback=self.parse2,dont_filter=True)

    # 进入链接保存文章内容
    def parse2(self, response):
        print("parse web page, get data .....")
        item = response.meta['item']
        url = response.url
        item['url'] = url
        item['uid'] = url[len("https://blog.csdn.net/"):].split('/')[0]
        hxs = Selector(response)
        title = hxs.xpath("//*[@id='mainBox']/main/div[1]/div/div/div[1]/h1//text()").extract()
        user = hxs.xpath("//*[@id='uid']//text()").extract()
        item['uir'] = user[0]
        records = hxs.xpath("//*[@id='asideProfile']/div[2]/dl/dt//text()").extract()
        records_num = hxs.xpath("//*[@id='asideProfile']/div[2]/dl/dd//text()").extract()
        for i in range(len(records)):
            item[records[i]] = records_num[i]
        sorts = hxs.xpath("//*[@id='asideProfile']/div[3]/dl/dt//text()").extract()
        sorts_num = hxs.xpath("//*[@id='asideProfile']/div[3]/dl/dd//@title").extract()
        sorts_num.append(hxs.xpath("//*[@id='asideProfile']/div[3]/dl[4]//@title").extract()[0])
        str = sorts_num[0]
        item['grade']=str[0:str.find(',')]
        item['visitor'] = sorts_num[1]
        item['integral'] = sorts_num[2]
        item['sort'] = sorts_num[3]
        # print(data)
        yield item

    def cleanInput(self,input):
        input = re.sub('\n+', '', input)
        input = re.sub(' +', '', input)
        input = re.sub('\t+', '', input)
        input = re.sub('\xa0', '', input)
        return input

    def dealUrl(self,url):
        if (url.find("https:") == 0):
            url = (url[url.find('https://') + len('https://'):url.find('.csdn')])
        else:
            url = (url[url.find('/nav/') + len('/nav/'):])
        return url



