import sys,threading,os,hashlib
import time,json
from PyQt5.QtCore import *


sys.path.append('..')

class FileOperClick(QThread):
    # Signal = pyqtSignal(dict, str)
    # SignalTranspan = pyqtSignal()
    def __init__(self,ui):
        self.ui = ui
        super().__init__()
        # self.Signal.connect(self.Downact)
        # self.SignalTranspan.connect(self.Transpanim)
        # self.SBCRe = self.ui.SBCRe

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
    def Down(self,share=None):
        DownInfos = []
        print('downbdc')
        ChosedFiles = self.GetChoseFiles()
        # if ChosedFiles:
        #     self.SignalTranspan.emit()
        for i in ChosedFiles:
            if i['fetype'] != 'folder':
                DownFaPath = self.ui.DownPath
                DownInfos.append([i,DownFaPath])
                # self.Downact(i,DownFaPath)
            else:
                # FatherPath0 = self.ui.DownPath+i['fename']+'/'
                CurPath = i['fepath']
                queinfo = {}
                if share:
                    queinfo = i
                else:
                    queinfo = {'path': CurPath}
                Files = self.ui.SBCRe.GetAllFilesfromFolder(json.dumps(queinfo))
                if Files['Files']:
                    for fei in Files['Files']:
                        if share:
                            fei['shareinfo'] = i['shareinfo']
                        # print(fei)
                        DownFaPath = self.ui.DownPath + i['fename']+'/'+fei['fapath']+'/'
                        DownFaPath = DownFaPath.replace('//','/')
                        # DownFaPath = DownFaPath.replace('//','/')

                        # t = threading.Thread(target=self.Downact, args=(fei, DownFaPath,))
                        # t.setDaemon(True)
                        # t.start()
                        DownInfos.append([fei, DownFaPath])
        print(DownInfos)
