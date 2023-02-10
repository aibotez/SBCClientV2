import sys,threading,os,hashlib,requests,json
import time,sip
from requests_toolbelt import MultipartEncoder,MultipartEncoderMonitor

sys.path.append('..')
from pack import DBManager
# from pack import SBCRequest
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QThread,QMutex
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import threading





qmut_1 = QMutex()
def size_format(size):
    if size < 1024:
        return '%i' % size + 'size'
    elif 1024 <= size < 1024 * 1024:
        return '%.1f' % float(size / 1024) + 'KB'
    elif 1024 * 1024 <= size < 1024 * 1024 * 1024:
        return '%.1f' % float(size / (1024 * 1024)) + 'MB'
    elif 1024 * 1024 * 1024 <= size < 1024 * 1024 * 1024 * 1024:
        return '%.1f' % float(size / (1024 * 1024 * 1024)) + 'GB'
    elif 1024 * 1024 * 1024 * 1024 <= size:
        return '%.1f' % float(size / (1024 * 1024 * 1024 * 1024)) + 'TB'


def CheckLoFile(UpInfo):
    # print(self.ui.UpPath)
    FileLoPath = UpInfo['LoFilePath'] + UpInfo['FileName']
    LoFileSize = 0
    LoFileExist = 0
    if os.path.exists(FileLoPath):
        LoFileSize = os.path.getsize(FileLoPath)
        LoFileExist = 1
    return {'exist': LoFileExist, 'size': LoFileSize}

def FileConChose(fetype):
    if fetype == 'folder':
        return 'img/filecon/foldersm.png'
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

def str_trans_to_md5(src):
    src = src.encode("utf-8")
    myMd5 = hashlib.md5()
    myMd5.update(src)
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest


class WSQLThread(QThread):
    # 定义信号,定义参数为str类型
    Signal = pyqtSignal(list)
    def __init__(self, ui,info,dbManager):
        super().__init__()
        self.ui = ui
        self.info = info
        self.dbManager = dbManager
        # self.Signal.connect(self.AniUpdate)
    def run(self):
        # dbManager = DBManager.DBManager()
        # self.Signal.emit(self.info)
        # self.dbManager = self.dbManager.self.dbManager()
        # self.dbManager.AddUserUpRecord(self.info)
        # self.dbManager.close()
            # self.dbManager.AddUserUpRecords(i)
        self.dbManager.WSQL(self.info, 'AddUserUpRecords')
        UpLayout = self.ui.TranspscrollArea['Up']
        UpLayout[3].setText(str(len(self.info)))
        self.Signal.emit(self.info)
class UpdateShowThread(QThread):
    Signal = pyqtSignal(dict,dict)
    def __init__(self,labelinfo,info):
        super().__init__()
        self.info = info
        self.labelinfo = labelinfo
    def run(self):
        self.Signal.emit(self.labelinfo,self.info)

class TransUp():
    # signalWSQL = pyqtSignal(list)
    # signaladdUp = pyqtSignal(dict)
    def __init__(self,ui,signaladdUp,signalaDelUp,signalaDelUp1,signalaUpdateUpProgress):
        super().__init__()
        self.ui = ui
        self.MaxUpNums = 2
        self.UpLayout = self.ui.TranspscrollArea['Up']
        self.qmut_1 = QMutex()
        self.ButtonBind()
        self.s = requests.Session()
        self.signaladdUp = signaladdUp
        self.signalaDelUp = signalaDelUp
        self.signalaDelUp1 = signalaDelUp1
        self.signalaUpdateUpProgress = signalaUpdateUpProgress
        self.dbManager = DBManager.DBManager()
        self.dbManager1 = DBManager.DBManager1()
        self.ClientSetting = self.dbManager.GetClientSetting()
        self.UpInfosUpdateLabs = {}
        self.signaladdUp.connect(self.AddUping1)
        self.signalaDelUp.connect(self.DelUp)
        self.signalaDelUp1.connect(self.DelUpact)
        self.signalaUpdateUpProgress.connect(self.UpdateUpProgress)
        self.AddUping()


    def add(self, scrollAreaWidgetContents, UpInfo):
        self.frame_22 = QtWidgets.QFrame(scrollAreaWidgetContents)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem6 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem6)
        self.label_34 = QtWidgets.QLabel(self.frame_22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setMinimumSize(QtCore.QSize(30, 30))
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_15.addWidget(self.label_34)
        self.frame_23 = QtWidgets.QFrame(self.frame_22)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_14.setContentsMargins(0, 8, 0, 8)
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_27 = QtWidgets.QLabel(self.frame_23)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_14.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.frame_23)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_14.addWidget(self.label_28)
        self.horizontalLayout_15.addWidget(self.frame_23)
        spacerItem7 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem7)
        self.frame_24 = QtWidgets.QFrame(self.frame_22)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_24)
        self.verticalLayout_15.setContentsMargins(0, 15, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.progressBar_5 = QtWidgets.QProgressBar(self.frame_24)
        self.progressBar_5.setMinimumSize(QtCore.QSize(0, 0))
        self.progressBar_5.setMaximumSize(QtCore.QSize(16777215, 15))
        self.progressBar_5.setProperty("value", 24)
        self.progressBar_5.setObjectName("progressBar_5")
        self.verticalLayout_15.addWidget(self.progressBar_5)
        self.label_29 = QtWidgets.QLabel(self.frame_24)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_15.addWidget(self.label_29)
        self.horizontalLayout_15.addWidget(self.frame_24)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem8)
        self.frame_25 = QtWidgets.QFrame(self.frame_22)
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_25)
        self.horizontalLayout_16.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_30 = QtWidgets.QLabel(self.frame_25)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_16.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(self.frame_25)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_16.addWidget(self.label_31)
        self.label_35 = QtWidgets.QLabel(self.frame_25)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_16.addWidget(self.label_35)
        self.horizontalLayout_15.addWidget(self.frame_25)
        spacerItem9 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem9)
        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 6)
        self.horizontalLayout_15.setStretch(2, 10)
        self.horizontalLayout_15.setStretch(3, 1)
        self.horizontalLayout_15.setStretch(4, 10)
        self.horizontalLayout_15.setStretch(5, 1)
        self.horizontalLayout_15.setStretch(6, 5)
        self.horizontalLayout_15.setStretch(7, 1)

        LoFile = CheckLoFile(UpInfo)
        LoSize = size_format(LoFile['size'])

        self.progressBar_5.setProperty("value", (LoFile['size']/UpInfo['Size'])*100)


        self.label_34.setText("")
        self.label_34.setPixmap(QtGui.QPixmap(FileConChose(UpInfo['fetype'])))
        self.label_34.setScaledContents(True)
        self.label_34.setMaximumSize(46, 46)




        self.label_27.setText(UpInfo['FileName'])
        self.label_27.setFixedWidth(260)
        self.label_28.setText("{}/{}".format(LoSize,size_format(UpInfo['Size'])))

        self.label_29.setText("--")
        # print(66,UpInfo)
        # print(int(UpInfo['isUp']))
        if int(UpInfo['isUp']) == 2:
            self.label_29.setText("等待上传")
        elif int(UpInfo['isUp']) == 0:
            # print('Paulse')
            self.label_29.setText("暂停")

        self.label_30.setText(">")
        # QFrame  # frame_16::hover
        self.label_30.setStyleSheet("QLabel{font-size:26px;font-weight:bold;font-family:Roman times;}"
                           "#label_30:hover{color:rgb(20, 90, 50);}")

        self.label_31.setText("X")
        self.label_31.setStyleSheet("QLabel{font-size:26px;font-family:Roman times;}"
                           "QLabel:hover{color:rgb(20, 90, 50);}")

        # label_24.setText("")
        # label_24.setStyleSheet("QLabel{font-size:26px;font-weight:bold;font-family:Roman times;}"
        #                    "QLabel:hover{color:rgb(20, 90, 50);}")
        self.label_31.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_30.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # label_24.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # Upinginfoi = {}
        Upinginfoi = UpInfo
        Upinginfoi['frame'] = self.frame_22
        Upinginfoi['statusButon'] = self.label_30
        Upinginfoi['statusLabel'] = self.label_29
        Upinginfoi['progressBar'] = self.progressBar_5
        Upinginfoi['UpSizeLabel'] = self.label_28
        # Upinginfoi['FilePath'] = UpInfo['FilePath']
        # Upinginfoi['FileName'] = UpInfo['FileName']
        # Upinginfoi['isUp'] = UpInfo['isUp']
        # Upinginfoi['size'] = UpInfo['Size']
        # Upinginfoi['RoFilePath'] = UpInfo['RoFilePath']
        Upinginfoi['LoFileSatus'] = LoFile
        Upinginfoi['LoPath'] = UpInfo['LoFilePath']+UpInfo['FileName']
        self.UpInfosUpdateLabs[str_trans_to_md5(Upinginfoi['RoFilePath']+UpInfo['FileName'])] = Upinginfoi

        self.label_30.mousePressEvent = partial(self.UpSatusChange,Upinginfoi)
        self.label_31.mousePressEvent = lambda e: self.DelUp(Upinginfoi)
        # self.label_31.mousePressEvent = partial(self.DelUp,Upinginfoi)

        return Upinginfoi


    def UpPause(self,info):
        info['statusButon'].setText(">")
        info['statusLabel'].setText("已暂停")
        self.UpInfosUpdateLabs[str_trans_to_md5(info['RoFilePath'] + info['FileName'])]['isUp'] = 0
        # self.dbManager1.setUpPar(info['LoFilePath'], info['FileName'], 0)
        self.dbManager1.WSQL(info, 'UpdataUserUpRecord',0)
        # self.dbManager.UpdataUserUpRecord(info['LoFilePath'], info['FileName'], 0)
        # info['isDown'] = 0
        self.UpManger()
    def UpGon(self,info):
        info['statusButon'].setText("||")
        self.UpInfosUpdateLabs[str_trans_to_md5(info['RoFilePath'] + info['FileName'])]['isUp'] = 1
        # self.dbManager1.setUpPar(info['LoFilePath'], info['FileName'], 1)
        self.dbManager1.WSQL(info, 'UpdataUserUpRecord',1)
        # self.dbManager.UpdataUserUpRecord(info['LoFilePath'], info['FileName'], 1)
        # info['isDown'] = 1
        self.Up(info)
        # self.Upact1(info)
        # self.UpManger(info)
        self.UpManger()
    def UpSatusChange(self,info,e):
        # print(info)
        UpInfoi = self.dbManager.GetUserUpRecord(info['LoFilePath'], info['FileName'])
        if UpInfoi and int(UpInfoi['isUp'])==1:
            self.UpPause(info)
        else:
            self.UpGon(info)
    # def DelUping(self,info,e):
    #     self.dbManager.DelUserUpRecord(info['LoFilePath'],info['FileName'])
    #     self.UpLayout[1].removeWidget(info['frame'])
    #     sip.delete(info['frame'])
    #     self.UpLayout[1].removeWidget(info['line'])
    #     sip.delete(info['line'])
    #     # self.RefreshUping()
    #     UpInfos = self.dbManager.GetUserUpRecordAll()
    #     # print('UpS',UpInfos)
    #     self.UpLayout[3].setText(str(len(UpInfos)))
    #     del self.UpInfosUpdateLabs[str_trans_to_md5(info['RoFilePath']+info['FileName'])]


    def OpenFile(self,info):
        fp = open(info['LoFilePath'], 'rb')
        fp.seek(info['FileSeekStart'],os.SEEK_SET)
        return fp

    def chunked_file_reader(self,info,block_size=20*1024 * 1024):
        """生成器函数：分块读取文件内容
        """
        file = info['LoFilePath']
        FileSeekStart = info['FileSeekStart']
        with open(file, 'rb') as f:
            f.seek(FileSeekStart,os.SEEK_SET)
            while True:
                c = f.read(block_size)
                if c:
                    yield c
                else:
                    break
    def GetUpFileFaPath(self,info):
        CurPath = info['CurPath']
        if 'SBC' not in self.ui.nav:
            CurRopath = '/home/'
        else:
            nav = self.ui.nav[self.ui.CurNetChosed]
            CurRopath = nav[-1]['path']
        CurPathFa = CurPath.replace(CurRopath,'')
        if CurPathFa:
            CurPathFa = CurPathFa.split('/')[0]+'#1'
        else:
            CurPathFa = info['FileName'] + '#0'
        return CurPathFa

    def DelUpact(self,info):
        i = info
        infoi = self.UpInfosUpdateLabs[str_trans_to_md5(i['RoFilePath'] + i['FileName'])]
        self.UpLayout[1].removeWidget(infoi['frame'])
        sip.delete(infoi['frame'])
        self.UpLayout[1].removeWidget(infoi['line'])
        sip.delete(infoi['line'])
        del self.UpInfosUpdateLabs[str_trans_to_md5(i['RoFilePath'] + i['FileName'])]
    def DelUp(self,info):
        t = threading.Thread(target=self.DelUp1,args=(info,))
        t.setDaemon(True)
        t.start()
        return
    def DelUp1(self,info):
        i = info
        infoi = self.UpInfosUpdateLabs[str_trans_to_md5(i['RoFilePath'] + i['FileName'])]
        self.dbManager1.WSQL(i, 'DelUserUpRecord')
        # # print('Finsh', info['FileName'])
        # # UpLayout = self.ui.TranspscrollArea['Up']
        # # infoi['frame'].setParent(None)
        # # infoi['line'].setParent(None)
        # self.UpLayout[1].removeWidget(infoi['frame'])
        # sip.delete(infoi['frame'])
        # self.UpLayout[1].removeWidget(infoi['line'])
        # sip.delete(infoi['line'])
        # del self.UpInfosUpdateLabs[str_trans_to_md5(i['RoFilePath'] + i['FileName'])]
        self.signalaDelUp1.emit(info)
        CurFileList = self.ui.CurFileListOld['SBC']['File']
        CurPathFiles = []
        # print(CurRopath,CurNavChosed,CurNetChosed,self.GetUpFileFaPath(info))
        for i in CurFileList:
            CurPathFiles.append(i['filename']+'#'+str(i['isdir']))
        if self.GetUpFileFaPath(info) not in CurPathFiles:
            self.ui.signalRefresh.emit()
        self.UpManger()
    def UpFinsh(self,info):
        # print('Finsh',info['FileName'])
        # self.dbManager1.setUpPar(info['LoFilePath'], info['FileName'], 3)
        # self.dbManager1.WSQL(0,'UpdataUserUpRecord')

        i = info
        # infoi = self.UpInfosUpdateLabs[str_trans_to_md5(i['RoFilePath'] + i['FileName'])]
        # self.dbManager1.WSQL(i, 'DelUserUpRecord')
        # print('Finsh', info['FileName'])
        # # UpLayout = self.ui.TranspscrollArea['Up']
        # # infoi['frame'].setParent(None)
        # # infoi['line'].setParent(None)
        # self.UpLayout[1].removeWidget(infoi['frame'])
        # sip.delete(infoi['frame'])
        # self.UpLayout[1].removeWidget(infoi['line'])
        # sip.delete(infoi['line'])
        # print('DEL')
        # QApplication.processEvents()
        # del self.UpInfosUpdateLabs[str_trans_to_md5(i['RoFilePath'] + i['FileName'])]
        # print(66)
        self.signalaDelUp.emit(info)
        return
        self.UpManger()
        # self.dbManager.UpdataUserUpRecord(info['LoFilePath'], info['FileName'], 3)
        # self.dbManager.conn.commit()
        # CurNavChosed = self.ui.CurNavChosed
        # CurNetChosed = self.ui.CurNetChosed
        # CurFileList = self.ui.CurFileListOld['SBC']['File']
        # CurPathFiles = []
        # # print(CurRopath,CurNavChosed,CurNetChosed,self.GetUpFileFaPath(info))
        # for i in CurFileList:
        #     CurPathFiles.append(i['filename']+'#'+str(i['isdir']))
        # if self.GetUpFileFaPath(info) not in CurPathFiles:
        #     self.ui.signalRefresh.emit()
        # self.UpManger()


        # info['statusLabel'].setText("校验文件...")
        # LofeMd5 = info['FileMd5']
        # if LofeMd5 == RofeMd5:
        #     info['statusLabel'].setText("校验通过")
        #     info['FeCheck'] = 1
        #     print('校验通过')
        # else:
        #     info['statusLabel'].setText("文件损坏")
        #     info['FeCheck'] = 0
        #     print('文件损坏')
        # info['timestamp'] = time.time()     # 当前时间戳
    def UpdateUpProgress(self,Labelinfo,info):
        # progressinfo = {'bar': progress, 'CurFileSize': CurFileSize1, 'FileTotSize': FileTotSize, 'Speed': Speed}
        # print(Labelinfo)
        try:
            # Labelinfo['statusButon'].setEnabled(False)
            Labelinfo['progressBar'].setProperty("value",info['bar'])
            Labelinfo['UpSizeLabel'].setText(
                "{}/{}".format(size_format(info['CurFileSize']),size_format(info['FileTotSize'])))
            Labelinfo['statusLabel'].setText("{}/S".format(info['Speed']))
        except Exception as e:
            print('UpdateProgessError',e)
    def Upact(self, info):
        # print('StartDown:',info['FileName'])
        # time.sleep(0.2)
        # self.UpFinsh(info)
        # return
        t0 = time.time()
        # print('Start', info)
        CurFileSize = 0
        CurFileSize0 = 0
        ShowProgress = 1
        dbManager = DBManager.DBManager()
        def Uping_callback(monitor, info):
            nonlocal t0,CurFileSize,CurFileSize0,ShowProgress
            if self.UpInfosUpdateLabs[str_trans_to_md5(info['RoFilePath'] + info['FileName'])]['isUp'] == 0:
                info['statusButon'].setEnabled(False)
            try:
                FileSeekStart = info['FileSeekStart']
                t1 = time.time()
                deltat = t1-t0
                if deltat >= 0.5 and ShowProgress:
                    CurFileSize1 = CurFileSize+monitor.bytes_read
                    FileTotSize = info['Size']
                    deltaFileSize = CurFileSize1 - CurFileSize0
                    progress = (CurFileSize1 / FileTotSize) * 100
                    Speed = size_format(deltaFileSize/(deltat))
                    # print(size_format(CurFileSize1), size_format(FileTotSize), progress)
                    # print('Check:',CurFileSize1/1024/1024,FileTotSize/1024/1024,deltat,CurFileSize0/1024/1024)
                    # print('UpProgress:', monitor.bytes_read, monitor.len)
                    if progress >100:
                        progress =100

                    progressinfo = {'bar':progress,'CurFileSize':CurFileSize1,'FileTotSize':FileTotSize,'Speed':Speed}
                    self.signalaUpdateUpProgress.emit(info,progressinfo)
                    # UpdateShowThread1 = UpdateShowThread(info,progressinfo)
                    # UpdateShowThread1.Signal.connect(self.UpdateUpProgress)
                    # self.ui.MainWindow.WSQLUpThread.Signal.connect(self.UpManger)
                    # print('Counts',self.UpLayout[1].count(),len(self.UpInfosUpdateLabs))
                    # UpdateShowThread1.run()
                    # print('Progress', info)
                    # info['progressBar'].setProperty("value",20)
                    # print(info['FileName'],progress,info['progressBar'])
                    # info['progressBar'].setProperty("value", progress)
                    # info['UpSizeLabel'].setText(
                    #     "{}/{}".format(size_format(CurFileSize1),size_format(FileTotSize)))
                    # info['statusLabel'].setText("{}/S".format(Speed))

                    t0 = t1
                    CurFileSize0 = CurFileSize1
            except Exception as e:
                print('Error',e)


        info['FileSize'] = info['Size']
        info['CurPath'] = info['RoFilePath']
        info['webkitRelativePath'] = ''
        info1 = {}
        for i in info:
            info1[i] = info[i]
        del info1['frame']
        del info1['line']
        del info1['statusLabel']
        del info1['statusButon']
        del info1['UpSizeLabel']
        del info1['progressBar']
        # print(info['FileName'])
        RoCheckFile = self.ui.SBCRe.CheckRoFile(info1)
        if RoCheckFile['exist']:
            print('文件已存在')
            self.UpFinsh(info)
            return
        # print(info['FileName'])
        FileSeekStart = RoCheckFile['FileStart']
        info['FileSeekStart'] = FileSeekStart

        CurFileSize = FileSeekStart
        CurFileSize0 = FileSeekStart

        url_fileUp = 'http://' + self.ClientSetting['host'] + '/Upfile1/'
        headers = self.ui.SBCRe.headers
        info['statusButon'].setText("||")
        s = requests.Session()
        for chunk in self.chunked_file_reader(info):
            # res = s.post(url_fileUp, data=info, files={'file': chunk},headers=headers)
            UpInfoi = dbManager.GetUserUpRecord(info['LoFilePath'], info['FileName'])
            if UpInfoi and int(UpInfoi['isUp']) == 1:

                # info['progressBar'].setProperty("value", 20)
                # UpdateShowThread1.run()
                e = MultipartEncoder(
                    fields={
                        'FileInfo':json.dumps(info1),
                        'file': (info['FileName'], chunk, 'application/octet-stream'),  # 文件1
                            }
                )
                url_fileUp = 'http://' + self.ui.host + '/Upfile1/'
                m = MultipartEncoderMonitor(e,lambda e : Uping_callback(e,info))
                # m = MultipartEncoderMonitor(e)
                headers = self.ui.SBCRe.headers
                headers1 = {}
                headers1['Cookie'] = headers['Cookie']
                headers1['Content-Type'] = m.content_type
                try:
                    # print('开始上传',info['FileName'])
                    # r = s.post(url_fileUp, data={'FileInfo':info1}, headers=headers)
                    r = s.post(url_fileUp, data=m, headers=headers1)
                    # time.sleep(2)
                    # print('上传完成一波', info['FileName'])
                    CurFileSize += len(chunk)
                except Exception as e:
                    print('上传出错',e)
        if str_trans_to_md5(info['RoFilePath'] + info['FileName']) in self.UpInfosUpdateLabs:
            info['statusButon'].setEnabled(True)
        ShowProgress = 0
        dbManager.close()
        if CurFileSize == info['Size']:
            self.UpFinsh(info)



    def Up(self,info):
        Path = info['LoPath']
        LoFileSatus = info['LoFileSatus']
        LoFileSize = LoFileSatus['size']
        LoFileExist = LoFileSatus['exist']
        # print(info)
        if not os.path.exists(info['LoFilePath']):
            return
        # qmut_1.lock()

        t = threading.Thread(target=self.run1, args=(info,))
        t.setDaemon(True)
        t.start()
        return

        # self.run1(info)
            # self.start()
            # qmut_1.unlock()
    def run1(self,info):
        # return
        self.Upact(info)
        # while True:
        #     print(time.time())
        #     time.sleep(1)
        # pass
    def StartAll1(self):
        UpInfosUpdateLabs = {}
        infos = []
        for i in self.UpInfosUpdateLabs:
            UpInfosUpdateLabs[i] = self.UpInfosUpdateLabs[i]
        # self.PauseAll()
        # self.DownInfos = self.dbManager.GetUserDownRecordAll()
        for keyi in UpInfosUpdateLabs:
            i = UpInfosUpdateLabs[keyi]
            infos.append(i)
            i['statusButon'].setText(">")
            i['statusLabel'].setText("等待上传")
            self.UpInfosUpdateLabs[str_trans_to_md5(i['RoFilePath'] + i['FileName'])]['isUp'] = 2
        # self.dbManager1.setUpPar(0,0, 2)
        self.dbManager1.WSQL(infos, 'UpdataUserUpRecords',2)
        self.UpManger()
    def StartAll(self):
        t = threading.Thread(target=self.StartAll1)
        t.setDaemon(True)
        t.start()

    def PauseAll1(self):
        UpInfosUpdateLabs={}
        infos = []
        for i in self.UpInfosUpdateLabs:
            UpInfosUpdateLabs[i] = self.UpInfosUpdateLabs[i]
        try:
            for keyi in UpInfosUpdateLabs:
                i = UpInfosUpdateLabs[keyi]
                infos.append(i)
                i['statusButon'].setText(">")
                i['statusLabel'].setText("已暂停")
                self.UpInfosUpdateLabs[str_trans_to_md5(i['RoFilePath'] + i['FileName'])]['isUp'] = 0
            # self.dbManager1.setUpPar(0, 0, 0)
            self.dbManager1.WSQL(infos, 'UpdataUserUpRecords',0)
        except Exception as e:
            print('PauseError',e)
    def PauseAll(self):
        t = threading.Thread(target=self.PauseAll1)
        t.setDaemon(True)
        t.start()
        # dbManager = DBManager.DBManager()
        # DownInfos = dbManager.GetUserDownRecordAll()
        # for i in DownInfos:
        #     self.DownCancel(i)
        # dbManager.close()

    def CancelAll1(self):
        infos = []
        UpInfosUpdateLabs={}
        for i in self.UpInfosUpdateLabs:
            UpInfosUpdateLabs[i] = self.UpInfosUpdateLabs[i]

        for keyi in UpInfosUpdateLabs:
            i = UpInfosUpdateLabs[keyi]
            infos.append(i)
            infoi = UpInfosUpdateLabs[str_trans_to_md5(i['RoFilePath'] + i['FileName'])]
            # print('Finsh', info['FileName'])
            # UpLayout = self.ui.TranspscrollArea['Up']
            # infoi['frame'].setParent(None)
            # infoi['line'].setParent(None)
            self.UpLayout[1].removeWidget(infoi['frame'])
            sip.delete(infoi['frame'])
            self.UpLayout[1].removeWidget(infoi['line'])
            sip.delete(infoi['line'])
        self.dbManager1.WSQL(infos,'DelUserUpRecords')
        self.UpInfosUpdateLabs = {}
        self.UpLayout[3].setText(str(0))
    def CancelAll(self):
        t = threading.Thread(target=self.CancelAll1)
        t.setDaemon(True)
        t.start()
    def ButtonBind(self):
        self.DownLayout = self.ui.TranspscrollArea['Up']
        self.DownLayout[4].clicked.connect(self.StartAll)
        self.DownLayout[5].clicked.connect(self.PauseAll)
        self.DownLayout[6].clicked.connect(self.CancelAll)
    def UpManger(self):
        qmut_1.lock()
        self.UpManger1()
        qmut_1.unlock()
    def UpManger1(self):
        # return
        dbManager = DBManager.DBManager()
        UpInfos = dbManager.GetUserUpRecordAll()
        # self.UpLayout[3].setText(str(len(UpInfos)))
        CurUpNums = 0
        MaxUpNums = self.MaxUpNums
        WaitUp = []
        CurUp = []
        DelUp = []
        for i in UpInfos:
            if int(i['isUp'])==1:
                # if self.UpInfosUpdateLabs[str_trans_to_md5(i['LoFilePath'] + i['FileName'])]['isUp'] != 1:
                #     self.UpInfosUpdateLabs[str_trans_to_md5(i['LoFilePath'] + i['FileName'])]['isUp'] = 1
                #     self.Up(self.UpInfosUpdateLabs[str_trans_to_md5(i['LoFilePath'] + i['FileName'])])
                CurUpNums += 1
                CurUp.append(i)
            elif int(i['isUp']) == 2:
                WaitUp.append(i)
            elif int(i['isUp']) == 3:
                DelUp.append(i)
        for i in DelUp:
            # print('Del',i['FileName'])
            infoi = self.UpInfosUpdateLabs[str_trans_to_md5(i['RoFilePath'] + i['FileName'])]
            self.dbManager1.WSQL(i,'DelUserUpRecord')
            # UpLayout = self.ui.TranspscrollArea['Up']
            # infoi['frame'].setParent(None)
            # infoi['line'].setParent(None)
            self.UpLayout[1].removeWidget(infoi['frame'])
            sip.delete(infoi['frame'])
            self.UpLayout[1].removeWidget(infoi['line'])
            sip.delete(infoi['line'])
            # QApplication.processEvents()

            # print('Del1', i['FileName'])
            del self.UpInfosUpdateLabs[str_trans_to_md5(i['RoFilePath'] + i['FileName'])]
        UpInfos = dbManager.GetUserUpRecordAll()
        self.UpLayout[3].setText(str(len(UpInfos)))
        dbManager.close()
        if CurUpNums < MaxUpNums:
            for i in range(MaxUpNums-CurUpNums):
                if i < len(WaitUp):
                    info = WaitUp[i]
                    # self.dbManager1.setUpPar(info['LoFilePath'], info['FileName'], 1)
                    self.dbManager1.WSQL(info,'UpdataUserUpRecord',1)
                    # dbManager.UpdataUserUpRecord(info['LoFilePath'], info['FileName'], 1)
                    infoi = self.UpInfosUpdateLabs[str_trans_to_md5(info['RoFilePath'] + info['FileName'])]
                    self.Up(infoi)
        # print(CurUpNums,MaxUpNums)
        if CurUpNums > MaxUpNums:
            for i in CurUp:
                if CurUpNums > MaxUpNums:
                    # self.dbManager1.setUpPar(i['LoFilePath'], i['FileName'], 2)
                    self.dbManager1.WSQL(i, 'UpdataUserUpRecord',2)
                    # self.dbManager.UpdataUserUpRecord(i['LoFilePath'], i['FileName'], 2)
                    infoi = self.UpInfosUpdateLabs[str_trans_to_md5(i['RoFilePath'] + i['FileName'])]
                    infoi['statusButon'].setText(">")
                    infoi['statusLabel'].setText("等待上传")
                    CurUpNums -= 1
        # dbManager.close()

    def AddUpFiles(self,info):
        # t = threading.Thread(target=lambda :self.signaladdUp.emit(info))
        self.signaladdUp.emit(info)
        # t.start()

    def AddUping(self,UpInfos=None):
        if not UpInfos:
            UpInfos = self.dbManager.GetUserUpRecordAll()

        self.signaladdUp.emit(UpInfos)
        # pass
    def UpdateDOwnNums(self,infos):
        self.UpLayout[3].setText(str(len(infos)))
        self.UpManger()

    def WSQL(self,info):
        self.dbManager1.WSQL(info, 'AddUserUpRecords')
        UpLayout = self.ui.TranspscrollArea['Up']
        UpLayout[3].setText(str(len(info)))
        self.UpManger()
    def AddUping1(self,UpInfos):
        FilesSQL = []
        for UpInfo in UpInfos:
            UpInfoExist = self.dbManager.GetUserUpRecord(UpInfo['LoFilePath'],UpInfo['FileName'])
            if not UpInfoExist or 'statusButon' not in UpInfo:
                UpInfo['size'] = UpInfo['Size']
                UpverticalLayout = self.UpLayout[1]
                scrollAreaWidgetContents_up = self.UpLayout[2]
                if 'isUp' not in UpInfo:
                    UpInfo['isUp'] = 2
                UpInfos = self.dbManager.GetUserUpRecordAll()
                self.UpLayout[3].setText(str(len(UpInfos)))
                Upinginfoi = self.add(scrollAreaWidgetContents_up,UpInfo)
                form = Upinginfoi['frame']
                UpverticalLayout.addWidget(form)
                line_3 = QtWidgets.QFrame(scrollAreaWidgetContents_up)
                line_3.setMinimumSize(QtCore.QSize(649, 0))
                line_3.setFrameShape(QtWidgets.QFrame.HLine)
                line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
                line_3.setObjectName("line_3")
                UpverticalLayout.addWidget(line_3)
                self.UpInfosUpdateLabs[str_trans_to_md5(UpInfo['RoFilePath'] + UpInfo['FileName'])]['line'] = line_3
                if not UpInfoExist:
                    FilesSQL.append(UpInfo)
            # QApplication.processEvents()

        if FilesSQL:
            # pass
            self.WSQLUpThread = threading.Thread(target=self.WSQL,args=(FilesSQL,))
            self.WSQLUpThread.setDaemon(True)
            self.WSQLUpThread.start()

            # self.ui.MainWindow.WSQLUpThread = WSQLThread(self.ui,FilesSQL,self.dbManager1)
            # self.ui.MainWindow.WSQLUpThread.Signal.connect(self.UpdateDOwnNums)
            # # self.ui.MainWindow.WSQLUpThread.Signal.connect(self.UpManger)
            # self.ui.MainWindow.WSQLUpThread.start()
        else:
            self.UpManger()


