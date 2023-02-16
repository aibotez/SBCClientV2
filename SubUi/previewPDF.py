import threading

import requests

from SubUi import previewPDFui
from PyQt5 import QtCore, QtGui, QtWidgets
import base64,json,sys,time
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject, pyqtSignal

class previewpdf(QObject,previewPDFui.Ui_Dialog):
    signalUpdatepdf = pyqtSignal(list,list)
    signalUpdatePage = pyqtSignal(str)
    signalAddpdfpage = pyqtSignal()
    signalWaitpdf = pyqtSignal()
    signalConvertResult = pyqtSignal(str)
    def __init__(self,ui,Dialog):
        super().__init__()
        self.ui = ui
        self.Dialog = Dialog
        self.pixSize = None
        self.init()
        self.resize0 = 0
        self.s = requests.Session()
        self.signalUpdatepdf.connect(self.ShowCon)
        self.signalAddpdfpage.connect(self.Addpdfpage)
        self.signalConvertResult.connect(self.ShowConvertResult)
        self.signalUpdatePage.connect(self.UpdatePage)


    def init(self):
        self.setupUi(self.Dialog)
        self.label.setText('')
        self.scrollBar = self.scrollArea.verticalScrollBar()
        self.scrollBar.valueChanged.connect(lambda :self.valueChanged())
        self.PageLabels = []
        self.Dialog.setWindowTitle('小黑云文件预览')
    def previewnopdf(self,info):
        t = threading.Thread(target=self.previewnopdf1,args=(info,))
        t.setDaemon(True)
        t.start()
    def ShowConvertResult(self,res):
        self.label.setText(res)
    def previewnopdf1(self,info):
        Waitstate = 1
        ConvertResult = 0
        def RequestConvert():
            nonlocal Waitstate,ConvertResult
            s = requests.session()
            url = 'http://' + self.ui.host + '/Convert2PDF/'
            r = s.post(url, data=json.dumps(data), headers=self.ui.SBCRe.headers)
            if r.text == '1':
                Waitstate = 0
                ConvertResult = 1
            else:
                Waitstate = 0

        data = {
            'client':'windows',
            'path':info['fepath']
        }
        self.signalConvertResult.emit('转换文件中...稍等片刻！')
        Convertthread = threading.Thread(target=RequestConvert)
        Convertthread.setDaemon(True)
        Convertthread.start()
        t0 = time.time()
        while Waitstate:
            self.signalConvertResult.emit('转换文件中...已用时：{}s'.format(int(time.time() - t0)))
            time.sleep(0.5)
        if not ConvertResult:
            self.signalConvertResult.emit('转换失败！（文件名不能有空格）')
        else:
            self.previewpdf1(info)

    def ShowCon(self,pxs,base64datas):
        px = pxs[0]
        base64data = base64datas[0]
        ba = base64data
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(ba)
        px.setPixmap(pixmap)
        # px.resize(pixmap.size())
        self.pixSize = pixmap.size()
        scal = self.pixSize.height()/self.pixSize.width()
        # if not self.resize0:
        #     self.Dialog.resize(800, 800 * scal)
        #     self.resize0 = 1
        px.setMaximumSize(QtCore.QSize(760, 760 * scal))
        # print(self.pixSize)
        px.setScaledContents(True)
    def Addpdfpage(self):
        label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setObjectName("label")
        # scal = self.pixSize[1]/self.pixSize[1]
        self.verticalLayout_2.addWidget(label)
        img_b64decode = self.GetpdfImg(self.info)
        self.ShowCon([label], [img_b64decode])
    def valueChanged(self):
        Maxmun = self.scrollBar.maximum()
        if self.scrollBar.value() >= Maxmun-200:
            self.page += 1
            if self.page < self.PdfMaxpage:
                self.signalAddpdfpage.emit()
                # label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                # label.setAlignment(QtCore.Qt.AlignCenter)
                # label.setObjectName("label")
                # # scal = self.pixSize[1]/self.pixSize[1]
                # self.verticalLayout_2.addWidget(label)
                # img_b64decode = self.GetpdfImg(self.info)
                # self.signalUpdatepdf.emit([label],[img_b64decode])

            else:
                self.page = self.PdfMaxpage-1
        CurPage = str(int(self.page*self.scrollBar.value()/self.scrollBar.maximum())+1)
        self.signalUpdatePage.emit('{}/{}'.format(CurPage, str(self.PdfMaxpage)))


    def UpdatePage(self,pagestr):
        self.label_3.setText(pagestr)
    def GetpdfImg(self,info):
        data = {
            'page':self.page,
            'client':'windows',
            'filepath':info['fepath']
        }
        url = 'http://' + self.ui.host + '/preview/'
        res = self.s.post(url, data=json.dumps(data),headers=self.ui.SBCRe.headers)
        redata = json.loads(res.text)
        # redata = self.ui.SBCRe.GetPdfImg(data)
        data = redata['data']
        MaxPage = data['pages']
        base64data = data['data']
        img_b64decode = base64.b64decode(base64data, altchars=None, validate=False)
        self.PdfMaxpage = MaxPage
        return img_b64decode


    def previewpdf(self,info):
        self.label_2.setText(info['fename'])
        self.label_3.setText('/')
        t = threading.Thread(target=self.previewpdf1,args=(info,))
        t.setDaemon(True)
        t.start()
    def previewpdf1(self,info):
        self.info =info
        self.page = 0
        img_b64decode = self.GetpdfImg(info)
        self.signalUpdatePage.emit('{}/{}'.format('1',str(self.PdfMaxpage)))
        self.signalUpdatepdf.emit([self.label], [img_b64decode])
        # self.ShowCon(self.label, img_b64decode)

        if self.PdfMaxpage >1:
            try:
                self.page += 1
                self.signalAddpdfpage.emit()
                # label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                # label.setAlignment(QtCore.Qt.AlignCenter)
                # label.setObjectName("label")
                # self.verticalLayout_2.addWidget(label)
                # img_b64decode = self.GetpdfImg(self.info)
                # self.signalUpdatepdf.emit([label], [img_b64decode])
            except:
                pass


        # for i in range(self.PdfMaxpage-1):
        #     label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        #     label.setObjectName("label")
        #     self.verticalLayout_2.addWidget(label)
        #     # self.ShowCon(label,b'123')
        #     self.ShowCon(label, img_b64decode)
        #     self.PageLabels.append(label)



        # self.scrollArea.verticalScrollBar().rangeChanged.connect(
        #     lambda: self.scrollArea.verticalScrollBar().setValue(
        #         self.scrollArea.verticalScrollBar().maximum()
        #     )
        # )
        # print(self.scrollArea.verticalScrollBar().maximum())
