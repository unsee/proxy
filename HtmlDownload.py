#coding:utf-8
import requests
import chardet

class HtmlDownloader(object):
    def __init__(self):
        self.urls = []
    
    @staticmethod
    def download(url):
        proxy = {"HTTP":"115.223.197.91:9000"}

        res = requests.get(url=url, timeout=5, proxies=proxy)
        res.encoding = chardet.detect(res.content)['encoding']
        if(not res.ok) or len(res.content)<500:
            return "error"
        else:
            return res.text

if __name__ == '__main__':
    #htmldownload = HtmlDownloader()
    #result = htmldownload.download("http://www.66ip.cn/")
    #print("print result")
    #print(result)
    pass