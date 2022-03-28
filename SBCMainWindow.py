# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SBCclient.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SBCclient(object):
    def setupUi(self, SBCclient):
        SBCclient.setObjectName("SBCclient")
        SBCclient.resize(960, 663)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        SBCclient.setFont(font)
        SBCclient.setWindowOpacity(1.0)
        SBCclient.setStyleSheet("#SBCclient{\n"
"    background-color:white;\n"
"}\n"
"#centralwidget{\n"
"    background-color:white;\n"
"}\n"
"QLabel{\n"
"    font-size:16px;\n"
"}\n"
"Line{\n"
"    background:rgb(173, 173, 173);\n"
"}\n"
"#frame{\n"
"    border-radius:3px;\n"
"    background:rgb(173, 173, 173);\n"
"}\n"
"#frame_7 QFrame:hover{\n"
"    background:#A2D9CE;\n"
"    border-radius:10px;\n"
"    opacity:0.5;\n"
"    }\n"
"#SBCCapacity{\n"
"    border-radius:5px;\n"
"    background:#5B5B5B;\n"
"}\n"
"#usedCap{\n"
"    border-radius:5px;\n"
"    background:#006000;\n"
"    Width:60px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(SBCclient)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 161, 600))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("#label{\n"
"    font-size:26px;\n"
"}")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 540, 161, 1))
        self.line.setStyleSheet("Line{\n"
"    background:#D0D3D4;\n"
"}")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 490, 141, 16))
        self.label_7.setObjectName("label_7")
        self.SBCCapacity = QtWidgets.QFrame(self.frame)
        self.SBCCapacity.setGeometry(QtCore.QRect(10, 520, 141, 10))
        self.SBCCapacity.setStyleSheet("")
        self.SBCCapacity.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SBCCapacity.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SBCCapacity.setObjectName("SBCCapacity")
        self.usedCap = QtWidgets.QFrame(self.SBCCapacity)
        self.usedCap.setGeometry(QtCore.QRect(0, 0, 20, 10))
        self.usedCap.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.usedCap.setFrameShadow(QtWidgets.QFrame.Raised)
        self.usedCap.setObjectName("usedCap")
        self.label_usercon = QtWidgets.QLabel(self.frame)
        self.label_usercon.setGeometry(QtCore.QRect(10, 550, 41, 41))
        self.label_usercon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_usercon.setStyleSheet("#label_usercon{\n"
"    border-radius:20px;\n"
"}")
        self.label_usercon.setText("")
        self.label_usercon.setPixmap(QtGui.QPixmap("../SBCv2/static/img/Sure.jpg"))
        self.label_usercon.setObjectName("label_usercon")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(60, 560, 71, 21))
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_9.setObjectName("label_9")
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setGeometry(QtCore.QRect(0, 70, 161, 301))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.frame_6 = QtWidgets.QFrame(self.frame_7)
        self.frame_6.setGeometry(QtCore.QRect(0, 240, 161, 41))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        self.label_6.setGeometry(QtCore.QRect(30, 10, 61, 21))
        self.label_6.setObjectName("label_6")
        self.frame_5 = QtWidgets.QFrame(self.frame_7)
        self.frame_5.setGeometry(QtCore.QRect(0, 170, 161, 41))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(30, 10, 61, 21))
        self.label_5.setObjectName("label_5")
        self.frame_3 = QtWidgets.QFrame(self.frame_7)
        self.frame_3.setGeometry(QtCore.QRect(0, 90, 161, 41))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 61, 21))
        self.label_3.setObjectName("label_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_7)
        self.frame_4.setGeometry(QtCore.QRect(0, 130, 161, 41))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 61, 21))
        self.label_4.setObjectName("label_4")
        self.frame_2 = QtWidgets.QFrame(self.frame_7)
        self.frame_2.setGeometry(QtCore.QRect(-1, 50, 161, 41))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 61, 21))
        self.label_2.setObjectName("label_2")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("../SBCv2/static/img/xhy.jpg"))
        self.label_10.setObjectName("label_10")
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setGeometry(QtCore.QRect(160, 50, 801, 28))
        self.frame_8.setStyleSheet("#frame_8 QLabel{\n"
"    background:white;\n"
"    opacity:0.9;\n"
"    }")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.line_2 = QtWidgets.QFrame(self.frame_8)
        self.line_2.setGeometry(QtCore.QRect(40, 2, 5, 25))
        self.line_2.setMaximumSize(QtCore.QSize(5, 16777215))
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_11 = QtWidgets.QLabel(self.frame_8)
        self.label_11.setGeometry(QtCore.QRect(50, 0, 31, 31))
        self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_8)
        self.label_12.setGeometry(QtCore.QRect(20, 0, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_12.setObjectName("label_12")
        self.label_19 = QtWidgets.QLabel(self.frame_8)
        self.label_19.setGeometry(QtCore.QRect(85, 0, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(161, 50, 801, 5))
        self.line_3.setMaximumSize(QtCore.QSize(16777215, 5))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(161, 80, 801, 5))
        self.line_4.setMaximumSize(QtCore.QSize(16777215, 5))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 10, 791, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_9 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.frame_Buttons = QtWidgets.QFrame(self.frame_9)
        self.frame_Buttons.setGeometry(QtCore.QRect(0, 0, 286, 34))
        self.frame_Buttons.setStyleSheet("#frame_Buttons{\n"
"    background:#D1F2EB;\n"
"    border-radius:15px;\n"
"    opacity:0.8;\n"
"}\n"
"#frame_Buttons QLabel:hover{\n"
"    color:blue;\n"
"    }")
        self.frame_Buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Buttons.setObjectName("frame_Buttons")
        self.label_14 = QtWidgets.QLabel(self.frame_Buttons)
        self.label_14.setGeometry(QtCore.QRect(9, 9, 32, 16))
        self.label_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_14.setObjectName("label_14")
        self.line_6 = QtWidgets.QFrame(self.frame_Buttons)
        self.line_6.setGeometry(QtCore.QRect(50, 9, 1, 16))
        self.line_6.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_15 = QtWidgets.QLabel(self.frame_Buttons)
        self.label_15.setGeometry(QtCore.QRect(56, 9, 32, 16))
        self.label_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_Buttons)
        self.label_16.setGeometry(QtCore.QRect(103, 9, 48, 16))
        self.label_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_16.setObjectName("label_16")
        self.line_8 = QtWidgets.QFrame(self.frame_Buttons)
        self.line_8.setGeometry(QtCore.QRect(160, 9, 2, 16))
        self.line_8.setMaximumSize(QtCore.QSize(2, 16777215))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.label_17 = QtWidgets.QLabel(self.frame_Buttons)
        self.label_17.setGeometry(QtCore.QRect(166, 9, 32, 16))
        self.label_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_17.setObjectName("label_17")
        self.line_9 = QtWidgets.QFrame(self.frame_Buttons)
        self.line_9.setGeometry(QtCore.QRect(200, 9, 2, 16))
        self.line_9.setMaximumSize(QtCore.QSize(2, 16777215))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.label_18 = QtWidgets.QLabel(self.frame_Buttons)
        self.label_18.setGeometry(QtCore.QRect(213, 9, 64, 16))
        self.label_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_18.setObjectName("label_18")
        self.line_13 = QtWidgets.QFrame(self.frame_Buttons)
        self.line_13.setGeometry(QtCore.QRect(90, 10, 2, 16))
        self.line_13.setMaximumSize(QtCore.QSize(2, 16777215))
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.horizontalLayout_4.addWidget(self.frame_9)
        spacerItem = QtWidgets.QSpacerItem(308, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.frame_10 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.frame_Search = QtWidgets.QFrame(self.frame_10)
        self.frame_Search.setGeometry(QtCore.QRect(50, 0, 171, 31))
        self.frame_Search.setStyleSheet("#frame_Search{\n"
"    background:#ECF0F1;\n"
"    border-radius:15px;\n"
"    opacity:0.5;\n"
"}\n"
"#frame_Search QLineEdit{\n"
"    background:#ECF0F1;\n"
"    border-radius:15px;\n"
"    opacity:0.5;\n"
"}\n"
"#frame_Search Line{\n"
"    background:#B3B6B7;\n"
"}\n"
"#frame_Search QLabel{\n"
"    color:#979A9A;\n"
"    font-size:15px;\n"
"}")
        self.frame_Search.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Search.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Search.setObjectName("frame_Search")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_Search)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 112, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.line_5 = QtWidgets.QFrame(self.frame_Search)
        self.line_5.setGeometry(QtCore.QRect(120, 7, 2, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_13 = QtWidgets.QLabel(self.frame_Search)
        self.label_13.setGeometry(QtCore.QRect(130, 5, 31, 21))
        self.label_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.frame_10)
        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(2, 2)
        self.frame_11 = QtWidgets.QFrame(self.centralwidget)
        self.frame_11.setGeometry(QtCore.QRect(160, 80, 801, 31))
        self.frame_11.setStyleSheet("#frame_11 QLabel\n"
"{\n"
"    color:#979A9A;\n"
"    font-size:15px;\n"
"}")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_20 = QtWidgets.QLabel(self.frame_11)
        self.label_20.setGeometry(QtCore.QRect(40, 0, 51, 31))
        self.label_20.setObjectName("label_20")
        self.line_10 = QtWidgets.QFrame(self.frame_11)
        self.line_10.setGeometry(QtCore.QRect(470, 1, 5, 28))
        self.line_10.setMaximumSize(QtCore.QSize(5, 16777215))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.label_21 = QtWidgets.QLabel(self.frame_11)
        self.label_21.setGeometry(QtCore.QRect(480, 0, 71, 31))
        self.label_21.setObjectName("label_21")
        self.line_11 = QtWidgets.QFrame(self.frame_11)
        self.line_11.setGeometry(QtCore.QRect(650, 1, 5, 28))
        self.line_11.setMaximumSize(QtCore.QSize(5, 16777215))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.label_22 = QtWidgets.QLabel(self.frame_11)
        self.label_22.setGeometry(QtCore.QRect(660, 0, 51, 31))
        self.label_22.setObjectName("label_22")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(161, 110, 801, 5))
        self.line_12.setMaximumSize(QtCore.QSize(16777215, 5))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(161, 111, 801, 491))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(True)
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet("#scrollAreaWidgetContents\n"
"{\n"
"    background:white;\n"
"}\n"
"\n"
"#scrollAreaWidgetContents QFrame:hover{\n"
"    background:#A2D9CE;\n"
"    border-radius:20px;\n"
"    opacity:0.5;\n"
"    }")
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setLineWidth(-1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 774, 487))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.frame_12 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_12.setGeometry(QtCore.QRect(0, 0, 771, 41))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.label_23 = QtWidgets.QLabel(self.frame_12)
        self.label_23.setGeometry(QtCore.QRect(70, 0, 391, 41))
        self.label_23.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame_12)
        self.label_24.setGeometry(QtCore.QRect(480, 0, 121, 41))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_12)
        self.label_25.setGeometry(QtCore.QRect(660, 0, 111, 41))
        self.label_25.setObjectName("label_25")
        self.checkBox = QtWidgets.QCheckBox(self.frame_12)
        self.checkBox.setGeometry(QtCore.QRect(10, 0, 16, 41))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.label_26 = QtWidgets.QLabel(self.frame_12)
        self.label_26.setGeometry(QtCore.QRect(30, 0, 31, 41))
        self.label_26.setObjectName("label_26")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.widget)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayout.addWidget(self.verticalScrollBar)
        self.layoutWidget.raise_()
        self.frame.raise_()
        self.frame_8.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.layoutWidget.raise_()
        self.frame_11.raise_()
        self.line_12.raise_()
        SBCclient.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SBCclient)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 23))
        self.menubar.setObjectName("menubar")
        SBCclient.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SBCclient)
        self.statusbar.setObjectName("statusbar")
        SBCclient.setStatusBar(self.statusbar)

        self.retranslateUi(SBCclient)
        QtCore.QMetaObject.connectSlotsByName(SBCclient)

    def retranslateUi(self, SBCclient):
        _translate = QtCore.QCoreApplication.translate
        SBCclient.setWindowTitle(_translate("SBCclient", "小黑云客户端"))
        self.label.setText(_translate("SBCclient", "小黑云"))
        self.label_7.setText(_translate("SBCclient", "10.1GB/6.0T"))
        self.label_9.setText(_translate("SBCclient", "用户"))
        self.label_6.setText(_translate("SBCclient", "传输列表"))
        self.label_5.setText(_translate("SBCclient", "分享"))
        self.label_3.setText(_translate("SBCclient", "图片"))
        self.label_4.setText(_translate("SBCclient", "视频"))
        self.label_2.setText(_translate("SBCclient", "文件"))
        self.label_11.setText(_translate("SBCclient", "Home"))
        self.label_12.setText(_translate("SBCclient", "<"))
        self.label_19.setText(_translate("SBCclient", ">"))
        self.label_14.setText(_translate("SBCclient", "下载"))
        self.label_15.setText(_translate("SBCclient", "上传"))
        self.label_16.setText(_translate("SBCclient", "重命名"))
        self.label_17.setText(_translate("SBCclient", "更多"))
        self.label_18.setText(_translate("SBCclient", "切换网盘"))
        self.lineEdit.setPlaceholderText(_translate("SBCclient", "搜索网盘文件"))
        self.label_13.setText(_translate("SBCclient", "搜索"))
        self.label_20.setText(_translate("SBCclient", "文件名"))
        self.label_21.setText(_translate("SBCclient", "修改时间"))
        self.label_22.setText(_translate("SBCclient", "大小"))
        self.label_23.setText(_translate("SBCclient", "File1"))
        self.label_24.setText(_translate("SBCclient", "2020-03-02"))
        self.label_25.setText(_translate("SBCclient", "100MB"))
        self.label_26.setText(_translate("SBCclient", "con"))

