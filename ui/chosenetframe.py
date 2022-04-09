# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chosenetframe.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.frame_ChoseNet = QtWidgets.QFrame(Form)
        self.frame_ChoseNet.setGeometry(QtCore.QRect(120, 50, 101, 171))
        self.frame_ChoseNet.setStyleSheet("#frame_ChoseNet\n"
"{\n"
"    background:#D0D3D4;\n"
"}\n"
"\n"
"#frame_ChoseNet QLabel:hover{\n"
"    background:#A2D9CE;\n"
"    \n"
"    opacity:0.5;\n"
"    }")
        self.frame_ChoseNet.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ChoseNet.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ChoseNet.setObjectName("frame_ChoseNet")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_ChoseNet)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_ChoseNet)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_ChoseNet)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_ChoseNet)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "小黑云"))
        self.label_2.setText(_translate("Form", "百度云"))
        self.label_3.setText(_translate("Form", "阿里云"))

