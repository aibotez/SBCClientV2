import sys,threading,os,hashlib
import time,json
from PyQt5.QtCore import *


sys.path.append('..')

class FileOperClick(QThread):
    Signal = pyqtSignal(dict, str)
    SignalTranspan = pyqtSignal()
    def __init__(self,ui):
        self.ui = ui
        super().__init__()
        self.Signal.connect(self.Downact)
        self.SignalTranspan.connect(self.Transpanim)
        self.SBCRe = self.ui.SBCRe

    def GetChoseFiles(self):
        ChosedFiles = []
        FileDicts = self.ui.SBCFilesDict[self.ui.CurNetChosed][self.ui.CurNavChosed]['File']
        for i in FileDicts:
            Filei = FileDicts[i]
            if Filei['checkBox'].isChecked():
                Filei['checkBox'].setChecked(False)
                # print('InitWind',Filei)
                ChosedFiles.append({'size':Filei['size'],'fepath':Filei['fepath'],'fename':Filei['fename'],'isdir':Filei['isdir'],'fepath_base64':Filei['fepath_base64'],'fetype':Filei['fetype']})
        return ChosedFiles
    def Down(self):
        ChosedFiles = self.GetChoseFiles()
        if ChosedFiles:
            self.SignalTranspan.emit()
