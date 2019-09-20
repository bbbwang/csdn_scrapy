from scrapy import cmdline
import time
#在编译器中执行命令
cmdline.execute('scrapy crawl csdn.com'.split())

# import os
# while 1:
#     os.system("scrapy crawl csdn.com")
#     time.sleep(3600) # 休眠2分钟
