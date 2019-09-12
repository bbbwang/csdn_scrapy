# csdn_scrapy
* 爬取csdn前1万排名作者信息
* csdn是开发者必备的查询工具之一，里面有很多优秀的文章，在这里也可以分享我们的学习记录。它的排名机制也鼓励开发着创造更多的文章，有时候在想，排名普通作者都这么厉害，那前1万的岂不是更厉害，所以想到，有没有什么方法，获取csdn前1万所有大佬的信息。
### 项目介绍
* 因为系统没有专门的排行榜，所以没法直接获取前1万名作者信息。但是他的排名算法是基于积分计算的，只有不断更新，才能保持排名靠前，具体规则参考[博客积分规则](https://blog.csdn.net/home/help.html)
更新频繁的博客会优先展示在csdn首页上，而且你每次访问的时候都是更新不同的内容。所以，我就从csdn首页为入口，一直刷新，记录每次出现不同的博客。记录次数多后，筛选出排名靠前的博客作者，这样，就能得到前1万名csdn作者。
#### 爬虫工具：scrapy
* 学习教程：[https://scrapy-chs.readthedocs.io/zh_CN/0.24/](https://scrapy-chs.readthedocs.io/zh_CN/0.24/)
#### 语言：python
* 推荐廖雪峰的python学习：[https://www.liaoxuefeng.com/wiki/1016959663602400](https://www.liaoxuefeng.com/wiki/1016959663602400)
#### 数据库：mongodb
* 推荐廖雪峰的python学习：[https://www.liaoxuefeng.com/wiki/1016959663602400](https://www.liaoxuefeng.com/wiki/1016959663602400)
#### git项目地址
* [https://github.com/bbbwang/csdn_scrapy](https://github.com/bbbwang/csdn_scrapy)
