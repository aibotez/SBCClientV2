from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QAction,QFileDialog,QMessageBox,QDialog
from PyQt5.QtCore import *
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets


class FileShare():
    def __init__(self,ui):
        self.ui = ui
        self.ShareWindow = self.ui.ShareWindow
        self.bindSignal()


    def FileClickDeal(self,info,e):
        if e.buttons() == QtCore.Qt.LeftButton:
            self.FileLeftDeal(info)
        elif e.buttons() == QtCore.Qt.RightButton:
            return
            # self.create_Filerightmenu(info,None)
    def FileLeftDeal(self,info):
        print(info)
        if info['isdir']:
            pass
            self.UpdateShareFile(info)
    def UpdateUi(self,infos):

        self.ui.ShareWindow.clearframe()
        for i in infos:
            self.ui.ShareWindow.add(i)
            self.ui.ShareWindow.label_36.mousePressEvent = partial(self.FileClickDeal,i)



    # http://10.147.17.148:90/SBCShare/?SBCShare=MuSP
    def UpdateShareFile(self,info):
        ShareLink = info['ShareLink']
        path = info['fepath']
        data = {
            'ShareLink':ShareLink,
            'path':path,
            'PassWord':self.PassWord
        }
        SBCShare = self.ui.SBCRe.GetSBCShareFile1(data)
        print(SBCShare)
        self.UpdateUi(SBCShare['res'])


    def GetShareFile(self):
        ShareLink = self.ShareWindow.lineEdit.text()
        SBCShare = self.ui.SBCRe.GetSBCShareFile0(ShareLink)
        self.PassWord = ''
        if 'check' in SBCShare:
            if SBCShare['check'] == '分享不存在':
                QMessageBox.information(self.ui.MainWindow, '提示', '分享文件不存在')
                return
            elif SBCShare['check'] == '分享已超时':
                QMessageBox.information(self.ui.MainWindow, '提示', '分享文件已超时')
                return
            elif SBCShare['check'] == 'password':
                QMessageBox.information(self.ui.MainWindow, '提示', '分享文件不存在')
                pass
        info = SBCShare['res']
        self.ShareUserName = info[0]['ShareUserName']
        for i in range(len(info)):
            info[i]['ShareLink'] = ShareLink.split('SBCShare=')[-1]
            info[i]['PassWord'] = self.PassWord
        self.UpdateUi(info)

    def bindSignal(self):
        self.ShareWindow.pushButton_13.clicked.connect(lambda: self.GetShareFile())
        self.ShareWindow.lineEdit.returnPressed.connect(self.GetShareFile)