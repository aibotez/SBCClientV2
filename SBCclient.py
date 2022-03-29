import sys,base64
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import SBCMainWindow
import time,io
from PyQt5.Qt import QThread
import os,hashlib
from PIL import Image

from pack import SBCRequest



class Thread_LoadImg(QThread):
    def __init__(self,ui):
        super().__init__()
        self.ui = ui

    def func(self,listTemp, n):
        for i in range(0, len(listTemp), n):
            yield listTemp[i:i + n]

    def ShowCon(self,px,base64data):
        # with open(str(num) + '.jpg', 'wb') as f:
        #     f.write(img_b64decode)
        img_io = io.BytesIO(base64data)
        img = Image.open(img_io)
        pix = img.toqpixmap()
        px.setPixmap(pix)
        px.setScaledContents(True)
    def run(self):
        temp = self.func(self.ui.FileCon, 3)
        for i in temp:
            SendList = [{'fepath':j['fepath']} for j in i]
            print('SendList',SendList)
            ConList = SBCRe.GetFileCon(SendList)
            for num in range(len(ConList['src'])):
                coninfo = ConList['src'][num]
                ConBase64 = coninfo.split(',')[-1]
                img_b64decode = base64.b64decode(ConBase64)  # [21:]

                i[num]['label'].setText(str(num))
                # self.ShowCon(i[num]['label'],img_b64decode)
                # with open(str(num)+'.jpg','wb') as f:
                #     f.write(img_b64decode)
                # img_io = io.BytesIO(img_b64decode)
                # img = Image.open(img_io)
                # pix = img.toqpixmap()
                # print(i[num]['fepath'])
                # i[num]['label'].setPixmap(pix)
                # i[num]['label'].setScaledContents(True)
            break



class ClickEventDeals():
    def __init__(self,ui):
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
                    self.ui.frame_3.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")
                if WosLabel == 'File':
                    self.ui.CurNavChosed = 'File'
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

    def FileRightDeal(self,FileInfo):
        print("右")


class SBC():
    def __init__(self,Main,Mui):
        self.ui = Mui
        self.Main = Main
        # self.Main.resizeEvent = self.MainWindowSizeChange
        self.width0 = 900
        self.height0 = 700
        self.FileList = []
        self.ClickEventDeals = ClickEventDeals(self.ui)
        self.Thread_LoadImg = Thread_LoadImg(self.ui)

    def MainWindowSizeChange(self,e):
        if self.ui.scrollArea.width() < 500:
            w = 760
        else:
            w = self.ui.scrollArea.width()
        for i in self.ui.FileLabel:
            FileInfo = self.FileList[i]
            Felabel = self.ui.FileLabel[i]
            # print(Felabel)
            metrics = QFontMetrics(Felabel.font())
            # print(metrics)
            new_file_name = metrics.elidedText(FileInfo['filename'], Qt.ElideRight, w*0.5)
            Felabel.setText(new_file_name)

    def FileCon(self,fetype):
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
        self.ui.frame_2.mousePressEvent = partial(self.ClickEventDeals.NavChoose,'File')
        self.ui.frame_3.mousePressEvent = partial(self.ClickEventDeals.NavChoose, 'Photo')
        self.ui.frame_4.mousePressEvent = partial(self.ClickEventDeals.NavChoose, 'Video')
        self.ui.frame_5.mousePressEvent = partial(self.ClickEventDeals.NavChoose, 'Share')
        self.ui.frame_6.mousePressEvent = partial(self.ClickEventDeals.NavChoose, 'Transmit')
        self.ui.CurNavChosed = 'File'
        ui = self.ui
        ui.frame_2.setStyleSheet("background:#7DCEA0;border-radius:20px;opacity:0.5;")
        self.Main.resize(self.width0, self.height0)
        self.Main.setMinimumSize(QtCore.QSize(800, 700))
        SBCRe.GetFileList('/home/')
        ui.scrollAreaWidgetContents = QtWidgets.QWidget()
        ui.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 0.839*self.width0, 0.8328*self.height0))
        ui.scrollAreaWidgetContents.setLayoutDirection(QtCore.Qt.LeftToRight)
        ui.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        ui.formLayout = QtWidgets.QFormLayout(ui.scrollAreaWidgetContents)
        ui.formLayout.setContentsMargins(0, 0, 0, 0)
        ui.formLayout.setVerticalSpacing(0)
        ui.formLayout.setObjectName("formLayout")
        ui.FileLabel = {}
        ui.FileCon = []
        self.FileList = SBCRe.CurFileList
        print(SBCRe.imgFiles)
        for i in range(len(SBCRe.CurFileList)):
            FileConLabel = {}
            FileInfo = SBCRe.CurFileList[i]
            ui.frame_13 = QtWidgets.QFrame(ui.scrollAreaWidgetContents)
            ui.frame_13.setMinimumSize(QtCore.QSize(0, 36))
            ui.frame_13.setMaximumSize(QtCore.QSize(16777215, 36))
            ui.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
            ui.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
            ui.frame_13.setObjectName("frame_13")
            ui.horizontalLayout_14 = QtWidgets.QHBoxLayout(ui.frame_13)
            ui.horizontalLayout_14.setContentsMargins(3, 0, 9, 0)
            ui.horizontalLayout_14.setSpacing(0)
            ui.horizontalLayout_14.setObjectName("horizontalLayout_14")
            ui.horizontalLayout_13 = QtWidgets.QHBoxLayout()
            ui.horizontalLayout_13.setContentsMargins(0, 0, 0, -1)
            ui.horizontalLayout_13.setSpacing(6)
            ui.horizontalLayout_13.setObjectName("horizontalLayout_13")
            ui.checkBox_2 = QtWidgets.QCheckBox(ui.frame_13)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(ui.checkBox_2.sizePolicy().hasHeightForWidth())
            ui.checkBox_2.setSizePolicy(sizePolicy)
            ui.checkBox_2.setText("")
            ui.checkBox_2.setObjectName("checkBox_2")
            ui.horizontalLayout_13.addWidget(ui.checkBox_2)
            # ui.label_27 = QtWidgets.QLabel(ui.frame_13)
            FileConLabel['label'] = QtWidgets.QLabel(ui.frame_13)
            FileConLabel['label'].setMaximumSize(QtCore.QSize(36, 36))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(FileConLabel['label'].sizePolicy().hasHeightForWidth())
            FileConLabel['label'].setSizePolicy(sizePolicy)
            FileConLabel['label'].setAlignment(QtCore.Qt.AlignCenter)
            FileConLabel['label'].setObjectName("label_27")
            ui.horizontalLayout_13.addWidget(FileConLabel['label'])
            ui.FileLabel[i] = QtWidgets.QLabel(ui.frame_13)
            # ui.label_28 = QtWidgets.QLabel(ui.frame_13)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(9)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(ui.FileLabel[i].sizePolicy().hasHeightForWidth())
            ui.FileLabel[i].setSizePolicy(sizePolicy)
            ui.FileLabel[i].setMinimumSize(QtCore.QSize(0, 30))
            ui.FileLabel[i].setMaximumSize(QtCore.QSize(16777215, 36))
            ui.FileLabel[i].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

            ui.FileLabel[i].setObjectName(FileInfo["filelj"])
            # ui.FileLabel[i].setObjectName("label_28")

            ui.horizontalLayout_13.addWidget(ui.FileLabel[i])
            ui.horizontalLayout_13.setStretch(0, 1)
            ui.horizontalLayout_13.setStretch(1, 1)
            ui.horizontalLayout_13.setStretch(2, 20)
            ui.horizontalLayout_14.addLayout(ui.horizontalLayout_13)
            ui.label_29 = QtWidgets.QLabel(ui.frame_13)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(3)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(ui.label_29.sizePolicy().hasHeightForWidth())
            ui.label_29.setSizePolicy(sizePolicy)
            ui.label_29.setAlignment(QtCore.Qt.AlignCenter)
            ui.label_29.setObjectName("label_29")
            ui.horizontalLayout_14.addWidget(ui.label_29)
            ui.label_30 = QtWidgets.QLabel(ui.frame_13)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(3)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(ui.label_30.sizePolicy().hasHeightForWidth())
            ui.label_30.setSizePolicy(sizePolicy)
            ui.label_30.setAlignment(QtCore.Qt.AlignCenter)
            ui.label_30.setObjectName("label_30")
            ui.horizontalLayout_14.addWidget(ui.label_30)
            ui.horizontalLayout_14.setStretch(0, 7)
            ui.horizontalLayout_14.setStretch(1, 2)
            ui.horizontalLayout_14.setStretch(2, 2)
            ui.formLayout.setWidget(i, QtWidgets.QFormLayout.SpanningRole, ui.frame_13)
            ui.scrollArea.setWidget(ui.scrollAreaWidgetContents)
            ui.verticalLayout_2.addWidget(ui.scrollArea)

            # ui.FileLabel[i].setText(FileInfo['filename'])
            # print(ui.FileLabel[i].width())
            metrics = QFontMetrics(ui.FileLabel[i].font())
            new_file_name = metrics.elidedText(FileInfo['filename'], Qt.ElideRight, 360)
            ui.FileLabel[i].setText(new_file_name)

            if FileInfo['fetype'] == 'img':
                filepath = base64.decodebytes(FileInfo['filelj'].encode('utf8')).decode()
                FileConLabel['fepath'] = filepath
                ui.FileCon.append(FileConLabel)
            FileConLabel['label'].setText("")
            FileConLabel['label'].setPixmap(QtGui.QPixmap(self.FileCon(FileInfo['fetype'])))
            FileConLabel['label'].setScaledContents(True)
            # ui.FileLabel[i].setText(FileInfo['filename'])
            ui.label_29.setText(FileInfo['date'])
            ui.label_30.setText(FileInfo['big'])
            ui.FileLabel[i].mousePressEvent = partial(self.ClickEventDeals.FileClickDeal,FileInfo)
            self.Main.resizeEvent = self.MainWindowSizeChange
            # self.Main.resizeEvent = partial(self.MainWindowSizeChange, ui.FileLabel[i])
        self.ui.FileLabel = ui.FileLabel
        print(ui.FileCon)
        self.Thread_LoadImg.start()
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
from PyQt5.QtCore import *
from functools import partial
def print_some(i):
    print(i)
def print_some1(i,e):
    print(i)
    if e.buttons() == QtCore.Qt.LeftButton:
        print("左")
    # 右键按下
    elif e.buttons() == QtCore.Qt.RightButton:
        print("右")
    # 中键按下
    elif e.buttons() == QtCore.Qt.MidButton:
        print("中")

# def MainWindowSizeChange(e):
#     w = e.size().width()
#     h = e.size().height()
#     print(w,h)
from PyQt5.QtGui import QFontMetrics
def test(ui,clickdeal):
    SBCRe.GetFileList('/home/')
    ui.scrollAreaWidgetContents = QtWidgets.QWidget()
    ui.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 737, 583))
    ui.scrollAreaWidgetContents.setLayoutDirection(QtCore.Qt.LeftToRight)
    ui.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
    ui.formLayout = QtWidgets.QFormLayout(ui.scrollAreaWidgetContents)
    ui.formLayout.setContentsMargins(0, 0, 0, 0)
    ui.formLayout.setVerticalSpacing(0)
    ui.formLayout.setObjectName("formLayout")
    for i in range(len(SBCRe.CurFileList)):
        FileInfo = SBCRe.CurFileList[i]
        ui.frame_13 = QtWidgets.QFrame(ui.scrollAreaWidgetContents)
        ui.frame_13.setMinimumSize(QtCore.QSize(0, 36))
        ui.frame_13.setMaximumSize(QtCore.QSize(16777215, 36))
        ui.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ui.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        ui.frame_13.setObjectName("frame_13")
        ui.horizontalLayout_14 = QtWidgets.QHBoxLayout(ui.frame_13)
        ui.horizontalLayout_14.setContentsMargins(3, 0, 9, 0)
        ui.horizontalLayout_14.setSpacing(0)
        ui.horizontalLayout_14.setObjectName("horizontalLayout_14")
        ui.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        ui.horizontalLayout_13.setContentsMargins(0, 0, 0, -1)
        ui.horizontalLayout_13.setSpacing(6)
        ui.horizontalLayout_13.setObjectName("horizontalLayout_13")
        ui.checkBox_2 = QtWidgets.QCheckBox(ui.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui.checkBox_2.sizePolicy().hasHeightForWidth())
        ui.checkBox_2.setSizePolicy(sizePolicy)
        ui.checkBox_2.setText("")
        ui.checkBox_2.setObjectName("checkBox_2")
        ui.horizontalLayout_13.addWidget(ui.checkBox_2)
        ui.label_27 = QtWidgets.QLabel(ui.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui.label_27.sizePolicy().hasHeightForWidth())
        ui.label_27.setSizePolicy(sizePolicy)
        ui.label_27.setAlignment(QtCore.Qt.AlignCenter)
        ui.label_27.setObjectName("label_27")
        ui.horizontalLayout_13.addWidget(ui.label_27)
        ui.label_28 = QtWidgets.QLabel(ui.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui.label_28.sizePolicy().hasHeightForWidth())
        ui.label_28.setSizePolicy(sizePolicy)
        ui.label_28.setMinimumSize(QtCore.QSize(0, 30))
        ui.label_28.setMaximumSize(QtCore.QSize(16777215, 36))
        ui.label_28.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        ui.label_28.setObjectName("label_28")
        ui.horizontalLayout_13.addWidget(ui.label_28)
        ui.horizontalLayout_13.setStretch(0, 1)
        ui.horizontalLayout_13.setStretch(1, 1)
        ui.horizontalLayout_13.setStretch(2, 20)
        ui.horizontalLayout_14.addLayout(ui.horizontalLayout_13)
        ui.label_29 = QtWidgets.QLabel(ui.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui.label_29.sizePolicy().hasHeightForWidth())
        ui.label_29.setSizePolicy(sizePolicy)
        ui.label_29.setAlignment(QtCore.Qt.AlignCenter)
        ui.label_29.setObjectName("label_29")
        ui.horizontalLayout_14.addWidget(ui.label_29)
        ui.label_30 = QtWidgets.QLabel(ui.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui.label_30.sizePolicy().hasHeightForWidth())
        ui.label_30.setSizePolicy(sizePolicy)
        ui.label_30.setAlignment(QtCore.Qt.AlignCenter)
        ui.label_30.setObjectName("label_30")
        ui.horizontalLayout_14.addWidget(ui.label_30)
        ui.horizontalLayout_14.setStretch(0, 7)
        ui.horizontalLayout_14.setStretch(1, 2)
        ui.horizontalLayout_14.setStretch(2, 2)
        ui.formLayout.setWidget(i, QtWidgets.QFormLayout.SpanningRole, ui.frame_13)
        ui.scrollArea.setWidget(ui.scrollAreaWidgetContents)
        ui.verticalLayout_2.addWidget(ui.scrollArea)

        # ui.label_28.setText(FileInfo['filename'])
        # print(ui.label_28.width())
        metrics = QFontMetrics(ui.label_28.font())
        new_file_name = metrics.elidedText(FileInfo['filename'], Qt.ElideRight, 200)
        ui.label_28.setText(new_file_name)

        ui.label_27.setText("con")
        # ui.label_28.setText(FileInfo['filename'])
        ui.label_29.setText(FileInfo['date'])
        ui.label_30.setText(FileInfo['big'])
        ui.label_28.mousePressEvent = partial(print_some, i)

# # 加载图片
# self.label_2.setPixmap(QtGui.QPixmap("./res/tay.jpeg"))
# # 图片居中
# self.label_2.setAlignment(Qt.AlignCenter)
# # 图片自适应控件尺寸
# self.label_2.setScaledContents(True)
def rs(e):
    print(66)
if __name__ == '__main__':
    # clickdeal = EventDeals()
    SBCRe = SBCRequest.SBCRe()
    app = QApplication(sys.argv)
    Main = QMainWindow()
    ui = SBCMainWindow.Ui_SBCclient()
    ui.setupUi(Main)
    SBCM = SBC(Main,ui)
    SBCM.initdWindow()
    # Main.resizeEvent = MainWindowSizeChange
    # ui.label_23.mousePressEvent = print_some
    # test(ui,clickdeal)
    Main.show()
    sys.exit(app.exec_())