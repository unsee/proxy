#coding:utf-8
from lxml import etree
from HtmlDownload import HtmlDownloader
from time import time
from Mysql import DbMysql

class HtmlParseIP(object):
    def __init__(self):
        self.db = DbMysql()

    def parse(self, url):
        response = HtmlDownloader.download(url)

        tree = etree.HTML(response)
        nodes = tree.xpath("//td/text()")

        txt = ""
        for count in range(len(nodes)):
            if(count % 7 == 0):
                txt = txt + "('" + nodes[count] +"'"
                txt = txt + ",'" + nodes[count+1] +"'"
                txt = txt + ",'" + nodes[count+3] +"'),"
        txt =txt[:-1] 
        sql = "insert into iprecord(ip,port,protocol) values" + txt
        print(sql)
        self.db.execute(sql)


if __name__ == '__main__':
    a = HtmlParseIP()
    a.parse("https://www.kuaidaili.com/free/inha/1")