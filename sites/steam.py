import requests
import re


headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}


def checkID(id):
    pageUrl = "https://steamcommunity.com/id/{id}".format(id=id)
    req = requests.get(url=pageUrl, headers=headers).text
    if u"无法找到" in req:
        result = {'steam': 'notFound'}
    else:
        result = {'steam': pageUrl}
    return [result]


if __name__ == '__main__':
    res = checkID('lannvalaaa')
    print(res)