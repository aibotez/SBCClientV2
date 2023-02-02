from . import Loginui
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QAction,QFileDialog,QDialog

class LoginUi(Loginui.Ui_Dialog):
    def __init__(self,ui):
        super().__init__()
        self.ui = ui
        self.LoginStatu = 0

    # def init(self):
    #     self.Dialog.setStyleSheet("#Dialog{\n"
    #                          "    border-image:url(login.jpg)\n"
    #                          "}")
    def Login(self):
        self.ui.SBCLoginWindowDialog = QDialog()
        self.ui.SBCLoginWindow = self.setupUi(self.ui.SBCLoginWindowDialog)
        # self.ui.SBCLoginWindowDialog.setStyleSheet("#Dialog{border-image:url(img/login.jpg)}")
        self.ui.SBCLoginWindowDialog.show()
        self.ui.SBCLoginWindowDialog.exec_()



