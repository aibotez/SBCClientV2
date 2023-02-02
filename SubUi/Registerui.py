# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(777, 570)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("#Dialog{\n"
"    border-image:url(img/login.jpg)\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(-1, 60, 20, -1)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("#frame{\n"
"    background:rgba(5,9,20,0.5);\n"
"    color:#ffffff;\n"
"    border-radius:16px;\n"
"}\n"
"#frame QLabel{\n"
"\n"
"    color:#ffffff;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(30, 9, 30, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("#label{\n"
"    color:#1f6671;\n"
"    color:#bfbfbf;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setMinimumSize(QtCore.QSize(0, 20))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_6.setStyleSheet("#label_6{\n"
"    color:#ff0000;\n"
"}")
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setStyleSheet("#frame_8 QFrame{\n"
"    background:#ffffff;\n"
"    border:1px groove gray;\n"
"    border-radius:10px;\n"
"    \n"
"}\n"
"#frame_8 QLineEdit{\n"
"    border:none;\n"
"}\n"
"#frame_8 QLabel{\n"
"    border:none;\n"
"    color:#ffffff;\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_9.setStyleSheet("#frame_2{\n"
"    background:#ffffff;\n"
"    border:1px groove gray;\n"
"    border-radius:10px;\n"
"    \n"
"}\n"
"#frame_2 QLineEdit{\n"
"    border:none;\n"
"}\n"
"#frame_2 QLabel{\n"
"    border:none;\n"
"}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.frame_9)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setText("")
        self.lineEdit_6.setReadOnly(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_8.addWidget(self.lineEdit_6)
        self.verticalLayout.addWidget(self.frame_9)
        self.frame_13 = QtWidgets.QFrame(self.frame_8)
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_13.setStyleSheet("#frame_3{\n"
"    background:#ffffff;\n"
"    border:1px groove gray;\n"
"    border-radius:10px;\n"
"    \n"
"}\n"
"#frame_3 QLineEdit{\n"
"    border:none;\n"
"}\n"
"")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_11 = QtWidgets.QLabel(self.frame_13)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_12.addWidget(self.label_11)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_13)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_12.addWidget(self.lineEdit_9)
        self.verticalLayout.addWidget(self.frame_13)
        self.frame_11 = QtWidgets.QFrame(self.frame_8)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_11.setStyleSheet("#frame_11{\n"
"    background-color: rgba(255, 132, 139, 0);\n"
"    border:none;\n"
"}")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_12.setStyleSheet("#frame_6{\n"
"    background:#ffffff;\n"
"    border:1px groove gray;\n"
"    border-radius:10px;\n"
"    \n"
"}\n"
"#frame_6 QLineEdit{\n"
"    border:none;\n"
"}\n"
"")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setContentsMargins(30, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_11.addWidget(self.lineEdit_8)
        self.horizontalLayout_10.addWidget(self.frame_12)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("#pushButton_3{\n"
"    background:#cacaca;\n"
"    border-radius:6px;\n"
"    color:#55557f;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_10.addWidget(self.pushButton_3)
        self.horizontalLayout_10.setStretch(0, 3)
        self.horizontalLayout_10.setStretch(1, 1)
        self.verticalLayout.addWidget(self.frame_11)
        self.frame_14 = QtWidgets.QFrame(self.frame_8)
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_14.setStyleSheet("#frame_4{\n"
"    background:#ffffff;\n"
"    border:1px groove gray;\n"
"    border-radius:10px;\n"
"    \n"
"}\n"
"#frame_4 QLineEdit{\n"
"    border:none;\n"
"}\n"
"")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_13.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_12 = QtWidgets.QLabel(self.frame_14)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_13.addWidget(self.label_12)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_14)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_13.addWidget(self.lineEdit_10)
        self.verticalLayout.addWidget(self.frame_14)
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_10.setStyleSheet("#frame_10{\n"
"    background:#ffffff;\n"
"    border:1px groove gray;\n"
"    border-radius:10px;\n"
"    \n"
"}\n"
"#frame_10 QLineEdit{\n"
"    border:none;\n"
"}\n"
"")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.frame_10)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_9.addWidget(self.lineEdit_7)
        self.verticalLayout.addWidget(self.frame_10)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(9, 0, -1, -1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setStyleSheet("#label_4{\n"
"    color:#5555ff;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("#pushButton{\n"
"    background:#00aa7f;\n"
"    border-radius:6px;\n"
"    color:#ffffff;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_3.setStretch(1, 10)
        self.horizontalLayout_3.setStretch(2, 3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 5)
        self.verticalLayout_2.setStretch(3, 1)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("#label_7{\n"
"    color:#ffffff;\n"
"}")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 2)
        self.gridLayout.setColumnStretch(0, 10)
        self.gridLayout.setColumnStretch(1, 9)
        self.gridLayout.setRowStretch(0, 10)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "小黑云登录"))
        self.label.setText(_translate("Dialog", "小黑云账号注册"))
        self.label_9.setText(_translate("Dialog", "con"))
        self.lineEdit_6.setPlaceholderText(_translate("Dialog", "用户名"))
        self.label_11.setText(_translate("Dialog", "con"))
        self.lineEdit_9.setPlaceholderText(_translate("Dialog", "邮箱"))
        self.lineEdit_8.setPlaceholderText(_translate("Dialog", "验证码"))
        self.pushButton_3.setText(_translate("Dialog", "获取验证码"))
        self.label_12.setText(_translate("Dialog", "con"))
        self.lineEdit_10.setPlaceholderText(_translate("Dialog", "密码"))
        self.label_10.setText(_translate("Dialog", "con"))
        self.lineEdit_7.setPlaceholderText(_translate("Dialog", "再次输入密码"))
        self.label_4.setText(_translate("Dialog", "已有账号"))
        self.pushButton.setText(_translate("Dialog", "注册"))
        self.label_7.setText(_translate("Dialog", "Ver 2.0.0 Copyright by zz"))

