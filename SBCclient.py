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
                    SBCM.ChoseNav_Video()
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

    def ChoseNet(self,WosLabel,e):
        if e.buttons() == QtCore.Qt.LeftButton:
            if self.ui.CurNetChosed != WosLabel:
                if WosLabel == 'SBC':
                    pass
                if WosLabel == 'BDC':
                    pass

class ChoseNetNav():
    def __init__(self):
        pass
    def CreatFrame(self):
        self.frame_ChoseNet = QtWidgets.QFrame(ui.frame_14)
        self.frame_ChoseNet.setGeometry(QtCore.QRect(220, 25, 101, 171))
        self.frame_ChoseNet.setStyleSheet("#frame_ChoseNet\n"
                                          "{\n"
                                          "    background:#D0D3D4;\n"
                                          "}\n"
                                          "\n"
                                          "#frame_ChoseNet QLabel:hover{\n"
                                          "    background:#A2D9CE;\n"
                                          "    \n"
                                          "    opacity:0.5;\n"
                                          "    }")
        self.frame_ChoseNet.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ChoseNet.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ChoseNet.setObjectName("frame_ChoseNet")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_ChoseNet)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_ChoseNet)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_ChoseNet)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_ChoseNet)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        # self.retranslateUi(Form)
        # QtCore.QMetaObject.connectSlotsByName(Form)
        self.label.setText("小黑云")
        self.label_2.setText("百度云")
        self.label_3.setText("阿里云")
        ui.frame_ChoseNet = self.frame_ChoseNet
        ui.choseSBCLabel = self.label
        ui.choseBDCLabel = self.label_2
        ui.choseALCLabel = self.label_3
        ui.frame_ChoseNet.hide()




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
        self.frame_ChoseNetshow = 0
        self.initdWindow()

        # self.signal.connect(self.Refresh)


    def WindowReSize(self):
        # if ui.scrollArea.width() < 500:
        #     w = 760
        # else:
        #     w = ui.scrollArea.width()
        w = Main.width() - 150

        if ui.CurNavChosed in ui.SBCFilesDict[ui.CurNetChosed]:
            CurSBCFilesDict = ui.SBCFilesDict[ui.CurNetChosed][ui.CurNavChosed]['File']
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


    def initFrame(self):
        ui.nav = {}
        # ui.nav['SBC'] = {}
        # ui.nav['BDC'] = {}
        # ui.nav['ALC'] = {}
        ui.frameandscroll = {}
        ui.frameandscroll['SBC'] = {}
        ui.frameandscroll['BDC'] = {}
        ui.frameandscroll['ALC'] = {}
        ui.SBCFilesDict = {}
        ui.SBCFilesDict['SBC'] = {}
        ui.SBCFilesDict['BDC'] = {}
        ui.SBCFilesDict['ALC'] = {}
        ui.FileCons = {}
        ui.FileCons['SBC'] = {}
        ui.FileCons['BDC'] = {}
        ui.FileCons['ALC'] = {}
        for i in ui.frameandscroll:
            ui.frameandscroll[i]['Photo'] = subui.InitShow()
            ui.frameandscroll[i]['Video'] = subui.InitShow()
            # ui.frameandscroll[i]['File'] = subui.InitFileShow()
            ui.frameandscroll[i]['File'] = subui.initfileshow()
        # ui.frameandscroll['Photo'] = subui.InitShow()
        # ui.frameandscroll['Video'] = subui.InitShow()
        # ui.frameandscroll['File'] = subui.InitFileShow()

    def initdWindow(self):
        global ui,Main
        ui.CurNetChosed = 'SBC'
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
        # Main.resizeEvent = self.MainWindowSizeChange
        ui.PhotoShowFilesDict = {}
        ui.VdeoShowFilesDict = {}
        ui.DocumenttoShowFilesDict = {}
        ui.SharehowFilesDict = {}
        # ui.SBCFilesDict = {}
        # ui.FileCons = {}
        ui.CurShow = ''
        Main.resizeEvent = self.MainWindowSizeChange
        # ui.frame_12.resizeEvent = self.MainWindowSizeChange

        chosenetnav = ChoseNetNav()
        chosenetnav.CreatFrame()
        ui.choseBDCLabel.mousePressEvent = partial(self.ClickEventDeals.NavChoose, 'File')

        ui.label_18.mousePressEvent = self.ChoseNetShow
        ui.frame_ChoseNet.leaveEvent = self.ChoseNetHide

        ui.choseBDCLabel.mousePressEvent = partial(self.ChoseNet, 'BDC')

        self.initFrame()

        self.HideFrames()
        subui.FileShow()

    def ChoseNet(self,chose,e):
        print(chose)

    def ChoseNetHide(self,e):
        ui.frame_ChoseNet.hide()
        self.frame_ChoseNetshow = 0

    def ChoseNetShow(self,e):
        if self.frame_ChoseNetshow:
            ui.frame_ChoseNet.hide()
            self.frame_ChoseNetshow = 0
        else:
            ui.frame_ChoseNet.show()
            self.frame_ChoseNetshow = 1


        # t = threading.Thread(target=self.ThreadRun,args=(path,))
        # t.setDaemon(True)
        # t.start()


    def HideFrames(self):
        # ui.frame_12.hide()
        for i in ui.frameandscroll:
            # print(i)
            ui.frameandscroll[i]['Photo']['frame'].hide()
            ui.frameandscroll[i]['Video']['frame'].hide()
            ui.frameandscroll[i]['File']['frame'].hide()

        # ui.frameandscroll['Photo']['frame'].hide()
        # ui.frameandscroll['Video']['frame'].hide()

    def ChoseNav_Photo(self):
        self.HideFrames()
        # ui.frame_12.hide()
        ui.CurShow = 'Photo'
        subui.PhotoShow()
        # subui.frame_PhotoShow.resizeEvent = self.MainWindowSizeChange1

    def ChoseNav_File(self):
        self.HideFrames()
        subui.FileShow()
        # ui.frame_PhotoShow.hide()
        # ui.frame_12.show()

        # ui.scrollAreaWidgetContents.raise_()
    def ChoseNav_Video(self):
        self.HideFrames()
        # ui.frame_12.hide()
        subui.VideoShow()







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
    # ui.frameandscroll = {}
    # ui.frameandscroll['Photo'] = subui.InitShow()
    # ui.frameandscroll['Video'] = subui.InitShow()
    # ui.frameandscroll['File'] = subui.InitFileShow()

    SBCM = SBC()
    # SBCM.FileShow('/home/')

    print(Main.width())
    Main.show()
    sys.exit(app.exec_())