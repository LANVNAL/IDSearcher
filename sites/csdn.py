import requests
import json

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}


# 判断用户id是否存在，通过用户页
def idJudge(id):
    userResult = []
    # 用户页 存在为200 不存在为404
    userPage = "https://blog.csdn.net/{id}".format(id=id)
    reqStatus = requests.get(url=userPage, headers=headers).status_code
    if reqStatus == 200:
        userInfo = {'userpage': userPage}
        userResult.append(userInfo)
    else:
        userInfo = {'userpage': 'notFound'}
        userResult.append(userInfo)
    return userResult


if __name__ == '__main__':
    res = idJudge('leo')
    print(res)
