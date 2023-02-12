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
        self.label.setText('')

    def previewnopdf(self):
        pass

    def ShowCon(self, px, base64data):
        ba = base64data
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(ba)
        px.setPixmap(pixmap)
        px.resize(pixmap.size())
        self.pixSize = pixmap.size()
    def previewpdf(self,info):
        print(info)
        self.page = 0
        data = {
            'page':self.page,
            'client':'windows',
            'filepath':info['filepath']
        }
        redata = self.ui.SBCRe.GetPdfImg(data)
        data = redata['data']
        MaxPage = data['pages']
        base64data = data['data']
        print(MaxPage)
        img_b64decode = base64.b64decode(base64data.decode("utf-8"), altchars=None, validate=False)
        self.ShowCon(self.label, img_b64decode)
        for i in range(MaxPage-1):
            label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            label.setObjectName("label")
            self.verticalLayout_2.addWidget(self.label)
            self.ShowCon(label,b'123')
