
import sys
sys.path.append('..')
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QThread
import SBCMainWindow
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtCore import *
import base64
from pack import SBCRequest







class ClickEventDeals():
    def __init__(self):
        pass
    def DownDeal(self,e):
        pass
    def UpDeal(self,e):
        pass
    def ReameDeal(self,e):
        pass
    def MoreDeal(self,e):
        pass
    def ChooseNetDeal(self,e):
        pass
    def SearchDeal(self,e):
        pass
    def NetBackDeal(self,e):
        pass
    def NetRefresh(self,e):
        pass



    def FileClickDeal(self,FileInfo,e):
        if e.buttons() == QtCore.Qt.LeftButton:
            self.FileLeftDeal(FileInfo)
        elif e.buttons() == QtCore.Qt.RightButton:
            self.FileRightDeal(FileInfo)
    def FileLeftDeal(self,FileInfo):
        print('FileLeft',FileInfo)
        # SBCM.FileShow(FileInfo['fepath'])

    def FileRightDeal(self,FileInfo):
        print("右")
        # SBCM.FileShow('/home/')
class Ui_PhotoShow(QThread):
    signal = pyqtSignal()
    def __init__(self,ui):
        super().__init__()
        self.MainWindow= ui
        self.signal.connect(self.ScrollContentUpdate)
        self.ClickEventDeals = ClickEventDeals()
        self.Thread_LoadImg = Thread_LoadImg()
        self.path = '/home/'

    def FileClickDeal(self,FileInfo,e):
        if e.buttons() == QtCore.Qt.LeftButton:
            self.FileLeftDeal(FileInfo)
        elif e.buttons() == QtCore.Qt.RightButton:
            self.FileRightDeal(FileInfo)
    def FileLeftDeal(self,FileInfo):
        print('FileLeft',FileInfo)
        self.FileShow1(FileInfo['fepath'])

    def FileRightDeal(self,FileInfo):
        print("右")
        # SBCM.FileShow('/home/')

    def FileShow1(self,path):
        self.path = path

        if self.isRunning():
            self.wait()
        self.start()

    def InitFileShow(self):
        frame = {'frame':self.MainWindow.frame_12,'scrollArea':self.MainWindow.scrollArea}
        return frame

    def InitShow(self):
        # self.centralwidget = self.MainWindow.centralwidget
        self.frame_PhotoShow = QtWidgets.QFrame(self.MainWindow.frame_14)
        self.frame_PhotoShow.setGeometry(QtCore.QRect(100, 0, 756, 677))
        self.frame_PhotoShow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_PhotoShow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_PhotoShow.setObjectName("frame_PhotoShow")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_PhotoShow)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_12 = QtWidgets.QFrame(self.frame_PhotoShow)
        self.line_12.setMaximumSize(QtCore.QSize(16777215, 5))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.verticalLayout.addWidget(self.line_12)
        self.frame_8 = QtWidgets.QFrame(self.frame_PhotoShow)
        self.frame_8.setStyleSheet("#frame_8 QLabel{\n"
                                   "    background:white;\n"
                                   "    opacity:0.9;\n"
                                   "    }")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setContentsMargins(9, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.frame_8)
        self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        spacerItem = QtWidgets.QSpacerItem(681, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_8 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_8.setFont(font)
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_8.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.verticalLayout.addWidget(self.frame_8)
        self.line_3 = QtWidgets.QFrame(self.frame_PhotoShow)
        self.line_3.setMaximumSize(QtCore.QSize(16777215, 5))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.verticalLayout.addWidget(self.line_3)
        self.frame_11 = QtWidgets.QFrame(self.frame_PhotoShow)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 41))
        self.frame_11.setStyleSheet("#frame_11 QLabel\n"
                                    "{\n"
                                    "    color:#979A9A;\n"
                                    "    font-size:15px;\n"
                                    "}")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_2.setContentsMargins(9, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_20 = QtWidgets.QLabel(self.frame_11)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_2.addWidget(self.label_20)
        self.line_10 = QtWidgets.QFrame(self.frame_11)
        self.line_10.setMaximumSize(QtCore.QSize(5, 16777215))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.horizontalLayout_2.addWidget(self.line_10)
        self.label_21 = QtWidgets.QLabel(self.frame_11)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_2.addWidget(self.label_21)
        self.line_11 = QtWidgets.QFrame(self.frame_11)
        self.line_11.setMaximumSize(QtCore.QSize(5, 16777215))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.horizontalLayout_2.addWidget(self.line_11)
        self.label_22 = QtWidgets.QLabel(self.frame_11)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_2.addWidget(self.label_22)
        self.horizontalLayout_2.setStretch(0, 10)
        self.horizontalLayout_2.setStretch(2, 3)
        self.horizontalLayout_2.setStretch(4, 3)
        self.verticalLayout.addWidget(self.frame_11)
        self.line_4 = QtWidgets.QFrame(self.frame_PhotoShow)
        self.line_4.setMaximumSize(QtCore.QSize(16777215, 5))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.scrollAreaPhotoShow = QtWidgets.QScrollArea(self.frame_PhotoShow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaPhotoShow.sizePolicy().hasHeightForWidth())
        self.scrollAreaPhotoShow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(True)

        self.scrollAreaPhotoShow.setFont(font)
        self.scrollAreaPhotoShow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaPhotoShow.setAutoFillBackground(False)
        self.scrollAreaPhotoShow.setStyleSheet("#scrollAreaWidgetContents\n"
                                               "{\n"
                                               "    background:white;\n"
                                               "}\n"
                                               "\n"
                                               "#scrollAreaWidgetContents QFrame:hover{\n"
                                               "    background:#D0D3D4;\n"
                                               "    border-radius:18px;\n"
                                               "    opacity:0.5;\n"
                                               "    }")
        self.scrollAreaPhotoShow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollAreaPhotoShow.setLineWidth(-1)
        self.scrollAreaPhotoShow.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollAreaPhotoShow.setWidgetResizable(True)
        self.scrollAreaPhotoShow.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.scrollAreaPhotoShow.setObjectName("scrollAreaPhotoShow")
        self.scrollAreaWidgetContentsPhotoShow = QtWidgets.QWidget()
        self.scrollAreaWidgetContentsPhotoShow.setGeometry(QtCore.QRect(0, 0, 752, 623))
        self.scrollAreaWidgetContentsPhotoShow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContentsPhotoShow.setObjectName("scrollAreaWidgetContentsPhotoShow")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContentsPhotoShow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.frame_13 = QtWidgets.QFrame(self.scrollAreaWidgetContentsPhotoShow)
        self.frame_13.setMinimumSize(QtCore.QSize(0, 36))
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 36))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_14.setContentsMargins(3, 0, 9, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_13.addWidget(self.checkBox_2)
        self.label_27 = QtWidgets.QLabel(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_13.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setMinimumSize(QtCore.QSize(0, 30))
        self.label_28.setMaximumSize(QtCore.QSize(16777215, 36))
        self.label_28.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_13.addWidget(self.label_28)
        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 1)
        self.horizontalLayout_13.setStretch(2, 20)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_13)
        self.label_29 = QtWidgets.QLabel(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_14.addWidget(self.label_29)
        self.label_30 = QtWidgets.QLabel(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_14.addWidget(self.label_30)
        self.horizontalLayout_14.setStretch(0, 7)
        self.horizontalLayout_14.setStretch(1, 2)
        self.horizontalLayout_14.setStretch(2, 2)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.frame_13)
        self.scrollAreaPhotoShow.setWidget(self.scrollAreaWidgetContentsPhotoShow)
        self.verticalLayout_2.addWidget(self.scrollAreaPhotoShow)


        self.MainWindow.frame_PhotoShow = self.frame_PhotoShow
        self.MainWindow.verticalLayout_6.addWidget(self.frame_PhotoShow)
        # self.MainWindow.horizontalLayout.addWidget(self.frame_PhotoShow)
        # self.MainWindow.frame_PhotoShow.raise_()
        self.label_8.setText("...")
        self.label_20.setText("文件名")
        self.label_21.setText("修改时间")
        self.label_22.setText("大小")
        self.MainWindow.frame_PhotoShow.hide()

        frame = {'frame':self.frame_PhotoShow,'scrollArea':self.scrollAreaPhotoShow,'label':self.label_11}
        return frame


        # self.retranslateUi()

    def MainWindowSizeChange1(self,e):

        if self.MainWindow.scrollArea.width() < 500:
            w = 760
        else:
            w = self.MainWindow.scrollArea.width()
        for i in self.MainWindow.CurSBCFilesDict:
            FIleinfo = self.MainWindow.CurSBCFilesDict[i]
            FileName = FIleinfo['fename']
            Felabel = FIleinfo['FileNameLabel']
            # print(Felabel)
            metrics = QFontMetrics(Felabel.font())
            # print(metrics)
            new_file_name = metrics.elidedText(FileName, Qt.ElideRight, w*0.5)
            Felabel.setText(new_file_name)

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

    def ScrollContentUpdate(self):
        # print('CurNavChosed',self.MainWindow.CurNavChosed)
        if self.MainWindow.CurNavChosed in self.MainWindow.SBCFilesDict[self.MainWindow.CurNetChosed]:
            print('pr',self.MainWindow.SBCFilesDict)
            print(self.MainWindow.SBCFilesDict)
            # print(self.MainWindow.SBCFilesDict[self.MainWindow.CurNavChosed]['scrollAreaWidgetContents'])
            self.MainWindow.SBCFilesDict[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['scrollAreaWidgetContents'].deleteLater()
        self.MainWindow.SBCFilesDict[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed] = {}
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 806, 565))
        self.scrollAreaWidgetContents.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        formLayout.setContentsMargins(0, 0, 0, 0)
        formLayout.setVerticalSpacing(0)
        formLayout.setObjectName("formLayout")

        # print(self.MainWindow.FileCons)
        self.MainWindow.FileCons[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed] = {}
        Filecon = []
        self.CurSBCFilesDict = {}
        SBCFile = {}
        self.CurSBCFilesDict['scrollAreaWidgetContents'] = self.scrollAreaWidgetContents

        for i in range(len(self.CurFileList)):
            CurSBCFiles = {}
            FileInfo = self.CurFileList[i]
            CurSBCFiles['frame'] = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            CurSBCFiles['frame'].setMinimumSize(QtCore.QSize(0, 36))
            CurSBCFiles['frame'].setMaximumSize(QtCore.QSize(16777215, 36))
            CurSBCFiles['frame'].setFrameShape(QtWidgets.QFrame.StyledPanel)
            CurSBCFiles['frame'].setFrameShadow(QtWidgets.QFrame.Raised)
            CurSBCFiles['frame'].setObjectName("frame_13")
            horizontalLayout_14 = QtWidgets.QHBoxLayout(CurSBCFiles['frame'])
            horizontalLayout_14.setContentsMargins(3, 0, 9, 0)
            horizontalLayout_14.setSpacing(0)
            horizontalLayout_14.setObjectName("horizontalLayout_14")
            horizontalLayout_13 = QtWidgets.QHBoxLayout()
            horizontalLayout_13.setContentsMargins(0, 0, 0, -1)
            horizontalLayout_13.setSpacing(6)
            horizontalLayout_13.setObjectName("horizontalLayout_13")
            checkBox_2 = QtWidgets.QCheckBox(CurSBCFiles['frame'])
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(checkBox_2.sizePolicy().hasHeightForWidth())
            checkBox_2.setSizePolicy(sizePolicy)
            checkBox_2.setText("")
            checkBox_2.setObjectName("checkBox_2")
            horizontalLayout_13.addWidget(checkBox_2)
            CurSBCFiles['con'] = QtWidgets.QLabel(CurSBCFiles['frame'])
            CurSBCFiles['con'].setMaximumSize(QtCore.QSize(36, 36))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(CurSBCFiles['con'].sizePolicy().hasHeightForWidth())
            CurSBCFiles['con'].setSizePolicy(sizePolicy)
            CurSBCFiles['con'].setAlignment(QtCore.Qt.AlignCenter)
            CurSBCFiles['con'].setObjectName("label_27")
            horizontalLayout_13.addWidget(CurSBCFiles['con'])
            CurSBCFiles['FileNameLabel'] = QtWidgets.QLabel(CurSBCFiles['frame'])
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(9)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(CurSBCFiles['FileNameLabel'].sizePolicy().hasHeightForWidth())
            CurSBCFiles['FileNameLabel'].setSizePolicy(sizePolicy)
            CurSBCFiles['FileNameLabel'].setMinimumSize(QtCore.QSize(0, 30))
            CurSBCFiles['FileNameLabel'].setMaximumSize(QtCore.QSize(16777215, 36))
            CurSBCFiles['FileNameLabel'].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            CurSBCFiles['FileNameLabel'].setObjectName(FileInfo["filelj"])
            horizontalLayout_13.addWidget(CurSBCFiles['FileNameLabel'])
            horizontalLayout_13.setStretch(0, 1)
            horizontalLayout_13.setStretch(1, 1)
            horizontalLayout_13.setStretch(2, 20)
            horizontalLayout_14.addLayout(horizontalLayout_13)
            label_29 = QtWidgets.QLabel(CurSBCFiles['frame'])
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(3)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(label_29.sizePolicy().hasHeightForWidth())
            label_29.setSizePolicy(sizePolicy)
            label_29.setAlignment(QtCore.Qt.AlignCenter)
            label_29.setObjectName("label_29")
            horizontalLayout_14.addWidget(label_29)
            label_30 = QtWidgets.QLabel(CurSBCFiles['frame'])
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(3)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(label_30.sizePolicy().hasHeightForWidth())
            label_30.setSizePolicy(sizePolicy)
            label_30.setAlignment(QtCore.Qt.AlignCenter)
            label_30.setObjectName("label_30")
            horizontalLayout_14.addWidget(label_30)
            horizontalLayout_14.setStretch(0, 7)
            horizontalLayout_14.setStretch(1, 2)
            horizontalLayout_14.setStretch(2, 2)
            formLayout.setWidget(i, QtWidgets.QFormLayout.SpanningRole, CurSBCFiles['frame'])
            metrics = QFontMetrics(CurSBCFiles['FileNameLabel'].font())
            new_file_name = metrics.elidedText(FileInfo['filename'], Qt.ElideRight, 300)
            CurSBCFiles['FileNameLabel'].setText(new_file_name)
            filepath = base64.decodebytes(FileInfo['filelj'].encode('utf8')).decode()
            CurSBCFiles['fepath'] = filepath
            CurSBCFiles['fename'] = FileInfo['filename']
            CurSBCFiles['fepath_base64'] = FileInfo['filelj']
            if FileInfo['fetype'] == 'img':
                Filecon.append(CurSBCFiles)
            CurSBCFiles['con'].setText("")
            CurSBCFiles['con'].setPixmap(QtGui.QPixmap(self.FileConChose(FileInfo['fetype'])))
            CurSBCFiles['con'].setScaledContents(True)

            label_29.setText(FileInfo['date'])
            label_30.setText(FileInfo['big'])
            # CurSBCFiles['FileNameLabel'].mousePressEvent = partial(self.ClickEventDeals.FileClickDeal, CurSBCFiles)
            CurSBCFiles['FileNameLabel'].mousePressEvent = partial(self.FileClickDeal, CurSBCFiles)

            # self.CurSBCFilesDict['File'] = {FileInfo['filelj']:CurSBCFiles}
            # self.CurSBCFilesDict[FileInfo['filelj']] = CurSBCFiles
            SBCFile[FileInfo['filelj']] = CurSBCFiles


        self.MainWindow.FileCons[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed] = Filecon
        self.MainWindow.frameandscroll[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['scrollArea'].setWidget(self.scrollAreaWidgetContents)
        # self.scrollAreaPhotoShow.setWidget(self.scrollAreaWidgetContents)
        # self.verticalLayout_2.addWidget(self.scrollAreaPhotoShow)
        # self.MainWindow.verticalLayout_6.addWidget(self.frame_PhotoShow)
        # self.MainWindow.SBCFilesDict[self.MainWindow.CurNavChosed] = self.CurSBCFilesDict
        self.MainWindow.SBCFilesDict[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['scrollAreaWidgetContents'] = self.scrollAreaWidgetContents
        self.MainWindow.SBCFilesDict[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['File'] = SBCFile
        # print(self.MainWindow.SBCFilesDict[self.MainWindow.CurNavChosed]['scrollAreaWidgetContents'])



        if self.Thread_LoadImg.isRunning():
            self.Thread_LoadImg.wait()
        self.Thread_LoadImg.runthread(self.MainWindow)


    def run(self):
        self.SBCRe = SBCRequest.SBCRe()
        # if self.isRunning():
        #     return
        if self.MainWindow.CurNavChosed == 'File':
            self.SBCRe.GetFileList(self.path)
            self.CurFileListOld = self.SBCRe.CurFileList
            self.CurFileList = self.SBCRe.CurFileList
            print(self.CurFileList)
            self.signal.emit()
        if self.MainWindow.CurNavChosed == 'Photo':
            # self.SBCRe.GetFileList(self.path)
            self.SBCRe.SearchFile()
            self.CurFileListOld = self.SBCRe.CurFileList
            self.CurFileList = self.SBCRe.CurFileList
            print(self.CurFileList)
            self.signal.emit()
        if self.MainWindow.CurNavChosed == 'Video':
            self.SBCRe.GetFileList('/home/BaiduNet/')
            self.CurFileListOld = self.SBCRe.CurFileList
            self.CurFileList = self.SBCRe.CurFileList
            self.signal.emit()

    def UpdateShow(self,Show):
        # self.CurShow = Show
        self.start()


    def FileShow(self):
        # self.MainWindow.frame_PhotoShow.hide()
        # self.MainWindow.frame_12.show()
        self.MainWindow.frameandscroll[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['frame'].show()
        self.UpdateShow('File')

    def PhotoShow(self):
        # self.label_11.setText("图片")
        self.MainWindow.frameandscroll[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['label'].setText("图片")
        # self.MainWindow.frame_12.hide()
        self.MainWindow.frameandscroll[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['frame'].show()
        # self.MainWindow.frameandscroll['frame'].show()
        # self.MainWindow.frame_PhotoShow.show()
        # self.MainWindow.frame_PhotoShow.resizeEvent = self.MainWindowSizeChange1
        self.UpdateShow('Photo')

    def VideoShow(self):
        # self.label_11.setText("视频")
        self.MainWindow.frameandscroll[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['label'].setText("视频")
        # self.MainWindow.frame_12.hide()
        self.MainWindow.frameandscroll[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['frame'].show()
        # self.MainWindow.frame_PhotoShow.show()
        self.UpdateShow('Video')



    # def retranslateUi(self):
    #     _translate = QtCore.QCoreApplication.translate
    #     self.label_11.setText("图片")
    #     self.label_8.setText("...")
    #     self.label_20.setText("文件名")
    #     self.label_21.setText("修改时间")
    #     self.label_22.setText("大小")
    #     self.label_27.setText("con")
    #     self.label_28.setText("File1")
    #     self.label_29.setText("2020-03-02")
    #     self.label_30.setText("100MB")


class Thread_LoadImg(QThread):
    def __init__(self):
        super().__init__()
        self.SBCRe = SBCRequest.SBCRe()

        # self.Thread_LoadImg = Thread_LoadImg(self.ui)

    def func(self, listTemp, n):
        for i in range(0, len(listTemp), n):
            yield listTemp[i:i + n]

    def ShowCon(self, px, base64data):
        ba = base64data
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(ba)
        px.setPixmap(pixmap)

    def runthread(self,MainWindow):
        self.MainWindow = MainWindow
        # print(self.FileCons)
        self.start()

    def run(self):

        FileCon = self.MainWindow.FileCons[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]
        temp = self.func(FileCon, 2)
        for i in temp:
            SendList = [{'fepath': j['fepath']} for j in i]
            # print('send',SendList)
            ConList = self.SBCRe.GetFileCon(SendList)
            try:
                for num in range(len(ConList['src'])):
                    coninfo = ConList['src'][num]
                    ConBase64 = coninfo.split(',')[-1]
                    img_b64decode = base64.b64decode(ConBase64)  # [21:]
                    self.ShowCon(i[num]['con'], img_b64decode)
            except:
                # print('threderror')
                break

