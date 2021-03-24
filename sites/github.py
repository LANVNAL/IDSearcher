import requests
import json


# 判断用户id是否存在，通过用户页和GitHub page
def idJudge(id):
    userResult = []
    # 用户页 存在为200 不存在为404
    userPage = "https://github.com/{id}".format(id=id)
    reqStatus = requests.get(url=userPage).status_code
    if reqStatus == 200:
        userInfo = {'userpage': userPage}
        userResult.append(userInfo)
    else:
        userInfo = {'userpage': 'notFound'}
        userResult.append(userInfo)

    # github page
    pageUrl = "http://{id}.github.io/".format(id=id)
    reqStatus = requests.get(url=pageUrl).status_code
    if reqStatus == 200:
        userInfo = {'githubPage': pageUrl}
        userResult.append(userInfo)
    else:
        userInfo = {'githubPage': 'notFound'}
        userResult.append(userInfo)
    return userResult


def search(id):
    userResult = []
    searchApi = "https://api.github.com/search/users?q={id}&per_page=10".format(id=id)
    req = requests.get(url=searchApi)
    responseData = json.loads(req.text)
    resNums = len(responseData['items'])
    for index in range(resNums):
        username = responseData['items'][index]['login']
        userpage = responseData['items'][index]['html_url']
        userInfo = {'username': username, 'userpage': userpage}
        userResult.append(userInfo)
    return userResult





if __name__ == '__main__':
    res = idJudge('leo')
    print(res)
    searchResult = search('leo')
    print(searchResult)