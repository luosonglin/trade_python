# coding:utf-8
import requests
from lxml import html

# 获取主页列表
def getPage():
    baseUrl = 'http://seku.tv/'
    selector = html.fromstring(requests.get(baseUrl).content)

    urls = []
    for i in selector.xpath('//div[@id="list_videos_most_recent_videos_items"]/div/a/@href'):
        urls.append(i)
    return urls

def getPageDetail(url):
    r = html.fromstring(requests.get(url).content)

    #地址
    u = r.xpath('//video[@class="fp-engine"]/@src')[0]
    # return u
    print(u)


if __name__ == '__main__':
    # urls = getPage()
    # for url in urls:
        getPageDetail('http://seku.tv/videos/6344/61p-720p/')