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
        SBCclient.resize(878, 700)
        SBCclient.setMinimumSize(QtCore.QSize(800, 700))
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
        SBCclient.setAnimated(True)
        SBCclient.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(SBCclient)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setContentsMargins(0, 9, 0, 0)
        self.verticalLayout_5.setSpacing(9)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMaximumSize(QtCore.QSize(50, 50))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("../SBCv2/static/img/xhy.jpg"))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("#label{\n"
"    font-size:26px;\n"
"}")
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 300))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame_7)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 61, 21))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame_7)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 61, 21))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_7)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 61, 21))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_7)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(30, 10, 61, 21))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.frame_5)
        spacerItem = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.frame_6 = QtWidgets.QFrame(self.frame_7)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        self.label_6.setGeometry(QtCore.QRect(30, 10, 61, 21))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.frame_6)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 1)
        self.verticalLayout_3.setStretch(4, 1)
        self.verticalLayout_3.setStretch(5, 1)
        self.verticalLayout_5.addWidget(self.frame_7)
        spacerItem1 = QtWidgets.QSpacerItem(20, 245, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.SBCCapacity = QtWidgets.QFrame(self.frame)
        self.SBCCapacity.setMaximumSize(QtCore.QSize(16777215, 10))
        self.SBCCapacity.setStyleSheet("")
        self.SBCCapacity.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SBCCapacity.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SBCCapacity.setObjectName("SBCCapacity")
        self.usedCap = QtWidgets.QFrame(self.SBCCapacity)
        self.usedCap.setGeometry(QtCore.QRect(0, 0, 20, 10))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usedCap.sizePolicy().hasHeightForWidth())
        self.usedCap.setSizePolicy(sizePolicy)
        self.usedCap.setMaximumSize(QtCore.QSize(20, 10))
        self.usedCap.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.usedCap.setFrameShadow(QtWidgets.QFrame.Raised)
        self.usedCap.setObjectName("usedCap")
        self.verticalLayout_4.addWidget(self.SBCCapacity)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setStyleSheet("Line{\n"
"    background:#D0D3D4;\n"
"}")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(10, -1, -1, 6)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_usercon = QtWidgets.QLabel(self.frame)
        self.label_usercon.setMaximumSize(QtCore.QSize(40, 40))
        self.label_usercon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_usercon.setStyleSheet("#label_usercon{\n"
"    border-radius:20px;\n"
"}")
        self.label_usercon.setText("")
        self.label_usercon.setPixmap(QtGui.QPixmap("../SBCv2/static/img/Sure.jpg"))
        self.label_usercon.setObjectName("label_usercon")
        self.horizontalLayout_7.addWidget(self.label_usercon)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(10, 5, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_9 = QtWidgets.QFrame(self.centralwidget)
        self.frame_9.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 2)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_Buttons = QtWidgets.QFrame(self.frame_9)
        self.frame_Buttons.setStyleSheet("#frame_Buttons{\n"
"    background:#D1F2EB;\n"
"    border-radius:17px;\n"
"    opacity:0.8;\n"
"}\n"
"#frame_Buttons QLabel:hover{\n"
"    color:blue;\n"
"    }")
        self.frame_Buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Buttons.setObjectName("frame_Buttons")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_Buttons)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_14 = QtWidgets.QLabel(self.frame_Buttons)
        self.label_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_9.addWidget(self.label_14)
        self.line_6 = QtWidgets.QFrame(self.frame_Buttons)
        self.line_6.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_9.addWidget(self.line_6)
        self.label_15 = QtWidgets.QLabel(self.frame_Buttons)
        self.label_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_9.addWidget(self.label_15)
        self.line_13 = QtWidgets.QFrame(self.frame_Buttons)
        self.line_13.setMaximumSize(QtCore.QSize(2, 16777215))
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.horizontalLayout_9.addWidget(self.line_13)
        self.label_16 = QtWidgets.QLabel(self.frame_Buttons)
        self.label_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_9.addWidget(self.label_16)
        self.line_8 = QtWidgets.QFrame(self.frame_Buttons)
        self.line_8.setMaximumSize(QtCore.QSize(2, 16777215))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.horizontalLayout_9.addWidget(self.line_8)
        self.label_17 = QtWidgets.QLabel(self.frame_Buttons)
        self.label_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_9.addWidget(self.label_17)
        self.line_9 = QtWidgets.QFrame(self.frame_Buttons)
        self.line_9.setMaximumSize(QtCore.QSize(2, 16777215))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayout_9.addWidget(self.line_9)
        self.label_18 = QtWidgets.QLabel(self.frame_Buttons)
        self.label_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_9.addWidget(self.label_18)
        self.horizontalLayout_10.addWidget(self.frame_Buttons)
        self.horizontalLayout_4.addWidget(self.frame_9)
        spacerItem2 = QtWidgets.QSpacerItem(308, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.frame_10 = QtWidgets.QFrame(self.centralwidget)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_10.setMaximumSize(QtCore.QSize(260, 16777215))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setContentsMargins(0, 0, 5, 2)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_Search = QtWidgets.QFrame(self.frame_10)
        self.frame_Search.setStyleSheet("#frame_Search{\n"
"    background:#ECF0F1;\n"
"    border-radius:17px;\n"
"    opacity:0.5;\n"
"}\n"
"#frame_Search QLineEdit{\n"
"    background:#ECF0F1;\n"
"    border-radius:17px;\n"
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
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_Search)
        self.horizontalLayout_11.setContentsMargins(6, 0, 9, 0)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_Search)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_11.addWidget(self.lineEdit)
        self.line_5 = QtWidgets.QFrame(self.frame_Search)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_11.addWidget(self.line_5)
        self.label_13 = QtWidgets.QLabel(self.frame_Search)
        self.label_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_11.addWidget(self.label_13)
        self.horizontalLayout_12.addWidget(self.frame_Search)
        self.horizontalLayout_4.addWidget(self.frame_10)
        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(2, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setMaximumSize(QtCore.QSize(16777215, 5))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.verticalLayout.addWidget(self.line_12)
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
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
        self.line_2 = QtWidgets.QFrame(self.frame_8)
        self.line_2.setMaximumSize(QtCore.QSize(5, 16777215))
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.label_11 = QtWidgets.QLabel(self.frame_8)
        self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.label_19 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_3.addWidget(self.label_19)
        spacerItem3 = QtWidgets.QSpacerItem(681, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label_8 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_8.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.verticalLayout.addWidget(self.frame_8)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setMaximumSize(QtCore.QSize(16777215, 5))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.frame_11 = QtWidgets.QFrame(self.centralwidget)
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
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setMaximumSize(QtCore.QSize(16777215, 5))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
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
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 736, 565))
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
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_5.setStretch(0, 1)
        SBCclient.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SBCclient)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 878, 23))
        self.menubar.setObjectName("menubar")
        SBCclient.setMenuBar(self.menubar)

        self.retranslateUi(SBCclient)
        QtCore.QMetaObject.connectSlotsByName(SBCclient)

    def retranslateUi(self, SBCclient):
        _translate = QtCore.QCoreApplication.translate
        SBCclient.setWindowTitle(_translate("SBCclient", "小黑云客户端"))
        self.label.setText(_translate("SBCclient", "小黑云"))
        self.label_2.setText(_translate("SBCclient", "文件"))
        self.label_3.setText(_translate("SBCclient", "图片"))
        self.label_4.setText(_translate("SBCclient", "视频"))
        self.label_5.setText(_translate("SBCclient", "分享"))
        self.label_6.setText(_translate("SBCclient", "传输列表"))
        self.label_7.setText(_translate("SBCclient", "10.1GB/6.0T"))
        self.label_9.setText(_translate("SBCclient", "用户"))
        self.label_14.setText(_translate("SBCclient", "下载"))
        self.label_15.setText(_translate("SBCclient", "上传"))
        self.label_16.setText(_translate("SBCclient", "重命名"))
        self.label_17.setText(_translate("SBCclient", "更多"))
        self.label_18.setText(_translate("SBCclient", "切换网盘"))
        self.lineEdit.setPlaceholderText(_translate("SBCclient", "搜索网盘文件"))
        self.label_13.setText(_translate("SBCclient", "搜索"))
        self.label_12.setText(_translate("SBCclient", "<"))
        self.label_11.setText(_translate("SBCclient", "Home"))
        self.label_19.setText(_translate("SBCclient", ">"))
        self.label_8.setText(_translate("SBCclient", "..."))
        self.label_20.setText(_translate("SBCclient", "文件名"))
        self.label_21.setText(_translate("SBCclient", "修改时间"))
        self.label_22.setText(_translate("SBCclient", "大小"))
        self.label_27.setText(_translate("SBCclient", "con"))
        self.label_28.setText(_translate("SBCclient", "File1"))
        self.label_29.setText(_translate("SBCclient", "2020-03-02"))
        self.label_30.setText(_translate("SBCclient", "100MB"))

