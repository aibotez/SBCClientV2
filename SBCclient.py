import sys,base64
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import SBCMainWindow
import time

import os,hashlib




class EventDeals():
    def __init__(self):
        pass
    def DownDeal(self,e):
        pass
    def UpDeal(self,e):
        pass
    def ReameDeal(self,e):
        pass
    def MoreDeal(self,e):
        pass
    def ChooseNetDeal(self,e):
        pass
    def SearchDeal(self,e):
        pass
    def NetBackDeal(self,e):
        pass
    def NetRefresh(self,e):
        pass
    def FileClickDeal(self, e):
        if e.buttons() == QtCore.Qt.LeftButton:
            self.FileLeftDeal()
        elif e.buttons() == QtCore.Qt.RightButton:
            self.FileRightDeal()
    def FileLeftDeal(self):
        print('FileLeft')
    def FileRightDeal(self):
        print("右")

def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename ,"rb")
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()
def size_format(size):
    if size < 1024:
        return '%i' % size + 'size'
    elif 1024 <= size < 1024*1024:
        return '%.1f' % float(size/1024) + 'KB'
    elif 1024*1024 <= size < 1024*1024*1024:
        return '%.1f' % float(size/(1024*1024)) + 'MB'
    elif 1024*1024*1024 <= size < 1024*1024*1024*1024:
        return '%.1f' % float(size/(1024*1024*1024)) + 'GB'
    elif 1024*1024*1024*1024 <= size:
        return '%.1f' % float(size/(1024*1024*1024*1024)) + 'TB'
from PyQt5.QtCore import *
def print_some(e):
    if e.buttons() == QtCore.Qt.LeftButton:
        print("左")
    # 右键按下
    elif e.buttons() == QtCore.Qt.RightButton:
        print("右")
    # 中键按下
    elif e.buttons() == QtCore.Qt.MidButton:
        print("中")
    pyqtSignal().emit()
def test(ui,clickdeal):
    ui.scrollAreaWidgetContents = QtWidgets.QWidget()
    ui.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 737, 583))
    ui.scrollAreaWidgetContents.setLayoutDirection(QtCore.Qt.LeftToRight)
    ui.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
    ui.formLayout = QtWidgets.QFormLayout(ui.scrollAreaWidgetContents)
    ui.formLayout.setContentsMargins(0, 0, 0, 0)
    ui.formLayout.setVerticalSpacing(0)
    ui.formLayout.setObjectName("formLayout")
    for i in range(20):
        ui.frame_13 = QtWidgets.QFrame(ui.scrollAreaWidgetContents)
        ui.frame_13.setMinimumSize(QtCore.QSize(0, 36))
        ui.frame_13.setMaximumSize(QtCore.QSize(16777215, 36))
        ui.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ui.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        ui.frame_13.setObjectName("frame_13")
        ui.horizontalLayout_14 = QtWidgets.QHBoxLayout(ui.frame_13)
        ui.horizontalLayout_14.setContentsMargins(3, 0, 9, 0)
        ui.horizontalLayout_14.setSpacing(0)
        ui.horizontalLayout_14.setObjectName("horizontalLayout_14")
        ui.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        ui.horizontalLayout_13.setContentsMargins(0, 0, 0, -1)
        ui.horizontalLayout_13.setSpacing(6)
        ui.horizontalLayout_13.setObjectName("horizontalLayout_13")
        ui.checkBox_2 = QtWidgets.QCheckBox(ui.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui.checkBox_2.sizePolicy().hasHeightForWidth())
        ui.checkBox_2.setSizePolicy(sizePolicy)
        ui.checkBox_2.setText("")
        ui.checkBox_2.setObjectName("checkBox_2")
        ui.horizontalLayout_13.addWidget(ui.checkBox_2)
        ui.label_27 = QtWidgets.QLabel(ui.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui.label_27.sizePolicy().hasHeightForWidth())
        ui.label_27.setSizePolicy(sizePolicy)
        ui.label_27.setAlignment(QtCore.Qt.AlignCenter)
        ui.label_27.setObjectName("label_27")
        ui.horizontalLayout_13.addWidget(ui.label_27)
        ui.label_28 = QtWidgets.QLabel(ui.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui.label_28.sizePolicy().hasHeightForWidth())
        ui.label_28.setSizePolicy(sizePolicy)
        ui.label_28.setMinimumSize(QtCore.QSize(0, 30))
        ui.label_28.setMaximumSize(QtCore.QSize(16777215, 36))
        ui.label_28.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        ui.label_28.setObjectName("label_28")
        ui.horizontalLayout_13.addWidget(ui.label_28)
        ui.horizontalLayout_13.setStretch(0, 1)
        ui.horizontalLayout_13.setStretch(1, 1)
        ui.horizontalLayout_13.setStretch(2, 20)
        ui.horizontalLayout_14.addLayout(ui.horizontalLayout_13)
        ui.label_29 = QtWidgets.QLabel(ui.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui.label_29.sizePolicy().hasHeightForWidth())
        ui.label_29.setSizePolicy(sizePolicy)
        ui.label_29.setAlignment(QtCore.Qt.AlignCenter)
        ui.label_29.setObjectName("label_29")
        ui.horizontalLayout_14.addWidget(ui.label_29)
        ui.label_30 = QtWidgets.QLabel(ui.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui.label_30.sizePolicy().hasHeightForWidth())
        ui.label_30.setSizePolicy(sizePolicy)
        ui.label_30.setAlignment(QtCore.Qt.AlignCenter)
        ui.label_30.setObjectName("label_30")
        ui.horizontalLayout_14.addWidget(ui.label_30)
        ui.horizontalLayout_14.setStretch(0, 7)
        ui.horizontalLayout_14.setStretch(1, 2)
        ui.horizontalLayout_14.setStretch(2, 2)
        ui.formLayout.setWidget(i, QtWidgets.QFormLayout.SpanningRole, ui.frame_13)
        ui.scrollArea.setWidget(ui.scrollAreaWidgetContents)
        ui.verticalLayout_2.addWidget(ui.scrollArea)


        ui.label_27.setText("con")
        ui.label_28.setText("File1")
        ui.label_29.setText("2020-03-02")
        ui.label_30.setText("100MB")
        ui.label_28.mousePressEvent = print_some

if __name__ == '__main__':
    clickdeal = EventDeals()
    app = QApplication(sys.argv)
    Main = QMainWindow()
    ui = SBCMainWindow.Ui_SBCclient()
    ui.setupUi(Main)
    # ui.label_23.mousePressEvent = print_some
    test(ui,clickdeal)
    Main.show()
    sys.exit(app.exec_())