
import sys
sys.path.append('..')
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QThread
import SBCMainWindow
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtCore import *
import base64
from pack import SBCRequest
from pack.preview import ImgPreview

from SubUi import SBCMainWindow
from SubUi import NavShow
from UpdateUi import FileUpdate

class initWindow():
    def __init__(self,Main):
        self.SBCMain = SBCMainWindow.Ui_SBCclient()
        self.SBCMain.setupUi(Main)
        self.SBCMain = self.initFrame()
        # self.Navshows = NavShow.Ui_PhotoShow(self.SBCMain)
        self.FileUpdates = FileUpdate.FileUpdate(self.SBCMain)

    def initparameter(self):
        self.SBCMain.nav = {}
        self.SBCMain.frameandscroll = {}
        self.SBCMain.SBCFilesDict = {}
        self.SBCMain.FileCons = {}
        self.SBCMain.CurFileListOld = {}
        self.SBCMain.NetOper = {}
        self.SBCMain.CurNetChosed = 'SBC'
        self.SBCMain.CurNavChosed = 'File'

    def initFrame(self):
        self.initparameter()
        self.Navshows = NavShow.Ui_PhotoShow(self.SBCMain)
        Nets = ['SBC', 'BDC', 'ALC']
        for i in Nets:
            self.SBCMain.frameandscroll[i] = {}
            self.SBCMain.SBCFilesDict[i] = {}
            self.SBCMain.FileCons[i] = {}
            self.SBCMain.NetOper[i] = {}

            self.SBCMain.frameandscroll[i]['Photo'] = self.Navshows.InitShow()
            self.SBCMain.frameandscroll[i]['Video'] = self.Navshows.InitShow()
            self.SBCMain.frameandscroll[i]['File'] = self.Navshows.initfileshow()
        return self.SBCMain

    def initBindSignal(self):
        self.SBCMain.NetOper[self.SBCMain.CurNetChosed]['backbutton'].mousePressEvent = partial(self.FileUpdates.navBackClick)  # back
        self.SBCMain.NetOper[self.SBCMain.CurNetChosed]['refreshbutton'].mousePressEvent = partial(self.FileUpdates.Refresh)










