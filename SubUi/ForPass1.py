from SubUi import ForPassui
import os,wmi,sys,time,threading
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QAction,QFileDialog,QDialog,QLineEdit
from SubUi import Loginui1


class ForPassUi(ForPassui.Ui_Dialog):
    def __init__(self,ui):
        super().__init__()
        self.ui = ui
    def ForPass(self,e):
        self.ui.SBCLoginWindowDialog.hide()
        self.ui.SBCForPassWindowDialog = QDialog()
        # self.ui.SBCLoginWindowDialog.setWindowModality(Qt.ApplicationModal)
        self.ui.SBCRegiWindow = self.setupUi(self.ui.SBCForPassWindowDialog)
        # self.ui.SBCForPassWindowDialog.resize(1000, 870)
        # self.frame_9.setMaximumSize(QtCore.QSize(16777215, 55))
        # self.ui.SBCLoginWindowDialog.setStyleSheet("#Dialog{border-image:url(img/login.jpg)}")
        self.ui.SBCForPassWindowDialog.show()
        # self.pushButton.clicked.connect(self.regiact)
        # self.pushButton_3.clicked.connect(self.GetVcode)
        # self.label_4.mousePressEvent = self.HaveCount
        # self.lineEdit_7.setEchoMode(QLineEdit.Password)
        # self.lineEdit_10.setEchoMode(QLineEdit.Password)
        self.ui.SBCForPassWindowDialog.exec_()
