import os,wmi,requests
from pack import DBManager
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QAction,QFileDialog,QMessageBox,QDialog,QInputDialog,QLineEdit

class UserCheck():
    ###################
    ###             登录流程
    ##  1、连接/创建储存客户端信息的本地数据库
    ##  2、判断域名是否可用、网络是否通畅
    ##  3、判断用户信息/更改用户信息
    ##  4、完成登录
    ####################
    def __init__(self,ui):
        self.s = wmi.WMI()
        self.ui = ui
        self.UserFile = './uci'
        self.ConnectDB()
    def ConnectDB(self):
        Disk = ['C:/','D:/','E:/']
        Diskexist = []
        for i in Disk:
            if os.path.isdir(i):
                Diskexist.append(i)
        self.SBCDownDisk = Diskexist[-1]
        self.SBCDownPath = self.SBCDownDisk+'小黑云下载/'
        self.dbManager = DBManager.DBManager({'BackupLoPath':'','DownPath':self.SBCDownPath,'host':self.ui.YM0,'BackupRoPath':'',
                                              'DowNum':2,'UpNum':2,'SycOpen':0,'SycFre':'','MSK':'','AutoUpdate':1})



        if not os.path.exists(self.UserFile):
            print('NotLogin')
            # if os.path.exists('./UserDB.db'):
            #     os.remove('./UserDB.db')
        UserInfo = self.GetUser()
        CurComputerId = self.get_mainboard_info()
        if CurComputerId != UserInfo['ComputerId']:
            pass
            # if os.path.exists('./UserDB.db'):
            #     os.remove('./UserDB.db')


    def ConnectTest(self,host):
        url = 'http://'+host+'/ConnectTest'
        res = requests.get(url,timeout=2).text
        if res == '1':
            return 1
        return 0
    def init(self):
        self.GetClientInfo()
        hosts = self.hosts
        hostsavi = []
        for i in hosts:
            if i:
                if self.ConnectTest(i):
                    hostsavi.append(i)
        if hostsavi:
            self.ui.host = hostsavi[0]
        else:
            while True:
                text, okPressed = QInputDialog.getText(self.ui.MainWindow, "连接错误", "输入域名及端口：", QLineEdit.Normal, "")
                if okPressed and text != '':
                    if self.ConnectTest(text):
                        self.ui.host = text
                        break





    def GetClientInfo(self):
        Result = self.dbManager.GetClientSetting()
        self.ui.DownPath = Result['DownPath']
        self.hosts = Result['host']
        self.ui.BackupRoPath = Result['BackupRoPath']
        self.ui.DowNum = Result['DowNum']
        self.ui.UpNum = Result['UpNum']
        self.ui.SycOpen = Result['SycOpen']
        self.ui.SycFre = Result['SycFre']
        self.ui.MSK = Result['MSK']
        self.ui.AutoUpdate = Result['AutoUpdate']


    # 主板序列号
    def get_mainboard_info(self):
        mainboard = []
        for board_id in self.s.Win32_BaseBoard():
            mainboard.append(board_id.SerialNumber.strip().strip('.'))
        return mainboard[0]


    def GetUser(self):
        with open(self.UserFile,'r') as f:
            UserInfo_= f.read()
        Temp = UserInfo_.split('#')
        ComputerId = Temp[0]
        UserName = Temp[1]
        UserPass = Temp[2]
        UserInfo = {'ComputerId':ComputerId,'UserName':UserName,'UserPass':UserPass}
        return UserInfo
    def LoginCheck(self):
        self.GetClientInfo()




        if not os.path.exists(self.UserFile):
            print('NotLogin')
            return 'LoginError'
        UserInfo = self.GetUser()
        CurComputerId = self.get_mainboard_info()
        if CurComputerId != UserInfo['ComputerId']:
            return 'LoginError'

