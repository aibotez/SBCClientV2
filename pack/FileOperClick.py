
import sys,threading,os,hashlib
import time


sys.path.append('..')
from functools import partial
import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QAction,QFileDialog,QMessageBox,QDialog
from PyQt5.Qt import QThread
from PyQt5.QtCore import *
from . import FileType
from SubUi import ReNameui
from SubUi import Shareui
from SubUi import ShowShareLinkui
from SubUi import Moveuiinit
from SubUi import Copyui

from PyQt5.QtGui import QFontMetrics,QCursor, QIcon


def FileConChose(fetype):
    if fetype == 'folder':
        return 'img/filecon/folder1.png'
    if fetype == 'zip':
        return 'img/filecon/zipcon.png'
    if fetype == 'img':
        return 'img/filecon/imgcon.jpg'
    if fetype == 'pdf':
        return 'img/filecon/pdfcon.jpg'
    if fetype == 'ppt':
        return 'img/filecon/pptcon.jpg'
    if fetype == 'exe':
        return 'img/filecon/execon.jpg'
    if fetype == 'excel':
        return 'img/filecon/excelcon.jpg'
    if fetype == 'word':
        return 'img/filecon/wordcon.jpg'
    if fetype == 'html':
        return 'img/filecon/htmlcon.jpg'
    else:
        return 'img/filecon/wj.jfif'
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

    def Downact(self,Downinfos):
        DownFeInfos = []
        # DownFePath = [i[0]['fepath'] for i in Downinfos]
        for i in Downinfos:
            DownFile = i[0]
            DownFaPath = i[1]
            Femd5 = None
            # FeMd5req = self.ui.SBCRe.GetRoFileMd5(DownFile['fepath'])
            # if not FeMd5req['error']:
            #     Femd5 = FeMd5req['md5']

            DownFeInfo ={}

            if DownFile['fetype'] != 'folder':
                DownFeInfo['FileMd5'] = Femd5
                DownFeInfo['FileName'] = DownFile['fename']
                DownFeInfo['size'] = DownFile['size']
                DownFeInfo['Size'] = DownFile['size']
                DownFeInfo['fetype'] = DownFile['fetype']
                DownFeInfo['FilePath'] = DownFaPath
                DownFeInfo['RoFilePath'] = DownFile['fepath']
                # print(DownFeInfo)
                DownFeInfos.append(DownFeInfo)
        self.ui.TransFilesManager.AddDownRecord(DownFeInfos)

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
                    FileInfo = self.GetMoreInfo(i['Lofepath'], i['Rofepath'])
                    if FileInfo['Size'] != 0:
                        FileAll.append(self.GetMoreInfo(i['Lofepath'], i['Rofepath']))
            else:
                # print(66, i)
                FileInfo = self.GetMoreInfo(i['Path'],CurRopath)
                if FileInfo['Size'] != 0:
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
        # self.start()
        # thread = Mythread()
        # # thread.SetPar(fei, DownFaPath)
        # thread.Signal.connect(self.Down1)
        # thread.start()
        # self.SignalTranspan.emit()
        # self.ui.thread = TranspAnithread(self.ui)
        # self.ui.thread.start()
        # self.ui.thread.wait()
        t = threading.Thread(target=self.run1)
        t.setDaemon(True)
        t.start()

    def SBCFileCopy(self,e):
        ChosedFiles = self.GetChoseFiles()
        if ChosedFiles:
            self.ui.SBCFileCopyWindowDialog = QDialog()
            self.ui.SBCFileCopyWindow = Copyui.CopyUi(self.ui.SBCFileCopyWindowDialog,self.ui,ChosedFiles)
            self.ui.SBCFileCopyWindowDialog.show()
    def SBCFileMove(self,e):
        ChosedFiles = self.GetChoseFiles()
        if ChosedFiles:
            self.ui.SBCFileMoveWindowDialog = QDialog()
            self.ui.SBCFileMoveWindow = Moveuiinit.MoveUi(self.ui.SBCFileMoveWindowDialog,self.ui,ChosedFiles)
            self.ui.SBCFileMoveWindowDialog.show()


    def CopyLink(self,sharelink):
        pyperclip.copy(sharelink)
        self.ui.SBCShowShareLinkuiWindowDialog.destroy()
    def SBCShareact(self,ChosedFiles):
        self.ui.SBCShareWindowDialog.destroy()
        DuringTime = self.ui.SBCShareWindow.label_4.text()
        Password = self.ui.SBCShareWindow.lineEdit.text()
        ShareFile = {
            'ShareFile':ChosedFiles,
            'ShareDateDur':DuringTime,
            'SharePass':Password
        }
        res = self.ui.SBCRe.SBCShare(ShareFile)
        self.ui.SBCShowShareLinkuiWindow = ShowShareLinkui.Ui_Dialog()
        self.ui.SBCShowShareLinkuiWindowDialog = QDialog()
        self.ui.SBCShowShareLinkuiWindow.setupUi(self.ui.SBCShowShareLinkuiWindowDialog)
        # self.ui.SBCNewWindowDialog.setWindowTitle("新建文件夹")
        self.ui.SBCShowShareLinkuiWindow.lineEdit.setText(res['res'])
        self.ui.SBCShowShareLinkuiWindow.lineEdit.selectAll()
        self.ui.SBCShowShareLinkuiWindow.pushButton.clicked.connect(lambda: self.CopyLink(res['res']))
        self.ui.SBCShowShareLinkuiWindowDialog.show()
    def ShareMenu(self,e):
        self.groupBox_Moremenu = QMenu()
        self.actionShare1 = self.groupBox_Moremenu.addAction(u'1天内有效')
        self.actionShare2 = self.groupBox_Moremenu.addAction(u'7天内有效')
        self.actionShare3 = self.groupBox_Moremenu.addAction(u'1个月内有效')
        self.actionShare4 = self.groupBox_Moremenu.addAction(u'永久有效')
        self.groupBox_Moremenu.popup(QCursor.pos())
        self.groupBox_Moremenu.setStyleSheet("QMenu{margin:0px 10px 10px 0px;color:blue;font-size:15px;}")
        self.actionShare1.triggered.connect(lambda: self.ui.SBCShareWindow.label_4.setText('1天内有效'))
        self.actionShare2.triggered.connect(lambda: self.ui.SBCShareWindow.label_4.setText('7天内有效'))
        self.actionShare3.triggered.connect(lambda: self.ui.SBCShareWindow.label_4.setText('1个月内有效'))
        self.actionShare4.triggered.connect(lambda: self.ui.SBCShareWindow.label_4.setText('永久有效'))
    def SBCShare(self):
        ChosedFiles = self.GetChoseFiles()
        if ChosedFiles:
            self.ui.SBCShareWindow = Shareui.Ui_Dialog()
            self.ui.SBCShareWindowDialog = QDialog()
            self.ui.SBCShareWindow.setupUi(self.ui.SBCShareWindowDialog)
            self.ui.SBCShareWindow.label_5.setPixmap(QtGui.QPixmap('img/filecon/drop.jpg'))
            self.ui.SBCShareWindow.label_5.setScaledContents(True)
            # self.ui.SBCShareWindowDialog.setWindowTitle("新建文件夹")
            if len(ChosedFiles)>1:
                self.ui.SBCShareWindow.label.setText('')
                self.ui.SBCShareWindow.label.setPixmap(QtGui.QPixmap('img/filecon/folder2.jfif'))
                self.ui.SBCShareWindow.label.setScaledContents(True)
                self.ui.SBCShareWindow.label_2.setText('共{}个文件'.format(str(len(ChosedFiles))))
            else:
                self.ui.SBCShareWindow.label.setText('')
                self.ui.SBCShareWindow.label.setPixmap(QtGui.QPixmap('img/filecon/folder1.png'))
                self.ui.SBCShareWindow.label.setScaledContents(True)
                self.ui.SBCShareWindow.label_2.setText('{}'.format(str(ChosedFiles[0]['fename'])))
            self.ui.SBCShareWindowDialog.show()
            self.ui.SBCShareWindow.label_4.mousePressEvent = self.ShareMenu
            self.ui.SBCShareWindow.pushButton.clicked.connect(lambda: self.SBCShareact(ChosedFiles))
    def NewFolderact(self,info):
        self.ui.SBCNewWindowDialog.destroy()
        NewNameValue = self.ui.SBCNewWindow.lineEdit.text()
        if NewNameValue and NewNameValue not in info['FileNames']:
            self.ui.SBCRe.NewFolder(info)
            self.ui.signalRefresh.emit()

    def NewFolder(self):
        FileDicts = self.ui.SBCFilesDict[self.ui.CurNetChosed][self.ui.CurNavChosed]['File']
        FileNames = [FileDicts[i]['fename'] for i in FileDicts if FileDicts[i]['isdir']]
        NewFolderName = '新建文件夹'
        j = 1
        while True:
            if NewFolderName not in FileNames:
                break
            NewFolderName = '新建文件夹（{}）'.format(str(j))
            j+=1
        nav = self.ui.nav[self.ui.CurNetChosed]
        CurRopath = nav[-1]['path']
        info = {}
        info['NewFolderName'] = NewFolderName
        info['FileNames'] = FileNames
        info ['CurPath'] = CurRopath

        self.ui.SBCNewWindow = ReNameui.Ui_Dialog()
        self.ui.SBCNewWindowDialog = QDialog()
        self.ui.SBCNewWindow.setupUi(self.ui.SBCNewWindowDialog)
        self.ui.SBCNewWindowDialog.setWindowTitle("新建文件夹")
        self.ui.SBCNewWindow.lineEdit.setText(NewFolderName)
        self.ui.SBCNewWindow.lineEdit.selectAll()
        self.ui.SBCNewWindow.label.setText('')
        self.ui.SBCNewWindow.label.setPixmap(QtGui.QPixmap('img/filecon/folder1.png'))
        self.ui.SBCNewWindow.label.setScaledContents(True)
        self.ui.SBCNewWindowDialog.show()
        self.ui.SBCNewWindow.pushButton.clicked.connect(lambda: self.NewFolderact(info))
    def ReNameact(self,info):
        self.ui.SBCReNameWindowDialog.destroy()
        reNameValue = self.ui.SBCReNameWindow.lineEdit.text()
        if reNameValue and reNameValue != info['fename']:
            info['NewName'] = reNameValue
            self.ui.SBCRe.ReName(info)
            self.ui.signalRefresh.emit()
    def ReName(self,e):
        ChosedFiles = self.GetChoseFiles()
        if ChosedFiles:
            ChosedFile = ChosedFiles[0]
            self.ui.SBCReNameWindow = ReNameui.Ui_Dialog()
            self.ui.SBCReNameWindowDialog = QDialog()
            self.ui.SBCReNameWindow.setupUi(self.ui.SBCReNameWindowDialog)
            self.ui.SBCReNameWindow.lineEdit.setText(ChosedFile['fename'])
            self.ui.SBCReNameWindow.lineEdit.selectAll()
            self.ui.SBCReNameWindow.label.setText('')
            self.ui.SBCReNameWindow.label.setPixmap(QtGui.QPixmap(FileConChose(ChosedFile['fetype'])))
            self.ui.SBCReNameWindow.label.setScaledContents(True)
            self.ui.SBCReNameWindowDialog.show()
            self.ui.SBCReNameWindow.pushButton.clicked.connect(lambda: self.ReNameact(ChosedFile))



    def Transpanim(self):
        self.ui.anim.start()
        # self.ui.thread = TranspAnithread(self.ui)
        # self.ui.thread.start()

        # self.anim = QtCore.QPropertyAnimation(self.ui.TranspArrow1, b'geometry')  # 设置动画的对象及其属性
        # self.anim.setDuration(2000)  # 设置动画间隔时间
        # self.anim.setStartValue(QtCore.QRect(200, 20, 40, 40))  # 设置动画对象的起始属性
        # self.anim.setEndValue(QtCore.QRect(50, 360, 0, 0))  # 设置动画对象的结束属性
        # self.anim.start()  # 启动动画
    def run1(self):
        # time.sleep(10)
        import threading
        ChosedFiles = self.GetChoseFiles()
        DownInfos = []
        if ChosedFiles:
            self.SignalTranspan.emit()
            # self.ui.thread = TranspAnithread(self.ui)
            # self.ui.thread.start()
            # self.SignalTranspan.emit()
        for i in ChosedFiles:
            if i['fetype'] != 'folder':
                DownFaPath = self.ui.DownPath
                DownInfos.append([i,DownFaPath])
                # self.Downact(i,DownFaPath)
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
                        DownInfos.append([fei, DownFaPath])
                        # self.Downact(fei, DownFaPath)
        # DownNums = len(DownInfos)
        # if DownNums >= 50:
        #     reply = QMessageBox.question(self.ui.MainWindow, '提示', '下载的文件数超过50个，是否继续？',
        #                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        #     if reply == QMessageBox.Yes:
        #         return
        self.Downact(DownInfos)