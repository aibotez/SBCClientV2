from SubUi import Registerui
import os,wmi,sys,time,threading
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QAction,QFileDialog,QDialog,QLineEdit
from SubUi import Loginui1


class RegisterUi(Registerui.Ui_Dialog):
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
        # time.sleep(1)

    def regiact(self):
        self.UserName = self.lineEdit_6.text()
        self.UserEmail = self.lineEdit_9.text()
        self.Vcode = self.lineEdit_8.text()
        self.UserPassword = self.lineEdit_10.text()
        self.UserPassword_2 = self.lineEdit_7.text()
        if self.UserPassword != self.UserPassword_2:
            self.label_6.setText('两次输入密码不一致')
            return
        data = {
            'username':self.UserName,
            'useremail':self.UserEmail,
            'vcode':self.Vcode,
            'userpassword1':self.UserPassword,
            'userpassword2': self.UserPassword_2
        }
        RegRes = self.ui.SBCRe.Register(data)
        if RegRes == 1:
            self.ui.SBCRegiWindowDialog.hide()
            Loginui = Loginui1.LoginUi(self.ui)
            Loginui.Login()
        else:
            self.label_6.setText(RegRes)

    def GetVcode(self):
        if '@' not in self.lineEdit_9.text():
            self.label_6.setText('输入邮箱')
            return
        self.pushButton_3.setEnabled(False)
        self.timer.start(1000)
        self.time0 = time.time()
        self.ui.SBCRe.GetVcode({'useremail':self.lineEdit_9.text()})

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
        self.label_7.setText('Ver {} Copyright by zz'.format(self.ui.Version))
        # self.ui.SBCRegiWindowDialog.resize(1000, 870)
        # self.frame_9.setMaximumSize(QtCore.QSize(16777215, 55))
        # self.ui.SBCLoginWindowDialog.setStyleSheet("#Dialog{border-image:url(img/login.jpg)}")
        self.ui.SBCRegiWindowDialog.show()
        self.pushButton.clicked.connect(self.regiact)
        self.pushButton_3.clicked.connect(self.GetVcode)
        self.label_4.mousePressEvent = self.HaveCount
        self.lineEdit_7.setEchoMode(QLineEdit.Password)
        self.lineEdit_10.setEchoMode(QLineEdit.Password)


        self.ui.SBCRegiWindowDialog.exec_()