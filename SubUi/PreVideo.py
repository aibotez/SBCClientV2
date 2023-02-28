import os,shutil
import time

from SubUi import PerVideoui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2,requests,json
from PyQt5.QtGui import QImage
from PyQt5 import QtCore
from PyQt5.QtCore import Qt


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
        self.VideoStock = {}
        self.closeact = 0
        self.FaPath = 'TEMP/video/'
        self.FileName = info['fename']
        self.ui = ui
        self.ui.Main = QMainWindow()
        self.s = requests.Session()
        self.setupUi(self.ui.Main)
        self.ui.Main.show()
        self.ui.Main.closeEvent=self.closeWindw
        self.init()
        self.CurVIdeotime = 0


    def closeWindw(self,e):
        cv2.destroyAllWindows()
        self.closeact = 1
    def init(self):

        if not os.path.isdir(self.FaPath):
            os.makedirs(self.FaPath)
        else:
            for f in os.listdir(self.FaPath):
                os.remove(os.path.join(self.FaPath, f))

        # self.verticalLayout.itemAt(0).widget().deleteLater()
        # self.labelShow = QtWidgets.QLabel(self.frame)
        # self.verticalLayout.addWidget(self.labelShow)
        self.label_5.setText('')
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

    def playvideo(self):
        for i in self.VideoStock:
            print(i)
            if self.closeact:
                cv2.destroyAllWindows()
                break
            info = self.VideoStock[i]
            print(info)
            self.LoadVideo(info)
            videopath = self.FaPath + info['name']
            video = cv2.VideoCapture(videopath)  # 读取视频（视频源为视频文件）
            # video = cv2.VideoCapture(0)                # 读取视频（视频源为编号0的摄像头）
            fps = video.get(cv2.CAP_PROP_FPS)  # 读取视频帧速率
            # image_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))  # 视频帧宽度
            # image_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 视频帧高度
            # self.label_5.resize(800, 800 * image_height / image_width)
            # 显示视频
            while True:
                ret, frame = video.read()  # 读取一帧视频，一帧就是一张图像
                if ret == False:
                    break
                show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
                # showImage=showImage.copy(self.x1, self.y1,self.x2, self.y2)
                pix = QtGui.QPixmap.fromImage(showImage)
                # self.labelShow.resize(image_width,image_height)
                pix = pix.scaled(self.label_5.width(), self.label_5.height(), Qt.IgnoreAspectRatio)
                self.label_5.setPixmap(pix)
                # cv2.imshow("myframe", frame)  # 显示
                cv2.waitKey(int(1000/fps))  # 用帧率来计算显示帧间隔
        cv2.destroyAllWindows()
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
            self.VideoStock[i] = {'name':'{}_{}#'.format(starttime,endtime)+self.FileName,'path':self.path,
                                  'start':starttime,'end':endtime}
            starttime = endtime
        self.playvideo()
        # for i in self.VideoStock:
        #     # print(self.VideoStock[i])
        #     self.LoadVideo(self.VideoStock[i])

    def LoadVideo(self,info):
        videopath = self.FaPath + info['name']
        if os.path.exists(videopath):
            return
        url = 'http://' + self.ui.host + '/preview/'
        data = {
            'client': 'windows',
            'VideoFram': [info['start'], info['end']],
            # 'AudioFram':[int(StartAudioFram),int(EndAudioFram)],
            'filepath': self.path
        }
        r = self.s.post(url, data=json.dumps(data), headers=self.ui.SBCRe.headers)
        with open(videopath , 'wb') as f:
            f.write(r.content)



    def LoadVideo1(self,StartTime):
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
            # 'AudioFram':[int(StartAudioFram),int(EndAudioFram)],
            'filepath': self.path
        }
        print(int(StartVideoFram),int(EndVideoFram))
        r = self.s.post(url, data=json.dumps(data), headers=self.ui.SBCRe.headers)
        data = json.loads(r.text)
        print(len(data['VideoFrams']))

    def GetVideoInfo(self):
        url = 'http://'+self.ui.host+'/preview/'
        data = {
            'client': 'windows',
            'filepath': self.path
        }
        res = self.s.post(url, data=json.dumps(data), headers=self.ui.SBCRe.headers)
        redata = json.loads(res.text)
        self.VideoDuring = redata['timeduring']
        self.fename = redata['fename']
        print(redata)
        self.VideoDuring = self.VideoDuring*1000
        self.StructData()

        # self.VideoInfo = redata['VideoFile']
        # print(redata)
        # TotalTime = self.VideoInfo['VideoFramsTotal']/self.VideoInfo['VideoFramRate']
        # self.label_2.setText(TimeFormat(TotalTime))
        # self.LoadVideo(1)

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
