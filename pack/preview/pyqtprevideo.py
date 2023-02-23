import time

from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
import sys,subprocess,os
from PerVideoui import Ui_MainWindowPerVideo
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal





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

    def mousePressEvent(self, QMouseEvent):  # 重写的鼠标点击事件
        super().mousePressEvent(QMouseEvent)
        pos = QMouseEvent.pos().x() / self.width()
        self.setValue(round(pos * (self.maximum() - self.minimum()) + self.minimum()))  # 设定滑动条滑块位置为鼠标点击处
        self.customSliderClicked.emit("mouse Press")  # 发送信号


class CutVideo():
    def __init__(self):
        pass
    def get_length(self,filename):
        result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                                 "format=duration", "-of",
                                 "default=noprint_wrappers=1:nokey=1", filename],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        return {'timeduring':float(result.stdout),'fename':os.path.basename(filename)}
    def cutVideo(self,path, timespan):
        videoName = 'tmp/{}_{}'.format(timespan[0], timespan[1]) + os.path.basename(path)
        # 'ffmpeg -i input.mp4 -ss 00:01:20 -t 02:00:00 -vcodec copy -acodec copy output.mp4'
        command = 'ffmpeg -i {} -ss {} -to {} -vcodec copy -acodec copy  {}'.format(path, TimeFormat(timespan[0]),
                                                                                    TimeFormat(timespan[1]), videoName)
        os.system(command)

        videocount = None
        try:
            with open(videoName,'rb') as f:
                videocount = f.read()
        except:
            pass
        return videocount
class GetReVideo():
    def __init__(self):
        self.cutVid = CutVideo()
    def GetVideoDuring(self,path):
        return self.cutVid.get_length(path)
    def GetCutVideo(self,CUtInfo):
        CutSpans = CUtInfo['cutspans']
        Serpath = CUtInfo['path']
        videocount = self.cutVid.cutVideo(Serpath,CutSpans)
        return videocount



class PreV():
    def __init__(self):
        self.playstate = 0
        self.VideoStock = {}
        self.TEMPPath = 'tmp/'
        self.timespan = 10
        self.path = 'test1.mp4'
        self.GetReVideo = GetReVideo()
        self._buffer = QtCore.QBuffer()
        self._data = None
        self.MainWindowPerVideo = Ui_MainWindowPerVideo()
        self.Main = QMainWindow()
        self.MainWindowPerVideo.setupUi(self.Main)
        self.Main.show()
        self.init()

    def get_length(self,filename):
        result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                                 "format=duration", "-of",
                                 "default=noprint_wrappers=1:nokey=1", filename],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        return float(result.stdout)
    def init(self):

        # for i in range(self.MainWindowPerVideo.horizontalLayout_2.count()):
        self.MainWindowPerVideo.horizontalLayout_2.itemAt(0).widget().deleteLater()
        # self.MainWindowPerVideo.horizontalLayout_2.removeWidget(self.MainWindowPerVideo.horizontalSlider)
        self.MainWindowPerVideo.horizontalSlider = MySlider(self.MainWindowPerVideo.frame_3)
        self.MainWindowPerVideo.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MainWindowPerVideo.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.MainWindowPerVideo.horizontalSlider.setObjectName("horizontalSlider")
        self.MainWindowPerVideo.horizontalLayout_2.addWidget(self.MainWindowPerVideo.horizontalSlider)

        self.MainWindowPerVideo.label_4.setText('')
        self.MainWindowPerVideo.label_2.setText('00:00:00')
        self.MainWindowPerVideo.label.setText('00:00:00')
        self.MainWindowPerVideo.label_3.setText('')

        self.MainWindowPerVideo.verticalLayout.removeWidget(self.MainWindowPerVideo.widget)
        self.MainWindowPerVideo.vw = QVideoWidget(self.MainWindowPerVideo.frame)  # 定义视频显示的widget
        self.MainWindowPerVideo.verticalLayout.addWidget(self.MainWindowPerVideo.vw)
        self.player = QMediaPlayer()
        self.player.positionChanged.connect(self.setCurrent)
        self.MainWindowPerVideo.horizontalSlider.sliderMoved.connect(self.change_time)
        self.MainWindowPerVideo.horizontalSlider.customSliderClicked.connect(self.change_time1)
        self.player.setVideoOutput(self.MainWindowPerVideo.vw)  # 视频播放输出的widget，就是上面定义的
        # self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))  # 选取视频文件

        feinfo = self.GetReVideo.GetVideoDuring(self.path)
        VideoDuring = feinfo['timeduring']
        self.FileName = feinfo['fename']
        self.MainWindowPerVideo.label_2.setText(TimeFormat(VideoDuring))
        self.VideoDuring = VideoDuring*1000
        self.StructData()



        self.Changeplaystate()



        # self.MainWindowPerVideo.label_3.setPixmap(QtGui.QPixmap('img/start1.png'))
        # self.MainWindowPerVideo.label_3.setPixmap(QtGui.QPixmap('img/plause1.png'))
        # self.MainWindowPerVideo.label_3.setScaledContents(True)

    def StructData(self):
        if self.VideoDuring/1000/10 - int(self.VideoDuring/1000/10) >0:
            nums = int(self.VideoDuring / 1000 / 10)+1
        else:
            nums = int(self.VideoDuring/1000/10)
        starttime = 0
        for i in range(nums):
            endtime = starttime+10
            if endtime > self.VideoDuring/1000:
                endtime = self.VideoDuring/1000
            self.VideoStock[i] = {'name':'{}_{}'.format(starttime,endtime)+self.FileName,'path':self.path}
            starttime = endtime
        for i in self.VideoStock:
            print(self.VideoStock[i])

    def change_time1(self):
        # num = self.MainWindowPerVideo.horizontalSlider.value()
        # self.player.setPosition((num / 100) * self.maxProgressvalue)

        path = 'tmp/0_10test1.mp4'
        self._data = self.GetVideo(path)
        self._buffer.setData(self._data)
        # self._buffer.open(QtCore.QIODevice.ReadOnly)
        # self.player.setMedia(QMediaContent(), self._buffer)
        # self.player.play()


    def change_time(self,num):
        if self.player.duration():
            self.player.setPosition((num/100)*self.maxProgressvalue)
    def setCurrent(self):
        # self.maxProgressvalue = self.player.duration()
        # print(self.maxProgressvalue,self.player.position())
        if self.player.duration():
            self.maxProgressvalue = self.player.duration()
            self.CurProgress = self.player.position()
            self.MainWindowPerVideo.label_2.setText(TimeFormat(self.maxProgressvalue/1000))
            self.MainWindowPerVideo.label.setText(TimeFormat(self.CurProgress/1000))
            print(self.maxProgressvalue,self.player.position())
            self.MainWindowPerVideo.horizontalSlider.setValue(100*self.CurProgress/self.maxProgressvalue)


    def GetVideo(self,path):
        with open(path, 'rb') as stream:
            return stream.read()

    def playvideo(self):
        path = 'tmp/0_10test1.mp4'
        self.MainWindowPerVideo.label_4.setText(path)
        self.MainWindowPerVideo.label_3.setPixmap(QtGui.QPixmap('img/plause1.png'))
        self.MainWindowPerVideo.label_3.setScaledContents(True)
        self._data = self.GetVideo(path)
        self._buffer.setData(self._data)
        self._buffer.open(QtCore.QIODevice.ReadOnly)
        self.player.setMedia(QMediaContent(), self._buffer)

        time.sleep(0.01)
        self.player.play()  # 播放视频


    def stopvideo(self):
        pass

    def Changeplaystate(self):
        if not self.playstate:
            self.playvideo()
            self.playstate = 1
        else:
            self.stopvideo()
            self.playstate = 0



    def setCurrent_(self):
        print(self.player.position())#ms

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PreV()
    # window.show()
    sys.exit(app.exec_())


