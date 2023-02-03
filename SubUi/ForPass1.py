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
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_func)

    def update_func(self):
        dt = time.time()-self.time0
        if dt >= 60:
            self.pushButton_3.setEnabled(True)
            self.timer.stop()
            self.pushButton_3.setText('获取验证码')
            return
        self.pushButton_3.setText(str(int(dt))+'s后重试')
    def GetVcode(self):
        if '@' not in self.lineEdit_6.text():
            self.label_6.setText('输入邮箱')
            return
        self.pushButton_3.setEnabled(False)
        self.timer.start(1000)
        self.time0 = time.time()
        self.ui.SBCRe.GetVcode({'useremail':self.lineEdit_6.text()})
    def Lgin(self,e):
        # self.ui.SBCLoginWindowDialog.show()
        self.ui.SBCForPassWindowDialog.hide()
        Loginui = Loginui1.LoginUi(self.ui)
        Loginui.Login()
    def ForPassact(self):
        pass
    def ForPass(self,e):
        self.ui.SBCLoginWindowDialog.hide()
        self.ui.SBCForPassWindowDialog = QDialog()
        # self.ui.SBCLoginWindowDialog.setWindowModality(Qt.ApplicationModal)
        self.ui.SBCRegiWindow = self.setupUi(self.ui.SBCForPassWindowDialog)
        # self.ui.SBCForPassWindowDialog.resize(1000, 870)
        # self.frame_9.setMaximumSize(QtCore.QSize(16777215, 55))
        # self.ui.SBCLoginWindowDialog.setStyleSheet("#Dialog{border-image:url(img/login.jpg)}")
        self.ui.SBCForPassWindowDialog.show()
        self.label_4.mousePressEvent = self.Lgin
        self.pushButton.clicked.connect(self.ForPassact)
        self.pushButton_3.clicked.connect(self.GetVcode)
        # self.label_4.mousePressEvent = self.HaveCount
        # self.lineEdit_7.setEchoMode(QLineEdit.Password)
        # self.lineEdit_10.setEchoMode(QLineEdit.Password)
        self.ui.SBCForPassWindowDialog.exec_()
