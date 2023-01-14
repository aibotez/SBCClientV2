
import sys,threading,os,hashlib
import time


sys.path.append('..')
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QAction,QFileDialog,QMessageBox
from PyQt5.Qt import QThread
from PyQt5.QtCore import *
from . import FileType

from PyQt5.QtGui import QFontMetrics,QCursor, QIcon
def getfileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename, "rb")
    while True:
        b = f.read(10*1024*1024)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()
def GetAllFiles(LoPath,RoPath):
    Files = []
    FaPath0 = os.path.abspath(os.path.dirname(LoPath)).replace('\\', '/')
    if FaPath0[-1] == '/':
         FaPath0 = FaPath0[0:-1]
    for root, dirs, files in os.walk(LoPath):
        root += '/'
        root = root.replace('\\', '/').replace('//','/')
        Rofepath = RoPath + root.replace(FaPath0+'/', '')
        for i in files:
            FileInfo = {}
            Lofepath = root + i
            FileInfo['Lofepath'] = Lofepath
            FileInfo['Rofepath'] = Rofepath
            Files.append(FileInfo)

    return Files
class TranspAnithread(QThread):
    # 定义信号,定义参数为str类型
    Signal = pyqtSignal()
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.Signal.connect(self.AniUpdate)
    def AniUpdate(self):
        # self.anim = QtCore.QPropertyAnimation(self.ui.TranspArrow1, b'geometry')  # 设置动画的对象及其属性
        # self.anim.setDuration(2000)  # 设置动画间隔时间
        # self.anim.setStartValue(QtCore.QRect(200, 20, 40, 40))  # 设置动画对象的起始属性
        # self.anim.setEndValue(QtCore.QRect(50, 360, 0, 0))  # 设置动画对象的结束属性
        # self.anim.start()  # 启动动画
        self.ui.anim.start()
    def run(self):
        self.Signal.emit()
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

    def Downact(self,DownFile,DownFaPath):
        FeMd5req = self.ui.SBCRe.GetRoFileMd5(DownFile['fepath'])
        Femd5 = None
        if not FeMd5req['error']:
            Femd5 = FeMd5req['md5']
        DownFeInfo ={}
        if DownFile['fetype'] != 'folder':
            DownFeInfo['FileMd5'] = Femd5
            DownFeInfo['FileName'] = DownFile['fename']
            DownFeInfo['size'] = DownFile['size']
            DownFeInfo['fetype'] = DownFile['fetype']
            DownFeInfo['FilePath'] = DownFaPath
            DownFeInfo['RoFilePath'] = DownFile['fepath']
            # print(DownFeInfo)
            self.ui.TransFilesManager.AddDownRecord(DownFeInfo)

    def UpFile(self):
        fname = QFileDialog.getOpenFileName(self.ui.MainWindow, "选择要上传的文件", "./")
        FilePath = fname[0]
        if FilePath:
            self.Up([{'Path':FilePath,'isDir':0}])
    def UpFolder(self):
        FolderPath = QFileDialog.getExistingDirectory(self.ui.MainWindow, "选择要上传的文件夹", "./")
        if FolderPath:
            self.Up([{'Path': FolderPath, 'isDir': 1}])

    def GetMoreInfo(self,LoPath,CurRopath):
        LoFileMd5 = getfileMd5(LoPath)
        Upinfo = {}
        Upinfo['FileMd5'] = LoFileMd5
        Upinfo['CurPath'] = CurRopath
        Upinfo['webkitRelativePath'] = ''
        Upinfo['FileName'] = os.path.basename(LoPath)
        Upinfo['RoFilePath'] = CurRopath
        Upinfo['LoFilePath'] = LoPath
        fetypeObj = FileType.FileType()
        fetype = fetypeObj.FileType(LoPath)
        Upinfo['fetype'] = fetype[1]
        Upinfo['Size'] = os.path.getsize(LoPath)
        Upinfo['FileSize'] = Upinfo['Size']
        # print(Upinfo)
        # self.ui.TransFilesManager.AddUpRecord(Upinfo)
        return Upinfo

    def UpChose(self,Upinfo):

        nav = self.ui.nav[self.ui.CurNetChosed]
        CurRopath = nav[-1]['path']
        # print('CurRoPath:',CurRopath)
        # time.sleep(0.2)
        # self.SignalTranspan.emit()
        FileAll = []
        for i in Upinfo:

            if i['isDir']:
                FilesAll = GetAllFiles(i['Path'],CurRopath)
                # print(FilesAll)
                for i in FilesAll:
                    FileAll.append(self.GetMoreInfo(i['Lofepath'], i['Rofepath']))
            else:
                # print(66, i)
                FileAll.append(self.GetMoreInfo(i['Path'],CurRopath))


        self.ui.TransFilesManager.AddUpRecord(FileAll)

    def UpChose1(self,e):
        # self.ui.thread = TranspAnithread(self.ui)
        while True:
            # self.ui.thread = TranspAnithread(self.ui)
            # self.ui.thread.start()
            print(time.time())
            time.sleep(1)
    def Up(self,Upinfo):
        # self.Transpanim()
        # self.SignalTranspan.emit()
        self.ui.thread = TranspAnithread(self.ui)
        self.ui.thread.start()
        t = threading.Thread(target=self.UpChose,args=(Upinfo,))
        t.setDaemon(True)
        t.start()
        # self.UpChose(Upinfo)
    def DelFileMessage(self,info):
        ShowInfo = ''
        if len(info) == 1:
            ShowInfo = '"{}"'.format(info[0]['fename'])
        else:
            ShowInfo = '{}个文件'.format(str(len(info)))
        reply = QMessageBox.question(self.ui.MainWindow,'提示', '是否要删除{}？'.format(ShowInfo),
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.SBCRe.DelFile({'data': info})
            self.ui.signalRefresh.emit()
        else:
            return
    def DelFile(self):
        ChosedFiles = self.GetChoseFiles()
        DelFileInfo = []
        for i in ChosedFiles:
            DelFileInfo.append({'fename':i['fename'],'fepath':i['fepath'],'feisdir':i['isdir'],'fileId':''})
        self.DelFileMessage(DelFileInfo)

    def Down(self,e):
        # self.ui.thread = TranspAnithread(self.ui)
        # self.ui.thread.start()
        self.start()
        # thread = Mythread()
        # # thread.SetPar(fei, DownFaPath)
        # thread.Signal.connect(self.Down1)
        # thread.start()

    def Transpanim(self):
        self.ui.thread = TranspAnithread(self.ui)
        self.ui.thread.start()
        # self.anim = QtCore.QPropertyAnimation(self.ui.TranspArrow1, b'geometry')  # 设置动画的对象及其属性
        # self.anim.setDuration(2000)  # 设置动画间隔时间
        # self.anim.setStartValue(QtCore.QRect(200, 20, 40, 40))  # 设置动画对象的起始属性
        # self.anim.setEndValue(QtCore.QRect(50, 360, 0, 0))  # 设置动画对象的结束属性
        # self.anim.start()  # 启动动画
    def run(self):
        import threading
        ChosedFiles = self.GetChoseFiles()
        # if ChosedFiles:
        #     self.SignalTranspan.emit()
        for i in ChosedFiles:
            if i['fetype'] != 'folder':
                DownFaPath = self.ui.DownPath
                self.Downact(i,DownFaPath)
            else:
                # FatherPath0 = self.ui.DownPath+i['fename']+'/'
                CurPath = i['fepath']
                Files = self.ui.SBCRe.GetAllFilesfromFolder(CurPath)
                if Files['Files']:
                    for fei in Files['Files']:
                        # print(fei)
                        DownFaPath = self.ui.DownPath + i['fename']+'/'+fei['fapath']+'/'
                        DownFaPath = DownFaPath.replace('//','/')
                        # DownFaPath = DownFaPath.replace('//','/')

                        # t = threading.Thread(target=self.Downact, args=(fei, DownFaPath,))
                        # t.setDaemon(True)
                        # t.start()
                        self.Downact(fei, DownFaPath)