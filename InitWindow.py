
import sys,threading,os,hashlib
import time

sys.path.append('.')
sys.path.append('..')
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QAction,QFileDialog,QDialog
from PyQt5.Qt import QThread

from PyQt5.QtGui import QFontMetrics,QCursor, QIcon
from PyQt5.QtCore import *
import base64
from pack import SBCRequest
from pack import TransFileManager
from pack import FileType
from pack import DBManager
from pack import FileOperClick
from pack.preview import ImgPreview

from SubUi import SBCMainWindow
from SubUi import NavShow
# from SubUi import Transmitui
from UpdateUi import FileUpdate
# from UpdateUi import TransShowUpdate
# from SubUi import ReNameui
from UpdateUi import FileShare
from SubUi import Setting1
from PyQt5.QtCore import QObject, pyqtSignal
from pack import UserCheck
from pack import GetMoniterPPi
from pack import FileSyc
from SubUi import FloatWindowui1




class ClickEventDeals():
    def __init__(self,ui,FileUpdates):
        self.ui = ui
        self.filepdate = FileUpdates
    def ClearNavStyle(self):
        self.ui.frame_2.setStyleSheet("")
        self.ui.frame_3.setStyleSheet("")
        self.ui.frame_4.setStyleSheet("")
        self.ui.frame_5.setStyleSheet("")
        self.ui.frame_6.setStyleSheet("")

    def HideFrames(self):
        # ui.frame_12.hide()
        for i in self.ui.frameandscroll:
            # print(i)
            if 'Tran' != i and i!='Share':
                self.ui.frameandscroll[i]['Photo']['frame'].hide()
                self.ui.frameandscroll[i]['Video']['frame'].hide()
                self.ui.frameandscroll[i]['File']['frame'].hide()
        self.ui.frameandscroll['Tran'].hide()
        self.ui.frameandscroll['Share'].hide()
        self.ui.frame_14.hide()
    def NavChoose(self,WosLabel,e):
        if e.buttons() == QtCore.Qt.LeftButton:
            if self.ui.CurNavChosed != WosLabel:
                self.HideFrames()
                self.ClearNavStyle()
                # print(WosLabel)
                if WosLabel == 'Photo':
                    self.ui.CurNavChosed = 'Photo'
                    self.ui.frame_14.show()
                    self.filepdate.PhotoShow()
                    # SBCM.ChoseNav_Photo()
                    self.ui.frame_3.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")
                if WosLabel == 'File':
                    self.ui.CurNavChosed = 'File'
                    self.ui.frame_14.show()
                    self.filepdate.FileShow()
                    # SBCM.ChoseNav_File()
                    self.ui.frame_2.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")
                if WosLabel == 'Video':
                    self.ui.CurNavChosed = 'Video'
                    self.ui.frame_4.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")
                    self.ui.frame_14.show()
                    self.filepdate.VideoShow()
                    # SBCM.ChoseNav_Video()
                if WosLabel == 'Share':
                    self.ui.CurNavChosed = 'Share'
                    self.ui.frameandscroll['Share'].show()
                    self.ui.frame_5.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")
                if WosLabel == 'Transmit':
                    self.ui.CurNavChosed = 'Transmit'
                    # self.ui.frame_14.show()
                    self.ui.frameandscroll['Tran'].show()
                    self.ui.frame_6.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")

def CreatPopFram(SBCMain):
    frame_ChoseNet = QtWidgets.QFrame(SBCMain.frame_14)
    frame_ChoseNet.setGeometry(QtCore.QRect(220, 35, 101, 171))
    frame_ChoseNet.setStyleSheet("#frame_ChoseNet\n"
                                      "{\n"
                                      "    background:#D0D3D4;\n"
                                      "}\n"
                                      "\n"
                                      "#frame_ChoseNet QLabel:hover{\n"
                                      "    background:#A2D9CE;\n"
                                      "    \n"
                                      "    opacity:0.5;\n"
                                      "    }")
    frame_ChoseNet.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_ChoseNet.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_ChoseNet.setObjectName("frame_ChoseNet")
    verticalLayout_3 = QtWidgets.QVBoxLayout(frame_ChoseNet)
    verticalLayout_3.setContentsMargins(0, 0, 0, 0)
    verticalLayout_3.setSpacing(0)
    verticalLayout_3.setObjectName("verticalLayout_3")
    label = QtWidgets.QLabel(frame_ChoseNet)
    label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setObjectName("label")
    verticalLayout_3.addWidget(label)
    label_2 = QtWidgets.QLabel(frame_ChoseNet)
    label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    label_2.setAlignment(QtCore.Qt.AlignCenter)
    label_2.setObjectName("label_2")
    verticalLayout_3.addWidget(label_2)
    label_3 = QtWidgets.QLabel(frame_ChoseNet)
    label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    label_3.setAlignment(QtCore.Qt.AlignCenter)
    label_3.setObjectName("label_3")
    verticalLayout_3.addWidget(label_3)
    # self.retranslateUi(Form)
    # QtCore.QMetaObject.connectSlotsByName(Form)
    label.setText("小黑云")
    label_2.setText("百度云")
    label_3.setText("阿里云")
    SBCMain.frame_ChoseNet = frame_ChoseNet
    SBCMain.choseSBCLabel = label
    SBCMain.choseBDCLabel = label_2
    SBCMain.choseALCLabel = label_3
    SBCMain.frame_ChoseNet.raise_()
    SBCMain.frame_ChoseNet.hide()


class initWindow(QObject):
    signalUpdateUser = pyqtSignal()
    def __init__(self,Main):
        super().__init__()
        # Main.close()
        # return
        self.Main = Main
        self.SBCMain = SBCMainWindow.Ui_SBCclient()
        self.SBCMain.Version = '2.0.0.0'
        self.SBCMain.YM0 = 'pi.sbc.plus:800'
        self.SBCMain.PPIw0 = 36.92
        self.SBCMain.PPIh0 = 33.75
        self.SBCMain.signalUpdateUser = self.signalUpdateUser
        self.SBCMain.signalUpdateUser.connect(self.UpdateUserInfo)

        # [PPIw,PPIh] = GetMoniterPPi.GetMoniterPPI()
        # self.SBCMain.PPIwper = PPIw/self.SBCMain.PPIw0
        # self.SBCMain.PPIhper = PPIh/self.SBCMain.PPIh0
        self.SBCMain.MainWindow = self.Main
        # self.SBCMain.FloatWind.setupUi(self.Main)
        self.SBCMain.SBCRe = SBCRequest.SBCRe()
        # self.SBCMain.MainWindow.hide()
        self.SBCMain.setupUi(self.Main)
        self.SBCMain.label_23.setText('')
        self.usercheck = UserCheck.UserCheck(self.SBCMain)
        if not self.usercheck.LoginStatu:
            sys.exit()
        self.Main.setAcceptDrops(True)
        self.Main.dragEnterEvent = self.dragEnterEvent
        self.Main.dropEvent = self.dropEvent
        # self.SBCMain.setupUi(self.Main)
        # self.SBCMain.MainWindow.show()
        self.SBCMain.TranspArrow = self.SBCMain.label_23
        # self.SBCMain.TranspArrow.setText("↓↑")
        self.SBCMain.DownRecordFile = 'DownRecord.txt'
        self.SBCMain.UpRecordFile = 'UpRecord.txt'
        self.SBCMain.FinishRcordFile = 'FinishRcord.txt'
        self.Thread_LoadImgs = FileUpdate.Thread_LoadImg(self.SBCMain)
        self.SBCMain = self.initFrame()
        self.SBCMain.TransFilesManager = TransFileManager.TransFileManager(self.Main, self.SBCMain)
        # self.Navshows = NavShow.Ui_PhotoShow(self.SBCMain)
        self.FileUpdates = FileUpdate.FileUpdate(self.SBCMain)
        self.fileoperclick = FileOperClick.FileOperClick(self.SBCMain)
        self.FileSycs = FileSyc.FileSyc(self.SBCMain)
        self.SBCMain.OutErrorInfo = self.OutErrorInfo
        self.FloatShow()
        self.FileSycs.SycMain()

        # self.WrVer()
        self.init()

    def WrVer(self):
        Ver = self.SBCMain.Version
        if not os.path.isdir('Ver/'):
            os.mkdir('Ver/')
        if not os.path.exists('Ver/'+Ver):
            with open('Ver/'+Ver,'w'):
                pass

    def OutErrorInfo(self,err):
        localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if not os.path.exists('SBCErrorlog.txt'):
            with open('SBCErrorlog.txt', 'w') as f:
                f.write(localtime + '\n' + err + '\n')
        else:
            with open('SBCErrorlog.txt','a') as f:
                f.write(localtime+'\n'+err+'\n')

    def dragEnterEvent(self, evn):
        self.DrageFileIntoPath = evn.mimeData().text()
        evn.accept()
    # 鼠标放开执行
    def dropEvent(self, evn):
        paths = self.DrageFileIntoPath.split('\n')
        FileAll = []
        # print(paths)
        for i in paths:
            if i:
                FilePath = i.replace('file:///', '')
                if os.path.isdir(FilePath):
                    FileAll.append({'Path': FilePath, 'isDir': 1})
                else:
                    FileAll.append({'Path': FilePath, 'isDir': 0})
        if FileAll:
            self.fileoperclick.Up(FileAll)

        # FilePath = self.DrageFileIntoPath.replace('file:///','')
        # fileoperclick = FileOperClick(self.SBCMain)
        # fileoperclick.Up({'Path':FilePath, 'isDir': 0})

    def WindowReSize(self):
        # if ui.scrollArea.width() < 500:
        #     w = 760
        # else:
        #     w = ui.scrollArea.width()
        w = self.Main.width() - 150

        if self.SBCMain.CurNavChosed in self.SBCMain.SBCFilesDict[self.SBCMain.CurNetChosed]:
            CurSBCFilesDict = self.SBCMain.SBCFilesDict[self.SBCMain.CurNetChosed][self.SBCMain.CurNavChosed]['File']
            # print(CurSBCFilesDict)
            for i in CurSBCFilesDict:
                FIleinfo = CurSBCFilesDict[i]
                FileName = FIleinfo['fename']
                Felabel = FIleinfo['FileNameLabel']
                # print(Felabel)
                metrics = QFontMetrics(Felabel.font())
                # print(metrics)
                new_file_name = metrics.elidedText(FileName, Qt.ElideRight, w*0.5)
                Felabel.setText(new_file_name)

    def MainWindowSizeChange(self,e):
        self.WindowReSize()

    def initparameter(self):
        self.SBCMain.nav = {}
        self.SBCMain.frameandscroll = {}
        self.SBCMain.SBCFilesDict = {}
        self.SBCMain.FileCons = {}
        self.SBCMain.CurFileListOld = {}
        self.SBCMain.NetOper = {}
        self.SBCMain.CurNetChosed = 'SBC'
        self.SBCMain.CurNavChosed = 'File'
        Nets = ['SBC','BDC','ALC']
        for i in Nets:
            self.SBCMain.CurFileListOld[i] = {}
            self.SBCMain.CurFileListOld[i]['Photo'] = []
            self.SBCMain.CurFileListOld[i]['Video'] = []
            self.SBCMain.CurFileListOld[i]['File'] = []

        self.SBCMain.TransDicts = {'Downing':[],'Uping':[],'AcrossNeting':[],'Finish':[]}

    def test1(self):
        horizontal_bar = self.SBCMain.frameandscroll['SBC']['File']['scrollArea'].verticalScrollBar()
        # print(horizontal_bar.value(),horizontal_bar.maximum())
        # print(self.SBCMain.frameandscroll['SBC']['File']['scrollArea'].size())
    # def test(self,e):
    #     horizontal_bar = self.SBCMain.frameandscroll['SBC']['File']['scrollArea'].verticalScrollBar()
    #     delta_y = - e.angleDelta().y()
    #     v = horizontal_bar.value() + delta_y
    #     v = max(min(v, horizontal_bar.maximum()), horizontal_bar.minimum())
    #     print(horizontal_bar.minimum(),horizontal_bar.maximum())
    #     horizontal_bar.setValue(v)
    def LoginOut(self,e):
        # self.SBCMain.MainWindow.destroy()
        # self.SBCMain.MainWindow.close()
        self.SBCMain.MainWindow.hide()
        os.remove('uci/uci')
        sys.exit()
        # self.init()
        # self.SBCMain.SBCLoginWindowDialog.show()

    def FloatShow(self):
        self.SBCMain.SBCFloatWindowDialog = QDialog()
        self.SBCMain.FloatWind = FloatWindowui1.FloatWd(self.SBCMain,self.SBCMain.SBCFloatWindowDialog)
        self.SBCMain.SBCFloatWindowDialog.show()
    def SettingShow(self,e):
        self.SBCMain.SBCSettingWindowDialog = QDialog()
        self.SBCMain.SBCSettingWindow = Setting1.SettingShow(self.SBCMain.SBCSettingWindowDialog,self.SBCMain)
        self.SBCMain.SBCSettingWindowDialog.show()

    def creat_Usermenu(self,e):
        self.groupBox_Upmenu = QMenu()
        self.actionSetting = self.groupBox_Upmenu.addAction(u'设置')
        self.groupBox_Upmenu.addSeparator()
        self.actionTools = self.groupBox_Upmenu.addAction(u'工具')
        self.groupBox_Upmenu.addSeparator()
        self.actionLoginOut = self.groupBox_Upmenu.addAction(u'退出登录')
        self.groupBox_Upmenu.popup(QCursor.pos())
        self.groupBox_Upmenu.setStyleSheet("QMenu{\n"
                                        "    margin:0px 10px 10px 0px;\n"
                                        "    color:blue;\n"
                                        "    font-size:18px;\n"
                                        "}\n")
        self.actionSetting.triggered.connect(self.SettingShow)
        self.actionLoginOut.triggered.connect(self.LoginOut)

    def creat_Upmenu(self,e):
        self.groupBox_Upmenu = QMenu()
        self.actionUpfile = self.groupBox_Upmenu.addAction(u'上传文件')
        self.actionUpfolder = self.groupBox_Upmenu.addAction(u'上传文件夹')
        self.groupBox_Upmenu.popup(QCursor.pos())
        self.groupBox_Upmenu.setStyleSheet("QMenu{\n"
                                        "    margin:0px 10px 10px 0px;\n"
                                        "    color:blue;\n"
                                        "    font-size:18px;\n"
                                        "}\n")
        self.actionUpfile.triggered.connect(self.fileoperclick.UpFile)
        self.actionUpfolder.triggered.connect(self.fileoperclick.UpFolder)
        # self.SBCMain.label_14.mousePressEvent = self.fileoperclick.Down
    def creat_ChoseNetmenu(self,e):
        self.groupBox_ChoseNetmenu = QMenu()
        self.actionSBC = self.groupBox_ChoseNetmenu.addAction(u'小黑云')
        self.actionBDC = self.groupBox_ChoseNetmenu.addAction(u'百度云')
        self.actionALC = self.groupBox_ChoseNetmenu.addAction(u'阿里云')
        self.groupBox_ChoseNetmenu.popup(QCursor.pos())
        self.groupBox_ChoseNetmenu.setStyleSheet("QMenu{\n"
                                        "    margin:0px 10px 10px 0px;\n"
                                        "    color:blue;\n"
                                        "    font-size:18px;\n"
                                        "}\n")
    def creat_Moremenu(self,e):
        self.groupBox_Moremenu = QMenu()
        self.actionShare = self.groupBox_Moremenu.addAction(u'分享')
        self.actionMove = self.groupBox_Moremenu.addAction(u'移动')
        self.actionCopy = self.groupBox_Moremenu.addAction(u'复制')
        self.actionDel = self.groupBox_Moremenu.addAction(u'删除')
        self.actionPorper = self.groupBox_Moremenu.addAction(u'属性')
        self.actionNewFolders = self.groupBox_Moremenu.addAction(u'新建文件夹')
        self.groupBox_Moremenu.popup(QCursor.pos())

        self.groupBox_Moremenu.setStyleSheet("QMenu{\n"
                                        "    margin:0px 10px 10px 0px;\n"
                                        "    color:blue;\n"
                                        "    font-size:18px;\n"
                                        "}\n")
        self.actionDel.triggered.connect(self.fileoperclick.DelFile)
        self.actionNewFolders.triggered.connect(self.fileoperclick.NewFolder)
        self.actionShare.triggered.connect(self.fileoperclick.SBCShare)
        self.actionMove.triggered.connect(self.fileoperclick.SBCFileMove)
        self.actionCopy.triggered.connect(self.fileoperclick.SBCFileCopy)
        self.actionPorper.triggered.connect(self.fileoperclick.SBCFileInfos)
    def initpopup(self):
        pass

    def initFrame(self):
        self.initparameter()
        self.Navshows = NavShow.Ui_PhotoShow(self.SBCMain)
        Nets = ['SBC', 'BDC', 'ALC']
        for i in Nets:
            self.SBCMain.CurNetChosed = i
            self.SBCMain.frameandscroll[i] = {}
            self.SBCMain.SBCFilesDict[i] = {}
            self.SBCMain.FileCons[i] = {}
            self.SBCMain.NetOper[i] = {}
            self.SBCMain.frameandscroll[i]['Photo'] = self.Navshows.InitShow()
            self.SBCMain.frameandscroll[i]['Photo']['frame'].resizeEvent = self.MainWindowSizeChange
            self.SBCMain.frameandscroll[i]['Video'] = self.Navshows.InitShow()
            self.SBCMain.frameandscroll[i]['Video']['frame'].resizeEvent = self.MainWindowSizeChange
            self.SBCMain.frameandscroll[i]['File'] = self.Navshows.initfileshow()
            self.SBCMain.frameandscroll[i]['File']['frame'].resizeEvent = self.MainWindowSizeChange
            # self.SBCMain.frameandscroll[i]['File']['scrollArea'].wheelEvent = self.test

            self.SBCMain.frameandscroll[i]['File']['scrollArea'].verticalScrollBar().valueChanged.connect(self.Thread_LoadImgs.runthread1)
            # vertical.valueChanged.connect(self.test1)
        ShareShow = self.Navshows.InitShareShow()
        TranShow = self.Navshows.InitTranShow()

        # self.SBCMain.TranspscrollArea = TranShow[1]
        # self.SBCMain.frameandscroll['Tran'] = TranShow[0]

        self.SBCMain.CurNetChosed = 'SBC'
        self.SBCMain.frameandscroll['SBC']['File']['frame'].show()

        # self.SBCMain.creat_ChoseNetmenu = self.creat_ChoseNetmenu

        # self.Main.resizeEvent = self.MainWindowSizeChange
        return self.SBCMain

    def initBindSignal(self):
        # print(self.SBCMain.NetOper)
        self.SBCMain.NetOper[self.SBCMain.CurNetChosed]['backbutton'].mousePressEvent = partial(self.FileUpdates.navBackClick)  # back
        self.SBCMain.NetOper[self.SBCMain.CurNetChosed]['refreshbutton'].mousePressEvent = partial(self.FileUpdates.Refresh)
        # self.SBCMain.label_18.mousePressEvent = self.SBCMain.creat_ChoseNetmenu
        CED = ClickEventDeals(self.SBCMain,self.FileUpdates)
        self.SBCMain.frame_13.deleteLater()
        self.SBCMain.frame_2.mousePressEvent = partial(CED.NavChoose,'File')
        self.SBCMain.frame_3.mousePressEvent = partial(CED.NavChoose, 'Photo')
        self.SBCMain.frame_4.mousePressEvent = partial(CED.NavChoose, 'Video')
        self.SBCMain.frame_5.mousePressEvent = partial(CED.NavChoose, 'Share')
        self.SBCMain.frame_6.mousePressEvent = partial(CED.NavChoose, 'Transmit')
        self.SBCMain.label_18.mousePressEvent = self.creat_ChoseNetmenu #切换网盘
        self.SBCMain.label_17.mousePressEvent = self.creat_Moremenu  # 更多
        self.SBCMain.label_15.mousePressEvent = self.creat_Upmenu  # 上传
        self.SBCMain.label_16.mousePressEvent = self.fileoperclick.ReName  # 重命名
        self.fileoperclick = FileOperClick.FileOperClick(self.SBCMain)
        self.SBCMain.label_14.mousePressEvent = self.fileoperclick.Down  # 下载

        self.SBCMain.label_9.mousePressEvent = self.creat_Usermenu  # 用户



    def AniUpdate(self):
        self.anim = QtCore.QPropertyAnimation(self.ui.TranspArrow1, b'geometry')  # 设置动画的对象及其属性
        self.anim.setDuration(2000)  # 设置动画间隔时间
        self.anim.setStartValue(QtCore.QRect(200, 20, 40, 40))  # 设置动画对象的起始属性
        self.anim.setEndValue(QtCore.QRect(50, 360, 0, 0))  # 设置动画对象的结束属性

    def UpdateUserInfo(self):
        data = self.SBCMain.SBCRe.GetUserInfo()
        if 'error' not in data:
            self.SBCMain.label_7.setText(data['usedcappercentstr'])
            self.SBCMain.label_9.setText(data['username'])
            usedper = data['usedcappercent']*130
            self.SBCMain.usedCap.setMinimumSize(QtCore.QSize(usedper, 0))
            self.SBCMain.usedCap.setMaximumSize(QtCore.QSize(usedper, 10))

    def init(self):
        self.SBCMain.signalUpdateUser.emit()
        self.initBindSignal()
        # self.SBCMain.FileUpdate = threading.Thread(target=self.FileUpdates.run)
        # self.SBCMain.FileUpdate.setDaemon(True)
        # self.SBCMain.FileUpdate.start()
        self.FileUpdates.start()
        FileShare_ = FileShare.FileShare(self.SBCMain)

        self.SBCMain.frame_2.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")

        self.SBCMain.TranspArrow1 = QtWidgets.QLabel(self.Main) #
        self.SBCMain.TranspArrow1.setGeometry(200,20,0,0)
        self.SBCMain.TranspArrow1.setPixmap(QtGui.QPixmap('img/Transp2.jpg'))
        self.SBCMain.TranspArrow1.setScaledContents(True) # 图片随文本部件的大小变动
        self.SBCMain.anim = QtCore.QPropertyAnimation(self.SBCMain.TranspArrow1, b'geometry')  # 设置动画的对象及其属性
        self.SBCMain.anim.setDuration(1000)  # 设置动画间隔时间
        self.SBCMain.anim.setStartValue(QtCore.QRect(200, 20, 40, 40))  # 设置动画对象的起始属性
        self.SBCMain.anim.setEndValue(QtCore.QRect(50, 360, 0, 0))  # 设置动画对象的结束属性
















