import sys,threading,os,hashlib,requests,json
import time

sys.path.append('..')
from pack import DBManager
# from pack import SBCRequest
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QThread,QMutex
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont
import threading

qmut_1 = QMutex()


class ThreadUpdate(QThread):
    signal = pyqtSignal()
    def __init__(self,ui):
        super().__init__()
        self.ui = ui
        self.dbManager = DBManager.DBManager()
        self.ClientSetting = self.dbManager.GetClientSetting()
        self.signal.connect(self.UpdateDowning)

    def size_format(self,size):
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

    def setPar(self,par):
        self.info = par

    def UpdateDowning(self):
        self.info['progressBar'].setProperty("value", (self.LoFileSize/self.RoFileSize)*100)
        self.info['DownSizeLabel'].setText("{}/{}".format(self.size_format(self.LoFileSize),self.size_format(self.RoFileSize)))
        self.info['statusLabel'].setText("{}/S".format(self.size_format(self.DownSpeed)))
    def Downact(self,info):

        if int(info['isDown']):
            info['statusButon'].setText("||")
            LoFileSatus = info['LoFileSatus']
            LoFileSize = LoFileSatus['size']
            RoFileSize = info['Size']

            if LoFileSize >= RoFileSize:
                pass
                # self.DownFinsh(info)
            else:

                downinfo = {
                    'fename':info['FileName'],
                    'fepath':info['RoFilePath'],
                    'feseek':LoFileSize
                }
                data = {
                    'downinfo':downinfo
                }
                url_fileDown = 'http://'+self.ClientSetting['host']+'/FileDown1/'
                dbManager = DBManager.DBManager()

                r = requests.post(url_fileDown,data=json.dumps(data),headers=self.ui.SBCRe.headers,stream=True)
                with open(info['LoPath'], 'ab') as f:
                    t0 = time.time()
                    # for chunk1 in r.iter_content(chunk_size=1*1024*1024):
                    #     print(66,len(chunk1))
                    for chunk in r.iter_content(chunk_size=2*1024*1024):
                        # DownInfoi = dbManager.GetUserDownRecord(info['FilePath'],info['FileName'])
                        # if int(DownInfoi['isDown']):
                        s = 1
                        if s:
                            DownSpeed = 0
                            if chunk:

                                f.write(chunk)
                                LoFileSize += len(chunk)
                                deltat = time.time()-t0
                                t0 = time.time()
                                if deltat ==0:
                                    deltat = 0.001
                                DownSpeed = len(chunk)/deltat
                                self.DownSpeed = DownSpeed
                                self.LoFileSize = LoFileSize
                                self.RoFileSize = RoFileSize
                                self.signal.emit()
                                # info['progressBar'].setProperty("value", (LoFileSize/RoFileSize)*100)
                                # info['DownSizeLabel'].setText("{}/{}".format(self.size_format(LoFileSize),self.size_format(RoFileSize)))
                                # info['statusLabel'].setText("{}/S".format(self.size_format(DownSpeed)))

                            # if LoFileSize >= RoFileSize:
                            #     self.DownFinsh(info)

                        else:
                            # self.DownCancel(info)
                            break

    def Down(self,info):
        #
        # info = self.info
        Path = info['LoPath']
        LoFileSatus = info['LoFileSatus']
        LoFileSize = LoFileSatus['size']
        LoFileExist = LoFileSatus['exist']
        if int(info['isDown']):
            if not os.path.isdir(info['FilePath']):
                os.makedirs(info['FilePath'])
            # qmut_1.lock()

            t = threading.Thread(target=self.run1,args=(info,))
            t.setDaemon(True)
            t.start()
            # self.start()

            # qmut_1.unlock()
    def run1(self,info):
        # print(66)
        self.info = info
        self.Downact(info)

class TransShowUpdate(QThread):
    signal = pyqtSignal()
    def __init__(self,ui):
        super().__init__()
        self.ui = ui
        self.DownInfos = []
        self.dbManager = DBManager.DBManager()
        self.ClientSetting = self.dbManager.GetClientSetting()
        self.signal.connect(self.RefreshDowning)
        # self.SBCRequest = SBCRequest.SBCRe()

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
    def add1(self,scrollAreaWidgetContents,DownInfo):
        self.frame_16 = QtWidgets.QFrame(scrollAreaWidgetContents)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
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

        LoFile = self.CheckLoFile(DownInfo)
        LoSize = self.size_format(LoFile['size'])

        progressBar_4.setProperty("value", (LoFile['size']/DownInfo['Size'])*100)


        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap(self.FileConChose(DownInfo['fetype'])))
        self.label_33.setScaledContents(True)
        self.label_33.setMaximumSize(46, 46)




        self.label_19.setText(DownInfo['FileName'])
        self.label_19.setFixedWidth(260)
        label_20.setText("{}/{}".format(LoSize,self.size_format(DownInfo['Size'])))
        label_21.setText("--")
        label_22.setText(">")
        label_22.setStyleSheet("QLabel{font-size:26px;font-weight:bold;font-family:Roman times;}"
                           "QLabel:hover{color:rgb(20, 90, 50);}")

        label_23.setText("X")
        label_23.setStyleSheet("QLabel{font-size:26px;font-family:Roman times;}"
                           "QLabel:hover{color:rgb(20, 90, 50);}")

        label_24.setText("[]")
        label_24.setStyleSheet("QLabel{font-size:26px;font-weight:bold;font-family:Roman times;}"
                           "QLabel:hover{color:rgb(20, 90, 50);}")



        # label_23.setText("")
        # label_23.setMaximumSize(20,20)
        # label_23.setPixmap(QtGui.QPixmap('./img/del1.png'))
        # label_23.setScaledContents(True)
        # label_22.setText("")
        # label_22.setMaximumSize(22,23)
        # label_22.setPixmap(QtGui.QPixmap('./img/start1.png'))
        # label_22.setScaledContents(True)
        # label_22.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 2px;")


        # label_23.setStyleSheet("border:1px groove gray;border-radius:10px;padding:0px 0px;")

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
        # Downinginfoi['FilePath'] = DownInfo['FilePath']
        # Downinginfoi['FileName'] = DownInfo['FileName']
        # Downinginfoi['isDown'] = DownInfo['isDown']
        # Downinginfoi['size'] = DownInfo['Size']
        # Downinginfoi['RoFilePath'] = DownInfo['RoFilePath']
        Downinginfoi['LoFileSatus'] = LoFile
        Downinginfoi['LoPath'] = DownInfo['FilePath']+DownInfo['FileName']
        label_22.mousePressEvent = partial(self.DownSatusChange,Downinginfoi)
        label_23.mousePressEvent = partial(self.DelDowing,Downinginfoi)
        label_24.mousePressEvent = partial(self.OpenDownFile, Downinginfoi)
        return Downinginfoi

    def getfileMd5(self,filename):
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

    def DownFinsh(self,info):
        dbManager = DBManager.DBManager()
        info['statusLabel'].setText("校验文件...")
        LofeMd5 = self.getfileMd5(info['LoPath'])
        RofeMd5 = info['FileMd5']
        if LofeMd5 == RofeMd5:
            info['statusLabel'].setText("校验通过")
            print('校验通过')
        else:
            info['statusLabel'].setText("文件损坏")
        dbManager.DelUserDownRecord(info['FilePath'],info['FileName'])
        self.signal.emit()


    def DownCancel(self,info):
        self.signal.emit()
    def DownSatusChange(self,info,e):
        dbManager = DBManager.DBManager()
        if int(info['isDown']):
            info['statusButon'].setText(">")
            dbManager.UpdataUserDownRecord(info['FilePath'],info['FileName'],0)
        else:
            info['statusButon'].setText("||")
            dbManager.UpdataUserDownRecord(info['FilePath'], info['FileName'], 1)
        self.signal.emit()

    def Downact(self,info):
        if int(info['isDown']):
            info['statusButon'].setText("||")
            LoFileSatus = info['LoFileSatus']
            LoFileSize = LoFileSatus['size']
            RoFileSize = info['Size']
            if LoFileSize >= RoFileSize:
                self.DownFinsh(info)
            else:
                downinfo = {
                    'fename':info['FileName'],
                    'fepath':info['RoFilePath'],
                    'feseek':LoFileSize
                }
                data = {
                    'downinfo':downinfo
                }
                url_fileDown = 'http://'+self.ClientSetting['host']+'/FileDown1/'
                dbManager = DBManager.DBManager()
                r = requests.post(url_fileDown,data=json.dumps(data),headers=self.ui.SBCRe.headers,stream=True)
                with open(info['LoPath'], 'ab') as f:
                    t0 = time.time()
                    # for chunk1 in r.iter_content(chunk_size=1*1024*1024):
                    #     print(66,len(chunk1))
                    for chunk in r.iter_content(chunk_size=2*1024*1024):
                        DownInfoi = dbManager.GetUserDownRecord(info['FilePath'],info['FileName'])
                        if int(DownInfoi['isDown']):
                            DownSpeed = 0
                            if chunk:

                                f.write(chunk)
                                LoFileSize += len(chunk)
                                deltat = time.time()-t0
                                t0 = time.time()
                                if deltat ==0:
                                    deltat = 0.001
                                DownSpeed = len(chunk)/deltat
                                try:
                                    info['progressBar'].setProperty("value", (LoFileSize/RoFileSize)*100)
                                    info['DownSizeLabel'].setText("{}/{}".format(self.size_format(LoFileSize),self.size_format(RoFileSize)))
                                    info['statusLabel'].setText("{}/S".format(self.size_format(DownSpeed)))
                                except Exception as e:
                                    print(e)
                                    print(info)

                            if LoFileSize >= RoFileSize:
                                self.DownFinsh(info)

                        else:
                            # self.DownCancel(info)
                            break

    def Down(self,info):
        Path = info['LoPath']
        LoFileSatus = info['LoFileSatus']
        LoFileSize = LoFileSatus['size']
        LoFileExist = LoFileSatus['exist']
        if int(info['isDown']):
            if not os.path.isdir(info['FilePath']):
                os.makedirs(info['FilePath'])
            # qmut_1.lock()
            self.info=info
            self.start()
            # qmut_1.unlock()
    def run(self):
        # return
        self.Downact(self.info)





    def OpenDownFile(self,info,e):
        Path = info['LoPath'].replace('/','\\')
        print(Path)
        os.system(r"explorer /select,{}".format(Path))

    def size_format(self,size):
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
    def CheckLoFile(self,downinfo):
        # print(self.ui.DownPath)
        FileLoPath = downinfo['FilePath']+downinfo['FileName']
        LoFileSize = 0
        LoFileExist = 0
        if os.path.exists(FileLoPath):
            LoFileSize = os.path.getsize(FileLoPath)
            LoFileExist = 1
        return {'exist':LoFileExist,'size':LoFileSize}

    def DelDowing(self,info,e):
        self.dbManager.DelUserDownRecord(info['FilePath'],info['FileName'])
        self.RefreshDowning()

        # j=0
        # for i in self.DownInfos:
        #     if i['FilePath']+i['FileName'] == info['LoPath']:
        #         DownverticalLayout = self.DownLayout[1]
        #         DownverticalLayout.itemAt(j).widget().deleteLater()
        #         break
        #     j+=1
        # del self.DownInfos[j]

    def RefreshDowning(self):
        self.infos = []

        DownLayout = self.ui.TranspscrollArea['Down']
        self.DownLayout = DownLayout
        DownformLayout = DownLayout[0]
        DownverticalLayout = DownLayout[1]
        scrollAreaWidgetContents_down = DownLayout[2]
        LaConts = DownverticalLayout.count()
        # for i in range(LaConts):
        #     DownverticalLayout.itemAt(i).widget().deleteLater()

        # dbManager = DBManager.DBManager()
        self.DownInfos = self.dbManager.GetUserDownRecordAll()
        # dbManager.close()

        self.DownInfosUpdateLabs = []
        for i in self.DownInfos:
            Downinginfoi = self.add1(scrollAreaWidgetContents_down,i)
            self.DownInfosUpdateLabs.append(Downinginfoi)
            form = Downinginfoi['frame']
            DownverticalLayout.addWidget(form)
            line_3 = QtWidgets.QFrame(scrollAreaWidgetContents_down)
            line_3.setMinimumSize(QtCore.QSize(649, 0))
            line_3.setFrameShape(QtWidgets.QFrame.HLine)
            line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
            line_3.setObjectName("line_3")
            DownverticalLayout.addWidget(line_3)
            ThreadUpdatei = ThreadUpdate(self.ui)
            # # ThreadUpdatei.setPar(Downinginfoi)
            ThreadUpdatei.Down(Downinginfoi)
            # self.Down(Downinginfoi)



# myLayout.count()
    def AddDown(self,DownInfo):
        self.RefreshDowning()
        # self.ui.TranspscrollAreaformLayout.itemAt(0).widget().deleteLater()
        DownLayout = self.ui.TranspscrollArea['Down']
        self.DownLayout = DownLayout
        DownformLayout = DownLayout[0]
        DownverticalLayout = DownLayout[1]
        scrollAreaWidgetContents_down = DownLayout[2]
        # DownverticalLayout.itemAt(0).widget().deleteLater()
        # DownverticalLayout.itemAt(0).widget().deleteLater()

        if DownInfo not in self.DownInfos:
            self.DownInfos.append(DownInfo)
            Downinginfoi = self.add1(scrollAreaWidgetContents_down, DownInfo)
            form = Downinginfoi['frame']
            DownverticalLayout.addWidget(form)
        # for i in range(10):
        #     # self.line_3 = QtWidgets.QFrame(scrollAreaWidgetContents_down)
        #     # self.line_3.setMinimumSize(QtCore.QSize(649, 0))
        #     # self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        #     # self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        #     # self.line_3.setObjectName("line_3")
        #     Downinginfoi = self.add1(scrollAreaWidgetContents_down)
        #     form = Downinginfoi['frame']
        #     DownverticalLayout.addWidget(form)
        #     # DownverticalLayout.addWidget(self.line_3)

