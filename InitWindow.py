
import sys
sys.path.append('..')
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QAction
from PyQt5.Qt import QThread
import SBCMainWindow
from PyQt5.QtGui import QFontMetrics,QCursor, QIcon
from PyQt5.QtCore import *
import base64
from pack import SBCRequest
from pack.preview import ImgPreview

from SubUi import SBCMainWindow
from SubUi import NavShow
from UpdateUi import FileUpdate


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
            self.ui.frameandscroll[i]['Photo']['frame'].hide()
            self.ui.frameandscroll[i]['Video']['frame'].hide()
            self.ui.frameandscroll[i]['File']['frame'].hide()
    def NavChoose(self,WosLabel,e):
        if e.buttons() == QtCore.Qt.LeftButton:
            if self.ui.CurNavChosed != WosLabel:
                self.HideFrames()
                self.ClearNavStyle()
                # print(WosLabel)
                if WosLabel == 'Photo':
                    self.ui.CurNavChosed = 'Photo'
                    self.filepdate.PhotoShow()
                    # SBCM.ChoseNav_Photo()
                    self.ui.frame_3.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")
                if WosLabel == 'File':
                    self.ui.CurNavChosed = 'File'
                    self.filepdate.FileShow()
                    # SBCM.ChoseNav_File()
                    self.ui.frame_2.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")
                if WosLabel == 'Video':
                    self.ui.CurNavChosed = 'Video'
                    self.ui.frame_4.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")
                    self.filepdate.VideoShow()
                    # SBCM.ChoseNav_Video()
                if WosLabel == 'Share':
                    self.ui.CurNavChosed = 'Share'
                    self.ui.frame_5.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")
                if WosLabel == 'Transmit':
                    self.ui.CurNavChosed = 'Transmit'
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


class initWindow():
    def __init__(self,Main):
        self.Main = Main
        self.SBCMain = SBCMainWindow.Ui_SBCclient()
        self.SBCMain.SBCRe = SBCRequest.SBCRe()
        self.SBCMain.setupUi(Main)

        self.Thread_LoadImgs = FileUpdate.Thread_LoadImg(self.SBCMain)
        self.SBCMain = self.initFrame()
        # self.Navshows = NavShow.Ui_PhotoShow(self.SBCMain)
        self.FileUpdates = FileUpdate.FileUpdate(self.SBCMain)

        self.init()

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

    def test1(self):
        horizontal_bar = self.SBCMain.frameandscroll['SBC']['File']['scrollArea'].verticalScrollBar()
        print(horizontal_bar.value(),horizontal_bar.maximum())
        print(self.SBCMain.frameandscroll['SBC']['File']['scrollArea'].size())
    # def test(self,e):
    #     horizontal_bar = self.SBCMain.frameandscroll['SBC']['File']['scrollArea'].verticalScrollBar()
    #     delta_y = - e.angleDelta().y()
    #     v = horizontal_bar.value() + delta_y
    #     v = max(min(v, horizontal_bar.maximum()), horizontal_bar.minimum())
    #     print(horizontal_bar.minimum(),horizontal_bar.maximum())
    #     horizontal_bar.setValue(v)

    def creat_ChoseNetmenu(self,e):
        self.groupBox_menu = QMenu()
        self.actionSBC = self.groupBox_menu.addAction(u'小黑云')
        self.actionBDC = self.groupBox_menu.addAction(u'百度云')
        self.actionALC = self.groupBox_menu.addAction(u'阿里云')
        self.groupBox_menu.popup(QCursor.pos())
    def initpopup(self):
        pass

    def initFrame(self):
        self.initparameter()
        self.Navshows = NavShow.Ui_PhotoShow(self.SBCMain)
        Nets = ['SBC', 'BDC', 'ALC']
        for i in Nets:
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
        self.SBCMain.frameandscroll['SBC']['File']['frame'].show()

        # self.SBCMain.creat_ChoseNetmenu = self.creat_ChoseNetmenu

        # self.Main.resizeEvent = self.MainWindowSizeChange
        return self.SBCMain

    def initBindSignal(self):
        self.SBCMain.NetOper[self.SBCMain.CurNetChosed]['backbutton'].mousePressEvent = partial(self.FileUpdates.navBackClick)  # back
        self.SBCMain.NetOper[self.SBCMain.CurNetChosed]['refreshbutton'].mousePressEvent = partial(self.FileUpdates.Refresh)
        # self.SBCMain.label_18.mousePressEvent = self.SBCMain.creat_ChoseNetmenu

    def init(self):
        CED = ClickEventDeals(self.SBCMain,self.FileUpdates)
        self.SBCMain.frame_13.deleteLater()
        self.SBCMain.frame_2.mousePressEvent = partial(CED.NavChoose,'File')
        self.SBCMain.frame_3.mousePressEvent = partial(CED.NavChoose, 'Photo')
        self.SBCMain.frame_4.mousePressEvent = partial(CED.NavChoose, 'Video')
        self.SBCMain.frame_5.mousePressEvent = partial(CED.NavChoose, 'Share')
        self.SBCMain.frame_6.mousePressEvent = partial(CED.NavChoose, 'Transmit')
        # print(self.SBCMain.CurFileListOld)
        self.SBCMain.label_18.mousePressEvent = self.creat_ChoseNetmenu
        self.FileUpdates.start()
        self.SBCMain.frame_2.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")










