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
import threading






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
class TransUp():
    # signal = pyqtSignal()
    # signaladdUp = pyqtSignal(dict)
    def __init__(self,ui,signaladdUp):
        super().__init__()
        self.ui = ui
        self.signaladdUp = signaladdUp
        self.dbManager = DBManager.DBManager()
        self.ClientSetting = self.dbManager.GetClientSetting()
        self.UpInfosUpdateLabs = {}
        self.signaladdUp.connect(self.AddUping1)
        self.RefreshUping()

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
        if int(UpInfo['isUp']) == 2:
            self.label_29.setText("等待上传")

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
        self.UpInfosUpdateLabs[str_trans_to_md5(Upinginfoi['LoPath'])] = Upinginfoi

        self.label_30.mousePressEvent = partial(self.UpSatusChange,Upinginfoi)
        self.label_31.mousePressEvent = partial(self.DelUping,Upinginfoi)

        return Upinginfoi


    def UpCancel(self,info):
        dbManager = DBManager.DBManager()

        info['statusButon'].setText(">")
        info['statusLabel'].setText("已暂停")
        dbManager.UpdataUserUpRecord(info['LoFilePath'], info['FileName'], 0)
        # info['isDown'] = 0
        dbManager.close()
        self.UpManger()
    def UpGon(self,info):
        dbManager = DBManager.DBManager()
        info['statusButon'].setText("||")
        dbManager.UpdataUserUpRecord(info['LoFilePath'], info['FileName'], 1)
        # info['isDown'] = 1
        dbManager.close()
        self.Up(info)
        # self.Upact1(info)
        self.UpManger(info)
    def UpSatusChange(self,info,e):
        # print(info)
        dbManager = DBManager.DBManager()
        UpInfoi = dbManager.GetUserUpRecord(info['LoFilePath'], info['FileName'])
        if UpInfoi and int(UpInfoi['isUp'])==1:
            self.UpCancel(info)
        else:
            self.UpGon(info)
    def DelUping(self,info,e):
        dbManager = DBManager.DBManager()
        dbManager.DelUserUpRecord(info['LoFilePath'],info['FileName'])
        self.UpLayout[1].removeWidget(info['frame'])
        sip.delete(info['frame'])
        self.UpLayout[1].removeWidget(info['line'])
        sip.delete(info['line'])
        # self.RefreshUping()
        UpInfos = dbManager.GetUserUpRecordAll()
        # print('UpS',UpInfos)
        self.UpLayout[3].setText(str(len(UpInfos)))
        del self.UpInfosUpdateLabs[str_trans_to_md5(info['LoFilePath']+info['FileName'])]
        dbManager.close()


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
        nav = self.ui.nav[self.ui.CurNetChosed]
        CurRopath = nav[-1]['path']
        CurPathFa = CurPath.replace(CurRopath,'')
        if CurPathFa:
            CurPathFa = CurPathFa.split('/')[0]+'#1'
        else:
            CurPathFa = info['FileName'] + '#0'
        return CurPathFa


    def UpFinsh(self,info):
        CurNavChosed = self.ui.CurNavChosed
        CurNetChosed = self.ui.CurNetChosed
        CurFileList = self.ui.CurFileListOld[CurNetChosed][CurNavChosed]
        CurPathFiles = []
        # print(CurRopath,CurNavChosed,CurNetChosed,self.GetUpFileFaPath(info))
        for i in CurFileList:
            CurPathFiles.append(i['filename']+'#'+str(i['isdir']))
        if self.GetUpFileFaPath(info) not in CurPathFiles:
            print('UPdate')
            self.ui.signalRefresh.emit()

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
        self.DelUping(info,0)
        self.UpManger()
    def Upact(self, info):

        t0 = time.time()
        CurFileSize = 0
        CurFileSize0 = 0
        def Uping_callback(monitor, info):
            nonlocal t0,CurFileSize,CurFileSize0
            FileSeekStart = info['FileSeekStart']
            t1 = time.time()
            deltat = t1-t0
            if deltat >= 0.5:
                CurFileSize1 = CurFileSize+monitor.bytes_read
                FileTotSize = info['Size']
                deltaFileSize = CurFileSize1 - CurFileSize0
                progress = (CurFileSize1 / FileTotSize) * 100
                Speed = size_format(deltaFileSize/(deltat))
                # print(Speed, progress)
                # print('Check:',CurFileSize1/1024/1024,FileTotSize/1024/1024,deltat,CurFileSize0/1024/1024)
                # print('UpProgress:', monitor.bytes_read, monitor.len)
                info['progressBar'].setProperty("value", progress)
                info['UpSizeLabel'].setText(
                    "{}/{}".format(size_format(CurFileSize1),size_format(FileTotSize)))
                info['statusLabel'].setText("{}/S".format(Speed))
                t0 = t1
                CurFileSize0 = CurFileSize1


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
        RoCheckFile = self.ui.SBCRe.CheckRoFile(info1)
        if RoCheckFile['exist']:
            print('文件已存在')
            self.UpFinsh(info)
            return
        FileSeekStart = RoCheckFile['FileStart']
        info['FileSeekStart'] = FileSeekStart

        CurFileSize = FileSeekStart
        CurFileSize0 = FileSeekStart

        url_fileUp = 'http://' + self.ClientSetting['host'] + '/Upfile1/'
        headers = self.ui.SBCRe.headers
        s = requests.Session()
        dbManager = DBManager.DBManager()
        for chunk in self.chunked_file_reader(info):
            # res = s.post(url_fileUp, data=info, files={'file': chunk},headers=headers)
            UpInfoi = dbManager.GetUserUpRecord(info['LoFilePath'], info['FileName'])
            if UpInfoi and int(UpInfoi['isUp']) == 1:
                info['statusButon'].setText("||")
                e = MultipartEncoder(
                    fields={
                        'FileInfo':json.dumps(info1),
                        'file': (info['FileName'], chunk, 'application/octet-stream'),  # 文件1
                            }
                )
                url_fileUp = 'http://' + self.ClientSetting['host'] + '/Upfile1/'
                m = MultipartEncoderMonitor(e,lambda e : Uping_callback(e,info))
                headers = self.ui.SBCRe.headers
                headers1 = {}
                headers1['Cookie'] = headers['Cookie']
                headers1['Content-Type'] = m.content_type
                r = s.post(url_fileUp, data=m, headers=headers1)
                CurFileSize += len(chunk)
        if CurFileSize == info['Size']:
            self.UpFinsh(info)
        dbManager.close()


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
        # self.run1(info)
            # self.start()
            # qmut_1.unlock()
    def run1(self,info):
        # return
        self.Upact(info)
        # pass
    def UpManger(self,Upinfo = None):
        dbManager = DBManager.DBManager()
        UpInfos = dbManager.GetUserUpRecordAll()

        CurUpNums = 0
        MaxUpNums = 2
        WaitUp = []
        CurUp = []
        for i in UpInfos:
            if int(i['isUp'])==1:
                CurUpNums += 1
                CurUp.append(i)
            elif int(i['isUp']) == 2:
                WaitUp.append(i)
        if CurUpNums < MaxUpNums:
            for i in range(MaxUpNums-CurUpNums):
                if i < len(WaitUp):
                    info = WaitUp[i]
                    dbManager.UpdataUserUpRecord(info['LoFilePath'], info['FileName'], 1)
                    infoi = self.UpInfosUpdateLabs[str_trans_to_md5(info['LoFilePath'] + info['FileName'])]
                    self.Up(infoi)

        if CurUpNums > MaxUpNums:
            for i in CurUp:
                if CurUpNums > MaxUpNums:
                    if not Upinfo or Upinfo['LoFilePath']+Upinfo['FileName'] == i['LoFilePath']+i['FileName']:
                        # print(i)
                        dbManager.UpdataUserUpRecord(i['LoFilePath'], i['FileName'],2)
                        infoi = self.UpInfosUpdateLabs[str_trans_to_md5(i['LoFilePath'] + i['FileName'])]
                        infoi['statusButon'].setText(">")
                        infoi['statusLabel'].setText("等待上传")
                        CurUpNums -= 1
        dbManager.close()
    def AddUping(self,UpInfo):
        self.signaladdUp.emit(UpInfo)
        # pass
    def AddUping1(self,UpInfo):
        # print(UpInfo)
        UpInfo['size'] = UpInfo['Size']
        UpLayout = self.ui.TranspscrollArea['Up']
        UpverticalLayout = UpLayout[1]
        scrollAreaWidgetContents_up = UpLayout[2]
        dbManager = DBManager.DBManager()
        dbManager.AddUserUpRecord(UpInfo)
        UpInfo['isUp'] =2
        UpInfos = dbManager.GetUserUpRecordAll()
        UpLayout[3].setText(str(len(UpInfos)))
        Upinginfoi = self.add(scrollAreaWidgetContents_up,UpInfo)
        form = Upinginfoi['frame']
        UpverticalLayout.addWidget(form)
        line_3 = QtWidgets.QFrame(scrollAreaWidgetContents_up)
        line_3.setMinimumSize(QtCore.QSize(649, 0))
        line_3.setFrameShape(QtWidgets.QFrame.HLine)
        line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        line_3.setObjectName("line_3")
        UpverticalLayout.addWidget(line_3)
        Upinginfoi['line'] = line_3
        dbManager.close()
        self.UpManger()
    def RefreshUping(self):
        self.infos = []
        UpLayout = self.ui.TranspscrollArea['Up']
        self.UpLayout = UpLayout
        UpformLayout = UpLayout[0]
        UpverticalLayout = UpLayout[1]
        scrollAreaWidgetContents_Up = UpLayout[2]
        LaConts = UpverticalLayout.count()
        dbManager = DBManager.DBManager()
        UpInfos = dbManager.GetUserUpRecordAll()
        # self.checkDelFile()
        self.UpLayout[3].setText(str(len(UpInfos)))
        # print(66,UpInfos)
        for i in UpInfos:
            Upinginfoi = self.add(scrollAreaWidgetContents_Up, i)
            form = Upinginfoi['frame']
            UpverticalLayout.addWidget(form)
            line_3 = QtWidgets.QFrame(scrollAreaWidgetContents_Up)
            line_3.setMinimumSize(QtCore.QSize(649, 0))
            line_3.setFrameShape(QtWidgets.QFrame.HLine)
            line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
            line_3.setObjectName("line_3")
            UpverticalLayout.addWidget(line_3)
            Upinginfoi['line'] = line_3
            # ThreadUpdatei = ThreadUpdate(self.ui)
            # # ThreadUpdatei.setPar(Upinginfoi)
            # ThreadUpdatei.Up(Upinginfoi)
            self.Up(Upinginfoi)
        self.UpManger()

