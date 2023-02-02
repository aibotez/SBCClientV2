from SubUi import Registerui
import os,wmi,sys
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QAction,QFileDialog,QDialog
from SubUi import Loginui1


class RegisterUi(Registerui.Ui_Dialog):
    def __init__(self,ui):
        super().__init__()
        self.ui = ui

    def regiact(self):
        self.UserName = self.lineEdit_6.text()
        self.UserEmail = self.lineEdit_9.text()
        self.Vcode = self.lineEdit_8.text()
        self.UserPassword = self.lineEdit_10.text()
        self.UserPassword_2 = self.lineEdit_7.text()
    def GetVcode(self):
        pass
    def HaveCount(self,e):
        # self.ui.SBCLoginWindowDialog.show()
        self.ui.SBCRegiWindowDialog.hide()
        Loginui = Loginui1.LoginUi(self.ui)
        Loginui.Login()
    def Regi(self,e):
        self.ui.SBCLoginWindowDialog.hide()
        self.ui.SBCRegiWindowDialog = QDialog()
        # self.ui.SBCLoginWindowDialog.setWindowModality(Qt.ApplicationModal)
        self.ui.SBCRegiWindow = self.setupUi(self.ui.SBCRegiWindowDialog)
        # self.ui.SBCLoginWindowDialog.setStyleSheet("#Dialog{border-image:url(img/login.jpg)}")
        self.ui.SBCRegiWindowDialog.show()
        self.pushButton.clicked.connect(self.regiact)
        self.pushButton_3.clicked.connect(self.GetVcode)
        self.label_4.mousePressEvent = self.HaveCount


        self.ui.SBCRegiWindowDialog.exec_()