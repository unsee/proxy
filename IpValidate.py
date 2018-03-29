from Mysql import DbMysql
import requests

class IpValidate():
    def __init__(self):
        self.db = DbMysql()
        sql = "select protocol,ip,port from iprecord"
        iprecords = self.db.getRecords(sql)
        self.iplist = []
        for ip in iprecords:
            dict = {ip[0]:ip[1]+":"+ip[2]}
            self.iplist.append(dict)

    def deleteIp(self, ip):
        sql = 'delete from iprecord where id="'+ip+'"'
        self.db.execute(sql)

    def validate(self):
        for proxy in self.iplist:
            try:
                
                ip = list(proxy.values())[0].split(":")[0]
                requests.get(url="http://www.baidu.com", timeout=5, proxies=proxy)
            except ConnectionRefusedError:
                self.deleteIP(ip)
                print(ip+"------>fail , deleted")
            else:
                print(ip+"------>success ")


if __name__ == '__main__':
    ip = IpValidate()
    ip.validate()