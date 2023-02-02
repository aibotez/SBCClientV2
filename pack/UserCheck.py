import os,wmi,requests
from pack import DBManager
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QAction,QFileDialog,QMessageBox,QDialog,QInputDialog,QLineEdit
from SubUi import Loginui1

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
        self.loginui = Loginui1.LoginUi(ui)
        self.UserFile = './uci/uci'
        self.LoginStatu = 0
        self.ConnectDB()
        self.init()
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



    def ConnectTest(self,host):
        url = 'http://'+host+'/ConnectTest'
        try:
            res = requests.get(url,timeout=2).text
            return 1
        except:
            return 0

    def Login(self):
        pass

    def init(self):
        ###连接测试
        self.GetClientInfo()
        hosts = self.hosts
        hostsavi = []
        for i in hosts:
            if i:
                if self.ConnectTest(i):
                    hostsavi.append(i)
        if hostsavi:
            self.ui.host = hostsavi[0]
            self.ui.SBCRe.host = hostsavi[0]
        else:
            while True:
                text, okPressed = QInputDialog.getText(self.ui.MainWindow, "连接错误", "输入域名及端口：", QLineEdit.Normal, "")
                if okPressed and text != '':
                    if self.ConnectTest(text):
                        self.ui.host = text
                        self.ClientInfo['host'] = text
                        self.dbManager.DelClientSettingAllRecords()
                        self.dbManager.AddClientSetting(self.ClientInfo)
                        break
                else:
                    return
        ###############判断用户登录
        if not os.path.exists(self.UserFile):
            print('NotLogin')
            self.loginui.Login()
            self.LoginStatu = self.loginui.LoginStatu
            # self.Login()
        else:
            UserInfo = self.GetUser()
            CurComputerId = self.get_mainboard_info()
            if CurComputerId != UserInfo['ComputerId']:
                ###打开登录界面
                self.loginui.Login()
                # self.Login()
            data = {
                'usercount':UserInfo['UserName'],
                'userpassword':UserInfo['UserPass']
            }
            ####登录尝试
            LginRes = self.ui.SBCRe.Login(data)
            if not LginRes:
                self.loginui.Login()






    def GetClientInfo(self):
        Result = self.dbManager.GetClientSetting()
        self.ui.DownPath = Result['DownPath']
        hosts = Result['host']
        self.hosts = hosts.split('#')
        self.ui.BackupRoPath = Result['BackupRoPath']
        self.ui.DowNum = Result['DowNum']
        self.ui.UpNum = Result['UpNum']
        self.ui.SycOpen = Result['SycOpen']
        self.ui.SycFre = Result['SycFre']
        self.ui.MSK = Result['MSK']
        self.ui.AutoUpdate = Result['AutoUpdate']
        self.ClientInfo = Result


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

