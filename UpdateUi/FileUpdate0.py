import sys,threading
sys.path.append('..')
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QAction
from PyQt5.Qt import QThread
import SBCMainWindow
from PyQt5.QtGui import QFontMetrics,QCursor, QIcon
from PyQt5.QtCore import *
import base64
from pack import SBCRequest
from pack.preview import ImgPreview


class Thread_LoadImg(QThread):
    def __init__(self,MainWindow):
        super().__init__()
        self.MainWindow = MainWindow
        self.SBCRe = self.MainWindow.SBCRe

        # self.Thread_LoadImg = Thread_LoadImg(self.ui)

    def func(self, listTemp, n):
        for i in range(0, len(listTemp), n):
            yield listTemp[i:i + n]


    def ShowCon(self, px, base64data):
        ba = base64data
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(ba)
        px.setPixmap(pixmap)

    def runthread(self,MainWindow):
        self.MainWindow = MainWindow
        # print(self.FileCons)
        print(self.MainWindow.SBCFilesDict[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['File'])
        Files = self.MainWindow.SBCFilesDict[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['File']
        if len(Files) <= 0:
            return

        FilesKeys = list(Files.keys())
        ConHeight = Files[FilesKeys[0]]['frame'].height()
        ScrollFrameHeight = self.MainWindow.frameandscroll['SBC']['File']['scrollArea'].height()
        # print(ConHeight,ScrollFrameHeight)
        horizontal_bar = self.MainWindow.frameandscroll['SBC']['File']['scrollArea'].verticalScrollBar()
        # print(horizontal_bar.value(),horizontal_bar.maximum())
        # print(self.MainWindow.frameandscroll['SBC']['File']['scrollArea'].size())
        offset = int(horizontal_bar.value()/ConHeight)
        shownums = int(ScrollFrameHeight/ConHeight)

        self.start()

    def run1(self):
        if 'File' not in self.MainWindow.SBCFilesDict[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]:
            return
        Files = self.MainWindow.SBCFilesDict[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['File']
        if len(Files) <= 0:
            return
        FilesKeys = list(Files.keys())
        ConHeight = Files[FilesKeys[0]]['frame'].height()
        ScrollFrameHeight = self.MainWindow.frameandscroll['SBC']['File']['scrollArea'].height()
        horizontal_bar = self.MainWindow.frameandscroll['SBC']['File']['scrollArea'].verticalScrollBar()
        offset = int(horizontal_bar.value()/ConHeight)
        shownums = int(ScrollFrameHeight/ConHeight)+1
        # print(offset,shownums)
        CurShowFiles = FilesKeys[offset:shownums+offset]
        FileCon = []
        for i in CurShowFiles:
            # print(Files[i]['fename'])
            # print(Files[i])
            if Files[i]['fetype'] == 'img' and 'LoadImg' not in Files[i]:
                # print(Files[i]['fename'])
                FileCon.append(Files[i])
                self.MainWindow.SBCFilesDict[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['File'][i]['LoadImg'] = 1
        temp = self.func(FileCon, 2)
        for i in temp:
            SendList = [{'fepath': j['fepath']} for j in i]
            # print('send',SendList)
            ConList = self.SBCRe.GetFileCon(SendList)
            try:
                for num in range(len(ConList['src'])):
                    coninfo = ConList['src'][num]
                    ConBase64 = coninfo.split(',')[-1]
                    img_b64decode = base64.b64decode(ConBase64)  # [21:]
                    # print(ConBase64)
                    # print(img_b64decode)
                    self.ShowCon(i[num]['con'], img_b64decode)
            except:
                # print('threderror')
                break

    def runthread1(self):
        t = threading.Thread(target=self.run1)
        t.setDaemon(True)
        t.start()

    def run(self):

        FileCon = self.MainWindow.FileCons[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]
        temp = self.func(FileCon, 2)
        for i in temp:
            SendList = [{'fepath': j['fepath']} for j in i]
            # print('send',SendList)
            ConList = self.SBCRe.GetFileCon(SendList)
            try:
                for num in range(len(ConList['src'])):
                    coninfo = ConList['src'][num]
                    ConBase64 = coninfo.split(',')[-1]
                    img_b64decode = base64.b64decode(ConBase64)  # [21:]
                    # print(ConBase64)
                    # print(img_b64decode)
                    self.ShowCon(i[num]['con'], img_b64decode)
            except:
                # print('threderror')
                break
class FileUpdate(QThread):
    signal = pyqtSignal()
    def __init__(self,ui):
        super().__init__()
        self.MainWindow = ui
        self.signal.connect(self.ScrollContentUpdate)
        self.path = '/home/'
        self.CurFileList = []
        self.Thread_LoadImgs = Thread_LoadImg(self.MainWindow)

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

    def FileClickDeal(self,FileInfo,e):
        if e.buttons() == QtCore.Qt.LeftButton:
            self.FileLeftDeal(FileInfo)
        elif e.buttons() == QtCore.Qt.RightButton:
            self.create_Filerightmenu(FileInfo)
            # self.FileRightDeal(FileInfo)
    def FileLeftDeal(self,FileInfo):
        print('FileLeft',FileInfo)
        # ImgPreviews = ImgPreview.ImageViewer()
        # self.FileShow1(FileInfo['fepath'])
        if FileInfo['fetype'] == 'img':
            imfdata = self.SBCRe.getImgdata(FileInfo['fepath'])
            # self.ImgPreviews = ImgPreview.ImageViewer()
            self.ImgPreviews.Previewact(base64.b64decode(imfdata))
            return
        if FileInfo['fetype'] == 'folder':
            self.FileShow1(FileInfo['fepath'])
            return

    def Refresh(self,e):
        if e.buttons() == QtCore.Qt.LeftButton:
            nav = self.MainWindow.nav[self.MainWindow.CurNetChosed]
            # print(nav[-1]['path'])
            self.FileShow1(nav[-1]['path'])

    def navBackClick(self,e):
        if e.buttons() == QtCore.Qt.LeftButton:
            nav = self.MainWindow.nav[self.MainWindow.CurNetChosed]
            idx = len(nav) - 2
            if idx <0:
                return
            self.FileShow1(nav[idx]['path'])
    def FileShow1(self,path):
        self.path = path
        if self.isRunning():
            self.wait()
        CurNavChosed = self.MainWindow.CurNavChosed
        CurNetChosed = self.MainWindow.CurNetChosed
        self.MainWindow.CurFileListOld[CurNetChosed][CurNavChosed] = []
        self.start()


    def navClick(self,FilePath,e):
        if e.buttons() == QtCore.Qt.LeftButton:
            self.FileShow1(FilePath)
    def NavUpdate(self):
        if self.MainWindow.CurNavChosed == 'File':
            frame_9_ = self.MainWindow.frameandscroll[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed][
                'frame_nav'].deleteLater()
            self.MainWindow.frameandscroll[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['frame_nav'] = QtWidgets.QFrame(self.MainWindow.frameandscroll[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['frame_navF'])
            frame_9_ = self.MainWindow.frameandscroll[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed][
                'frame_nav']
            horizontalLayout_1 = self.MainWindow.frameandscroll[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['horizontalLayout_nav']
            horizontalLayout_1.addWidget(frame_9_)
            horizontalLayout_ = QtWidgets.QHBoxLayout(frame_9_)
            horizontalLayout_.setContentsMargins(0, 0, 0, 0)
            horizontalLayout_.setObjectName("horizontalLayout_3")

            nav = self.MainWindow.nav[self.MainWindow.CurNetChosed]
            # print(nav)
            for i in range(len(nav)):
                # print(self.nav[i])
                label_11 = QtWidgets.QLabel(frame_9_)

                label_11.setObjectName("label_11")
                label_11.setText(nav[i]['navname'])
                horizontalLayout_.addWidget(label_11)

                if i == len(nav)-1:
                    label_11.setStyleSheet("color:#A6ACAF")
                if i < len(nav)-1:
                    label_11.mousePressEvent = partial(self.navClick, nav[i]['path'])
                    label_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    label_11 = QtWidgets.QLabel(frame_9_)
                    # label_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    label_11.setObjectName("label_11")
                    label_11.setText(">")
                    horizontalLayout_.addWidget(label_11)



            # frame = {'frame': frame_12, 'scrollArea': self.scrollArea, 'frame_nav': frame_9_,
            #          'horizontalLayout_nav': horizontalLayout_1}
    def creat_ChoseNetmenu(self):
        groupBox_menu = QMenu()
        actionSBC = QAction('小黑云', self)
        actionBDC = QAction('百度云', self)
        actionALC = QAction('阿里云', self)
        groupBox_menu.addAction(actionSBC)
        groupBox_menu.addAction(actionBDC)
        groupBox_menu.addAction(actionALC)
        groupBox_menu.popup(QCursor.pos())
    def create_Filerightmenu(self,FileInfo):
        print(FileInfo)
        # 菜单对象
        self.groupBox_menu = QMenu()
        # self.actionA = QAction(QIcon('image/保存.png'), u'保存数据', self)  # 创建菜单选项对象
        self.actionDown = QAction('下载', self)
        # self.actionA.setShortcut('Ctrl+S')  # 设置动作A的快捷键
        self.groupBox_menu.addAction(self.actionDown)  # 把动作A选项对象添加到菜单self.groupBox_menu上
        self.actionShare = QAction(u'分享', self)
        self.groupBox_menu.addAction(self.actionShare)
        self.actionProper = QAction(u'属性', self)
        self.groupBox_menu.addAction(self.actionProper)
        self.actionCopy = QAction(u'复制', self)
        self.groupBox_menu.addAction(self.actionCopy)
        self.actionMove = QAction(u'移动', self)
        self.groupBox_menu.addAction(self.actionMove)
        self.actionDel = QAction(u'删除', self)
        self.groupBox_menu.addAction(self.actionDel)
        self.actionNewname = QAction(u'重命名', self)
        self.groupBox_menu.addAction(self.actionNewname)
        # self.actionA.triggered.connect(self.button)  # 将动作A触发时连接到槽函数 button
        self.groupBox_menu.popup(QCursor.pos())  # 声明当鼠标在groupBox控件上右击时，在鼠标位置显示右键菜单   ,exec_,popup两个都可以，
        self.groupBox_menu.setStyleSheet("QMenu{\n"
                                        "    margin:0px 10px 10px 0px;\n"
                                        "    color:blue;\n"
                                        "    font-size:16px;\n"
                                        "}\n")

    def ScrollContentUpdate(self):
        self.NavUpdate()
        print('CurNavChosed',self.MainWindow.CurNavChosed)
        if self.MainWindow.CurNavChosed in self.MainWindow.SBCFilesDict[self.MainWindow.CurNetChosed]:
            # print('pr',self.MainWindow.SBCFilesDict)
            # print(self.MainWindow.SBCFilesDict)
            # print(self.MainWindow.SBCFilesDict[self.MainWindow.CurNavChosed]['scrollAreaWidgetContents'])
            self.MainWindow.SBCFilesDict[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['scrollAreaWidgetContents'].deleteLater()
        self.MainWindow.SBCFilesDict[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed] = {}
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 806, 565))
        self.scrollAreaWidgetContents.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        formLayout.setContentsMargins(0, 0, 0, 0)
        formLayout.setVerticalSpacing(0)
        formLayout.setObjectName("formLayout")

        # print(self.MainWindow.FileCons)
        self.MainWindow.FileCons[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed] = {}
        Filecon = []
        self.CurSBCFilesDict = {}
        SBCFile = {}
        self.CurSBCFilesDict['scrollAreaWidgetContents'] = self.scrollAreaWidgetContents

        # self.scrollAreaWidgetContents.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.scrollAreaWidgetContents.customContextMenuRequested.connect(self.create_rightmenu)

        self.FilescheckBox = []
        for i in range(len(self.CurFileList)):

            CurSBCFiles = {}
            FileInfo = self.CurFileList[i]
            CurSBCFiles['frame'] = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            CurSBCFiles['frame'].setMinimumSize(QtCore.QSize(0, 36))
            CurSBCFiles['frame'].setMaximumSize(QtCore.QSize(16777215, 36))
            CurSBCFiles['frame'].setFrameShape(QtWidgets.QFrame.StyledPanel)
            CurSBCFiles['frame'].setFrameShadow(QtWidgets.QFrame.Raised)
            CurSBCFiles['frame'].setObjectName("frame_13")

            # CurSBCFiles['frame'].setContextMenuPolicy(Qt.CustomContextMenu)
            # CurSBCFiles['frame'].customContextMenuRequested.connect(self.create_rightmenu)

            horizontalLayout_14 = QtWidgets.QHBoxLayout(CurSBCFiles['frame'])
            horizontalLayout_14.setContentsMargins(3, 0, 9, 0)
            horizontalLayout_14.setSpacing(0)
            horizontalLayout_14.setObjectName("horizontalLayout_14")
            horizontalLayout_13 = QtWidgets.QHBoxLayout()
            horizontalLayout_13.setContentsMargins(0, 0, 0, -1)
            horizontalLayout_13.setSpacing(6)
            horizontalLayout_13.setObjectName("horizontalLayout_13")
            checkBox_2 = QtWidgets.QCheckBox(CurSBCFiles['frame'])
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(checkBox_2.sizePolicy().hasHeightForWidth())
            checkBox_2.setSizePolicy(sizePolicy)
            checkBox_2.setText("")
            checkBox_2.setObjectName("checkBox_2")
            horizontalLayout_13.addWidget(checkBox_2)
            self.FilescheckBox.append(checkBox_2)
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
            label_29 = QtWidgets.QLabel(CurSBCFiles['frame'])
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(3)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(label_29.sizePolicy().hasHeightForWidth())
            label_29.setSizePolicy(sizePolicy)
            label_29.setAlignment(QtCore.Qt.AlignCenter)
            label_29.setObjectName("label_29")
            horizontalLayout_14.addWidget(label_29)
            label_30 = QtWidgets.QLabel(CurSBCFiles['frame'])
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(3)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(label_30.sizePolicy().hasHeightForWidth())
            label_30.setSizePolicy(sizePolicy)
            label_30.setAlignment(QtCore.Qt.AlignCenter)
            label_30.setObjectName("label_30")
            horizontalLayout_14.addWidget(label_30)
            horizontalLayout_14.setStretch(0, 7)
            horizontalLayout_14.setStretch(1, 2)
            horizontalLayout_14.setStretch(2, 2)
            formLayout.setWidget(i, QtWidgets.QFormLayout.SpanningRole, CurSBCFiles['frame'])
            metrics = QFontMetrics(CurSBCFiles['FileNameLabel'].font())
            new_file_name = metrics.elidedText(FileInfo['filename'], Qt.ElideRight, 260)

            CurSBCFiles['FileNameLabel'].setText(new_file_name)
            filepath = base64.decodebytes(FileInfo['filelj'].encode('utf8')).decode()
            CurSBCFiles['fepath'] = filepath
            CurSBCFiles['fename'] = FileInfo['filename']
            CurSBCFiles['fepath_base64'] = FileInfo['filelj']
            CurSBCFiles['fetype'] = FileInfo['fetype']
            CurSBCFiles['imgLoad'] = 0
            if FileInfo['fetype'] == 'img':
                Filecon.append(CurSBCFiles)
            CurSBCFiles['con'].setText("")
            CurSBCFiles['con'].setPixmap(QtGui.QPixmap(self.FileConChose(FileInfo['fetype'])))
            CurSBCFiles['con'].setScaledContents(True)

            label_29.setText(FileInfo['date'])
            label_30.setText(FileInfo['big'])
            # CurSBCFiles['FileNameLabel'].mousePressEvent = partial(self.ClickEventDeals.FileClickDeal, CurSBCFiles)
            CurSBCFiles['FileNameLabel'].mousePressEvent = partial(self.FileClickDeal, CurSBCFiles)
            # print(6)
            # self.CurSBCFilesDict['File'] = {FileInfo['filelj']:CurSBCFiles}
            # self.CurSBCFilesDict[FileInfo['filelj']] = CurSBCFiles
            SBCFile[FileInfo['filelj']] = CurSBCFiles


        self.MainWindow.FileCons[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed] = Filecon
        self.MainWindow.frameandscroll[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['scrollArea'].setWidget(self.scrollAreaWidgetContents)
        # self.scrollAreaPhotoShow.setWidget(self.scrollAreaWidgetContents)
        # self.verticalLayout_2.addWidget(self.scrollAreaPhotoShow)
        # self.MainWindow.verticalLayout_6.addWidget(self.frame_PhotoShow)
        # self.MainWindow.SBCFilesDict[self.MainWindow.CurNavChosed] = self.CurSBCFilesDict
        self.MainWindow.SBCFilesDict[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['scrollAreaWidgetContents'] = self.scrollAreaWidgetContents
        self.MainWindow.SBCFilesDict[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['File'] = SBCFile
        # print(self.MainWindow.SBCFilesDict[self.MainWindow.CurNavChosed]['scrollAreaWidgetContents'])

        #
        # if self.Thread_LoadImgs.isRunning():
        #     self.Thread_LoadImgs.wait()
        self.Thread_LoadImgs.runthread1()


    def run(self):
        self.SBCRe = self.MainWindow.SBCRe
        # if self.isRunning():
        #     return
        CurNavChosed = self.MainWindow.CurNavChosed
        CurNetChosed = self.MainWindow.CurNetChosed
        if CurNavChosed == 'File':
            if CurNetChosed == 'SBC':
                self.SBCRe.GetFileList(self.path)
                if self.MainWindow.CurFileListOld[CurNetChosed][CurNavChosed] != self.SBCRe.CurFileList:
                    self.CurFileList = self.SBCRe.CurFileList
                    self.MainWindow.nav[CurNetChosed] = self.SBCRe.Nav
                    # self.signal.emit()
                    self.MainWindow.CurFileListOld[CurNetChosed][
                        CurNavChosed] = self.SBCRe.CurFileList
                    self.signal.emit()

            # self.CurFileListOld = self.SBCRe.CurFileList
            # self.CurFileList = self.SBCRe.CurFileList
            # print(self.CurFileList)
            # self.signal.emit()
        if CurNavChosed == 'Photo':
            if CurNetChosed == 'SBC':
                # print(self.MainWindow.CurFileListOld[self.MainWindow.CurNetChosed][
                #     self.MainWindow.CurNavChosed])
                # print(self.CurFileList)
                if self.MainWindow.CurFileListOld[CurNetChosed][
                    CurNavChosed] == []:
                    # print('PhotoTe')
                    # print(6)
                    # self.SBCRe.GetFileList(self.path)
                    self.SBCRe.SearchFile('','image')
                    # self.CurFileListOld = self.SBCRe.CurFileList
                    self.CurFileList = self.SBCRe.CurFileList
                    # print(self.CurFileList)
                    self.MainWindow.CurFileListOld[CurNetChosed][
                        CurNavChosed] = self.SBCRe.CurFileList
                    self.signal.emit()
        if CurNavChosed == 'Video':
            if CurNetChosed == 'SBC':
                if self.MainWindow.CurFileListOld[CurNetChosed][
                    CurNavChosed] == []:
                    # self.SBCRe.GetFileList('/home/BaiduNet/')
                    self.SBCRe.SearchFile('', 'video')
                    # self.CurFileListOld = self.SBCRe.CurFileList
                    self.CurFileList = self.SBCRe.CurFileList
                    self.MainWindow.CurFileListOld[CurNetChosed][
                        CurNavChosed] = self.SBCRe.CurFileList
                    self.signal.emit()

    def UpdateShow(self,Show):
        # self.CurShow = Show
        self.start()


    def FileShow(self):
        # self.MainWindow.frame_PhotoShow.hide()
        # self.MainWindow.frame_12.show()
        self.MainWindow.frameandscroll[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['frame'].show()
        self.UpdateShow('File')

    def PhotoShow(self):
        # self.label_11.setText("图片")
        self.MainWindow.frameandscroll[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['label'].setText("图片")
        # self.MainWindow.frame_12.hide()
        self.MainWindow.frameandscroll[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['frame'].show()
        # self.MainWindow.frameandscroll['frame'].show()
        # self.MainWindow.frame_PhotoShow.show()
        # self.MainWindow.frame_PhotoShow.resizeEvent = self.MainWindowSizeChange1
        self.UpdateShow('Photo')

    def VideoShow(self):
        # self.label_11.setText("视频")
        self.MainWindow.frameandscroll[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['label'].setText("视频")
        # self.MainWindow.frame_12.hide()
        self.MainWindow.frameandscroll[self.MainWindow.CurNetChosed][self.MainWindow.CurNavChosed]['frame'].show()
        # self.MainWindow.frame_PhotoShow.show()
        self.UpdateShow('Video')

class Trans():
    def __init__(self,MainWindow):
        self.MainWindow = MainWindow