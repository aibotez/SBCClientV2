
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
from SubUi import Transmitui
from pack.preview import ImgPreview
from UpdateUi import TransShowUpdate
from SubUi import ShareShowui


class Ui_PhotoShow(QThread):
    def __init__(self,ui):
        super().__init__()
        self.MainWindow= ui


        # self.ImgPreviews = ImgPreview.ImageViewer()

    def initfileshow(self):
        self.MainWindow.frame_12.deleteLater()
        frame_12 = QtWidgets.QFrame(self.MainWindow.frame_14)
        frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_12.setObjectName("frame_12")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(frame_12)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_12 = QtWidgets.QFrame(frame_12)
        self.line_12.setMaximumSize(QtCore.QSize(16777215, 5))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.verticalLayout.addWidget(self.line_12)
        self.frame_8 = QtWidgets.QFrame(frame_12)
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
        self.label_12 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_12.setFont(font)
        self.label_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        self.label_12.setText("<")
        # print(self.MainWindow.nav)

        self.MainWindow.NetOper[self.MainWindow.CurNetChosed]['backbutton'] = self.label_12
        # self.label_12.mousePressEvent = partial(self.navBackClick) #back

        label_12 = QtWidgets.QLabel(self.frame_8)
        label_12.setMaximumSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        label_12.setFont(font)
        label_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(label_12)
        # label_12.setText("O")
        label_12.setPixmap(QtGui.QPixmap("img/Clientcon/refresh.jpg")) #refresh
        label_12.setScaledContents(True)

        self.MainWindow.NetOper[self.MainWindow.CurNetChosed]['refreshbutton'] = label_12
        # label_12.mousePressEvent = partial(self.Refresh)

        self.line_2 = QtWidgets.QFrame(self.frame_8)
        self.line_2.setMaximumSize(QtCore.QSize(5, 16777215))
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)


        # self.label_11 = QtWidgets.QLabel(self.frame_8)
        # self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.label_11.setObjectName("label_11")
        # self.horizontalLayout_3.addWidget(self.label_11)
        # self.label_19 = QtWidgets.QLabel(self.frame_8)
        # font = QtGui.QFont()
        # font.setPointSize(-1)
        # self.label_19.setFont(font)
        # self.label_19.setObjectName("label_19")
        # self.horizontalLayout_3.addWidget(self.label_19)
        # spacerItem3 = QtWidgets.QSpacerItem(681, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_3.addItem(spacerItem3)
        # self.label_8 = QtWidgets.QLabel(self.frame_8)
        # font = QtGui.QFont()
        # font.setPointSize(-1)
        # self.label_8.setFont(font)
        # self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.label_8.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        # self.label_8.setObjectName("label_8")
        # self.horizontalLayout_3.addWidget(self.label_8)


        self.verticalLayout.addWidget(self.frame_8)
        self.line_3 = QtWidgets.QFrame(frame_12)
        self.line_3.setMaximumSize(QtCore.QSize(16777215, 5))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.frame_11 = QtWidgets.QFrame(frame_12)
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
        self.line_4 = QtWidgets.QFrame(frame_12)
        self.line_4.setMaximumSize(QtCore.QSize(16777215, 5))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.scrollArea = QtWidgets.QScrollArea(frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(True)
        self.scrollArea.setFont(font)
        self.scrollArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet("#scrollAreaWidgetContents\n"
                                      "{\n"
                                      "    background:white;\n"
                                      "}\n"
                                      "\n"
                                      "#scrollAreaWidgetContents QFrame:hover{\n"
                                      "    background:#D0D3D4;\n"
                                      "    border-radius:18px;\n"
                                      "    opacity:0.5;\n"
                                      "    }")
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setLineWidth(-1)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # self.scrollArea.changeEvent()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 710, 579))
        self.scrollAreaWidgetContents.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.frame_13 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
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
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.MainWindow.verticalLayout_6.addWidget(frame_12)
        self.label_20.setText("文件名")
        self.label_21.setText("修改时间")
        self.label_22.setText("大小")

        frame_9 = QtWidgets.QFrame(self.MainWindow.frame_8)
        frame_9_ = QtWidgets.QFrame(frame_9)
        self.horizontalLayout_3.addWidget(frame_9)
        spacerItem3 = QtWidgets.QSpacerItem(681, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)

        label_11 = QtWidgets.QLabel(self.MainWindow.frame_8)
        label_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        label_11.setObjectName("label_11")
        label_11.setText("...")
        self.horizontalLayout_3.addWidget(label_11)

        horizontalLayout_1 = QtWidgets.QHBoxLayout(frame_9)
        horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_1.addWidget(frame_9_)
        horizontalLayout_ = QtWidgets.QHBoxLayout(frame_9_)
        horizontalLayout_.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_.setObjectName("horizontalLayout_3")
        # label_11 = QtWidgets.QLabel(frame_9)
        # label_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # label_11.setObjectName("label_11")
        # label_11.setText("Home66")
        # horizontalLayout_.addWidget(label_11)

        # frame_9_.deleteLater()

        # frame_9_ = QtWidgets.QFrame(frame_9)
        # horizontalLayout_1.addWidget(frame_9_)
        # horizontalLayout_ = QtWidgets.QHBoxLayout(frame_9_)
        # horizontalLayout_.setContentsMargins(0, 0, 0, 0)
        # horizontalLayout_.setObjectName("horizontalLayout_3")
        # for i in range(10):
        #     label_11 = QtWidgets.QLabel(frame_9_)
        #     label_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        #     label_11.setObjectName("label_11")
        #     label_11.setText("Home66")
        #     horizontalLayout_.addWidget(label_11)
        #     label_11 = QtWidgets.QLabel(frame_9_)
        #     label_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        #     label_11.setObjectName("label_11")
        #     label_11.setText(">")
        #     horizontalLayout_.addWidget(label_11)
        frame_12.hide()
        # self.scrollArea.changeEvent()
        frame = {'frame': frame_12, 'scrollArea': self.scrollArea,'frame_navF':frame_9,'frame_nav':frame_9_,'horizontalLayout_nav':horizontalLayout_1}
        return frame


    def InitTranShow(self):
        # print(self.MainWindow.frame_14.width())
        self.frame_TranShow = QtWidgets.QFrame(self.MainWindow.centralwidget)
        self.frame_TranShow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_TranShow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_TranShow.setObjectName("frame_TranShow")
        transmitui = Transmitui.Ui_Form()
        transmitui.setupUi(self.frame_TranShow)
        TranspscrollAreaformLayout= {
            'Down': [transmitui.formLayout_3, transmitui.verticalLayout_9, transmitui.scrollAreaWidgetContents_7, transmitui.label_18,transmitui.pushButton_7,transmitui.pushButton_8,transmitui.pushButton_9]}
        TranspscrollAreaformLayout['Down'][1].itemAt(1).widget().deleteLater()
        TranspscrollAreaformLayout['Down'][1].itemAt(0).widget().deleteLater()
        TranspscrollAreaformLayout['TranspFinsh'] = [0,transmitui.verticalLayout_4, transmitui.scrollAreaWidgetContents_6,transmitui.label_10,transmitui.pushButton_6,transmitui.label_13]
        TranspscrollAreaformLayout['Up'] = [0, transmitui.verticalLayout_13,
                                            transmitui.scrollAreaWidgetContents_8,
                                            transmitui.label_26,transmitui.pushButton_10,transmitui.pushButton_11,
                                            transmitui.pushButton_12]
        transmitui.verticalLayout_13.itemAt(1).widget().deleteLater()
        transmitui.verticalLayout_13.itemAt(0).widget().deleteLater()
        transmitui.verticalLayout_4.itemAt(1).widget().deleteLater()
        transmitui.verticalLayout_4.itemAt(0).widget().deleteLater()
        self.MainWindow.horizontalLayout.addWidget(self.frame_TranShow)
        self.frame_TranShow.hide()


        self.MainWindow.TranspscrollArea = TranspscrollAreaformLayout
        self.MainWindow.frameandscroll['Tran'] = self.frame_TranShow

        # self.TransShowUpdate_ = TransShowUpdate.TransShowUpdate(self.MainWindow)
        # self.TransShowUpdate_.RefreshDowning()

        return [self.frame_TranShow,TranspscrollAreaformLayout]

    def InitShareShow(self):
        self.frame_ShareShow = QtWidgets.QFrame(self.MainWindow.centralwidget)
        self.frame_ShareShow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ShareShow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ShareShow.setObjectName("frame_ShareShow")
        ShareShowuii = ShareShowui.Ui_Form()
        ShareShowuii.setupUi(self.frame_ShareShow)
        self.frame_ShareShow.hide()
        self.MainWindow.ShareWindow = ShareShowuii
        self.MainWindow.frameandscroll['Share'] = self.frame_ShareShow
        self.MainWindow.horizontalLayout.addWidget(self.frame_ShareShow)

    def InitShow(self):
        # self.centralwidget = self.MainWindow.centralwidget

        self.frame_PhotoShow = QtWidgets.QFrame(self.MainWindow.frame_14)
        # self.frame_PhotoShow.setGeometry(QtCore.QRect(100, 0, 756, 677))
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

        self.initSBCCurFile()

        frame = {'frame':self.frame_PhotoShow,'scrollArea':self.scrollAreaPhotoShow,'label':self.label_11}
        return frame


        # self.retranslateUi()

    def initSBCCurFile(self):
        Nets = ['SBC','BDC','ALC']
        for i in Nets:
            self.MainWindow.CurFileListOld[i] = {}
            self.MainWindow.CurFileListOld[i]['Photo'] = []
            self.MainWindow.CurFileListOld[i]['Video'] = []
            self.MainWindow.CurFileListOld[i]['File'] = []

    # def initSBCCurFile(self):
    #     Nets = ['SBC','BDC','ALC']
    #     for i in Nets:
    #         self.CurFileListOld[i] = {}
    #         self.CurFileListOld[i]['Photo'] = []
    #         self.CurFileListOld[i]['Video'] = []
    #         self.CurFileListOld[i]['File'] = []