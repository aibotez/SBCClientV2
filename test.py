from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia


# -*- coding:utf-8 -*-
import threading
import time,os,shutil
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.Qt import QThread


def mklink(pathsrc,pathdst):
    os.symlink(pathsrc,pathdst)
def copyfe(pathsrc,pathdst):
    shutil.copyfile(pathsrc,pathdst,follow_symlinks=False)
def copyfo(pathsrc,pathdst):
    shutil.copytree(pathsrc,pathdst,symlinks=True)

pathsrc = r'C:\Users\zzx\Desktop\FeTest\1\copyTranslator.7z'
pathdst = r'C:\Users\zzx\Desktop\FeTest\1\1\copyTranslator.7z'
# pathsrc = 'C:/Users/zzx/Desktop/FeTest/1/1'
# pathdst = 'C:/Users/zzx/Desktop/FeTest/1/2/1'

# mklink(pathsrc,pathdst)
copyfe(pathsrc,pathdst)
