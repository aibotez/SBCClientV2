from . import Settingui
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
import sip,requests
from PyQt5.QtGui import QFontMetrics,QCursor, QIcon
from PyQt5.QtCore import *
from pack import DBManager
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QAction,QFileDialog,QMessageBox,QDialog
from pack import ChoseRoPathUi
from pack import Update
import sys


class SettingShow(Settingui.Ui_Dialog,QObject):
    signalUpdateProgress = pyqtSignal(str)
    signalexit = pyqtSignal()
    def __init__(self,Dialog,ui):
        super().__init__()
        self.ui = ui
        self.signalUpdateProgress.connect(self.UpdateProgress)
        self.signalexit.connect(lambda :sys.exit())
        self.update = Update.Update(self.ui)
        self.Dialog = Dialog
        self.Dialog.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Tool)
        self.dbManager = DBManager.DBManager()
        self.init()

    def UpdateProgress(self,progress):
        self.label_36.setText(progress)
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
        self.lineEdit_4.setText(str(self.ClientInfo['SycFre']))
        self.lineEdit_5.setText(self.ClientInfo['MSK'])
        self.lineEdit_6.setText(str(self.ClientInfo['SycMode']))

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
        Result = self.dbManager.GetClientSetting()
        self.ClientInfo = Result
        hosts = self.textEdit.toPlainText()
        host = hosts.split('\n')
        hoststr = ''
        for i in host:
            if i:
                hoststr = hoststr + '#' + i
        self.ClientInfo['host'] = hoststr
        self.dbManager.DelClientSettingAllRecords()
        self.dbManager.AddClientSetting(self.ClientInfo)
    def DownFilePathSetting(self,e):
        FolderPath = QFileDialog.getExistingDirectory(self.ui.MainWindow, "选择文件夹", "./")
        if FolderPath:
            FolderPath += '/'
            Result = self.dbManager.GetClientSetting()
            self.ClientInfo = Result
            self.ClientInfo['DownPath'] = FolderPath
            self.dbManager.DelClientSettingAllRecords()
            self.dbManager.AddClientSetting(self.ClientInfo)
            self.LoadClienttingConfig()
    def SycLoPathSetting(self,e):
        FolderPath = QFileDialog.getExistingDirectory(self.ui.MainWindow, "选择文件夹", "./")
        if FolderPath:
            FolderPath += '/'
            Result = self.dbManager.GetClientSetting()
            self.ClientInfo = Result
            self.ClientInfo['BackupLoPath'] = FolderPath
            self.dbManager.DelClientSettingAllRecords()
            self.dbManager.AddClientSetting(self.ClientInfo)
            self.LoadClienttingConfig()
    def saveDownNum(self,num,up = None):
        self.ClientInfo = self.dbManager.GetClientSetting()
        if up:
            self.ClientInfo['UpNum'] = num
        else:
            self.ClientInfo['DowNum'] = num
        self.dbManager.DelClientSettingAllRecords()
        self.dbManager.AddClientSetting(self.ClientInfo)
        self.LoadClienttingConfig()

    def creat_UpNummenu(self,e):
        self.groupBox_Upmenu = QMenu()
        self.action1= self.groupBox_Upmenu.addAction(u'1')
        self.action2 = self.groupBox_Upmenu.addAction(u'2')
        self.action3 = self.groupBox_Upmenu.addAction(u'3')
        self.action4 = self.groupBox_Upmenu.addAction(u'4')
        self.action5 = self.groupBox_Upmenu.addAction(u'5')
        self.groupBox_Upmenu.popup(QCursor.pos())
        self.groupBox_Upmenu.setStyleSheet("QMenu{margin:0px 2px 2px 2px;color:blue;font-size:10px;}")
        self.action1.triggered.connect(lambda :self.saveDownNum(1,1))
        self.action2.triggered.connect(lambda: self.saveDownNum(2,1))
        self.action3.triggered.connect(lambda: self.saveDownNum(3,1))
        self.action4.triggered.connect(lambda: self.saveDownNum(4,1))
        self.action5.triggered.connect(lambda: self.saveDownNum(5,1))
    def creat_DowNummenu(self,e):
        self.groupBox_Upmenu = QMenu()
        self.action1= self.groupBox_Upmenu.addAction(u'1')
        self.action2 = self.groupBox_Upmenu.addAction(u'2')
        self.action3 = self.groupBox_Upmenu.addAction(u'3')
        self.action4 = self.groupBox_Upmenu.addAction(u'4')
        self.action5 = self.groupBox_Upmenu.addAction(u'5')
        self.groupBox_Upmenu.popup(QCursor.pos())
        self.groupBox_Upmenu.setStyleSheet("QMenu{margin:0px 2px 2px 2px;color:blue;font-size:10px;}")
        self.action1.triggered.connect(lambda :self.saveDownNum(1))
        self.action2.triggered.connect(lambda: self.saveDownNum(2))
        self.action3.triggered.connect(lambda: self.saveDownNum(3))
        self.action4.triggered.connect(lambda: self.saveDownNum(4))
        self.action5.triggered.connect(lambda: self.saveDownNum(5))
        # self.actionLoginOut.triggered.connect(self.LoginOut)
    def SycOpen_radio_button(self):
        self.ClientInfo = self.dbManager.GetClientSetting()
        self.ClientInfo['SycOpen'] = self.radioButton.isChecked()
        self.dbManager.DelClientSettingAllRecords()
        self.dbManager.AddClientSetting(self.ClientInfo)
        self.LoadClienttingConfig()

    def saveSycFre(self,SyTime):
        self.ClientInfo = self.dbManager.GetClientSetting()
        self.ClientInfo['SycFre'] = SyTime
        self.dbManager.DelClientSettingAllRecords()
        self.dbManager.AddClientSetting(self.ClientInfo)
        self.LoadClienttingConfig()
    def creat_SycFreNummenu(self,e):
        self.groupBox_Upmenu = QMenu()
        self.action1= self.groupBox_Upmenu.addAction(u'10分钟')
        self.action2 = self.groupBox_Upmenu.addAction(u'30分钟')
        self.action3 = self.groupBox_Upmenu.addAction(u'1小时')
        self.action4 = self.groupBox_Upmenu.addAction(u'2小时')
        self.action5 = self.groupBox_Upmenu.addAction(u'5分钟')
        self.groupBox_Upmenu.popup(QCursor.pos())
        self.groupBox_Upmenu.setStyleSheet("QMenu{margin:0px 2px 2px 2px;color:blue;font-size:10px;}")
        self.action1.triggered.connect(lambda :self.saveSycFre('10分钟'))
        self.action2.triggered.connect(lambda: self.saveSycFre('30分钟'))
        self.action3.triggered.connect(lambda: self.saveSycFre('1小时'))
        self.action4.triggered.connect(lambda: self.saveSycFre('2小时'))
        self.action5.triggered.connect(lambda: self.saveSycFre('5分钟'))

    def saveSycMode(self,num):
        self.ClientInfo = self.dbManager.GetClientSetting()
        self.ClientInfo['SycMode'] = num
        self.dbManager.DelClientSettingAllRecords()
        self.dbManager.AddClientSetting(self.ClientInfo)
        self.LoadClienttingConfig()
    def creat_SycModemenu(self,e):
        self.groupBox_Upmenu = QMenu()
        self.action1= self.groupBox_Upmenu.addAction(u'1')
        self.action2 = self.groupBox_Upmenu.addAction(u'2')
        self.action3 = self.groupBox_Upmenu.addAction(u'3')
        self.groupBox_Upmenu.popup(QCursor.pos())
        self.groupBox_Upmenu.setStyleSheet("QMenu{margin:0px 2px 2px 2px;color:blue;font-size:10px;}")
        self.action1.triggered.connect(lambda :self.saveSycMode(1))
        self.action2.triggered.connect(lambda: self.saveSycMode(2))
        self.action3.triggered.connect(lambda: self.saveSycMode(3))
    def MSKinput(self,keyevent):
        self.ClientInfo = self.dbManager.GetClientSetting()
        modifiers = keyevent.modifiers()
        if modifiers == Qt.ControlModifier:
            if keyevent.text():
                self.lineEdit_5.setText('Ctrl + ' + chr(keyevent.key()))
                self.ClientInfo['MSK'] = 'Ctrl + '+chr(keyevent.key())
                self.dbManager.DelClientSettingAllRecords()
                self.dbManager.AddClientSetting(self.ClientInfo)
            else:
                self.lineEdit_5.setText('Ctrl + ')
        elif modifiers == Qt.AltModifier:
            if keyevent.text():
                self.lineEdit_5.setText('Alt + ' + chr(keyevent.key()))
                self.ClientInfo['MSK'] = 'Alt + '+chr(keyevent.key())
                self.dbManager.DelClientSettingAllRecords()
                self.dbManager.AddClientSetting(self.ClientInfo)
            else:
                self.lineEdit_5.setText('Alt + ')
        elif modifiers == (Qt.ControlModifier|Qt.AltModifier ):
            if keyevent.text():
                self.lineEdit_5.setText('Ctrl + Alt + ' + chr(keyevent.key()))
                self.ClientInfo['MSK'] = 'Ctrl + Alt + '+chr(keyevent.key())
                self.dbManager.DelClientSettingAllRecords()
                self.dbManager.AddClientSetting(self.ClientInfo)
            else:
                self.lineEdit_5.setText('Ctrl + Alt + ')
        else:
            self.lineEdit_5.setText('')
    def SycRoPathSetting(self,e):
        ChoseRoPathui = ChoseRoPathUi.ChoseRoPathUi(self.ui)
        if ChoseRoPathui.ChosedRoPath:
            self.ClientInfo = self.dbManager.GetClientSetting()
            self.ClientInfo['BackupRoPath'] = ChoseRoPathui.ChosedRoPath
            self.dbManager.DelClientSettingAllRecords()
            self.dbManager.AddClientSetting(self.ClientInfo)
            self.LoadClienttingConfig()
    def Update(self,e):
        RoVer = self.update.GetRoVersion()
        RoVerstr = RoVer['Ver']
        # self.update.RoVer = RoVerstr
        RoVerint = RoVer['Verint']
        LoVerstr = self.ui.Version
        LoVerint = float('0.'+LoVerstr.replace('.',''))
        self.label_35.setText(RoVerstr)
        if RoVerint> LoVerint:
            self.label_36.setText('立即更新')
    def init(self):
        self.setupUi(self.Dialog)
        self.label_32.setText(self.ui.Version)
        self.label_2.setText('')
        self.label_3.setText('')
        self.label_5.setText('')
        self.label_7.setText('')
        self.label_16.setText('')
        self.label_22.setText('')
        self.label_25.setText('')
        self.label_35.setText('')
        self.label_36.setText('')
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.tabBar().hide()
        self.label.mousePressEvent = partial(self.NavOper,'NetCon')
        self.label_17.mousePressEvent = self.DownFilePathSetting
        self.label_4.mousePressEvent = partial(self.NavOper, 'UpDOwn')
        self.label_6.mousePressEvent = partial(self.NavOper, 'Syn')
        self.label_8.mousePressEvent = partial(self.NavOper, 'Other')
        self.NavOper('NetCon',0)
        self.LoadClienttingConfig()
        self.pushButton.clicked.connect(self.hosttest)
        self.pushButton_2.clicked.connect(self.SaveConnect)
        self.label_18.mousePressEvent = self.creat_DowNummenu
        self.label_20.mousePressEvent = self.creat_UpNummenu
        self.radioButton.clicked.connect(self.SycOpen_radio_button)
        self.label_28.mousePressEvent = self.creat_SycFreNummenu
        # self.lineEdit_5.textChanged.connect(self.MSKinput)
        # self.lineEdit_5.changeEvent = self.MSKinput
        self.lineEdit_5.keyPressEvent = self.MSKinput
        self.label_39.mousePressEvent = self.creat_SycModemenu
        self.label_23.mousePressEvent = self.SycLoPathSetting
        self.label_26.mousePressEvent = self.SycRoPathSetting
        self.label_33.mousePressEvent = self.Update
        self.label_36.mousePressEvent = lambda e: self.update.Downact(self.signalUpdateProgress,self.signalexit)
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

