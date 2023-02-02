from . import Loginui
import os,wmi
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QAction,QFileDialog,QDialog

class LoginUi(Loginui.Ui_Dialog):
    def __init__(self,ui):
        super().__init__()
        self.ui = ui
        self.s = wmi.WMI()
        self.LoginStatu = 0

    # def init(self):
    #     self.Dialog.setStyleSheet("#Dialog{\n"
    #                          "    border-image:url(login.jpg)\n"
    #                          "}")
    def get_mainboard_info(self):
        mainboard = []
        for board_id in self.s.Win32_BaseBoard():
            mainboard.append(board_id.SerialNumber.strip().strip('.'))
        return mainboard[0]
    def WRUserLoginInfo(self):
        path = 'uci/uci'
        if not os.path.isdir('uci'):
            os.mkdir('uci')
        with open(path, 'w') as f:
            f.write(self.get_mainboard_info() + '#' + self.UserCount + '#' + self.Password)
    def loginact(self):
        self.UserCount = self.lineEdit.text()
        self.Password = self.lineEdit_2.text()
        if self.UserCount and self.Password:
            data = {
                'usercount':self.UserCount,
                'userpassword':self.Password
            }
            LginRes = self.ui.SBCRe.Login(data)
            if LginRes:
                self.LoginStatu = 1
                self.WRUserLoginInfo()
                self.ui.SBCLoginWindowDialog.destroy()
    def Login(self):
        self.ui.SBCLoginWindowDialog = QDialog()
        self.ui.SBCLoginWindow = self.setupUi(self.ui.SBCLoginWindowDialog)
        # self.ui.SBCLoginWindowDialog.setStyleSheet("#Dialog{border-image:url(img/login.jpg)}")
        self.ui.SBCLoginWindowDialog.show()

        self.pushButton.clicked.connect(self.loginact)

        self.ui.SBCLoginWindowDialog.exec_()



