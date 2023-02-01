from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QAction,QFileDialog,QMessageBox,QDialog,QInputDialog,QLineEdit
from PyQt5.QtCore import *
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFontMetrics,QCursor, QIcon
import sip,threading,time
from SubUi import ShareSave2SBC
from pack import FileOperClick

class FileShare(QObject):
    signal = pyqtSignal(list)
    signal1 = pyqtSignal(str)
    signalMsgBox = pyqtSignal(str)
    signalMsgBoxInpuPass = pyqtSignal()
    def __init__(self,ui):
        super(FileShare, self).__init__()
        self.ui = ui
        self.signal.connect(self.adds)
        self.signal1.connect(self.NavUpdate)
        self.signalMsgBox.connect(lambda info:QMessageBox.information(self.ui.MainWindow, '提示',info))
        self.signalMsgBoxInpuPass.connect(self.InputPassword)
        self.ShareFiles = []
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
        return


    def adds(self,infos):
        for i in infos:
            self.ui.ShareWindow.add(i)
            self.ui.ShareWindow.label_36.mousePressEvent = partial(self.FileClickDeal,i)
            self.ShareFiles.append({'check':self.ui.ShareWindow.checkBox_2,'file':i})
        return

    def UpdateUi(self,infos,first=None):
        self.ui.ShareWindow.clearframe()
        self.ShareFiles = []
        shareFaPath = infos[0]['fepath'].split('/')
        del shareFaPath[0]
        del shareFaPath[-1]
        shareFaPath = '/'+'/'.join(shareFaPath)
        if not first:
            self.NavUpdate(shareFaPath)
        # self.signal1.emit(shareFaPath)
        self.signal.emit(infos)
        # for i in infos:
        #     self.ui.ShareWindow.add(i)
        #     self.ui.ShareWindow.label_36.mousePressEvent = partial(self.FileClickDeal,i)
        #     self.ShareFiles.append({'check':self.ui.ShareWindow.checkBox_2,'file':i})


    # {"ShareFile": [{"fepath": "/\u76f8\u51731.bmp", "fename": "\u76f8\u51731.bmp", "fetype": "img", "isdir": 0}],
    #  "ShareDateDur": "7\u5929\u5185\u6709\u6548", "SharePass": "", "useremail": "2290227486@qq.com",
    #  "shareFaPath": "/home"}

    # http://10.147.17.148:90/SBCShare/?SBCShare=GG2Z
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

    # http://10.147.17.148:90/SBCShare/?SBCShare=2Kc4
    def GetShareFile(self):
        self.ui.tShareS = threading.Thread(target=self.GetShareFile1)
        self.ui.tShareS.setDaemon(True)
        self.ui.tShareS.start()
    def InputPassword(self):
        text, okPressed = QInputDialog.getText(self.ui.MainWindow, "输入分享密码", "输入分享密码：", QLineEdit.Normal, "")
        if okPressed and text != '':
            data = {
                'ShareLink': self.ShareLink,
                'path': '',
                'PassWord':text
            }
            SBCShare = self.ui.SBCRe.GetSBCShareFile1(data)
            if type(SBCShare['res']) == str:
                self.signalMsgBox.emit('密码错误！')
                return
            info = SBCShare['res']
            self.ShareUserName = info[0]['ShareUserName']
            for i in range(len(info)):
                info[i]['ShareLink'] = self.ShareLink
                info[i]['PassWord'] = self.PassWord
            self.UpdateUi(info, 1)
        # okPressed.exec_()
    def GetShareFile1(self):
        ShareLink = self.ShareWindow.lineEdit.text()
        SBCShare = self.ui.SBCRe.GetSBCShareFile0(ShareLink)
        self.ShareLink = ShareLink.split('SBCShare=')[-1]
        self.PassWord = ''
        if 'check' in SBCShare:
            if SBCShare['check'] == '分享不存在':
                self.signalMsgBox.emit('分享文件不存在')
                return
            elif SBCShare['check'] == '分享已超时':
                self.signalMsgBox.emit('分享文件已超时')
                return
            elif SBCShare['check'] == 'password':
                self.signalMsgBoxInpuPass.emit()
                return
        info = SBCShare['res']
        self.ShareUserName = info[0]['ShareUserName']
        for i in range(len(info)):
            info[i]['ShareLink'] = self.ShareLink
            info[i]['PassWord'] = self.PassWord
        self.UpdateUi(info,1)
    def GetChoseFiles(self):
        ChosedFiles = []
        for i in self.ShareFiles:
            Filei =i
            if Filei['check'].isChecked():
                Filei['check'].setChecked(False)
                ChosedFiles.append(Filei['file'])
        return ChosedFiles

    def DownFile(self):
        GetChoseFiles = self.GetChoseFiles()
        DownFiles = []
        #Down {'size': 2613, 'fepath': '/home/Surface_ne1.m', 'fename': 'Surface_ne1.m', 'isdir': 0,
        #  'fepath_base64': 'L2hvbWUvU3VyZmFjZV9uZTEubQ==', 'fetype': 'other'}
        if GetChoseFiles:
            for i in GetChoseFiles:
                i['shareinfo'] = {'sharelink':i['ShareLink'],'password':i['password'],'fepath':i['fepath']}
                DownFiles.append(i)
            FileOperclick = FileOperClick.FileOperClick(self.ui)
            t = threading.Thread(target=FileOperclick.run1,args=(DownFiles,))
            t.setDaemon(True)
            t.start()


    def Save2SBC(self):
        GetChoseFiles = self.GetChoseFiles()
        if GetChoseFiles:
            self.ui.SBCFileSave2SBCWindowDialog = QDialog()
            ShareSave2SBCi = ShareSave2SBC.CopyUi(self.ui.SBCFileSave2SBCWindowDialog,self.ui,GetChoseFiles)
            self.ui.SBCFileSave2SBCWindowDialog.show()
    def SaveFilebtn(self):
        self.groupBox_Moremenu = QMenu()
        self.actionSaveSBC = self.groupBox_Moremenu.addAction(u'保存进小黑云')
        self.actionSaveBD = self.groupBox_Moremenu.addAction(u'保存进百度云')
        self.actionSaveAL = self.groupBox_Moremenu.addAction(u'保存进阿里云')
        self.groupBox_Moremenu.popup(QCursor.pos())
        self.groupBox_Moremenu.setStyleSheet("QMenu{\n"
                                        "    margin:0px 10px 10px 0px;\n"
                                        "    color:blue;\n"
                                        "    font-size:18px;\n"
                                        "}\n")
        self.actionSaveSBC.triggered.connect(self.Save2SBC)
    def bindSignal(self):
        self.ShareWindow.pushButton_13.clicked.connect(lambda: self.GetShareFile())
        self.ShareWindow.lineEdit.returnPressed.connect(self.GetShareFile)
        self.ShareWindow.pushButton_15.clicked.connect(lambda: self.SaveFilebtn())
        self.ShareWindow.pushButton_14.clicked.connect(lambda: self.DownFile())
