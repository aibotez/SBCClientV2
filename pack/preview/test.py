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
        px.resize(pixmap.size())
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
