import sys,sqlite3,os



class Demo():
    def __init__(self):
        self.cur = None
        self.conn = None
        self.db_connect()
    def db_connect(self):
        if not os.path.exists('./UserDB.db'):
            conn = sqlite3.connect('./UserDB.db')
            cur = conn.cursor()
            self.cur = cur
            self.conn = conn
            self.creatClientSettingform()
            self.creatUserDownRecordform()
            # # 关闭资源
            # cur.close()
            # conn.close()
        else:
            conn = sqlite3.connect('./UserDB.db')
            cur = conn.cursor()
            self.cur = cur
            self.conn = conn
    def creatClientSettingform(self):
        sql = "create table ClientSetting(DownPath,BackupPath)"
        self.cur.execute(sql)
        self.conn.commit()
    def creatUserDownRecordform(self):
        sql = "create table UserDown(FileMd5,FileName,FilePath,RoFilePath,isDown)"
        self.cur.execute(sql)
        self.conn.commit()
    def creatUserUpRecordform(self):
        sql = "create table UserDown(FileMd5,FileName,FilePath,RoFilePath,isUp)"
        self.cur.execute(sql)
        self.conn.commit()


    def AddUserDownRecord(self,DownInfo):
        DownInfo = {'FileMd5':'abcd','FileName':'record.txt','FilePath':'/home/p','RoFilePath':'Ro/home'}
        sql = "insert into UserDown(FileMd5,FileName,FilePath,RoFilePath,isDown) values (?,?,?,?,?)"
        data = (DownInfo['FileMd5'],DownInfo['FileName'],DownInfo['FilePath'],DownInfo['RoFilePath'],'1')
        self.cur.execute(sql, data)
        self.conn.commit()

    def GetUserDownRecord(self):
        FilePath = '/home/p'
        FileName = 'record.txt'
        sql = "select * from UserDown where FilePath ='{}' and FileName='{}'".format(FilePath,FileName)
        self.cur.execute(sql)
        self.conn.commit()
        Result = None
        for i in self.cur:
            info = list(i)
            Result = {'FileMd5':info[0],'FileName':info[1],'FilePath':info[2],'RoFilePath':info[3],'isDown':int(info[4])}
        return Result
    def GetUserDownRecordAll(self):
        FilePath = '/home/p'
        FileName = 'record.txt'
        sql = "select * from UserDown".format(FilePath,FileName)
        self.cur.execute(sql)
        self.conn.commit()
        Result = []
        for i in self.cur:
            info = list(i)
            Resulti = {'FileMd5':info[0],'FileName':info[1],'FilePath':info[2],'RoFilePath':info[3],'isDown':int(info[4])}
            Result.append(Resulti)
        return Result
    def UpdataUserDownRecord(self):
        FilePath = '/home/p1'
        FileName = 'record.txt'
        sql = "update UserDown set isDown=? where FilePath ='{}' and FileName='{}'".format(FilePath,FileName)
        data = ('0')
        self.cur.execute(sql,data)
        self.conn.commit()

    def DelUserDownRecord(self):
        FilePath = '/home/p1'
        FileName = 'record.txt'
        sql = "delete from UserDown where FilePath ='{}' and FileName='{}'".format(FilePath, FileName)
        self.cur.execute(sql)
        self.conn.commit()


#     sql = "update users set username=?,password=?,company=? where id=2"



    # def delete_data():
    #     # 获取连接
    #     conn = sqlite3.connect(db_file)
    #     # 打开游标cursor
    #     cur = conn.cursor()
    #     # 删除ql语句
    #     sql = "delete from users where id=3"
    #     cur.execute(sql)
    #     conn.commit()
    #     cur.close()
    #     conn.close()
    #
    # def updata_data():
    #     # 连接数据库
    #     conn = sqlite3.connect(db_file)
    #     # 打开游标cursor
    #     cur = conn.cursor()
    #     # sql语句
    #     sql = "update users set username=?,password=?,company=? where id=2"
    #     data = ('李思', 1234567890, '山东')
    #     cur.execute(sql, data)
    #     # 执行插入时，显示插入的提交数据
    #     conn.commit()
    #     # 关闭资源
    #     cur.close()
    #     conn.close()








demo = Demo()
# demo.AddUserDownRecord(1)
# demo.GetUserDownRecordAll()
# demo.UpdataUserDownRecord()
demo.DelUserDownRecord()
