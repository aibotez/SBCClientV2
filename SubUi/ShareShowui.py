# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShareShow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(784, 627)
        Form.setStyleSheet("")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setStyleSheet("#tabWidget{\n"
"    background:#ffffff;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_14 = QtWidgets.QFrame(self.tab)
        self.frame_14.setStyleSheet("#frame_14\n"
"{\n"
"    background:#ffffff;\n"
"}\n"
"")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_17 = QtWidgets.QLabel(self.frame_14)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout.addWidget(self.label_17)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_14)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(303, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_13.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout.addWidget(self.pushButton_13)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 15)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.verticalLayout.addWidget(self.frame_14)
        spacerItem1 = QtWidgets.QSpacerItem(20, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setStyleSheet("#frame{\n"
"    background:#FDFEFE;\n"
"}\n"
"#frame QPushButton{\n"
"    background:#637dff;\n"
"    color:#ffffff;\n"
"    border-radius:12px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_15.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_2.addWidget(self.pushButton_15)
        spacerItem2 = QtWidgets.QSpacerItem(22, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_14.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet("#pushButton_14{\n"
"    background:#85929E;\n"
"    color:#ffffff;\n"
"}")
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_2.addWidget(self.pushButton_14)
        self.horizontalLayout_2.setStretch(0, 6)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(3, 1)
        self.verticalLayout.addWidget(self.frame)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.frame_11 = QtWidgets.QFrame(self.tab)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 41))
        self.frame_11.setStyleSheet("#frame_11 QLabel\n"
"{\n"
"    color:#979A9A;\n"
"    font-size:15px;\n"
"}")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_3.setContentsMargins(9, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame_11)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(414, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.line_10 = QtWidgets.QFrame(self.frame_11)
        self.line_10.setMaximumSize(QtCore.QSize(5, 16777215))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.horizontalLayout_3.addWidget(self.line_10)
        self.label_40 = QtWidgets.QLabel(self.frame_11)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_3.addWidget(self.label_40)
        self.line_11 = QtWidgets.QFrame(self.frame_11)
        self.line_11.setMaximumSize(QtCore.QSize(5, 16777215))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.horizontalLayout_3.addWidget(self.line_11)
        self.label_41 = QtWidgets.QLabel(self.frame_11)
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_3.addWidget(self.label_41)
        self.horizontalLayout_3.setStretch(0, 12)
        self.horizontalLayout_3.setStretch(2, 3)
        self.horizontalLayout_3.setStretch(4, 3)
        self.verticalLayout.addWidget(self.frame_11)
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setStyleSheet("#scrollAreaWidgetContents{\n"
"    background:#ffffff;\n"
"}\n"
"#scrollAreaWidgetContents QFrame:hover{\n"
"    background:#D0D3D4;\n"
"    border-radius:18px;\n"
"    opacity:0.5;\n"
"    }")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 776, 482))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.frame_13 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_13.setMinimumSize(QtCore.QSize(0, 36))
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 36))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_17.setContentsMargins(3, 0, 9, 0)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_18.addWidget(self.checkBox_2)
        self.label_32 = QtWidgets.QLabel(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setMinimumSize(QtCore.QSize(30, 30))
        self.label_32.setMaximumSize(QtCore.QSize(30, 30))
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_18.addWidget(self.label_32)
        self.label_36 = QtWidgets.QLabel(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        self.label_36.setMinimumSize(QtCore.QSize(0, 30))
        self.label_36.setMaximumSize(QtCore.QSize(16777215, 36))
        self.label_36.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_18.addWidget(self.label_36)
        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(1, 1)
        self.horizontalLayout_18.setStretch(2, 20)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_18)
        self.label_37 = QtWidgets.QLabel(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_17.addWidget(self.label_37)
        self.label_38 = QtWidgets.QLabel(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_17.addWidget(self.label_38)
        self.horizontalLayout_17.setStretch(0, 7)
        self.horizontalLayout_17.setStretch(1, 2)
        self.horizontalLayout_17.setStretch(2, 2)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.frame_13)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 20)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("#scrollArea_2\n"
"{\n"
"    background:white;\n"
"    border:none;\n"
"}\n"
"#tab_2\n"
"{\n"
"    background:white;\n"
"    border:none;\n"
"}")
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_20 = QtWidgets.QFrame(self.tab_2)
        self.frame_20.setStyleSheet("#frame_20\n"
"{\n"
"    background:#E5E7E9;\n"
"}")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_13.setContentsMargins(6, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_25 = QtWidgets.QLabel(self.frame_20)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_13.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(self.frame_20)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_13.addWidget(self.label_26)
        spacerItem4 = QtWidgets.QSpacerItem(303, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem4)
        self.frame_21 = QtWidgets.QFrame(self.frame_20)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_10.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_14.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_11.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_14.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_12.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_14.addWidget(self.pushButton_12)
        self.horizontalLayout_13.addWidget(self.frame_21)
        self.verticalLayout_12.addWidget(self.frame_20)
        self.scrollArea_8 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_8.setStyleSheet("#scrollAreaWidgetContents_8\n"
"{\n"
"    background:white;\n"
"    border:none;\n"
"}\n"
"#scrollArea_8\n"
"{\n"
"    background:white;\n"
"    border:none;\n"
"}\n"
"\n"
"#scrollAreaWidgetContents_8 QFrame:hover{\n"
"    background:#D0D3D4;\n"
"    border-radius:22px;\n"
"    opacity:0.5;\n"
"    }\n"
"")
        self.scrollArea_8.setLineWidth(0)
        self.scrollArea_8.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollArea_8.setObjectName("scrollArea_8")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 776, 560))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.formLayout_4 = QtWidgets.QFormLayout(self.scrollAreaWidgetContents_8)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setSpacing(0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_22 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem5 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem5)
        self.label_34 = QtWidgets.QLabel(self.frame_22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setMinimumSize(QtCore.QSize(30, 30))
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_15.addWidget(self.label_34)
        self.frame_23 = QtWidgets.QFrame(self.frame_22)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_14.setContentsMargins(0, 8, 0, 8)
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_27 = QtWidgets.QLabel(self.frame_23)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_14.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.frame_23)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_14.addWidget(self.label_28)
        self.horizontalLayout_15.addWidget(self.frame_23)
        spacerItem6 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem6)
        self.frame_24 = QtWidgets.QFrame(self.frame_22)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_24)
        self.verticalLayout_15.setContentsMargins(0, 15, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.progressBar_5 = QtWidgets.QProgressBar(self.frame_24)
        self.progressBar_5.setMinimumSize(QtCore.QSize(0, 0))
        self.progressBar_5.setMaximumSize(QtCore.QSize(16777215, 15))
        self.progressBar_5.setProperty("value", 24)
        self.progressBar_5.setObjectName("progressBar_5")
        self.verticalLayout_15.addWidget(self.progressBar_5)
        self.label_29 = QtWidgets.QLabel(self.frame_24)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_15.addWidget(self.label_29)
        self.horizontalLayout_15.addWidget(self.frame_24)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem7)
        self.frame_25 = QtWidgets.QFrame(self.frame_22)
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_25)
        self.horizontalLayout_16.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_30 = QtWidgets.QLabel(self.frame_25)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_16.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(self.frame_25)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_16.addWidget(self.label_31)
        self.label_35 = QtWidgets.QLabel(self.frame_25)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_16.addWidget(self.label_35)
        self.horizontalLayout_15.addWidget(self.frame_25)
        spacerItem8 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem8)
        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 6)
        self.horizontalLayout_15.setStretch(2, 10)
        self.horizontalLayout_15.setStretch(3, 1)
        self.horizontalLayout_15.setStretch(4, 10)
        self.horizontalLayout_15.setStretch(5, 1)
        self.horizontalLayout_15.setStretch(6, 5)
        self.horizontalLayout_15.setStretch(7, 1)
        self.verticalLayout_13.addWidget(self.frame_22)
        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.line_4.setMinimumSize(QtCore.QSize(649, 0))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_13.addWidget(self.line_4)
        self.formLayout_4.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.verticalLayout_13)
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)
        self.verticalLayout_12.addWidget(self.scrollArea_8)
        self.gridLayout_4.addLayout(self.verticalLayout_12, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "文件分享"))
        self.label_17.setText(_translate("Form", "分享链接："))
        self.pushButton_13.setText(_translate("Form", "确认"))
        self.label.setText(_translate("Form", "用户分享的文件"))
        self.pushButton_15.setText(_translate("Form", "保存"))
        self.pushButton_14.setText(_translate("Form", "下载"))
        self.label_2.setText(_translate("Form", "TextLabel"))
        self.label_40.setText(_translate("Form", "修改时间"))
        self.label_41.setText(_translate("Form", "大小"))
        self.label_32.setText(_translate("Form", "con"))
        self.label_36.setText(_translate("Form", "File1"))
        self.label_37.setText(_translate("Form", "2020-03-02"))
        self.label_38.setText(_translate("Form", "100MB"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "文件分享"))
        self.label_25.setText(_translate("Form", "总上传个数："))
        self.label_26.setText(_translate("Form", "6"))
        self.pushButton_10.setText(_translate("Form", "全部开始"))
        self.pushButton_11.setText(_translate("Form", "全部暂停"))
        self.pushButton_12.setText(_translate("Form", "全部取消"))
        self.label_34.setText(_translate("Form", "con"))
        self.label_27.setText(_translate("Form", "5K.mat"))
        self.label_28.setText(_translate("Form", "752KB/19.95MB"))
        self.label_29.setText(_translate("Form", "暂停"))
        self.label_30.setText(_translate("Form", ">"))
        self.label_31.setText(_translate("Form", "X"))
        self.label_35.setText(_translate("Form", "[]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "跨盘互传"))

