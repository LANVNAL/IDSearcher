from sites import weibo, github, csdn, steam

def getSearchId():
    id = input(u'输入要查询的id:')
    return id


def goSearch(id):
    weiboRes = weibo.search(id)
    githubRes1 = github.idJudge(id)
    githubRes2 = github.search(id)
    csdnRes = csdn.idJudge(id)
    steamRes = steam.checkID(id)
    searchResult = {'weibo': weiboRes, 'githubUser': githubRes1, 'Github': githubRes2, 'CSDN': csdnRes, 'Steam': steamRes}
    resultFromat(searchResult)



# result format is dict
def resultFromat(result):
    for key in result.keys():
        print("\n============== {title} ==============\n".format(title=key))
        oneResult = result[key]
        length = len(oneResult)
        for index in range(length):
            oneInfo = oneResult[index]
            for iterm in oneInfo.keys():
                print("{key}: {value}".format(key=iterm, value=oneInfo[iterm]))




if __name__ == '__main__':
    id = getSearchId()
    goSearch(id)


