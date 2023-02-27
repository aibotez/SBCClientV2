import time

from SubUi import PerVideoui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2,requests,json


def TimeFormat(t0):
    hour = int(t0/60/60)
    if hour < 0:
        hourstr = '00'
    else:
        if hour <10:
            hourstr = '0'+str(int(hour))
        else:
            hourstr = str(int(hour))
    tm0 = t0 - int(hour)*60*60
    tm = tm0/60
    if tm < 0:
        minstr = '00'
    else:
        if tm <10:
            minstr = '0'+str(int(tm))
        else:
            minstr = str(int(tm))
    ts = tm0 - int(tm) * 60
    if ts < 10:
        Secstr = '0'+str(int(ts))
    else:
        Secstr = str(int(ts))

    return hourstr+':'+minstr+':'+Secstr
class MySlider(QSlider):  # 继承QSlider
    customSliderClicked = pyqtSignal(str)  # 创建信号

    def __init__(self, parent=None):
        super(QSlider, self).__init__(parent)
        self.fps = None
        self.isPlay = 1

    def mousePressEvent(self, QMouseEvent):  # 重写的鼠标点击事件
        super().mousePressEvent(QMouseEvent)
        pos = QMouseEvent.pos().x() / self.width()
        self.setValue(round(pos * (self.maximum() - self.minimum()) + self.minimum()))  # 设定滑动条滑块位置为鼠标点击处
        self.customSliderClicked.emit("mouse Press")  # 发送信号

class PerViewVideo(PerVideoui.Ui_MainWindowPerVideo):
    def __init__(self,ui,info):
        super(PerViewVideo, self).__init__()
        self.path = info['fepath']
        self.FileName = info['fename']
        self.ui = ui
        self.ui.Main = QMainWindow()
        self.s = requests.Session()
        self.setupUi(self.ui.Main)
        self.ui.Main.show()
        self.init()
        self.CurVIdeotime = 0

    def init(self):
        self.horizontalLayout_2.itemAt(0).widget().deleteLater()
        # self.horizontalLayout_2.removeWidget(self.horizontalSlider)
        self.horizontalSlider = MySlider(self.frame_3)
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_2.addWidget(self.horizontalSlider)
        self.label_4.setText(self.FileName)
        self.label_2.setText('00:00:00')
        self.label.setText('00:00:00')
        self.label_3.setText('')
        # self.player.positionChanged.connect(self.setCurrent)
        # self.horizontalSlider.sliderMoved.connect(self.change_time)
        self.horizontalSlider.customSliderClicked.connect(self.change_time)
        print('PreviewVideo',self.path)
        self.GetVideoInfo()

    def change_time(self):
        pass

    def LoadVideo(self,StartTime):
        timespan = 10
        StartAudioFram = None
        EndAudioFram = None
        StartVideoFram = StartTime*self.VideoInfo['VideoFramRate']
        EndVideoFram = (StartTime+timespan) * self.VideoInfo['VideoFramRate']
        if self.VideoInfo['AudioFramRate']:
            StartAudioFram = StartTime * self.VideoInfo['AudioFramRate']
            EndAudioFram = (StartTime+timespan) * self.VideoInfo['AudioFramRate']
        url = 'http://'+self.ui.host+'/preview/'
        data = {
            'client': 'windows',
            'VideoFram':[int(StartVideoFram),int(EndVideoFram)],
            'AudioFram':[int(StartAudioFram),int(EndAudioFram)],
            'filepath': self.path
        }
        print(int(StartVideoFram),int(EndVideoFram))
        r = self.s.post(url, data=json.dumps(data), headers=self.ui.SBCRe.headers)
        data = json.loads(r.text)
        print(data['VideoFrams'])

    def GetVideoInfo(self):
        url = 'http://'+self.ui.host+'/preview/'
        data = {
            'client': 'windows',
            'filepath': self.path
        }
        res = self.s.post(url, data=json.dumps(data), headers=self.ui.SBCRe.headers)
        redata = json.loads(res.text)
        self.VideoInfo = redata['VideoFile']
        print(redata)
        TotalTime = self.VideoInfo['VideoFramsTotal']/self.VideoInfo['VideoFramRate']
        self.label_2.setText(TimeFormat(TotalTime))

        self.LoadVideo(1)

    # def playvideo(self,frams):
    #     for frame in frams:
    #         if not self.isPlay:
    #             break
    #         self.img = frame
    #         show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #         showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
    #         # showImage=showImage.copy(self.x1, self.y1,self.x2, self.y2)
    #         pix = QPixmap.fromImage(showImage)
    #         pix = pix.scaled(self.label.width(), self.label.height(), Qt.IgnoreAspectRatio)
    #         # # --------------------------------------
    #         # # 局部放大
    #         # pix = pix.copy(self.x1, self.y1, self.x2, self.y2)
    #         self.label.setPixmap(pix)
    #         # 进度条
    #         # self.jdt()
    #         cv2.waitKey(int(1000 / self.fps))
