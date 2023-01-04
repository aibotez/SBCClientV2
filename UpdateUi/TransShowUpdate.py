import sys,threading
sys.path.append('..')
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets

class TransShowUpdate():
    def __init__(self,ui):
        self.ui = ui

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
        self.progressBar_4.setProperty("value", 24)
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
        self.label_33.setText("con")
        self.label_19.setText("5K.mat")
        self.label_20.setText("752KB/19.95MB")
        self.label_21.setText("暂停")
        self.label_22.setText(">")
        self.label_23.setText("X")
        self.label_24.setText("[]")
        Downinginfoi = {}
        Downinginfoi['frame'] = self.frame_16
        Downinginfoi['status'] = self.label_22
        Downinginfoi['progressBar'] = self.progressBar_4
        Downinginfoi['LoPath'] = DownInfo['FilePath']+DownInfo['FileName']
        self.label_23.mousePressEvent = partial(self.DelDowing,Downinginfoi)
        return Downinginfoi

    def DelDowing(self,info,e):
        DownverticalLayout = self.DownLayout[1]
        print(info['frame'])
        DownverticalLayout.itemAt(0).widget().deleteLater()
# myLayout.count()
    def AddDown(self,DownInfo):
        # self.ui.TranspscrollAreaformLayout.itemAt(0).widget().deleteLater()
        print(self.ui.TranspscrollArea)
        DownLayout = self.ui.TranspscrollArea['Down']
        self.DownLayout = DownLayout
        DownformLayout = DownLayout[0]
        DownverticalLayout = DownLayout[1]
        scrollAreaWidgetContents_down = DownLayout[2]
        DownverticalLayout.itemAt(0).widget().deleteLater()
        DownverticalLayout.itemAt(0).widget().deleteLater()
        print(DownInfo)
        Downinginfoi = self.add1(scrollAreaWidgetContents_down,DownInfo)
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

