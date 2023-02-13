from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtCore import QBuffer, QIODevice
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.Qt import QByteArray



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QVideoWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 500, 500))
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.mediaPlayer = QtMultimedia.QMediaPlayer(self)
        # QMediaPlayer(None, QtMultimedia.QMediaPlayer.VideoSurface)

        self.mediaPlayer.setVideoOutput(self.widget)
        # # fileName = "/path/of/your/local_file"
        # url = QtCore.QUrl.fromLocalFile("./2023-01-1616_59_13.mp4")
        #
        # with open('./2023-01-1616_59_13.mp4' ,'rb') as f:
        #     b = f.read()
        # outByteArray = QByteArray(b)
        # mediaStream = QBuffer()
        # mediaStream.setBuffer(outByteArray)
        # mediaStream.open(QIODevice.ReadWrite)
        #
        # self.mediaPlayer.setMedia(QtMultimedia.QMediaContent(), mediaStream)
        # self.mediaPlayer.play()

        # self.mediaPlayer.setMedia(QtMultimedia.QMediaContent(url))
        # self.mediaPlayer.play()
        self._buffer = QtCore.QBuffer(self)
        with open('./2023-01-1616_59_13.mp4', 'rb') as stream:
            self._data = stream.read()
            self._buffer.setData(self._data)
            self._buffer.open(QtCore.QIODevice.ReadOnly)
            self.mediaPlayer.setMedia(
                QtMultimedia.QMediaContent(), self._buffer)
            self.mediaPlayer.play()

from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtMultimedia, QtMultimediaWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.player = QtMultimedia.QMediaPlayer(self)
        self.viewer = QtMultimediaWidgets.QVideoWidget(self)
        self.player.setVideoOutput(self.viewer)
        self.player.stateChanged.connect(self.handleStateChanged)
        self.button1 = QtWidgets.QPushButton('Play', self)
        self.button2 = QtWidgets.QPushButton('Stop', self)
        self.button1.clicked.connect(self.handleButton)
        self.button2.clicked.connect(self.player.stop)
        self.button2.setEnabled(False)
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.viewer, 0, 0, 1, 2)
        layout.addWidget(self.button1, 1, 0)
        layout.addWidget(self.button2, 1, 1)
        self._buffer = QtCore.QBuffer(self)
        self._data = None

    def handleButton(self):
        path = './2023-01-1616_59_13.mp4'
        if path:
            self.button1.setEnabled(False)
            self.button2.setEnabled(True)

            with open(path, 'rb') as stream:
                self._data = stream.read()
                self._buffer.setData(self._data)
                self._buffer.open(QtCore.QIODevice.ReadOnly)
                self.player.setMedia(
                    QtMultimedia.QMediaContent(), self._buffer)
                self.player.play()

    def handleStateChanged(self, state):
        if state == QtMultimedia.QMediaPlayer.StoppedState:
            self._buffer.close()
            self._data = None
            self.button1.setEnabled(True)
            self.button2.setEnabled(False)

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(500, 50, 640, 480)
    window.show()
    sys.exit(app.exec_())

