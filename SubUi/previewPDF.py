from SubUi import previewPDFui
from PyQt5 import QtCore, QtGui, QtWidgets
import base64,json,sys,time

class previewpdf(previewPDFui.Ui_Dialog):
    def __init__(self,ui,Dialog):
        self.ui = ui
        self.Dialog = Dialog
        self.pixSize = None
        self.init()


    def init(self):
        self.setupUi(self.Dialog)
        self.label.setText('')
        self.scrollBar = self.scrollArea.verticalScrollBar()
        self.scrollBar.valueChanged.connect(lambda :self.valueChanged())
        self.PageLabels = []

    def previewnopdf(self):
        pass

    def ShowCon(self, px, base64data):
        ba = base64data
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(ba)
        px.setPixmap(pixmap)
        px.resize(pixmap.size())
        self.pixSize = pixmap.size()
    def valueChanged(self):
        Maxmun = self.scrollBar.maximum()
        if self.scrollBar.value() >= Maxmun-200:
            self.page += 1

            label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            label.setObjectName("label")
            self.verticalLayout_2.addWidget(label)
            img_b64decode = self.GetpdfImg(self.info)
            self.ShowCon(label, img_b64decode)


    def GetpdfImg(self,info):
        data = {
            'page':self.page,
            'client':'windows',
            'filepath':info['fepath']
        }
        redata = self.ui.SBCRe.GetPdfImg(data)
        data = redata['data']
        MaxPage = data['pages']
        base64data = data['data']
        img_b64decode = base64.b64decode(base64data, altchars=None, validate=False)
        self.PdfMaxpage = MaxPage
        return img_b64decode
    def previewpdf(self,info):
        self.info =info
        print(info)
        self.page = 0
        self.label_2.setText(info['fename'])
        img_b64decode = self.GetpdfImg(info)
        self.ShowCon(self.label, img_b64decode)
        self.PageLabels.append(self.label)
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
