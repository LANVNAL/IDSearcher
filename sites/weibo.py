import requests
import json
from urllib.parse import urlencode


def search(id, page=1):
    userResult = []
    idUrl = "https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D3%26q%3D{id}%26t%3D0&page_type=searchuser&page={page}".format(id=id, page=page)
    req = requests.get(idUrl)
    responseData = req.text
    responseJson = json.loads(responseData)
    if responseJson['ok'] == 0:
        return [{'searchResult': 'notFound'}]
    # 获取一页中有多少用户信息，下面json用到这个来取用户信息的list
    userNumInPage = len(responseJson['data']['cards'][1]['card_group'])
    for index in range(userNumInPage):
        userid = responseJson['data']['cards'][1]['card_group'][index]['user']['id']
        username = responseJson['data']['cards'][1]['card_group'][index]['user']['screen_name']
        description = responseJson['data']['cards'][1]['card_group'][index]['user']['description']
        userpage = 'https://weibo.com/u/{id}'.format(id=userid)
        # print("id: {id}; \nusername: {name}; \ndescription: {description}\n".format(id=userid, name=username, description=description))
        userInfo = {'id': userid, 'username': username, 'description': description, 'userpage': userpage}
        userResult.append(userInfo)
    return userResult


if __name__ == '__main__':
    res = search('lanvnal',1)
    print(res)