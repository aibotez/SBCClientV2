
import sys,threading,os,hashlib
import time

sys.path.append('..')
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QAction,QFileDialog
from PyQt5.Qt import QThread

from PyQt5.QtGui import QFontMetrics,QCursor, QIcon
from PyQt5.QtCore import *
import base64
from pack import SBCRequest
from pack import TransFileManager
from pack import FileType
from pack import DBManager
from pack.preview import ImgPreview

from SubUi import SBCMainWindow
from SubUi import NavShow
# from SubUi import Transmitui
from UpdateUi import FileUpdate
# from UpdateUi import TransShowUpdate

def getfileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename, "rb")
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()
def GetAllFiles(LoPath,RoPath):
    Files = []
    path = LoPath.replace('\\', '/')
    for root, dirs, files in os.walk(path):
        root += '/'
        root = root.replace('\\', '/').replace('//','/')
        Rofepath = RoPath + root.replace(path+'/', '')
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
    # Signal = pyqtSignal(dict, str)

    def __init__(self, ui):
        super().__init__()
        # 下面的初始化方法都可以，有的python版本不支持
        #  super(Mythread, self).__init__()
        self.ui = ui
        self.Signal.connect(self.AniUpdate)
    def AniUpdate(self):
        self.anim = QtCore.QPropertyAnimation(self.ui.TranspArrow1, b'geometry')  # 设置动画的对象及其属性
        self.anim.setDuration(2000)  # 设置动画间隔时间
        self.anim.setStartValue(QtCore.QRect(200, 20, 40, 40))  # 设置动画对象的起始属性
        self.anim.setEndValue(QtCore.QRect(50, 360, 0, 0))  # 设置动画对象的结束属性
        self.anim.start()  # 启动动画

    def SetPar(self,dictpar,strpar):
        self.dictpar = dictpar
        self.strpar = strpar
    def run(self):
        self.Signal.emit()
        # self.Signal.emit(self.dictpar, self.strpar)



class FileOperClick(QThread):
    Signal = pyqtSignal(dict, str)
    SignalTranspan = pyqtSignal()
    def __init__(self,ui):
        self.ui = ui
        super().__init__()
        self.Signal.connect(self.Downact)
        self.SignalTranspan.connect(self.Transpanim)


    def GetChoseFiles(self):
        ChosedFiles = []
        FileDicts = self.ui.SBCFilesDict[self.ui.CurNetChosed][self.ui.CurNavChosed]['File']
        for i in FileDicts:
            Filei = FileDicts[i]
            if Filei['checkBox'].isChecked():
                # print('InitWind',Filei)
                ChosedFiles.append({'size':Filei['size'],'fepath':Filei['fepath'],'fename':Filei['fename'],'fepath_base64':Filei['fepath_base64'],'fetype':Filei['fetype']})
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
        self.Up({'Path':FilePath,'isDir':0})
    def UpFolder(self):
        FolderPath = QFileDialog.getExistingDirectory(self.ui.MainWindow, "选择要上传的文件夹", "./")
        self.Up({'Path': FolderPath, 'isDir': 1})

    def Upact(self,LoPath,CurRopath):
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
        self.ui.TransFilesManager.AddUpRecord(Upinfo)

    def UpChose(self,Upinfo):
        nav = self.ui.nav[self.ui.CurNetChosed]
        CurRopath = nav[-1]['path']
        print('CurRoPath:',CurRopath)
        # time.sleep(0.2)
        # self.SignalTranspan.emit()
        if Upinfo['isDir']:
            FilesAll = GetAllFiles(Upinfo['Path'],CurRopath)
            for i in FilesAll:
                self.Upact(i['Lofepath'], i['Rofepath'])
        else:
            self.Upact(Upinfo['Path'],CurRopath)

    def Up(self,Upinfo):
        # self.Transpanim()
        # self.SignalTranspan.emit()
        self.ui.thread = TranspAnithread(self.ui)
        self.ui.thread.start()
        t = threading.Thread(target=self.UpChose,args=(Upinfo,))
        t.setDaemon(True)
        t.start()

    def Down(self,e):
        self.start()
        # thread = Mythread()
        # # thread.SetPar(fei, DownFaPath)
        # thread.Signal.connect(self.Down1)
        # thread.start()

    def Transpanim(self):
        self.anim = QtCore.QPropertyAnimation(self.ui.TranspArrow1, b'geometry')  # 设置动画的对象及其属性
        self.anim.setDuration(2000)  # 设置动画间隔时间
        self.anim.setStartValue(QtCore.QRect(200, 20, 40, 40))  # 设置动画对象的起始属性
        self.anim.setEndValue(QtCore.QRect(50, 360, 0, 0))  # 设置动画对象的结束属性
        self.anim.start()  # 启动动画
    def run(self):
        import threading
        ChosedFiles = self.GetChoseFiles()
        if ChosedFiles:
            self.SignalTranspan.emit()
            # self.anim = QtCore.QPropertyAnimation(self.ui.TranspArrow1, b'geometry')  # 设置动画的对象及其属性
            # self.anim.setDuration(2000)  # 设置动画间隔时间
            # self.anim.setStartValue(QtCore.QRect(200, 20, 40, 40))  # 设置动画对象的起始属性
            # self.anim.setEndValue(QtCore.QRect(50, 360, 0, 0))  # 设置动画对象的结束属性
            # self.anim.start()  # 启动动画
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
                        # self.Signal.emit(fei, DownFaPath)
                # while True:
                #     self.ui.SBCRe.GetFileList(CurPath)
                #     CurFileList = self.ui.SBCRe.CurFileList
                #     for j in CurFileList:
                #         if j['fetype'] != 'folder':
                #             DownPathi = FatherPath0
                # print(CurFileList)


class ClickEventDeals():
    def __init__(self,ui,FileUpdates):
        self.ui = ui
        self.filepdate = FileUpdates
    def ClearNavStyle(self):
        self.ui.frame_2.setStyleSheet("")
        self.ui.frame_3.setStyleSheet("")
        self.ui.frame_4.setStyleSheet("")
        self.ui.frame_5.setStyleSheet("")
        self.ui.frame_6.setStyleSheet("")

    def HideFrames(self):
        # ui.frame_12.hide()
        for i in self.ui.frameandscroll:
            # print(i)
            if 'Tran' != i:
                self.ui.frameandscroll[i]['Photo']['frame'].hide()
                self.ui.frameandscroll[i]['Video']['frame'].hide()
                self.ui.frameandscroll[i]['File']['frame'].hide()
        self.ui.frameandscroll['Tran'].hide()
        self.ui.frame_14.hide()
    def NavChoose(self,WosLabel,e):
        if e.buttons() == QtCore.Qt.LeftButton:
            if self.ui.CurNavChosed != WosLabel:
                self.HideFrames()
                self.ClearNavStyle()
                # print(WosLabel)
                if WosLabel == 'Photo':
                    self.ui.CurNavChosed = 'Photo'
                    self.ui.frame_14.show()
                    self.filepdate.PhotoShow()
                    # SBCM.ChoseNav_Photo()
                    self.ui.frame_3.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")
                if WosLabel == 'File':
                    self.ui.CurNavChosed = 'File'
                    self.ui.frame_14.show()
                    self.filepdate.FileShow()
                    # SBCM.ChoseNav_File()
                    self.ui.frame_2.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")
                if WosLabel == 'Video':
                    self.ui.CurNavChosed = 'Video'
                    self.ui.frame_4.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")
                    self.ui.frame_14.show()
                    self.filepdate.VideoShow()
                    # SBCM.ChoseNav_Video()
                if WosLabel == 'Share':
                    self.ui.CurNavChosed = 'Share'
                    self.ui.frame_14.show()
                    self.ui.frame_5.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")
                if WosLabel == 'Transmit':
                    self.ui.CurNavChosed = 'Transmit'
                    # self.ui.frame_14.show()
                    self.ui.frameandscroll['Tran'].show()
                    self.ui.frame_6.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")







def CreatPopFram(SBCMain):
    frame_ChoseNet = QtWidgets.QFrame(SBCMain.frame_14)
    frame_ChoseNet.setGeometry(QtCore.QRect(220, 35, 101, 171))
    frame_ChoseNet.setStyleSheet("#frame_ChoseNet\n"
                                      "{\n"
                                      "    background:#D0D3D4;\n"
                                      "}\n"
                                      "\n"
                                      "#frame_ChoseNet QLabel:hover{\n"
                                      "    background:#A2D9CE;\n"
                                      "    \n"
                                      "    opacity:0.5;\n"
                                      "    }")
    frame_ChoseNet.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame_ChoseNet.setFrameShadow(QtWidgets.QFrame.Raised)
    frame_ChoseNet.setObjectName("frame_ChoseNet")
    verticalLayout_3 = QtWidgets.QVBoxLayout(frame_ChoseNet)
    verticalLayout_3.setContentsMargins(0, 0, 0, 0)
    verticalLayout_3.setSpacing(0)
    verticalLayout_3.setObjectName("verticalLayout_3")
    label = QtWidgets.QLabel(frame_ChoseNet)
    label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setObjectName("label")
    verticalLayout_3.addWidget(label)
    label_2 = QtWidgets.QLabel(frame_ChoseNet)
    label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    label_2.setAlignment(QtCore.Qt.AlignCenter)
    label_2.setObjectName("label_2")
    verticalLayout_3.addWidget(label_2)
    label_3 = QtWidgets.QLabel(frame_ChoseNet)
    label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    label_3.setAlignment(QtCore.Qt.AlignCenter)
    label_3.setObjectName("label_3")
    verticalLayout_3.addWidget(label_3)
    # self.retranslateUi(Form)
    # QtCore.QMetaObject.connectSlotsByName(Form)
    label.setText("小黑云")
    label_2.setText("百度云")
    label_3.setText("阿里云")
    SBCMain.frame_ChoseNet = frame_ChoseNet
    SBCMain.choseSBCLabel = label
    SBCMain.choseBDCLabel = label_2
    SBCMain.choseALCLabel = label_3
    SBCMain.frame_ChoseNet.raise_()
    SBCMain.frame_ChoseNet.hide()


class initWindow():
    def __init__(self,Main):

        self.Main = Main
        self.SBCMain = SBCMainWindow.Ui_SBCclient()
        self.SBCMain.MainWindow = Main
        self.Main.setAcceptDrops(True)
        self.Main.dragEnterEvent = self.dragEnterEvent
        self.Main.dropEvent = self.dropEvent
        self.SBCMain.SBCRe = SBCRequest.SBCRe()

        self.SBCMain.setupUi(Main)

        self.SBCMain.TranspArrow = self.SBCMain.label_23

        # self.SBCMain.TranspArrow.setText("↑↓")
        self.SBCMain.DownRecordFile = 'DownRecord.txt'
        self.SBCMain.UpRecordFile = 'UpRecord.txt'
        self.SBCMain.FinishRcordFile = 'FinishRcord.txt'
        self.SBCMain.DownPath = 'D:/SBCDown/'
        # self.SBCMain.TransFilesManager = TransFileManager.TransFileManager(self.SBCMain.DownRecordFile,self.SBCMain.UpRecordFile,self.SBCMain.FinishRcordFile)

        self.Thread_LoadImgs = FileUpdate.Thread_LoadImg(self.SBCMain)
        self.SBCMain = self.initFrame()
        self.SBCMain.TransFilesManager = TransFileManager.TransFileManager(self.Main, self.SBCMain)
        # self.Navshows = NavShow.Ui_PhotoShow(self.SBCMain)
        self.FileUpdates = FileUpdate.FileUpdate(self.SBCMain)
        self.init()

    def dragEnterEvent(self, evn):
        self.DrageFileIntoPath = evn.mimeData().text()
        evn.accept()
    # 鼠标放开执行
    def dropEvent(self, evn):
        fileoperclick = FileOperClick(self.SBCMain)
        paths = self.DrageFileIntoPath.split('\n')
        for i in paths:
            if i:
                FilePath = i.replace('file:///', '')
                if os.path.isdir(FilePath):
                    print('DragFolderPath',FilePath)
                else:
                    print('DragFilePath', FilePath)
                    fileoperclick.Up({'Path': FilePath, 'isDir': 0})

        # FilePath = self.DrageFileIntoPath.replace('file:///','')
        # fileoperclick = FileOperClick(self.SBCMain)
        # fileoperclick.Up({'Path':FilePath, 'isDir': 0})

    def WindowReSize(self):
        # if ui.scrollArea.width() < 500:
        #     w = 760
        # else:
        #     w = ui.scrollArea.width()
        w = self.Main.width() - 150

        if self.SBCMain.CurNavChosed in self.SBCMain.SBCFilesDict[self.SBCMain.CurNetChosed]:
            CurSBCFilesDict = self.SBCMain.SBCFilesDict[self.SBCMain.CurNetChosed][self.SBCMain.CurNavChosed]['File']
            # print(CurSBCFilesDict)
            for i in CurSBCFilesDict:
                FIleinfo = CurSBCFilesDict[i]
                FileName = FIleinfo['fename']
                Felabel = FIleinfo['FileNameLabel']
                # print(Felabel)
                metrics = QFontMetrics(Felabel.font())
                # print(metrics)
                new_file_name = metrics.elidedText(FileName, Qt.ElideRight, w*0.5)
                Felabel.setText(new_file_name)

    def MainWindowSizeChange(self,e):
        self.WindowReSize()

    def initparameter(self):
        self.SBCMain.nav = {}
        self.SBCMain.frameandscroll = {}
        self.SBCMain.SBCFilesDict = {}
        self.SBCMain.FileCons = {}
        self.SBCMain.CurFileListOld = {}
        self.SBCMain.NetOper = {}
        self.SBCMain.CurNetChosed = 'SBC'
        self.SBCMain.CurNavChosed = 'File'
        Nets = ['SBC','BDC','ALC']
        for i in Nets:
            self.SBCMain.CurFileListOld[i] = {}
            self.SBCMain.CurFileListOld[i]['Photo'] = []
            self.SBCMain.CurFileListOld[i]['Video'] = []
            self.SBCMain.CurFileListOld[i]['File'] = []

        self.SBCMain.TransDicts = {'Downing':[],'Uping':[],'AcrossNeting':[],'Finish':[]}

    def test1(self):
        horizontal_bar = self.SBCMain.frameandscroll['SBC']['File']['scrollArea'].verticalScrollBar()
        print(horizontal_bar.value(),horizontal_bar.maximum())
        print(self.SBCMain.frameandscroll['SBC']['File']['scrollArea'].size())
    # def test(self,e):
    #     horizontal_bar = self.SBCMain.frameandscroll['SBC']['File']['scrollArea'].verticalScrollBar()
    #     delta_y = - e.angleDelta().y()
    #     v = horizontal_bar.value() + delta_y
    #     v = max(min(v, horizontal_bar.maximum()), horizontal_bar.minimum())
    #     print(horizontal_bar.minimum(),horizontal_bar.maximum())
    #     horizontal_bar.setValue(v)

    def creat_Upmenu(self,e):
        self.groupBox_Upmenu = QMenu()
        self.actionUpfile = self.groupBox_Upmenu.addAction(u'上传文件')
        self.actionUpfolder = self.groupBox_Upmenu.addAction(u'上传文件夹')
        self.groupBox_Upmenu.popup(QCursor.pos())
        self.groupBox_Upmenu.setStyleSheet("QMenu{\n"
                                        "    margin:0px 10px 10px 0px;\n"
                                        "    color:blue;\n"
                                        "    font-size:18px;\n"
                                        "}\n")
        fileoperclick = FileOperClick(self.SBCMain)
        self.actionUpfile.triggered.connect(fileoperclick.UpFile)
        self.actionUpfolder.triggered.connect(fileoperclick.UpFolder)
        # self.SBCMain.label_14.mousePressEvent = self.fileoperclick.Down
    def creat_ChoseNetmenu(self,e):
        self.groupBox_ChoseNetmenu = QMenu()
        self.actionSBC = self.groupBox_ChoseNetmenu.addAction(u'小黑云')
        self.actionBDC = self.groupBox_ChoseNetmenu.addAction(u'百度云')
        self.actionALC = self.groupBox_ChoseNetmenu.addAction(u'阿里云')
        self.groupBox_ChoseNetmenu.popup(QCursor.pos())
        self.groupBox_ChoseNetmenu.setStyleSheet("QMenu{\n"
                                        "    margin:0px 10px 10px 0px;\n"
                                        "    color:blue;\n"
                                        "    font-size:18px;\n"
                                        "}\n")
    def creat_Moremenu(self,e):
        self.groupBox_Moremenu = QMenu()
        self.actionShare = self.groupBox_Moremenu.addAction(u'分享')
        self.actionMove = self.groupBox_Moremenu.addAction(u'移动')
        self.actionCopy = self.groupBox_Moremenu.addAction(u'复制')
        self.actionPorper = self.groupBox_Moremenu.addAction(u'属性')
        self.actionNewFolders = self.groupBox_Moremenu.addAction(u'新建文件夹')
        self.groupBox_Moremenu.popup(QCursor.pos())

        self.groupBox_Moremenu.setStyleSheet("QMenu{\n"
                                        "    margin:0px 10px 10px 0px;\n"
                                        "    color:blue;\n"
                                        "    font-size:18px;\n"
                                        "}\n")
    def initpopup(self):
        pass

    def initFrame(self):
        self.initparameter()
        self.Navshows = NavShow.Ui_PhotoShow(self.SBCMain)
        Nets = ['SBC', 'BDC', 'ALC']
        for i in Nets:
            self.SBCMain.CurNetChosed = i
            self.SBCMain.frameandscroll[i] = {}
            self.SBCMain.SBCFilesDict[i] = {}
            self.SBCMain.FileCons[i] = {}
            self.SBCMain.NetOper[i] = {}
            self.SBCMain.frameandscroll[i]['Photo'] = self.Navshows.InitShow()
            self.SBCMain.frameandscroll[i]['Photo']['frame'].resizeEvent = self.MainWindowSizeChange
            self.SBCMain.frameandscroll[i]['Video'] = self.Navshows.InitShow()
            self.SBCMain.frameandscroll[i]['Video']['frame'].resizeEvent = self.MainWindowSizeChange
            self.SBCMain.frameandscroll[i]['File'] = self.Navshows.initfileshow()
            self.SBCMain.frameandscroll[i]['File']['frame'].resizeEvent = self.MainWindowSizeChange
            # self.SBCMain.frameandscroll[i]['File']['scrollArea'].wheelEvent = self.test

            self.SBCMain.frameandscroll[i]['File']['scrollArea'].verticalScrollBar().valueChanged.connect(self.Thread_LoadImgs.runthread1)
            # vertical.valueChanged.connect(self.test1)

        TranShow = self.Navshows.InitTranShow()

        # self.SBCMain.TranspscrollArea = TranShow[1]
        # self.SBCMain.frameandscroll['Tran'] = TranShow[0]

        self.SBCMain.CurNetChosed = 'SBC'
        self.SBCMain.frameandscroll['SBC']['File']['frame'].show()

        # self.SBCMain.creat_ChoseNetmenu = self.creat_ChoseNetmenu

        # self.Main.resizeEvent = self.MainWindowSizeChange
        return self.SBCMain

    def initBindSignal(self):
        print(self.SBCMain.NetOper)
        self.SBCMain.NetOper[self.SBCMain.CurNetChosed]['backbutton'].mousePressEvent = partial(self.FileUpdates.navBackClick)  # back
        self.SBCMain.NetOper[self.SBCMain.CurNetChosed]['refreshbutton'].mousePressEvent = partial(self.FileUpdates.Refresh)
        # self.SBCMain.label_18.mousePressEvent = self.SBCMain.creat_ChoseNetmenu
        CED = ClickEventDeals(self.SBCMain,self.FileUpdates)
        self.SBCMain.frame_13.deleteLater()
        self.SBCMain.frame_2.mousePressEvent = partial(CED.NavChoose,'File')
        self.SBCMain.frame_3.mousePressEvent = partial(CED.NavChoose, 'Photo')
        self.SBCMain.frame_4.mousePressEvent = partial(CED.NavChoose, 'Video')
        self.SBCMain.frame_5.mousePressEvent = partial(CED.NavChoose, 'Share')
        self.SBCMain.frame_6.mousePressEvent = partial(CED.NavChoose, 'Transmit')
        self.SBCMain.label_18.mousePressEvent = self.creat_ChoseNetmenu #切换网盘
        self.SBCMain.label_17.mousePressEvent = self.creat_Moremenu  # 更多
        self.SBCMain.label_15.mousePressEvent = self.creat_Upmenu  # 上传
        self.fileoperclick = FileOperClick(self.SBCMain)
        self.SBCMain.label_14.mousePressEvent = self.fileoperclick.Down  # 下载


    def init(self):
        self.initBindSignal()
        self.FileUpdates.start()
        self.SBCMain.frame_2.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")

        self.SBCMain.TranspArrow1 = QtWidgets.QLabel(self.Main) #
        self.SBCMain.TranspArrow1.setGeometry(200,20,0,0)
        self.SBCMain.TranspArrow1.setPixmap(QtGui.QPixmap('img/Transp2.jpg'))
        self.SBCMain.TranspArrow1.setScaledContents(True) # 图片随文本部件的大小变动










