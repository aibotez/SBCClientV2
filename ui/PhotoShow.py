# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PhotoShow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SBCclient(object):
    def setupUi(self, SBCclient):
        SBCclient.setObjectName("SBCclient")
        SBCclient.resize(862, 706)
        SBCclient.setMinimumSize(QtCore.QSize(800, 700))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        SBCclient.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SBCclient.setWindowIcon(icon)
        SBCclient.setWindowOpacity(1.0)
        SBCclient.setStyleSheet("\n"
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
"}")
        SBCclient.setAnimated(True)
        SBCclient.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(SBCclient)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.frame_PhotoShow = QtWidgets.QFrame(self.centralwidget)
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
        self.label_8.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
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
        self.scrollAreaPhotoShow.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
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
        SBCclient.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SBCclient)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 862, 23))
        self.menubar.setObjectName("menubar")
        SBCclient.setMenuBar(self.menubar)

        self.retranslateUi(SBCclient)
        QtCore.QMetaObject.connectSlotsByName(SBCclient)

    def retranslateUi(self, SBCclient):
        _translate = QtCore.QCoreApplication.translate
        SBCclient.setWindowTitle(_translate("SBCclient", "小黑云客户端"))
        self.label_11.setText(_translate("SBCclient", "图片"))
        self.label_8.setText(_translate("SBCclient", "..."))
        self.label_20.setText(_translate("SBCclient", "文件名"))
        self.label_21.setText(_translate("SBCclient", "修改时间"))
        self.label_22.setText(_translate("SBCclient", "大小"))
        self.label_27.setText(_translate("SBCclient", "con"))
        self.label_28.setText(_translate("SBCclient", "File1"))
        self.label_29.setText(_translate("SBCclient", "2020-03-02"))
        self.label_30.setText(_translate("SBCclient", "100MB"))

