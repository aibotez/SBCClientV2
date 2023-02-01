from . import Settingui
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
import sip
from PyQt5.QtGui import QFontMetrics,QCursor, QIcon
from PyQt5.QtCore import *


class SettingShow(Settingui.Ui_Dialog):
    def __init__(self,Dialog):
        super().__init__()
        self.Dialog = Dialog
        self.init()
    def init(self):
        self.setupUi(self.Dialog)
        self.label_2.setText('')
        self.label_3.setText('')
        self.label_5.setText('')
        self.label_7.setText('')
        self.label_16.setText('')
        self.label_22.setText('')
        self.label_25.setText('')
        self.label_35.setText('')
        self.label_36.setText('')

        # self.tabWidget.tab().hide()
        # self.tabWidget.tab_2().hide()
        # self.tabWidget.tab_3().hide()
        # self.tabWidget.tab_4().hide()
        self.tabWidget.removeTab(3)
        self.tabWidget.removeTab(2)
        self.tabWidget.removeTab(1)
        self.tabWidget.removeTab(0)

        self.label.mousePressEvent = partial(self.NavOper,'NetCon')
        self.label_4.mousePressEvent = partial(self.NavOper, 'UpDOwn')
        self.label_6.mousePressEvent = partial(self.NavOper, 'Syn')
        self.label_8.mousePressEvent = partial(self.NavOper, 'Other')

    def ClearNavStyle(self):
        self.frame.setStyleSheet("")
        self.frame_2.setStyleSheet("")
        self.frame_3.setStyleSheet("")
        self.frame_4.setStyleSheet("")
    def NavOper(self,oper,e):
        self.ClearNavStyle()
        if oper == 'NetCon':
            self.tabWidget.setCurrentIndex(0)
            self.frame.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")
        elif oper == 'UpDOwn':
            self.tabWidget.setCurrentIndex(1)
            self.frame_2.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")
        elif oper == 'Syn':
            self.tabWidget.setCurrentIndex(2)
            self.frame_3.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")
        elif oper == 'Other':
            self.tabWidget.setCurrentIndex(3)
            self.frame_4.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")

