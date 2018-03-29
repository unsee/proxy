import pymysql

class DbMysql():
    def __init__(self):
        self.db = pymysql.connect('localhost', 'root', 'lm111111', 'proxy')
        self.cursor = self.db.cursor()

    def execute(self, sql):
        try:
            #print(sql)
            #s="insert into iprecord(ip,port,type,protocol,address,responsetime) values(%s,%s,%s,%s,%s,%s)"
            #print(s,('121.232.194.116','9000','高匿名','HTTP','中国 江苏省 镇江市 电信','2秒'))
            self.cursor.execute(sql)
            self.db.commit()
            
            return True
        except:
            self.db.rollback()

    def getRecords(self, sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def close(self):
        self.cursor.close()
        self.db.close()


if __name__=="__main__":
    db = DbMysql()
    data = db.getRecords("select * from iprecord")
    print(data)
    db.close()
