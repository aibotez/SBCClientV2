from SubUi import ForPassui
import os,wmi,sys,time,threading
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.Qt import *
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
        self.ui.SBCLoginWindowDialog.show()
        Loginui = Loginui1.LoginUi(self.ui)
        Loginui.Login()
    def ForPassact(self):
        self.UserEmail = self.lineEdit_6.text()
        self.Vcode = self.lineEdit_8.text()
        self.UserPassword = self.lineEdit_10.text()
        self.UserPassword_2 = self.lineEdit_7.text()
        if self.UserPassword != self.UserPassword_2:
            self.label_6.setText('两次输入密码不一致')
            return
        if not self.Vcode:
            self.label_6.setText('验证码为空')
            return
        if not self.UserEmail or not self.Vcode or not self.UserPassword or not self.UserPassword_2:
            self.label_6.setText('信息不全')
            return

        data = {
            'useremail':self.UserEmail,
            'Vcode':self.Vcode,
            'password':self.UserPassword,
            'client':'windows'
        }
        Res = self.ui.SBCRe.ForPass(data)
        if Res == '1':
            self.Lgin(0)
        else:
            self.label_6.setText(Res)
    def ForPass(self,e):

        self.ui.SBCLoginWindowDialog.hide()
        self.ui.SBCForPassWindowDialog = QDialog()
        # self.ui.SBCLoginWindowDialog.setWindowModality(Qt.ApplicationModal)
        self.ui.SBCRegiWindow = self.setupUi(self.ui.SBCForPassWindowDialog)
        self.label_7.setText('Ver {} Copyright by zz'.format(self.ui.Version))
        # self.ui.SBCForPassWindowDialog.resize(1000, 870)
        # self.frame_9.setMaximumSize(QtCore.QSize(16777215, 55))
        self.ui.SBCForPassWindowDialog.setStyleSheet("#Dialog{border-image:url(img/login.jpg)}")
        # palette = QPalette()
        # pix = QPixmap("img/login.jpg")
        # # palette.drawPixmap(self.ui.SBCForPassWindowDialog.rect(), pix)
        # palette.setBrush(self.ui.SBCForPassWindowDialog.backgroundRole(), QBrush(pix))
        # self.ui.SBCForPassWindowDialog.setPalette(palette)
        # self.ui.SBCForPassWindowDialog.setAutoFillBackground(True)



        self.ui.SBCForPassWindowDialog.show()
        self.label_4.mousePressEvent = self.Lgin
        self.pushButton.clicked.connect(self.ForPassact)
        self.pushButton_3.clicked.connect(self.GetVcode)
        # self.label_4.mousePressEvent = self.HaveCount
        # self.lineEdit_7.setEchoMode(QLineEdit.Password)
        # self.lineEdit_10.setEchoMode(QLineEdit.Password)
        self.ui.SBCForPassWindowDialog.exec_()
