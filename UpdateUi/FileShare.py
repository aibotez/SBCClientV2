from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QAction,QFileDialog,QMessageBox,QDialog
from PyQt5.QtCore import *
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
import sip


class FileShare():
    def __init__(self,ui):
        self.ui = ui
        self.ShareWindow = self.ui.ShareWindow
        self.bindSignal()
        # self.NavUpdate('/abd')


    def FileClickDeal(self,info,e):
        if e.buttons() == QtCore.Qt.LeftButton:
            self.FileLeftDeal(info)
        elif e.buttons() == QtCore.Qt.RightButton:
            return
            # self.create_Filerightmenu(info,None)
    def FileLeftDeal(self,info):
        if info['isdir']:
            pass
            self.UpdateShareFile(info['fepath'])

    def navClick(self, FilePath, e):
        if e.buttons() == QtCore.Qt.LeftButton:
            self.UpdateShareFile(FilePath)
    def NavUpdate(self,info):
        Childs = self.ui.ShareWindow.frame_2.findChildren(QtWidgets.QLabel,"label_2")
        for i in Childs:
            i.deleteLater()
            sip.delete(i)
        navtemp = info.split('/')
        navtempname = [i for i in navtemp if i]
        # if navtempname:
        #     del navtempname[-1]
        navtemppaths = []
        navtemppath = ''
        for i in navtempname:
            navtemppath = navtemppath + '/' + i
            navtemppaths.append(navtemppath)
        label_2 = QtWidgets.QLabel(self.ui.ShareWindow.frame_2)
        label_2.setObjectName("label_2")
        self.ui.ShareWindow.horizontalLayout_4.addWidget(label_2)
        label_2.setText('分享文件')
        if len(navtempname)>0:
            label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            label_2.mousePressEvent = partial(self.navClick, '')
        for i in range(len(navtempname)):
            label_2 = QtWidgets.QLabel(self.ui.ShareWindow.frame_2)
            label_2.setObjectName("label_2")
            self.ui.ShareWindow.horizontalLayout_4.addWidget(label_2)
            label_2.setText(' > ')
            label_2 = QtWidgets.QLabel(self.ui.ShareWindow.frame_2)
            label_2.setObjectName("label_2")
            self.ui.ShareWindow.horizontalLayout_4.addWidget(label_2)
            label_2.setText(navtempname[i])
            if i < len(navtempname)-1:
                label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                label_2.mousePressEvent = partial(self.navClick, navtemppaths[i])
            else:
                label_2.setStyleSheet("#label_2{color:#212F3C;}")


        label_2 = QtWidgets.QLabel(self.ui.ShareWindow.frame_2)
        label_2.setObjectName("label_2")
        self.ui.ShareWindow.horizontalLayout_4.addWidget(label_2)
        label_2.setText('')
        label_2.setMinimumSize(QtCore.QSize(3000, 30))
        label_2.setMaximumSize(QtCore.QSize(3000, 30))
    def UpdateUi(self,infos):
        self.ui.ShareWindow.clearframe()

        shareFaPath = infos[0]['fepath'].split('/')
        del shareFaPath[0]
        del shareFaPath[-1]
        shareFaPath = '/'+'/'.join(shareFaPath)
        self.NavUpdate(shareFaPath)
        for i in infos:
            self.ui.ShareWindow.add(i)
            self.ui.ShareWindow.label_36.mousePressEvent = partial(self.FileClickDeal,i)



    # http://10.147.17.148:90/SBCShare/?SBCShare=MuSP
    def UpdateShareFile(self,path):
        # ShareLink = info['ShareLink']
        # path = info['fepath']
        data = {
            'ShareLink':self.ShareLink,
            'path':path,
            'PassWord':self.PassWord
        }
        SBCShare = self.ui.SBCRe.GetSBCShareFile1(data)
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
        self.ShareLink = ShareLink.split('SBCShare=')[-1]
        for i in range(len(info)):
            info[i]['ShareLink'] = ShareLink.split('SBCShare=')[-1]
            info[i]['PassWord'] = self.PassWord
        self.UpdateUi(info)

    def bindSignal(self):
        self.ShareWindow.pushButton_13.clicked.connect(lambda: self.GetShareFile())
        self.ShareWindow.lineEdit.returnPressed.connect(self.GetShareFile)