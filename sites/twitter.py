import requests


def checkID(id):
    # pageUrl = "https://twitter.com/{id}".format(id=id)
    # req = requests.get(url=pageUrl).text
    # if "此账号不存在" in req:
    #     result = {'twitter': 'notFound'}
    # else:
    #     result = {'twitter': pageUrl}
    # return result
    # 申请不下来开发者key 再想想办法吧
    return


if __name__ == '__main__':
    res = checkID('ll')
    print(res)