import sys,base64
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import SBCMainWindow
import time

import os,hashlib

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

def print_some(e):
    if e.buttons() == QtCore.Qt.LeftButton:
        print("左")
    # 右键按下
    elif e.buttons() == QtCore.Qt.RightButton:
        print("右")
    # 中键按下
    elif e.buttons() == QtCore.Qt.MidButton:
        print("中")
def test(ui):
    for i in range(10):
        ui.frame_12 = QtWidgets.QFrame(ui.scrollAreaWidgetContents)
        ui.frame_12.setGeometry(QtCore.QRect(0, 50*i+100, 791, 41))
        ui.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ui.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        ui.frame_12.setObjectName("frame_12")
        ui.label_223 = QtWidgets.QLabel(ui.frame_12)
        ui.label_223.setText(str(i))
        ui.label_223.setGeometry(QtCore.QRect(100, 0, 160, 41))
        ui.label_223.mousePressEvent = print_some

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = QMainWindow()
    ui = SBCMainWindow.Ui_SBCclient()
    ui.setupUi(Main)
    ui.label_23.mousePressEvent = print_some
    test(ui)
    Main.show()
    sys.exit(app.exec_())