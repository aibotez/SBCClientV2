import sys,sqlite3,os



class DBManager():
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
            self.creatUserUpRecordform()
            self.creatUserTransFinshRecordform()
            # # 关闭资源
            # cur.close()
            # conn.close()
        else:
            conn = sqlite3.connect('./UserDB.db')
            cur = conn.cursor()
            self.cur = cur
            self.conn = conn

    def Connect(self):
        conn = sqlite3.connect('./UserDB.db')
        cur = conn.cursor()
        self.cur = cur
        self.conn = conn
    def close(self):
        # 关闭游标
        self.cur.close()
        # 关闭连接
        self.conn.close()

    def creatClientSettingform(self):
        sql = "create table ClientSetting(DownPath,BackupPath,host)"
        self.cur.execute(sql)
        self.conn.commit()
    def creatUserDownRecordform(self):
        sql = "create table UserDown(FileMd5,FileName,Size,FilePath,RoFilePath,isDown,fetype)"
        self.cur.execute(sql)
        self.conn.commit()
    def creatUserUpRecordform(self):
        sql = "create table UserUp(FileMd5,FileName,FilePath,RoFilePath,isUp)"
        self.cur.execute(sql)
        self.conn.commit()
    def creatUserTransFinshRecordform(self):
        sql = "create table TransFinsh(FileMd5,FileName,FilePath,size,fetype,fecheck)"
        self.cur.execute(sql)
        self.conn.commit()

    def GetClientSetting(self):
        sql = "select * from ClientSetting"
        self.cur.execute(sql)
        self.conn.commit()
        Result = {}
        for i in self.cur:
            info = list(i)
            Result = {'DownPath':info[0],'BackupPath':info[1],'host':info[2]}
        return Result

    def AddUserTranspFinshRecord(self,DownInfo):
        if self.GetUserTranspFinshRecord(DownInfo['FilePath'],DownInfo['FileName']):
            return 'Have'
        # DownInfo = {'FileMd5':'abcd','FileName':'record.txt','FilePath':'/home/p','RoFilePath':'Ro/home'}
        sql = "insert into TransFinsh(FileMd5,FileName,FilePath,size,fetype,fecheck) values (?,?,?,?,?,?)"
        data = (DownInfo['FileMd5'],DownInfo['FileName'],DownInfo['FilePath'],DownInfo['Size'],DownInfo['fetype'],DownInfo['FeCheck'])
        self.cur.execute(sql, data)
        self.conn.commit()
        return 1

    def AddUserDownRecord(self,DownInfo):
        if self.GetUserDownRecord(DownInfo['FilePath'],DownInfo['FileName']):
            print('Have Down')
            return 'Have'
        # DownInfo = {'FileMd5':'abcd','FileName':'record.txt','FilePath':'/home/p','RoFilePath':'Ro/home'}
        sql = "insert into UserDown(FileMd5,FileName,Size,FilePath,RoFilePath,isDown,fetype) values (?,?,?,?,?,?,?)"
        data = (DownInfo['FileMd5'],DownInfo['FileName'],DownInfo['size'],DownInfo['FilePath'],DownInfo['RoFilePath'],'1',DownInfo['fetype'])
        self.cur.execute(sql, data)
        self.conn.commit()
        return 1
    def GetUserDownRecord(self,FilePath,FileName):
        sql = "select * from UserDown where FilePath ='{}' and FileName='{}'".format(FilePath,FileName)
        self.cur.execute(sql)
        self.conn.commit()
        Result = None
        for i in self.cur:
            info = list(i)
            Result = {'FileMd5':info[0],'FileName':info[1],'Size':info[2],'FilePath':info[3],'RoFilePath':info[4],'isDown':int(info[5]),'fetype':info[6]}
        return Result
    def GetUserTranspFinshRecord(self,FilePath,FileName):
        sql = "select * from TransFinsh where FilePath ='{}' and FileName='{}'".format(FilePath,FileName)
        self.cur.execute(sql)
        self.conn.commit()
        Result = None
        for i in self.cur:
            info = list(i)
            Result = {'FileMd5':info[0],'FileName':info[1],'FilePath':info[2],'Size':info[3],'fetype':info[4],'fecheck':info[5]}
        return Result
    def GetUserTranspFinshRecordAll(self):
        sql = "select * from TransFinsh"
        self.cur.execute(sql)
        self.conn.commit()
        Result = []
        for i in self.cur:
            info = list(i)
            Resulti = {'FileMd5':info[0],'FileName':info[1],'FilePath':info[2],'Size':info[3],'fetype':info[4],'fecheck':info[5]}
            Result.append(Resulti)
        return Result
    def GetUserDownRecordAll(self):
        sql = "select * from UserDown"
        self.cur.execute(sql)
        self.conn.commit()
        Result = []
        for i in self.cur:
            info = list(i)
            Resulti = {'FileMd5':info[0],'FileName':info[1],'Size':info[2],'FilePath':info[3],'RoFilePath':info[4],'isDown':int(info[5]),'fetype':info[6]}
            Result.append(Resulti)

        return Result
    def UpdataUserDownRecord(self,FilePath,FileName,changeVaule):
        # self.close()
        # self.Connect()
        sql = "update UserDown set isDown=? where FilePath ='{}' and FileName='{}'".format(FilePath,FileName)
        data = (str(changeVaule))
        self.cur.execute(sql,data)
        self.conn.commit()

    def DelUserDownRecord(self,FilePath,FileName):
        sql = "delete from UserDown where FilePath ='{}' and FileName='{}'".format(FilePath, FileName)
        self.cur.execute(sql)
        self.conn.commit()
    def DelUserTranspFinshRecord(self,FilePath,FileName):
        sql = "delete from TransFinsh where FilePath ='{}' and FileName='{}'".format(FilePath, FileName)
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








# demo = DBManager()
# # demo.AddUserDownRecord(1)
# # demo.GetUserDownRecordAll()
# # demo.UpdataUserDownRecord()
# demo.DelUserDownRecord()
