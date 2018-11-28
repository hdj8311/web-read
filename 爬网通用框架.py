# 爬网通用框架.py

import requests

def getHtmlText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}# 模拟特定的浏览器访问或者爬去url
        r = requests.get(url,headers=kv,timeout=30)
        r.raise_for_status()#如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        print(r.request.headers)
        return r.text
    except Exception as e:
        print(e)


if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHtmlText(url)[:1000])
