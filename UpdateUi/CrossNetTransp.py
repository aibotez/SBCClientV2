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





def str_trans_to_md5(src):
    src = src.encode("utf-8")
    myMd5 = hashlib.md5()
    myMd5.update(src)
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest
class CrossTransShowUpdate(QThread):
    signaladdTran = pyqtSignal(list)
    def __init__(self,ui):
        super().__init__()
        self.MaxTranspNums = 2
        self.TranspInfosUpdateLabs = {}
        self.ui = ui
        self.TranLayout = ui.TranspscrollArea['CrossTran']
        self.signaladdTran.connect(self.AddTransping1)
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

        # LoFile = CheckLoFile(DownInfo)
        # LoSize = size_format(LoFile['size'])

        # progressBar_4.setProperty("value", (LoFile['size']/DownInfo['size'])*100)


        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap(self.FileConChose(DownInfo['fetype'])))
        self.label_33.setScaledContents(True)
        self.label_33.setMaximumSize(46, 46)




        self.label_19.setText(DownInfo['FileName'])
        self.label_19.setFixedWidth(260)
        # label_20.setText("{}/{}".format(LoSize,size_format(DownInfo['Size'])))

        label_21.setText("--")
        # print(66,DownInfo)
        if int(DownInfo['isTran']) == 2:
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
        # Downinginfoi['LoFileSatus'] = LoFile
        Downinginfoi['LoPath'] = DownInfo['FilePath']+DownInfo['FileName']
        self.TranspInfosUpdateLabs[str_trans_to_md5(Downinginfoi['LoPath'])] = Downinginfoi

        # label_22.mousePressEvent = partial(self.DownSatusChange,Downinginfoi)
        # label_23.mousePressEvent = partial(self.DelDown,Downinginfoi)
        # label_24.mousePressEvent = partial(self.OpenDownFile, Downinginfoi)
        return Downinginfoi



    def Downact(self,info):
        chunk_size = 400 * 1024
        heades = {'User-Agent': 'netdisk;P2SP;3.0.0.127','Connection': 'Keep - Alive','Host': 'bdcm01.baidupcs.com'}

        heades['Range'] = 'bytes={}-{}'.format(str(0), str(1024))
        with requests.get(FileInfo['url'],headers=heades,stream=True) as req:
            for chunk in req.iter_content(chunk_size=chunk_size):
                if chunk:
                    print(len(chunk))
                    yield chunk
                else:
                    print(chunk)
                    break
    def Downact1(self,info):
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
                url_fileDown = 'http://'+self.ui.host+'/FileDown1/'
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


    def AddTransping(self,TranspInfos=None):
        print(TranspInfos)

        if not TranspInfos:
            TranspInfos = self.dbManager.GetUserDownRecordAll()
        self.signaladdTran.emit(TranspInfos)

    def AddTransping1(self,TranspInfos):

        FilesSQL = []
        for TranInfo in TranspInfos:
            TranInfoExist =0
            # TranInfoExist = self.dbManager.GetUserDownRecord(TranInfo['FilePath'],TranInfo['FileName'])
            if not TranInfoExist or 'statusButon' not in TranInfo:
                if 'size' not in TranInfo:
                    TranInfo['size'] = TranInfo['Size']
                TranverticalLayout = self.TranLayout[1]
                scrollAreaWidgetContents_Tran = self.TranLayout[2]
                if 'isTran' not in TranInfo:
                    TranInfo['isTran'] = 2
                # TranspInfos = self.dbManager.GetUserDownRecordAll()
                # self.TranLayout[3].setText(str(len(TranspInfos)))
                Traninginfoi = self.add(scrollAreaWidgetContents_Tran,TranInfo)
                form = Traninginfoi['frame']
                TranverticalLayout.addWidget(form)
                line_3 = QtWidgets.QFrame(scrollAreaWidgetContents_Tran)
                line_3.setMinimumSize(QtCore.QSize(649, 0))
                line_3.setFrameShape(QtWidgets.QFrame.HLine)
                line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
                line_3.setObjectName("line_3")
                TranverticalLayout.addWidget(line_3)
                self.TranspInfosUpdateLabs[str_trans_to_md5(TranInfo['FilePath'] + TranInfo['FileName'])]['line'] = line_3
                if not TranInfoExist:
                    FilesSQL.append(TranInfo)
            # QApplication.processEvents()
            # print(TranInfo)

        # if FilesSQL:
        #     # pass
        #
        #     self.WSQLDownThread = threading.Thread(target=self.WSQL,args=(FilesSQL,))
        #     self.WSQLDownThread.setDaemon(True)
        #     self.WSQLDownThread.start()

            # self.ui.MainWindow.WSQLDownThread = WSQLThread(self.ui,FilesSQL,self.dbManager1)
            # self.ui.MainWindow.WSQLDownThread.Signal.connect(self.DowndateDOwnNums)
            # # self.ui.MainWindow.WSQLDownThread.Signal.connect(self.DownManger)
            # self.ui.MainWindow.WSQLDownThread.start()
        # else:
        #     self.DownManger()