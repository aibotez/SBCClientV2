from . import Settingui
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
import sip,requests
from PyQt5.QtGui import QFontMetrics,QCursor, QIcon
from PyQt5.QtCore import *
from pack import DBManager


class SettingShow(Settingui.Ui_Dialog):
    def __init__(self,Dialog,ui):
        super().__init__()
        self.ui = ui
        self.Dialog = Dialog
        self.dbManager = DBManager.DBManager()
        self.init()


    def GetClientInfo(self):
        Result = self.dbManager.GetClientSetting()
        # self.ui.DownPath = Result['DownPath']
        hosts = Result['host']
        self.hosts = hosts.split('#')
        # self.ui.BackupRoPath = Result['BackupRoPath']
        # self.ui.DowNum = Result['DowNum']
        # self.ui.UpNum = Result['UpNum']
        # self.ui.SycOpen = Result['SycOpen']
        # self.ui.SycFre = Result['SycFre']
        # self.ui.MSK = Result['MSK']
        # self.ui.AutoUpdate = Result['AutoUpdate']
        self.ClientInfo = Result
    def LoadClienttingConfig(self):
        self.GetClientInfo()
        host = ''
        for i in self.hosts:
            if i:
                host  = host + i +'\n'
        if host:
            self.textEdit.setText(host)
        self.label_16.setText(' '+self.ClientInfo['DownPath'])
        self.lineEdit_2.setText(str(self.ClientInfo['DowNum']))
        self.lineEdit_3.setText(str(self.ClientInfo['UpNum']))
        self.label_22.setText(' '+self.ClientInfo['BackupLoPath'])
        self.label_25.setText(' '+self.ClientInfo['BackupRoPath'])
        self.radioButton.setChecked(self.ClientInfo['SycOpen'])
        self.radioButton_2.setChecked(self.ClientInfo['AutoUpdate'])
        # Filei['checkBox'].setChecked(False)

    def hosttest(self):
        host = self.lineEdit.text()
        if host:
            print(host)
            url = 'http://' + host + '/ConnectTest'
            try:
                res = requests.get(url, timeout=2).text
                if res == '1':
                    self.label_12.setText('测试通过')
                    return 1
                self.label_12.setText('连接错误')
                return 0
            except:
                self.label_12.setText('连接超时')
                return 0
        else:
            self.label_12.setText('域名为空')
    def SaveConnect(self):
        hosts = self.textEdit.toPlainText()
        host = hosts.split('\n')
        hoststr = ''
        for i in host:
            if i:
                hoststr = hoststr + '#' + i
        self.ClientInfo['host'] = hoststr
        self.dbManager.DelClientSettingAllRecords()
        self.dbManager.AddClientSetting(self.ClientInfo)


    def init(self):
        self.setupUi(self.Dialog)
        self.label_2.setText('')
        self.label_3.setText('')
        self.label_5.setText('')
        self.label_7.setText('')
        self.label_16.setText('')
        self.label_22.setText('')
        self.label_25.setText('')
        self.label_35.setText('')
        self.label_36.setText('')
        self.tabWidget.tabBar().hide()
        self.label.mousePressEvent = partial(self.NavOper,'NetCon')
        self.label_4.mousePressEvent = partial(self.NavOper, 'UpDOwn')
        self.label_6.mousePressEvent = partial(self.NavOper, 'Syn')
        self.label_8.mousePressEvent = partial(self.NavOper, 'Other')
        self.NavOper('NetCon',0)
        self.LoadClienttingConfig()
        self.pushButton.clicked.connect(self.hosttest)
        self.pushButton_2.clicked.connect(self.SaveConnect)
    def ClearNavStyle(self):
        self.frame.setStyleSheet("#frame:hover{background:#D0D3D4;border-radius:18px;opacity:0.5;}")
        self.frame_2.setStyleSheet("#frame_2:hover{background:#D0D3D4;border-radius:18px;opacity:0.5;}")
        self.frame_3.setStyleSheet("#frame_3:hover{background:#D0D3D4;border-radius:18px;opacity:0.5;}")
        self.frame_4.setStyleSheet("#frame_4:hover{background:#D0D3D4;border-radius:18px;opacity:0.5;}")
    def NavOper(self,oper,e):
        self.ClearNavStyle()
        if oper == 'NetCon':
            self.tabWidget.setCurrentIndex(0)
            self.frame.setStyleSheet("background:#7DCEA0;border-radius:12px;opacity:0.5;")
        elif oper == 'UpDOwn':
            self.tabWidget.setCurrentIndex(1)
            self.frame_2.setStyleSheet("background:#7DCEA0;border-radius:12px;opacity:0.5;")
        elif oper == 'Syn':
            self.tabWidget.setCurrentIndex(2)
            self.frame_3.setStyleSheet("background:#7DCEA0;border-radius:12px;opacity:0.5;")
        elif oper == 'Other':
            self.tabWidget.setCurrentIndex(3)
            self.frame_4.setStyleSheet("background:#7DCEA0;border-radius:12px;opacity:0.5;")

