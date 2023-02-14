import os
import time

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtCore import QBuffer, QIODevice
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.Qt import QByteArray


from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtMultimedia, QtMultimediaWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.player = QtMultimedia.QMediaPlayer(self)
        self.viewer = QtMultimediaWidgets.QVideoWidget(self)
        self.player.setVideoOutput(self.viewer)
        # self.player.stateChanged.connect(self.handleStateChanged)
        self.player.positionChanged.connect(self.setCurrent_)
        self.button1 = QtWidgets.QPushButton('Play', self)
        self.button2 = QtWidgets.QPushButton('Stop', self)
        self.button1.clicked.connect(self.handleButton)
        self.button2.clicked.connect(self.handleStateChanged1)
        # self.player.durationChanged.connect(self.showDuration)

        self.button2.setEnabled(False)
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.viewer, 0, 0, 1, 2)
        layout.addWidget(self.button1, 1, 0)
        layout.addWidget(self.button2, 1, 1)
        self._buffer = QtCore.QBuffer(self)
        self._data = None

    # 获取当前播放进度包括时间和进度条显示
    def setCurrent_(self):
        # return
        try:
            print(self.player.position())

            # self.current_num = self.player.position()
            # print(self.current_num)
            print()
        except Exception as e:
            print(e)

        # self.label_start.setText(self.int2time(self.current_num))
        # self.s1.setValue(self.current_num)  # 设置当前值

    # 读取当前播放视频的总时长
    def showDuration(self):
        self.maxvalue = self.player.duration()
        print(self.maxvalue)
        # self.s1.setMaximum(self.maxvalue)
        # self.label_end.setText(self.int2time(self.maxvalue))


    def redvid(self):
        path = './2023-01-1616_59_13.mp4'
        with open(path, 'rb') as stream:
            # stream.seek(0)
            fe = stream.read()
        return fe
    def handleButton(self):
        path = '2023-01-1616_59_13.mp4'
        if path:
            self.button1.setEnabled(False)
            self.button2.setEnabled(True)
            print(self._buffer.data())
            with open(path, 'rb') as stream:
                stream.seek(0,os.SEEK_SET)
                self._data = stream.read()
                self._buffer.setData(self._data)
                self._buffer.open(QtCore.QIODevice.ReadOnly)
                self.player.setMedia(
                    QtMultimedia.QMediaContent(), self._buffer)
                # time.sleep(0.2)
                self.player.setPosition(0)
                print(self._buffer.data())
                self.player.play()

    def handleStateChanged1(self):
        self.maxvalue = self.player.duration()
        print(self.maxvalue)
        self.current_num = self.player.position()
        print(self.current_num)
        self.player.setPosition(1000*20)
        # if state == QtMultimedia.QMediaPlayer.StoppedState:
        #     self._buffer.close()
        #     self._data = None
        #     self.button1.setEnabled(True)
        #     self.button2.setEnabled(False)

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(500, 50, 640, 480)
    window.show()
    sys.exit(app.exec_())

