# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReName.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(434, 353)
        Form.setLayoutDirection(QtCore.Qt.RightToLeft)
        Form.setStyleSheet("#Form\n"
"{\n"
"    background:white;\n"
"    border:none;\n"
"}\n"
"#scrollArea_7\n"
"{\n"
"    background:white;\n"
"    border:none;\n"
"}\n"
"\n"
"#scrollAreaWidgetContents_7 QFrame:hover{\n"
"    background:#D0D3D4;\n"
"    border-radius:22px;\n"
"    opacity:0.5;\n"
"    }")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(9, 9, -1, 20)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(114, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(180, 180))
        self.label.setMaximumSize(QtCore.QSize(180, 180))
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(114, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame)
        spacerItem2 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setMinimumSize(QtCore.QSize(400, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(400, 30))
        self.lineEdit.setStyleSheet("#lineEdit\n"
"{\n"
"    background:#EAEDED;\n"
"    border:1px groove #566573;\n"
"    border-style: outset;\n"
"    border-radius:12px;\n"
"}\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(60, 30))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "重命名"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.pushButton.setText(_translate("Form", "确定"))
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = QMainWindow()
    Ui = Ui_Form()
    Ui.setupUi(Main)




    # SBCMain = SBCMain.initFrame()
    Main.show()
    sys.exit(app.exec_())
