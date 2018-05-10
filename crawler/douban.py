# coding:utf-8 
import requests 
from lxml import html 

url = 'https://movie.douban.com/top250' 
con = requests.get(url).content 
sel = html.fromstring(con)

# 所有的信息都在class属性为info的div标签里，可以先把这个节点取出来
for i in sel.xpath('//div[@class="info"]'):
    # 影片名称
    title = i.xpath('div[@class="hd"]/a/span[@class="title"]/text()')[0]
    info = i.xpath('div[@class="bd"]/p[1]/text()')

    # 导演演员信息
    info_1 = info[0].replace(" ", "").replace("\n", "")
    # 上映日期
    date = info[1].replace(" ", "").replace("\n", "").split("/")[0]
    # 制片国家
    country = info[1].replace(" ", "").replace("\n", "").split("/")[1]
    # 影片类型
    geners = info[1].replace(" ", "").replace("\n", "").split("/")[2]
    # 评分
    rate = i.xpath('//span[@class="rating_num"]/text()')[0]
    # 评论人数
    comCount = i.xpath('//div[@class="star"]/span[4]/text()')[0]
    # 打印结果看看
    print(title, info_1, rate, date, country, geners, comCount)