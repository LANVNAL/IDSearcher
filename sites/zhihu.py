import requests



def search(id):
    idUrl = "https://www.zhihu.com/api/v4/search_v3?t=people&q=LANVNAL&correction=1&offset=0&limit=20&lc_idx=0&show_all_topics=0".format(id=id)
    req = requests.get(idUrl)
    print(req.text)


if __name__ == '__main__':
    search('LANVNAL')