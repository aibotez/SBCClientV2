# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Move.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(460, 420)
        Dialog.setMinimumSize(QtCore.QSize(460, 420))
        Dialog.setMaximumSize(QtCore.QSize(460, 420))
        Dialog.setStyleSheet("#Dialog\n"
"{\n"
"    background:#FDFEFE;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(9, 0, 9, 12)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 10)
        self.verticalLayout.addWidget(self.frame)
        # self.treeView = QtWidgets.QTreeView(Dialog)
        self.treeView = QtWidgets.QTreeWidget(Dialog)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setStyleSheet("#label{\n"
"    color:#5555ff;\n"
"}")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(359, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(80, 30))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("#pushButton\n"
"{\n"
"    background:#637dff;\n"
"    color:#ffffff;\n"
"    border-radius:8px;\n"
"\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(33, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 20)
        self.horizontalLayout_3.setStretch(3, 2)
        self.horizontalLayout_3.setStretch(4, 1)
        self.verticalLayout.addWidget(self.frame_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "移动文件到"))
        self.label_2.setText(_translate("Dialog", "当前选择路径："))
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.label.setText(_translate("Dialog", "新建文件夹"))
        self.pushButton.setText(_translate("Dialog", "移动到此处"))

