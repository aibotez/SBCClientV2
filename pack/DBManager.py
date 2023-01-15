import sys,sqlite3,os,threading


class DBManager1():
    def __init__(self):
        self.lock = threading.Lock()
        self.dbmanager = DBManager()
        self.conn = self.dbmanager.conn
    def setUpPar(self,FilePath,FileName,changeVaule):
        self.UpFilePath = FilePath
        self.UpFileName = FileName
        self.UpchangeVaule = changeVaule
    def WSQL(self,DownInfo,Oper):
        dbmanager = DBManager()
        self.lock.acquire(True)
        if Oper == 'AddUserTranspFinshRecord':
            dbmanager.AddUserTranspFinshRecord(DownInfo)
        elif Oper == 'AddUserUpRecords':
            for i in DownInfo:
                dbmanager.AddUserUpRecords(i)
            dbmanager.conn.commit()
        elif Oper == 'AddUserUpRecord':
            dbmanager.AddUserUpRecord(DownInfo)
        elif Oper =='UpdataUserUpRecord':
            dbmanager.UpdataUserUpRecord(self.UpFilePath,self.UpFileName,self.UpchangeVaule)
        elif Oper =='UpdataUserUpRecords':
            for i in DownInfo:
                FilePath = i['LoFilePath']
                FileName = i['FileName']
                dbmanager.UpdataUserUpRecords(FilePath,FileName,self.UpchangeVaule)
            dbmanager.conn.commit()
        elif Oper =='DelUserUpRecord':
            FilePath = DownInfo['LoFilePath']
            FileName = DownInfo['FileName']
            dbmanager.DelUserUpRecord(FilePath,FileName)
        elif Oper =='DelUserUpRecords':
            for i in DownInfo:
                FilePath = i['LoFilePath']
                FileName = i['FileName']
                dbmanager.DelUserUpRecords(FilePath,FileName)
            dbmanager.conn.commit()
        self.lock.release()


        dbmanager.close()


class DBManager():
    def __init__(self):
        self.lock = threading.Lock()
        self.cur = None
        self.conn = None
        self.db_connect()
    def db_connect(self):
        if not os.path.exists('./UserDB.db'):
            conn = sqlite3.connect('./UserDB.db',check_same_thread=False)
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
            conn = sqlite3.connect('./UserDB.db',check_same_thread=False)
            cur = conn.cursor()
            self.cur = cur
            self.conn = conn

    def Connect(self):
        conn = sqlite3.connect('./UserDB.db',check_same_thread=False)
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
        sql = "create table UserUp(FileMd5,FileName,Size,LoFilePath,RoFilePath,isUp,fetype)"
        self.cur.execute(sql)
        self.conn.commit()
    def creatUserTransFinshRecordform(self):
        sql = "create table TransFinsh(FileMd5,FileName,FilePath,size,fetype,fecheck,timestamp)"
        self.cur.execute(sql)
        # self.conn.commit()

    def GetClientSetting(self):
        sql = "select * from ClientSetting"
        self.cur.execute(sql)
        # self.conn.commit()
        Result = {}
        for i in self.cur:
            info = list(i)
            Result = {'DownPath':info[0],'BackupPath':info[1],'host':info[2]}
        return Result

    def AddUserTranspFinshRecord(self,DownInfo):
        if self.GetUserTranspFinshRecord(DownInfo['FilePath'],DownInfo['FileName']):
            return 'Have'
        # DownInfo = {'FileMd5':'abcd','FileName':'record.txt','FilePath':'/home/p','RoFilePath':'Ro/home'}
        sql = "insert into TransFinsh(FileMd5,FileName,FilePath,size,fetype,fecheck,timestamp) values (?,?,?,?,?,?,?)"
        data = (DownInfo['FileMd5'],DownInfo['FileName'],DownInfo['FilePath'],DownInfo['Size'],DownInfo['fetype'],DownInfo['FeCheck'],DownInfo['timestamp'])
        self.lock.acquire(True)
        self.cur.execute(sql, data)
        self.conn.commit()
        self.lock.release()
        return 1

    def AddUserUpRecords(self,UpInfo):
        if self.GetUserUpRecord(UpInfo['RoFilePath'],UpInfo['FileName']):
            print('Have Up')
            return 'Have'
        # DownInfo = {'FileMd5':'abcd','FileName':'record.txt','FilePath':'/home/p','RoFilePath':'Ro/home'}
        sql = "insert into UserUp(FileMd5,FileName,Size,LoFilePath,RoFilePath,isUp,fetype) values (?,?,?,?,?,?,?)"
        data = (UpInfo['FileMd5'],UpInfo['FileName'],UpInfo['size'],UpInfo['LoFilePath'],UpInfo['RoFilePath'],'2',UpInfo['fetype'])
        self.lock.acquire(True)
        self.cur.execute(sql, data)
        # self.conn.commit()
        self.lock.release()
        return 1

    def AddUserUpRecord(self,UpInfo):
        if self.GetUserUpRecord(UpInfo['RoFilePath'],UpInfo['FileName']):
            print('Have Up')
            return 'Have'
        # DownInfo = {'FileMd5':'abcd','FileName':'record.txt','FilePath':'/home/p','RoFilePath':'Ro/home'}
        sql = "insert into UserUp(FileMd5,FileName,Size,LoFilePath,RoFilePath,isUp,fetype) values (?,?,?,?,?,?,?)"
        data = (UpInfo['FileMd5'],UpInfo['FileName'],UpInfo['size'],UpInfo['LoFilePath'],UpInfo['RoFilePath'],'2',UpInfo['fetype'])
        self.lock.acquire(True)
        self.cur.execute(sql, data)
        self.conn.commit()
        self.lock.release()
        return 1
    def AddUserDownRecord(self,DownInfo):
        if self.GetUserDownRecord(DownInfo['FilePath'],DownInfo['FileName']):
            print('Have Down')
            return 'Have'
        # DownInfo = {'FileMd5':'abcd','FileName':'record.txt','FilePath':'/home/p','RoFilePath':'Ro/home'}
        sql = "insert into UserDown(FileMd5,FileName,Size,FilePath,RoFilePath,isDown,fetype) values (?,?,?,?,?,?,?)"
        data = (DownInfo['FileMd5'],DownInfo['FileName'],DownInfo['size'],DownInfo['FilePath'],DownInfo['RoFilePath'],'2',DownInfo['fetype'])
        self.lock.acquire(True)
        self.cur.execute(sql, data)
        self.conn.commit()
        self.lock.release()
        return 1
    def GetUserUpRecord(self,RoFilePath,FileName):
        sql = "select * from UserUp where LoFilePath ='{}' and FileName='{}'".format(RoFilePath,FileName)
        self.cur.execute(sql)
        # self.conn.commit()
        Result = None
        for i in self.cur:
            info = list(i)
            Result = {'FileMd5':info[0],'FileName':info[1],'Size':info[2],'LoFilePath':info[3],'RoFilePath':info[4],'isUp':int(info[5]),'fetype':info[6]}
        return Result
    def GetUserDownRecord(self,FilePath,FileName):
        sql = "select * from UserDown where FilePath ='{}' and FileName='{}'".format(FilePath,FileName)
        self.cur.execute(sql)
        # self.conn.commit()
        Result = None
        for i in self.cur:
            info = list(i)
            Result = {'FileMd5':info[0],'FileName':info[1],'Size':info[2],'FilePath':info[3],'RoFilePath':info[4],'isDown':int(info[5]),'fetype':info[6]}
        return Result
    def GetUserTranspFinshRecord(self,FilePath,FileName):
        sql = "select * from TransFinsh where FilePath ='{}' and FileName='{}'".format(FilePath,FileName)
        self.cur.execute(sql)
        # self.conn.commit()
        Result = None
        for i in self.cur:
            info = list(i)
            Result = {'FileMd5':info[0],'FileName':info[1],'FilePath':info[2],'Size':info[3],'fetype':info[4],'fecheck':info[5],'timestamp':info[6]}
        return Result
    def GetUserTranspFinshRecordAll(self):
        sql = "select * from TransFinsh"
        self.cur.execute(sql)
        # self.conn.commit()
        Result = []
        for i in self.cur:
            info = list(i)
            Resulti = {'FileMd5':info[0],'FileName':info[1],'FilePath':info[2],'Size':info[3],'fetype':info[4],'fecheck':info[5],'timestamp':info[6]}
            Result.append(Resulti)
        return Result
    def GetUserUpRecordAll(self):
        sql = "select * from UserUp"
        self.cur.execute(sql)
        # self.conn.commit()
        Result = []
        for i in self.cur:
            info = list(i)
            Resulti = {'FileMd5':info[0],'FileName':info[1],'Size':info[2],'LoFilePath':info[3],'RoFilePath':info[4],'isUp':int(info[5]),'fetype':info[6]}
            Result.append(Resulti)

        return Result
    def GetUserDownRecordAll(self):
        sql = "select * from UserDown"
        self.cur.execute(sql)
        # self.conn.commit()
        Result = []
        for i in self.cur:
            info = list(i)
            Resulti = {'FileMd5':info[0],'FileName':info[1],'Size':info[2],'FilePath':info[3],'RoFilePath':info[4],'isDown':int(info[5]),'fetype':info[6]}
            Result.append(Resulti)

        return Result
    def UpdataUserUpRecords(self,FilePath,FileName,changeVaule):
        # self.close()
        # self.Connect()
        sql = "update UserUp set isUp=? where LoFilePath ='{}' and FileName='{}'".format(FilePath,FileName)
        data = (str(changeVaule))
        self.cur.execute(sql, data)
    def UpdataUserUpRecord(self,FilePath,FileName,changeVaule):
        # self.close()
        # self.Connect()
        sql = "update UserUp set isUp=? where LoFilePath ='{}' and FileName='{}'".format(FilePath,FileName)
        data = (str(changeVaule))
        self.lock.acquire(True)
        self.cur.execute(sql, data)
        self.conn.commit()
        self.lock.release()
    def UpdataUserDownRecord(self,FilePath,FileName,changeVaule):
        # self.close()
        # self.Connect()
        sql = "update UserDown set isDown=? where FilePath ='{}' and FileName='{}'".format(FilePath,FileName)
        data = (str(changeVaule))
        self.lock.acquire(True)
        self.cur.execute(sql, data)
        self.conn.commit()
        self.lock.release()

    def DelUserUpRecords(self,FilePath,FileName):
        sql = "delete from UserUp where LoFilePath ='{}' and FileName='{}'".format(FilePath, FileName)
        self.cur.execute(sql)
        # self.conn.commit()
    def DelUserUpRecord(self,FilePath,FileName):
        sql = "delete from UserUp where LoFilePath ='{}' and FileName='{}'".format(FilePath, FileName)
        self.lock.acquire(True)
        self.cur.execute(sql)
        self.conn.commit()
        self.lock.release()
    def DelUserDownRecord(self,FilePath,FileName):
        sql = "delete from UserDown where FilePath ='{}' and FileName='{}'".format(FilePath, FileName)
        self.lock.acquire(True)
        self.cur.execute(sql)
        self.conn.commit()
        self.lock.release()
    def DelUserTranspFinshRecord(self,FilePath,FileName):
        sql = "delete from TransFinsh where FilePath ='{}' and FileName='{}'".format(FilePath, FileName)
        self.lock.acquire(True)
        self.cur.execute(sql)
        self.conn.commit()
        self.lock.release()


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
