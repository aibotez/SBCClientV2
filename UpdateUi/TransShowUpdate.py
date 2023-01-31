import sys,threading,os,hashlib,requests,json
import time,sip

sys.path.append('..')
from pack import DBManager
from UpdateUi import TranspUp
# from pack import SBCRequest
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QThread,QMutex
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import threading

qmut_1 = QMutex()


def size_format(size):
    if size < 1024:
        return '%i' % size + 'size'
    elif 1024 <= size < 1024 * 1024:
        return '%.1f' % float(size / 1024) + 'KB'
    elif 1024 * 1024 <= size < 1024 * 1024 * 1024:
        return '%.1f' % float(size / (1024 * 1024)) + 'MB'
    elif 1024 * 1024 * 1024 <= size < 1024 * 1024 * 1024 * 1024:
        return '%.1f' % float(size / (1024 * 1024 * 1024)) + 'GB'
    elif 1024 * 1024 * 1024 * 1024 <= size:
        return '%.1f' % float(size / (1024 * 1024 * 1024 * 1024)) + 'TB'


def CheckLoFile(downinfo):
    # print(self.ui.DownPath)
    FileLoPath = downinfo['FilePath'] + downinfo['FileName']
    LoFileSize = 0
    LoFileExist = 0
    if os.path.exists(FileLoPath):
        LoFileSize = os.path.getsize(FileLoPath)
        LoFileExist = 1
    return {'exist': LoFileExist, 'size': LoFileSize}

def FileConChose(fetype):
    if fetype == 'folder':
        return 'img/filecon/foldersm.png'
    if fetype == 'zip':
        return 'img/filecon/zipcon.png'
    if fetype == 'img':
        return 'img/filecon/imgcon.jpg'
    if fetype == 'pdf':
        return 'img/filecon/pdfcon.jpg'
    if fetype == 'ppt':
        return 'img/filecon/pptcon.jpg'
    if fetype == 'exe':
        return 'img/filecon/execon.jpg'
    if fetype == 'excel':
        return 'img/filecon/excelcon.jpg'
    if fetype == 'word':
        return 'img/filecon/wordcon.jpg'
    if fetype == 'html':
        return 'img/filecon/htmlcon.jpg'
    else:
        return 'img/filecon/wj.jfif'

def str_trans_to_md5(src):
    src = src.encode("utf-8")
    myMd5 = hashlib.md5()
    myMd5.update(src)
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest
def getfileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename, "rb")
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()
class TransFinishShowUpdate():
    signal = pyqtSignal()
    def __init__(self,ui):
        super().__init__()
        self.ui = ui
        self.dbManager = DBManager.DBManager()
        self.ClientSetting = self.dbManager.GetClientSetting()
        # self.signal.connect(self.RefreshDowning)
        # self.ButtonBind()
        # self.RefreshDowning()
        self.ui.TranspscrollArea['TranspFinsh'][4].clicked.connect(self.CancelAll)
    def add(self,scrollAreaWidgetContents,DownInfo):
        self.frame_10 = QtWidgets.QFrame(scrollAreaWidgetContents)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.frame_10.setStyleSheet("QFrame#frame_10::hover{background:#D0D3D4;border-radius:22px;}")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem11 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem11)
        self.label_32 = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setMinimumSize(QtCore.QSize(30, 30))
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_7.addWidget(self.label_32)
        self.frame_11 = QtWidgets.QFrame(self.frame_10)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setContentsMargins(0, 8, 0, 8)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.frame_11)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.frame_11)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_5.addWidget(self.label_12)
        self.horizontalLayout_7.addWidget(self.frame_11)
        spacerItem12 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.frame_12 = QtWidgets.QFrame(self.frame_10)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_13 = QtWidgets.QLabel(self.frame_12)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_6.addWidget(self.label_13)
        self.horizontalLayout_7.addWidget(self.frame_12)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem13)
        self.frame_13 = QtWidgets.QFrame(self.frame_10)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_14 = QtWidgets.QLabel(self.frame_13)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_8.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.frame_13)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_8.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.frame_13)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_8.addWidget(self.label_16)
        self.horizontalLayout_7.addWidget(self.frame_13)
        spacerItem14 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem14)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 6)
        self.horizontalLayout_7.setStretch(2, 10)
        self.horizontalLayout_7.setStretch(3, 1)
        self.horizontalLayout_7.setStretch(4, 10)
        self.horizontalLayout_7.setStretch(5, 1)
        self.horizontalLayout_7.setStretch(6, 5)
        self.horizontalLayout_7.setStretch(7, 1)

        LoFile = CheckLoFile(DownInfo)
        LoSize = size_format(LoFile['size'])
        timestamp = float(DownInfo['timestamp'])
        strtime = time.strftime("%Y-%m-%d\n%H:%M:%S", time.localtime(timestamp))
        # strtime = time.strftime("%Y-%m-%d", time.localtime(timestamp))
        self.label_13.setText(strtime)
        if not int(DownInfo['fecheck']):
            self.label_14.setText("文件损坏")
            self.label_14.setStyleSheet("QLabel{color:red;}")

        self.label_32.setText("")
        self.label_32.setPixmap(QtGui.QPixmap(FileConChose(DownInfo['fetype'])))
        self.label_32.setScaledContents(True)
        self.label_32.setMaximumSize(46, 46)
        self.label_11.setText(DownInfo['FileName'])
        self.label_11.setFixedWidth(460)
        self.label_12.setText("{}/{}".format(LoSize,size_format(DownInfo['Size'])))

        self.label_15.setText("X")
        self.label_15.setStyleSheet("QLabel{font-size:26px;font-family:Roman times;padding-right:20px;}"
                           "QLabel:hover{color:rgb(20, 90, 50);}")

        self.label_16.setText("[]")
        self.label_16.setStyleSheet("QLabel{font-size:26px;font-weight:bold;font-family:Roman times;}"
                           "QLabel:hover{color:rgb(20, 90, 50);}")


        self.label_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Downinginfoi = {}
        Downinginfoi = DownInfo
        Downinginfoi['frame'] = self.frame_10
        Downinginfoi['statusLabel'] = self.label_14
        Downinginfoi['LoFileSatus'] = LoFile
        Downinginfoi['LoPath'] = DownInfo['FilePath']+DownInfo['FileName']
        self.label_15.mousePressEvent = partial(self.DelDowing,Downinginfoi)
        self.label_16.mousePressEvent = partial(self.OpenDownFile, Downinginfoi)
        return Downinginfoi
    def DelDowing(self,info,e):
        self.dbManager.DelUserTranspFinshRecord(info['FilePath'],info['FileName'])
        self.Refresh()
    def OpenDownFile(self,info,e):
        Path = info['LoPath'].replace('/','\\')
        os.system(r"explorer /select,{}".format(Path))
    def CancelAll(self):
        for i in self.DownInfos:
            self.dbManager.DelUserTranspFinshRecord(i['FilePath'],i['FileName'])
        self.Refresh()
    def Refresh(self):
        DownLayout = self.ui.TranspscrollArea['TranspFinsh']
        self.DownLayout = DownLayout
        DownformLayout = DownLayout[0]
        DownverticalLayout = DownLayout[1]
        scrollAreaWidgetContents_down = DownLayout[2]
        LaConts = DownverticalLayout.count()
        for i in range(LaConts):
            DownverticalLayout.itemAt(i).widget().deleteLater()
        # dbManager = DBManager.DBManager()
        dbManager = DBManager.DBManager()
        self.DownInfos = dbManager.GetUserTranspFinshRecordAll()
        dbManager.close()
        self.DownLayout[3].setText(str(len(self.DownInfos)))
        # dbManager.close()
        # self.DownInfosUpdateLabs = []
        for i in self.DownInfos:
            Downinginfoi = self.add(scrollAreaWidgetContents_down, i)
            form = Downinginfoi['frame']
            DownverticalLayout.addWidget(form)
            line_3 = QtWidgets.QFrame(scrollAreaWidgetContents_down)
            line_3.setMinimumSize(QtCore.QSize(649, 0))
            line_3.setFrameShape(QtWidgets.QFrame.HLine)
            line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
            line_3.setObjectName("line_3")
            DownverticalLayout.addWidget(line_3)



class TransShowUpdate(QThread):
    signal = pyqtSignal()
    signal1 = pyqtSignal()
    signaladd = pyqtSignal(dict)
    signaladdUp = pyqtSignal(list)
    signalaDelUp = pyqtSignal(dict)
    signalaDelUp1 = pyqtSignal(dict)
    signalaUpdateUpProgress = pyqtSignal(dict,dict)


    signaladdDown = pyqtSignal(list)
    signalaDowndateUpProgress = pyqtSignal(dict,dict)
    signalaDelDown = pyqtSignal(dict)


    def __init__(self,ui):
        super().__init__()
        self.MaxDownNums = 2
        self.DownInfosUpdateLabs = {}
        self.ui = ui
        self.TranspUps = TranspUp.TransUp(self.ui,self.signaladdUp,self.signalaDelUp,self.signalaDelUp1,self.signalaUpdateUpProgress)
        self.DownInfos = []
        self.PriDown = None
        self.ButtonBind()
        self.dbManager = DBManager.DBManager()
        self.dbManager1 = DBManager.DBManager1()
        self.ClientSetting = self.dbManager.GetClientSetting()
        # self.signal.connect(self.RefreshDowning)
        self.signaladdDown.connect(self.AddDowning1)
        self.DownLayout = ui.TranspscrollArea['Down']
        self.signalaDowndateUpProgress.connect(self.UpdateDownProgress)
        self.signalaDelDown.connect(self.DelDownact)



        # self.ButtonBind()
        # self.RefreshDowning()


        self.TransFinishShow = TransFinishShowUpdate(ui)
        self.TransFinishShow.Refresh()
        self.signal1.connect(self.TransFinishShow.Refresh)
        # self.SBCRequest = SBCRequest.SBCRe()
        self.AddDowning()

    def AddUping(self,UpInfos):
        self.TranspUps.AddUping(UpInfos)
        # self.TranspUps.AddUpFiles(UpInfos)

    def FileConChose(self,fetype):
        if fetype == 'folder':
            return 'img/filecon/foldersm.png'
        if fetype == 'zip':
            return 'img/filecon/zipcon.png'
        if fetype == 'img':
            return 'img/filecon/imgcon.jpg'
        if fetype == 'pdf':
            return 'img/filecon/pdfcon.jpg'
        if fetype == 'ppt':
            return 'img/filecon/pptcon.jpg'
        if fetype == 'exe':
            return 'img/filecon/execon.jpg'
        if fetype == 'excel':
            return 'img/filecon/excelcon.jpg'
        if fetype == 'word':
            return 'img/filecon/wordcon.jpg'
        if fetype == 'html':
            return 'img/filecon/htmlcon.jpg'
        else:
            return 'img/filecon/wj.jfif'
    def add(self,scrollAreaWidgetContents,DownInfo):

        self.frame_16 = QtWidgets.QFrame(scrollAreaWidgetContents)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.frame_16.setStyleSheet("QFrame#frame_16::hover{background:#D0D3D4;border-radius:22px;}")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem1 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.label_33 = QtWidgets.QLabel(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setMinimumSize(QtCore.QSize(30, 30))
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_11.addWidget(self.label_33)
        self.frame_17 = QtWidgets.QFrame(self.frame_16)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_10.setContentsMargins(0, 8, 0, 8)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_19 = QtWidgets.QLabel(self.frame_17)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_10.addWidget(self.label_19)
        label_20 = QtWidgets.QLabel(self.frame_17)
        label_20.setObjectName("label_20")
        self.verticalLayout_10.addWidget(label_20)
        self.horizontalLayout_11.addWidget(self.frame_17)
        spacerItem2 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem2)
        self.frame_18 = QtWidgets.QFrame(self.frame_16)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_11.setContentsMargins(0, 15, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        progressBar_4 = QtWidgets.QProgressBar(self.frame_18)
        progressBar_4.setMinimumSize(QtCore.QSize(0, 0))
        progressBar_4.setMaximumSize(QtCore.QSize(16777215, 15))
        # progressBar_4.setProperty("value", 24)
        progressBar_4.setObjectName("progressBar_4")
        self.verticalLayout_11.addWidget(progressBar_4)
        label_21 = QtWidgets.QLabel(self.frame_18)
        label_21.setObjectName("label_21")
        self.verticalLayout_11.addWidget(label_21)
        self.horizontalLayout_11.addWidget(self.frame_18)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.frame_19 = QtWidgets.QFrame(self.frame_16)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_12.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        label_22 = QtWidgets.QLabel(self.frame_19)
        label_22.setObjectName("label_22")
        self.horizontalLayout_12.addWidget(label_22)
        label_23 = QtWidgets.QLabel(self.frame_19)
        label_23.setObjectName("label_23")
        self.horizontalLayout_12.addWidget(label_23)
        label_24 = QtWidgets.QLabel(self.frame_19)
        label_24.setObjectName("label_24")
        self.horizontalLayout_12.addWidget(label_24)
        self.horizontalLayout_11.addWidget(self.frame_19)
        spacerItem4 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 6)
        self.horizontalLayout_11.setStretch(2, 10)
        self.horizontalLayout_11.setStretch(3, 1)
        self.horizontalLayout_11.setStretch(4, 10)
        self.horizontalLayout_11.setStretch(5, 1)
        self.horizontalLayout_11.setStretch(6, 5)
        self.horizontalLayout_11.setStretch(7, 1)

        LoFile = CheckLoFile(DownInfo)
        LoSize = size_format(LoFile['size'])

        progressBar_4.setProperty("value", (LoFile['size']/DownInfo['size'])*100)


        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap(self.FileConChose(DownInfo['fetype'])))
        self.label_33.setScaledContents(True)
        self.label_33.setMaximumSize(46, 46)




        self.label_19.setText(DownInfo['FileName'])
        self.label_19.setFixedWidth(260)
        label_20.setText("{}/{}".format(LoSize,size_format(DownInfo['Size'])))

        label_21.setText("--")
        # print(66,DownInfo)
        if int(DownInfo['isDown']) == 2:
            label_21.setText("等待下载")

        label_22.setText(">")
        # QFrame  # frame_16::hover
        label_22.setStyleSheet("QLabel{font-size:26px;font-weight:bold;font-family:Roman times;}"
                           "#label_22:hover{color:rgb(20, 90, 50);}")

        label_23.setText("X")
        label_23.setStyleSheet("QLabel{font-size:26px;font-family:Roman times;}"
                           "QLabel:hover{color:rgb(20, 90, 50);}")

        label_24.setText("[]")
        label_24.setStyleSheet("QLabel{font-size:26px;font-weight:bold;font-family:Roman times;}"
                           "QLabel:hover{color:rgb(20, 90, 50);}")

        label_23.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        label_22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        label_24.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Downinginfoi = {}
        Downinginfoi = DownInfo
        Downinginfoi['frame'] = self.frame_16
        Downinginfoi['statusButon'] = label_22
        Downinginfoi['statusLabel'] = label_21
        Downinginfoi['progressBar'] = progressBar_4
        Downinginfoi['DownSizeLabel'] = label_20
        Downinginfoi['LoFileSatus'] = LoFile
        Downinginfoi['LoPath'] = DownInfo['FilePath']+DownInfo['FileName']
        self.DownInfosUpdateLabs[str_trans_to_md5(Downinginfoi['LoPath'])] = Downinginfoi

        label_22.mousePressEvent = partial(self.DownSatusChange,Downinginfoi)
        label_23.mousePressEvent = partial(self.DelDown,Downinginfoi)
        label_24.mousePressEvent = partial(self.OpenDownFile, Downinginfoi)
        return Downinginfoi
    def OpenDownFile(self,info,e):
        Path = info['LoPath'].replace('/','\\')
        os.system(r"explorer /select,{}".format(Path))

    def DelDownact(self,info):
        t = threading.Thread(target=self.DelDownact1,args=(info,))
        t.setDaemon(True)
        t.start()
    def DelDownact1(self,info):
        i = info
        infoi = self.DownInfosUpdateLabs[str_trans_to_md5(i['FilePath'] + i['FileName'])]
        self.DownLayout[1].removeWidget(infoi['frame'])
        sip.delete(infoi['frame'])
        self.DownLayout[1].removeWidget(infoi['line'])
        sip.delete(infoi['line'])
        del self.DownInfosUpdateLabs[str_trans_to_md5(i['FilePath'] + i['FileName'])]
    def DelDown(self,info,e=None):
        t = threading.Thread(target=self.DelDown1,args=(info,))
        t.setDaemon(True)
        t.start()
        return
    def DelDown1(self,info,e=None):
        i = info
        infoi = self.DownInfosUpdateLabs[str_trans_to_md5(i['FilePath'] + i['FileName'])]
        self.dbManager1.WSQL(info, 'DelUserDownRecord')
        self.signalaDelDown.emit(info)
        self.DownManger()


    # def UpadateDownFinish(self,info):

    def DownFinsh(self,info):
        dbManager = DBManager.DBManager()
        LofeMd5 = getfileMd5(info['LoPath'])
        RofeMd5 = info['FileMd5']

        queinfo = {}
        if 'shareinfo' in info and info['shareinfo']:
            queinfo = {'shareinfo':info['shareinfo']}
        else:
            queinfo = {'path': info['RoFilePath']}

        try:
            info['statusLabel'].setText("校验文件...")
            RofeMd5_ = self.ui.SBCRe.GetRoFileMd5(json.dumps(queinfo))
            RofeMd5 = RofeMd5_['md5']
        except:
            pass
        if LofeMd5 == RofeMd5:
            info['FeCheck'] = 1
        else:
            info['FeCheck'] = 0
        info['timestamp'] = time.time()     # 当前时间戳
        dbManager.AddUserTranspFinshRecord(info)
        dbManager.close()
        self.signal1.emit()
        time.sleep(0.5)
        self.DelDown(info)
        return
    def DownPause(self,info):
        info['statusButon'].setText(">")
        info['statusLabel'].setText("已暂停")
        self.DownInfosUpdateLabs[str_trans_to_md5(info['FilePath'] + info['FileName'])]['isDown'] = 0
        self.dbManager1.WSQL(info, 'UpdataUserDownRecord',0)
        self.DownManger()
    def DownGon(self,info):
        info['statusButon'].setText("||")
        self.DownInfosUpdateLabs[str_trans_to_md5(info['FilePath'] + info['FileName'])]['isUp'] = 1
        self.dbManager1.WSQL(info, 'UpdataUserDownRecord',1)
        self.Down(info)
        self.DownManger()
    def DownSatusChange(self,info,e):
        dbManager = DBManager.DBManager()
        DownInfoi = dbManager.GetUserDownRecord(info['FilePath'], info['FileName'])
        if DownInfoi and int(DownInfoi['isDown'])==1:
            self.DownPause(info)
        else:
            self.DownGon(info)
    def StartAll1(self):
        DownInfosUpdateLabs = {}
        infos = []
        for i in self.DownInfosUpdateLabs:
            DownInfosUpdateLabs[i] = self.DownInfosUpdateLabs[i]
        for keyi in DownInfosUpdateLabs:
            i = DownInfosUpdateLabs[keyi]
            infos.append(i)
            i['statusButon'].setText(">")
            i['statusLabel'].setText("等待下载")
            self.DownInfosUpdateLabs[str_trans_to_md5(i['FilePath'] + i['FileName'])]['isDown'] = 2
        self.dbManager1.WSQL(infos, 'UpdataUserDownRecords',2)
        self.DownManger()
    def StartAll(self):
        t = threading.Thread(target=self.StartAll1)
        t.setDaemon(True)
        t.start()

    def PauseAll1(self):
        DownInfosUpdateLabs={}
        infos = []
        for i in self.DownInfosUpdateLabs:
            DownInfosUpdateLabs[i] = self.DownInfosUpdateLabs[i]
        try:
            for keyi in DownInfosUpdateLabs:
                i = DownInfosUpdateLabs[keyi]
                infos.append(i)
                i['statusButon'].setText(">")
                i['statusLabel'].setText("已暂停")
                self.DownInfosUpdateLabs[str_trans_to_md5(i['FilePath'] + i['FileName'])]['isDown'] = 0
            # self.dbManager1.setUpPar(0, 0, 0)
            self.dbManager1.WSQL(infos, 'UpdataUserDownRecords',0)
        except Exception as e:
            print('PauseError',e)
    def PauseAll(self):
        t = threading.Thread(target=self.PauseAll1)
        t.setDaemon(True)
        t.start()
        # dbManager = DBManager.DBManager()
        # DownInfos = dbManager.GetUserDownRecordAll()
        # for i in DownInfos:
        #     self.DownCancel(i)
        # dbManager.close()

    def CancelAll1(self):
        infos = []
        DownInfosUpdateLabs={}
        for i in self.DownInfosUpdateLabs:
            DownInfosUpdateLabs[i] = self.DownInfosUpdateLabs[i]

        for keyi in DownInfosUpdateLabs:
            i = DownInfosUpdateLabs[keyi]
            infos.append(i)
            infoi = DownInfosUpdateLabs[str_trans_to_md5(i['FilePath'] + i['FileName'])]
            # print('Finsh', info['FileName'])
            # UpLayout = self.ui.TranspscrollArea['Up']
            # infoi['frame'].setParent(None)
            # infoi['line'].setParent(None)
            self.DownLayout[1].removeWidget(infoi['frame'])
            sip.delete(infoi['frame'])
            self.DownLayout[1].removeWidget(infoi['line'])
            sip.delete(infoi['line'])
        self.dbManager1.WSQL(infos,'DelUserDownRecords')
        self.DownInfosUpdateLabs = {}
        self.DownLayout[3].setText(str(0))
    def CancelAll(self):
        t = threading.Thread(target=self.CancelAll1)
        t.setDaemon(True)
        t.start()
    def ButtonBind(self):
        self.DownLayout = self.ui.TranspscrollArea['Down']
        self.DownLayout[4].clicked.connect(self.StartAll)
        self.DownLayout[5].clicked.connect(self.PauseAll)
        self.DownLayout[6].clicked.connect(self.CancelAll)
    def UpdateDownProgress(self,Labelinfo,info):
        # return
        try:
            # Labelinfo['statusButon'].setEnabled(False)
            Labelinfo['progressBar'].setProperty("value",info['bar'])
            Labelinfo['DownSizeLabel'].setText(
                "{}/{}".format(size_format(info['CurFileSize']),size_format(info['FileTotSize'])))
            Labelinfo['statusLabel'].setText("{}/S".format(info['Speed']))
        except Exception as e:
            print('UpdateProgessError',e)
    def Downact(self,info):
        dbManager = DBManager.DBManager()
        DownInfoi = dbManager.GetUserDownRecord(info['FilePath'], info['FileName'])
        if DownInfoi and int(DownInfoi['isDown'])==1:
        # if int(info['isDown']):
            info['statusButon'].setText("||")
            LoFileSatus = CheckLoFile(info)
            # LoFileSatus = info['LoFileSatus']
            LoFileSize = LoFileSatus['size']
            RoFileSize = info['Size']
            shareinfo = None
            if LoFileSize >= RoFileSize:
                self.DownFinsh(info)
            else:
                if 'shareinfo' in info:
                    shareinfo = info['shareinfo']
                downinfo = {
                    'fename':info['FileName'],
                    'fepath':info['RoFilePath'],
                    'feseek':LoFileSize,
                    'shareinfo': shareinfo
                }
                # {'fename': 'Surface_ne1.m', 'fepath': 'D:/SBC/SBCUsers/2290227486@qq.com/Surface_ne1.m', 'feseek': 0}
                data = {
                    'downinfo':downinfo
                }
                url_fileDown = 'http://'+self.ClientSetting['host']+'/FileDown1/'
                # dbManager = DBManager.DBManager()
                r = requests.post(url_fileDown,data=json.dumps(data),headers=self.ui.SBCRe.headers,stream=True)
                with open(info['LoPath'], 'ab') as f:
                    t0 = time.time()
                    # for chunk1 in r.iter_content(chunk_size=1*1024*1024):
                    #     print(66,len(chunk1))
                    for chunk in r.iter_content(chunk_size=1024*1024):
                        DownInfoi = dbManager.GetUserDownRecord(info['FilePath'],info['FileName'])
                        if DownInfoi and int(DownInfoi['isDown'])==1:
                            DownSpeed = 0
                            if chunk:

                                f.write(chunk)
                                LoFileSize += len(chunk)
                                deltat = time.time()-t0
                                t0 = time.time()
                                if deltat ==0:
                                    deltat = 0.001
                                DownSpeed = len(chunk)/deltat
                                progressinfo = {'bar': (LoFileSize/RoFileSize)*100, 'CurFileSize': LoFileSize,
                                                'FileTotSize': RoFileSize, 'Speed': size_format(DownSpeed)}
                                self.signalaDowndateUpProgress.emit(info, progressinfo)
                        else:
                            # self.DownCancel(info)
                            break
                if LoFileSize >= RoFileSize:
                    self.DownFinsh(info)
        dbManager.close()
    def Down(self,info):
        print('Down',info)
        Path = info['LoPath']
        LoFileSatus = info['LoFileSatus']
        LoFileSize = LoFileSatus['size']
        LoFileExist = LoFileSatus['exist']
        # print(info)
        if not os.path.isdir(info['FilePath']):
            os.makedirs(info['FilePath'])
        # qmut_1.lock()
        t = threading.Thread(target=self.run1, args=(info,))
        t.setDaemon(True)
        t.start()
        self.info = info
            # self.start()
            # qmut_1.unlock()
    def run1(self,info):
        # return
        self.Downact(info)
    def AddDowning(self,DownInfos=None):
        if not DownInfos:
            DownInfos = self.dbManager.GetUserDownRecordAll()
        self.signaladdDown.emit(DownInfos)
    def WSQL(self,info):
        self.dbManager1.WSQL(info, 'AddUserDownRecords')
        DownLayout = self.ui.TranspscrollArea['Down']
        DownLayout[3].setText(str(len(info)))
        self.DownManger()
    def DownManger(self):
        qmut_1.lock()
        self.DownManger1()
        qmut_1.unlock()
    def DownManger1(self):
        # return
        dbManager = DBManager.DBManager()
        DownInfos = dbManager.GetUserDownRecordAll()
        # self.DownLayout[3].setText(str(len(DownInfos)))
        CurDownNums = 0
        MaxDownNums = self.MaxDownNums
        WaitDown = []
        CurDown = []
        DelDown = []
        for i in DownInfos:
            if int(i['isDown'])==1:
                CurDownNums += 1
                CurDown.append(i)
            elif int(i['isDown']) == 2:
                WaitDown.append(i)
            elif int(i['isDown']) == 3:
                DelDown.append(i)
        for i in DelDown:
            # print('Del',i['FileName'])
            infoi = self.DownInfosUpdateLabs[str_trans_to_md5(i['FilePath'] + i['FileName'])]
            self.dbManager1.WSQL(i,'DelUserDownRecord')
            self.DownLayout[1].removeWidget(infoi['frame'])
            sip.delete(infoi['frame'])
            self.DownLayout[1].removeWidget(infoi['line'])
            sip.delete(infoi['line'])
            # QApplication.processEvents()

            # print('Del1', i['FileName'])
            del self.DownInfosUpdateLabs[str_trans_to_md5(i['FilePath'] + i['FileName'])]
        DownInfos = dbManager.GetUserDownRecordAll()
        self.DownLayout[3].setText(str(len(DownInfos)))
        dbManager.close()
        if CurDownNums < MaxDownNums:
            for i in range(MaxDownNums-CurDownNums):
                if i < len(WaitDown):
                    info = WaitDown[i]
                    self.dbManager1.WSQL(info,'UpdataUserDownRecord',1)
                    infoi = self.DownInfosUpdateLabs[str_trans_to_md5(info['FilePath'] + info['FileName'])]
                    self.Down(infoi)
        if CurDownNums > MaxDownNums:
            for i in CurDown:
                if CurDownNums > MaxDownNums:
                    self.dbManager1.WSQL(i, 'UpdataUserDownRecord',2)
                    infoi = self.DownInfosUpdateLabs[str_trans_to_md5(i['FilePath'] + i['FileName'])]
                    infoi['statusButon'].setText(">")
                    infoi['statusLabel'].setText("等待上传")
                    CurDownNums -= 1
        # dbManager.close()
    def AddDowning1(self,DownInfos):

        FilesSQL = []
        for DownInfo in DownInfos:
            DownInfoExist = self.dbManager.GetUserDownRecord(DownInfo['FilePath'],DownInfo['FileName'])
            if not DownInfoExist or 'statusButon' not in DownInfo:
                DownInfo['size'] = DownInfo['Size']
                DownverticalLayout = self.DownLayout[1]
                scrollAreaWidgetContents_Down = self.DownLayout[2]
                if 'isDown' not in DownInfo:
                    DownInfo['isDown'] = 2
                DownInfos = self.dbManager.GetUserDownRecordAll()
                self.DownLayout[3].setText(str(len(DownInfos)))
                Downinginfoi = self.add(scrollAreaWidgetContents_Down,DownInfo)
                form = Downinginfoi['frame']
                DownverticalLayout.addWidget(form)
                line_3 = QtWidgets.QFrame(scrollAreaWidgetContents_Down)
                line_3.setMinimumSize(QtCore.QSize(649, 0))
                line_3.setFrameShape(QtWidgets.QFrame.HLine)
                line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
                line_3.setObjectName("line_3")
                DownverticalLayout.addWidget(line_3)
                self.DownInfosUpdateLabs[str_trans_to_md5(DownInfo['FilePath'] + DownInfo['FileName'])]['line'] = line_3
                if not DownInfoExist:
                    FilesSQL.append(DownInfo)
            # QApplication.processEvents()
            # print(DownInfo)

        if FilesSQL:
            # pass

            self.WSQLDownThread = threading.Thread(target=self.WSQL,args=(FilesSQL,))
            self.WSQLDownThread.setDaemon(True)
            self.WSQLDownThread.start()

            # self.ui.MainWindow.WSQLDownThread = WSQLThread(self.ui,FilesSQL,self.dbManager1)
            # self.ui.MainWindow.WSQLDownThread.Signal.connect(self.DowndateDOwnNums)
            # # self.ui.MainWindow.WSQLDownThread.Signal.connect(self.DownManger)
            # self.ui.MainWindow.WSQLDownThread.start()
        else:
            self.DownManger()