import sys,base64,threading
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from functools import partial
from PyQt5.QtGui import QFontMetrics
import SBCMainWindow
import time,io
from PyQt5.Qt import QThread
import os,hashlib
from PIL import Image
from ui import SubUi

from pack import SBCRequest




def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename ,"rb")
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()
def size_format(size):
    if size < 1024:
        return '%i' % size + 'size'
    elif 1024 <= size < 1024*1024:
        return '%.1f' % float(size/1024) + 'KB'
    elif 1024*1024 <= size < 1024*1024*1024:
        return '%.1f' % float(size/(1024*1024)) + 'MB'
    elif 1024*1024*1024 <= size < 1024*1024*1024*1024:
        return '%.1f' % float(size/(1024*1024*1024)) + 'GB'
    elif 1024*1024*1024*1024 <= size:
        return '%.1f' % float(size/(1024*1024*1024*1024)) + 'TB'
class Thread_LoadImg(QThread):
    def __init__(self):
        super().__init__()
        self.ui = ui
        # self.Thread_LoadImg = Thread_LoadImg(self.ui)

    def func(self,listTemp, n):
        for i in range(0, len(listTemp), n):
            yield listTemp[i:i + n]

    def ShowCon(self,px,base64data):
        ba = base64data
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(ba)
        px.setPixmap(pixmap)



    def run(self):
        temp = self.func(self.ui.FileCon, 2)
        for i in temp:
            SendList = [{'fepath':j['fepath']} for j in i]
            # print('send',SendList)
            ConList = SBCRe.GetFileCon(SendList)
            try:
                for num in range(len(ConList['src'])):
                    coninfo = ConList['src'][num]
                    ConBase64 = coninfo.split(',')[-1]
                    img_b64decode = base64.b64decode(ConBase64)  # [21:]
                    self.ShowCon(i[num]['con'],img_b64decode)
            except:
                # print('threderror')
                break



class ClickEventDeals():
    def __init__(self):
        self.ui = ui
    def DownDeal(self,e):
        pass
    def UpDeal(self,e):
        pass
    def ReameDeal(self,e):
        pass
    def MoreDeal(self,e):
        pass
    def ChooseNetDeal(self,e):
        pass
    def SearchDeal(self,e):
        pass
    def NetBackDeal(self,e):
        pass
    def NetRefresh(self,e):
        pass

    def ClearNavStyle(self):
        self.ui.frame_2.setStyleSheet("")
        self.ui.frame_3.setStyleSheet("")
        self.ui.frame_4.setStyleSheet("")
        self.ui.frame_5.setStyleSheet("")
        self.ui.frame_6.setStyleSheet("")
    def NavChoose(self,WosLabel,e):
        if e.buttons() == QtCore.Qt.LeftButton:
            if self.ui.CurNavChosed != WosLabel:
                self.ClearNavStyle()
                print(WosLabel)
                if WosLabel == 'Photo':
                    self.ui.CurNavChosed = 'Photo'
                    SBCM.ChoseNav_Photo()
                    self.ui.frame_3.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")
                if WosLabel == 'File':
                    self.ui.CurNavChosed = 'File'
                    SBCM.ChoseNav_File()
                    self.ui.frame_2.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")
                if WosLabel == 'Video':
                    self.ui.CurNavChosed = 'Video'
                    self.ui.frame_4.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")
                if WosLabel == 'Share':
                    self.ui.CurNavChosed = 'Share'
                    self.ui.frame_5.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")
                if WosLabel == 'Transmit':
                    self.ui.CurNavChosed = 'Transmit'
                    self.ui.frame_6.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")

    def FileClickDeal(self,FileInfo,e):
        if e.buttons() == QtCore.Qt.LeftButton:
            self.FileLeftDeal(FileInfo)
        elif e.buttons() == QtCore.Qt.RightButton:
            self.FileRightDeal(FileInfo)
    def FileLeftDeal(self,FileInfo):
        print('FileLeft',FileInfo)
        SBCM.FileShow(FileInfo['fepath'])

    def FileRightDeal(self,FileInfo):
        print("右")
        SBCM.FileShow('/home/')


class SBC(QThread):
    signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        # self.ui = ui
        # self.Main = Main
        # self.Main.resizeEvent = self.MainWindowSizeChange
        self.width0 = 900
        self.height0 = 700
        self.ClickEventDeals = ClickEventDeals()
        self.Thread_LoadImg = Thread_LoadImg()

        self.initdWindow()

        self.signal.connect(self.Refresh)

    def MainWindowSizeChange(self,e):
        if ui.scrollArea.width() < 500:
            w = 760
        else:
            w = ui.scrollArea.width()
        for i in ui.CurSBCFilesDict:
            FIleinfo = ui.CurSBCFilesDict[i]
            FileName = FIleinfo['fename']
            Felabel = FIleinfo['FileNameLabel']
            # print(Felabel)
            metrics = QFontMetrics(Felabel.font())
            # print(metrics)
            new_file_name = metrics.elidedText(FileName, Qt.ElideRight, w*0.5)
            Felabel.setText(new_file_name)

    def FileConChose(self,fetype):
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

    def initdWindow(self):
        global ui,Main
        ui.CurSBCFilesDict = {}
        ui.frame_13.deleteLater()
        ui.frame_2.mousePressEvent = partial(self.ClickEventDeals.NavChoose,'File')
        ui.frame_3.mousePressEvent = partial(self.ClickEventDeals.NavChoose, 'Photo')
        ui.frame_4.mousePressEvent = partial(self.ClickEventDeals.NavChoose, 'Video')
        ui.frame_5.mousePressEvent = partial(self.ClickEventDeals.NavChoose, 'Share')
        ui.frame_6.mousePressEvent = partial(self.ClickEventDeals.NavChoose, 'Transmit')
        ui.CurNavChosed = 'File'
        ui.frame_2.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")
        Main.resize(self.width0, self.height0)
        Main.setMinimumSize(QtCore.QSize(800, 700))
        Main.resizeEvent = self.MainWindowSizeChange


    def run(self):
        SBCRe.GetFileList(self.path)
        self.CurFileListOld = SBCRe.CurFileList
        self.CurFileList = SBCRe.CurFileList
        self.signal.emit()

    def FileShow(self,path):
        self.path = path

        if self.isRunning():
            self.wait()
        self.start()
        # t = threading.Thread(target=self.ThreadRun,args=(path,))
        # t.setDaemon(True)
        # t.start()


    def Refresh(self):
        global ui, Main


        ui.scrollAreaWidgetContents.deleteLater()
        ui.formLayout.deleteLater()
        for i in ui.CurSBCFilesDict:
            ui.CurSBCFilesDict[i]['frame'].deleteLater()
            break


        ui.CurSBCFilesDict = {}
        ui.FileCon = []

        ui.scrollAreaWidgetContents = QtWidgets.QWidget()
        ui.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 806, 565))
        ui.scrollAreaWidgetContents.setLayoutDirection(QtCore.Qt.LeftToRight)
        ui.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        ui.formLayout = QtWidgets.QFormLayout(ui.scrollAreaWidgetContents)
        ui.formLayout.setContentsMargins(0, 0, 0, 0)
        ui.formLayout.setVerticalSpacing(0)
        ui.formLayout.setObjectName("formLayout")
        for i in range(len(self.CurFileList)):

            CurSBCFiles = {}
            FileInfo = self.CurFileList[i]

            CurSBCFiles['frame'] = QtWidgets.QFrame(ui.scrollAreaWidgetContents)

            CurSBCFiles['frame'].setMinimumSize(QtCore.QSize(0, 36))
            CurSBCFiles['frame'].setMaximumSize(QtCore.QSize(16777215, 36))
            CurSBCFiles['frame'].setFrameShape(QtWidgets.QFrame.StyledPanel)
            CurSBCFiles['frame'].setFrameShadow(QtWidgets.QFrame.Raised)
            CurSBCFiles['frame'].setObjectName("frame_13")
            horizontalLayout_14 = QtWidgets.QHBoxLayout(CurSBCFiles['frame'])
            horizontalLayout_14.setContentsMargins(3, 0, 9, 0)
            horizontalLayout_14.setSpacing(0)
            horizontalLayout_14.setObjectName("horizontalLayout_14")
            horizontalLayout_13 = QtWidgets.QHBoxLayout()
            horizontalLayout_13.setContentsMargins(0, 0, 0, -1)
            horizontalLayout_13.setSpacing(6)
            horizontalLayout_13.setObjectName("horizontalLayout_13")

            ui.checkBox_2 = QtWidgets.QCheckBox(CurSBCFiles['frame'])

            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(ui.checkBox_2.sizePolicy().hasHeightForWidth())
            ui.checkBox_2.setSizePolicy(sizePolicy)
            ui.checkBox_2.setText("")
            ui.checkBox_2.setObjectName("checkBox_2")
            horizontalLayout_13.addWidget(ui.checkBox_2)


            CurSBCFiles['con'] = QtWidgets.QLabel(CurSBCFiles['frame'])
            CurSBCFiles['con'].setMaximumSize(QtCore.QSize(36, 36))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(CurSBCFiles['con'].sizePolicy().hasHeightForWidth())
            CurSBCFiles['con'].setSizePolicy(sizePolicy)
            CurSBCFiles['con'].setAlignment(QtCore.Qt.AlignCenter)
            CurSBCFiles['con'].setObjectName("label_27")
            horizontalLayout_13.addWidget(CurSBCFiles['con'])


            CurSBCFiles['FileNameLabel'] = QtWidgets.QLabel(CurSBCFiles['frame'])
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(9)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(CurSBCFiles['FileNameLabel'].sizePolicy().hasHeightForWidth())
            CurSBCFiles['FileNameLabel'].setSizePolicy(sizePolicy)
            CurSBCFiles['FileNameLabel'].setMinimumSize(QtCore.QSize(0, 30))
            CurSBCFiles['FileNameLabel'].setMaximumSize(QtCore.QSize(16777215, 36))
            CurSBCFiles['FileNameLabel'].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

            CurSBCFiles['FileNameLabel'].setObjectName(FileInfo["filelj"])

            horizontalLayout_13.addWidget(CurSBCFiles['FileNameLabel'])
            horizontalLayout_13.setStretch(0, 1)
            horizontalLayout_13.setStretch(1, 1)
            horizontalLayout_13.setStretch(2, 20)
            horizontalLayout_14.addLayout(horizontalLayout_13)
            ui.label_29 = QtWidgets.QLabel(CurSBCFiles['frame'])
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(3)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(ui.label_29.sizePolicy().hasHeightForWidth())
            ui.label_29.setSizePolicy(sizePolicy)
            ui.label_29.setAlignment(QtCore.Qt.AlignCenter)
            ui.label_29.setObjectName("label_29")
            horizontalLayout_14.addWidget(ui.label_29)
            ui.label_30 = QtWidgets.QLabel(CurSBCFiles['frame'])
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(3)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(ui.label_30.sizePolicy().hasHeightForWidth())
            ui.label_30.setSizePolicy(sizePolicy)
            ui.label_30.setAlignment(QtCore.Qt.AlignCenter)
            ui.label_30.setObjectName("label_30")
            horizontalLayout_14.addWidget(ui.label_30)
            horizontalLayout_14.setStretch(0, 7)
            horizontalLayout_14.setStretch(1, 2)
            horizontalLayout_14.setStretch(2, 2)
            ui.formLayout.setWidget(i, QtWidgets.QFormLayout.SpanningRole, CurSBCFiles['frame'])

            metrics = QFontMetrics(CurSBCFiles['FileNameLabel'].font())
            new_file_name = metrics.elidedText(FileInfo['filename'], Qt.ElideRight, 300)
            CurSBCFiles['FileNameLabel'].setText(new_file_name)

            filepath = base64.decodebytes(FileInfo['filelj'].encode('utf8')).decode()
            CurSBCFiles['fepath'] = filepath
            CurSBCFiles['fename'] = FileInfo['filename']
            CurSBCFiles['fepath_base64'] = FileInfo['filelj']

            if FileInfo['fetype'] == 'img':
                ui.FileCon.append(CurSBCFiles)
            CurSBCFiles['con'].setText("")
            CurSBCFiles['con'].setPixmap(QtGui.QPixmap(self.FileConChose(FileInfo['fetype'])))
            CurSBCFiles['con'].setScaledContents(True)

            ui.label_29.setText(FileInfo['date'])
            ui.label_30.setText(FileInfo['big'])
            CurSBCFiles['FileNameLabel'].mousePressEvent = partial(self.ClickEventDeals.FileClickDeal, CurSBCFiles)

            ui.CurSBCFilesDict[FileInfo['filelj']] = CurSBCFiles

        ui.scrollArea.setWidget(ui.scrollAreaWidgetContents)


        if self.Thread_LoadImg.isRunning():
            self.Thread_LoadImg.wait()
        self.Thread_LoadImg.start()

    def ChoseNav_Photo(self):
        ui.frame_12.hide()
        subui.InitShow()
    def ChoseNav_File(self):
        ui.frame_PhotoShow.hide()
        ui.frame_12.show()
        # ui.scrollAreaWidgetContents.raise_()







# # 加载图片
# self.label_2.setPixmap(QtGui.QPixmap("./res/tay.jpeg"))
# # 图片居中
# self.label_2.setAlignment(Qt.AlignCenter)
# # 图片自适应控件尺寸
# self.label_2.setScaledContents(True)

if __name__ == '__main__':
    # clickdeal = EventDeals()
    SBCRe = SBCRequest.SBCRe()
    app = QApplication(sys.argv)
    Main = QMainWindow()
    ui = SBCMainWindow.Ui_SBCclient()
    ui.setupUi(Main)
    subui = SubUi.Ui_PhotoShow(ui)
    SBCM = SBC()
    SBCM.FileShow('/home/')

    Main.show()
    sys.exit(app.exec_())