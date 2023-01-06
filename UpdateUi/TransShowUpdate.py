import sys,threading,os
sys.path.append('..')
from pack import DBManager
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont

class TransShowUpdate():
    def __init__(self,ui):
        self.ui = ui
        self.DownInfos = []
        self.dbManager = DBManager.DBManager()

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
        self.label_20 = QtWidgets.QLabel(self.frame_17)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_10.addWidget(self.label_20)
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
        self.progressBar_4 = QtWidgets.QProgressBar(self.frame_18)
        self.progressBar_4.setMinimumSize(QtCore.QSize(0, 0))
        self.progressBar_4.setMaximumSize(QtCore.QSize(16777215, 15))
        # self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setObjectName("progressBar_4")
        self.verticalLayout_11.addWidget(self.progressBar_4)
        self.label_21 = QtWidgets.QLabel(self.frame_18)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_11.addWidget(self.label_21)
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
        self.label_22 = QtWidgets.QLabel(self.frame_19)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_12.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.frame_19)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_12.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.frame_19)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_12.addWidget(self.label_24)
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

        self.progressBar_4.setProperty("value", (LoFile['size']/DownInfo['Size'])*100)


        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap(self.FileConChose(DownInfo['fetype'])))
        self.label_33.setScaledContents(True)
        self.label_33.setMaximumSize(46, 46)




        self.label_19.setText(DownInfo['FileName'])
        self.label_19.setFixedWidth(260)
        self.label_20.setText("{}/{}".format(LoSize,self.size_format(DownInfo['Size'])))
        self.label_21.setText("暂停")
        self.label_22.setText(">")
        self.label_22.setStyleSheet("QLabel{font-size:26px;font-weight:bold;font-family:Roman times;}"
                           "QLabel:hover{color:rgb(20, 90, 50);}")

        self.label_23.setText("X")
        self.label_23.setStyleSheet("QLabel{font-size:26px;font-family:Roman times;}"
                           "QLabel:hover{color:rgb(20, 90, 50);}")

        self.label_24.setText("[]")
        self.label_24.setStyleSheet("QLabel{font-size:26px;font-weight:bold;font-family:Roman times;}"
                           "QLabel:hover{color:rgb(20, 90, 50);}")



        # self.label_23.setText("")
        # self.label_23.setMaximumSize(20,20)
        # self.label_23.setPixmap(QtGui.QPixmap('./img/del1.png'))
        # self.label_23.setScaledContents(True)
        # self.label_22.setText("")
        # self.label_22.setMaximumSize(22,23)
        # self.label_22.setPixmap(QtGui.QPixmap('./img/start1.png'))
        # self.label_22.setScaledContents(True)
        # self.label_22.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 2px;")


        # self.label_23.setStyleSheet("border:1px groove gray;border-radius:10px;padding:0px 0px;")

        self.label_23.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_24.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        Downinginfoi = {}
        Downinginfoi['frame'] = self.frame_16
        Downinginfoi['status'] = self.label_22
        Downinginfoi['progressBar'] = self.progressBar_4
        Downinginfoi['DownSize'] = self.label_20
        Downinginfoi['FilePath'] = DownInfo['FilePath']
        Downinginfoi['FileName'] = DownInfo['FileName']
        Downinginfoi['LoPath'] = DownInfo['FilePath']+DownInfo['FileName']
        self.label_23.mousePressEvent = partial(self.DelDowing,Downinginfoi)
        self.label_24.mousePressEvent = partial(self.OpenDownFile, Downinginfoi)
        return Downinginfoi

    def OpenDownFile(self,info,e):
        Path = info['LoPath']
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
        DownLayout = self.ui.TranspscrollArea['Down']
        self.DownLayout = DownLayout
        DownformLayout = DownLayout[0]
        DownverticalLayout = DownLayout[1]
        scrollAreaWidgetContents_down = DownLayout[2]
        LaConts = DownverticalLayout.count()
        for i in range(LaConts):
            DownverticalLayout.itemAt(i).widget().deleteLater()
        self.DownInfos = self.dbManager.GetUserDownRecordAll()
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

