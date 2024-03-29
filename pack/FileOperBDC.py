import sys,threading,os,hashlib
import time,json
from PyQt5.QtCore import *


sys.path.append('..')
from UpdateUi import CrossNetTransp



class FileOperClick(QThread):
    # Signal = pyqtSignal(dict, str)
    # SignalTranspan = pyqtSignal()
    def __init__(self,ui):
        self.ui = ui
        super().__init__()
        # self.Signal.connect(self.Downact)
        # self.SignalTranspan.connect(self.Transpanim)
        # self.SBCRe = self.ui.SBCRe
        self.CrossNetTransp = CrossNetTransp.CrossTransShowUpdate(ui)

    def GetChoseFiles(self):
        ChosedFiles = []
        FileDicts = self.ui.SBCFilesDict[self.ui.CurNetChosed][self.ui.CurNavChosed]['File']
        for i in FileDicts:
            Filei = FileDicts[i]
            if Filei['checkBox'].isChecked():
                Filei['checkBox'].setChecked(False)
                # print('InitWind',Filei)
                info = {'size':Filei['size'],'fepath':Filei['fepath'],'fename':Filei['fename'],'isdir':Filei['isdir'],'fepath_base64':Filei['fepath_base64'],'fetype':Filei['fetype']}
                info['FileName'] = Filei['fename']
                info['FilePath'] = Filei['fepath']
                ChosedFiles.append(info)
        return ChosedFiles
    def Down(self,share=None):
        DownInfos = []
        print('downbdc')
        ChosedFiles = self.GetChoseFiles()
        # if ChosedFiles:
        #     self.SignalTranspan.emit()
        TranspDirs = []
        TranspFile = []
        for i in ChosedFiles:
            if i['fetype'] != 'folder':
                TranspFile.append(i)

            else:
                info = i
                info['tranto'] = 0
                TranspDirs.append(i)
        if TranspDirs:
            pass
        if TranspFile:
            self.CrossNetTransp.AddTransping(TranspFile)
