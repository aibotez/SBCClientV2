import json
import time

from PyQt5 import QtCore, QtGui, QtWidgets

import sys,requests
class Ui_SBCclient(object):

    def ShowCon(self, px, base64data):
        ba = base64data
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(ba)
        px.setPixmap(pixmap)

        # pixmap = QPixmap()
        # pixmap.convertFromImage(ba)
        # px.setPixmap(QPixmap(pixmap))
        # px.resize(pixmap.size())

        print(66)
    def generatePDFView(self):
        # self.doc = fitz.open(self.file_path)
        # trans_a = 200
        # trans_b = 200
        # trans = fitz.Matrix(trans_a / 100, trans_b / 100).prerotate(0)
        # pix = self.doc[self.page_num].get_pixmap(matrix=trans)
        # fmt = QImage.Format_RGBA8888 if pix.alpha else QImage.Format_RGB888
        # pageImage = QImage(pix.samples, pix.width, pix.height, pix.stride, fmt)
        pixmap = QPixmap()
        pixmap.convertFromImage(pageImage)
        self.label.setPixmap(QPixmap(pixmap))
        self.label.resize(pixmap.size())
    def requ(self,label):
        url = 'http://202.127.205.153:91/previewpdftest/'
        data = {
            'page':2
        }
        r = requests.post(url,data= json.dumps(data))
        r = r.content
        img_b64decode = base64.b64decode(r.decode("utf-8"), altchars=None, validate=False)
        print(type(r))
        self.ShowCon(label, img_b64decode)

        # ConBase64 = r.split(',')[-1]
        # for chunk in r.iter_content(chunk_size=1024*1024*100):
        #     if chunk:
        #         img_b64decode = base64.b64decode(chunk.decode("utf-8"), altchars=None, validate=False)
        #         # chunk = str(chunk)
        #         # ConBase64 = chunk.split(',')[-1]
        #         # print(chunk.decode("utf-8"))
        #         # break
        #         # img_b64decode = base64.b64decode(chunk.decode("utf-8"),altchars=None, validate=False)
        #         # print(img_b64decode)
        #         # # print(66,img_b64decode)
        #         self.ShowCon(label, img_b64decode)
        #         break
        #         # time.sleep(10)
        # # ConBase64 = coninfo.split(',')[-1]
        # # img_b64decode = base64.b64decode(ConBase64)  # [21:]
        # # # print(ConBase64)
        # # # print(img_b64decode)
        # # self.ShowCon(label, img_b64decode)

    def setupUi(self, SBCclient):
        SBCclient.setObjectName("SBCclient")
        SBCclient.resize(600, 600)
        SBCclient.setMinimumSize(QtCore.QSize(800, 700))


        self.label_10 = QtWidgets.QLabel(SBCclient)
        self.label_10.setMaximumSize(QtCore.QSize(500, 500))
        self.label_10.setMinimumSize(QtCore.QSize(500, 500))
        self.label_10.setText("254")
        self.label_10.setPixmap(QtGui.QPixmap("login.jpg"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_10.mousePressEvent = lambda e:self.requ(self.label_10)





import sys,base64,threading
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    Main = QMainWindow()

    SBCMain = Ui_SBCclient().setupUi(Main)
    # SBCMain = SBCMain.initFrame()
    Main.show()
    # SBCMain.SBCMain.show()
    # sys.exit()
    sys.exit(app.exec_())
