import os,shutil,sip,threading
import time,wave

from SubUi import PerVideoui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2,requests,json
from PyQt5.QtGui import QImage
from PyQt5 import QtCore
from PyQt5.QtCore import Qt



class MovieShow():
    def __init__(self,main,label):
        self.Main = main
        self.movie_label = label
        # self.init()
    def init(self):
        # self.movie_label = QtWidgets.QLabel(self.Main)
        # self.movie_label.setGeometry(0, 0, 300, 300)
        self.movie = QtGui.QMovie("img/loading.gif")
        self.movie_label.setMovie(self.movie)
        # self.movie.start()
    def show(self):
        self.movie = QtGui.QMovie("img/loading.gif")
        self.movie_label.setMovie(self.movie)
        self.movie.start()
    # def close(self):
    #     self.movie_label
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

class PerViewVideo(QObject,PerVideoui.Ui_MainWindowPerVideo):
    signalUpdateplay = pyqtSignal(list)
    signalmoveSide = pyqtSignal()
    def __init__(self,ui,info):
        super(PerViewVideo, self).__init__()

        self.signalUpdateplay.connect(self.updateplayshow)
        self.signalmoveSide.connect(self.moveSide)
        self.playvideothread = threading.Thread(target=self.playvideo1)
        self.lock = threading.Lock()
        self.path = info['fepath']
        self.VideoStock = {}
        self.closeact = 0
        self.HveAud = 0
        self.numidex = 0
        self.modms = 0
        self.fps = None
        self.videos = {}
        self.curtime = 0
        self.playstate = 1
        self.playint = -1
        self.FaPath = 'TEMP/video/'
        self.FileName = info['fename']
        self.ui = ui
        self.ui.Main = QMainWindow()
        self.s = requests.Session()
        self.setupUi(self.ui.Main)
        self.ui.Main.show()
        self.movie = MovieShow(self.ui.Main,self.label_5)
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
        # self.DownLayout[1].removeWidget(infoi['frame'])
        sip.delete(self.horizontalSlider)
        # self.frame_3.itemAt(0).widget().deleteLater()
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
        self.label_3.setMaximumSize(QtCore.QSize(36, 36))
        self.label_3.setPixmap(QtGui.QPixmap('img/plause.png'))
        self.label_3.setScaledContents(True)
        self.label_3.mousePressEvent = lambda e:self.playstateChange()
        # self.player.positionChanged.connect(self.setCurrent)
        # self.horizontalSlider.sliderMoved.connect(self.change_time)
        self.horizontalSlider.customSliderClicked.connect(self.change_time)
        print('PreviewVideo',self.path)
        self.GetVideoInfo()


    def playstateChange(self):
        if self.playstate:
            self.closeact = 1
            # self.playvideo(1)
            self.label_3.setPixmap(QtGui.QPixmap('img/start.png'))
            self.label_3.setScaledContents(True)
            self.playstate = 0
        else:
            self.numidex = int(self.curtime / 10)
            self.modms = (self.curtime - self.numidex * 10)*1000
            print('modms',self.modms,self.curtime)
            self.closeact = 0
            self.label_3.setPixmap(QtGui.QPixmap('img/plause.png'))
            self.label_3.setScaledContents(True)
            self.playstate = 1
            self.playvideo()


    def change_time(self):
        curtime = (self.horizontalSlider.value()/100)*self.VideoDuring
        self.curtime = curtime/1000
        self.numidex = int(curtime / 1000 / 10)
        self.modms = (curtime/1000 - self.numidex*10)*1000
        self.closeact = 1
        # self.playvideo(1)
        while self.playvideothread.is_alive():
            pass
        self.closeact = 0
        self.playvideo()
        if not self.playstate:
            self.playstate = 1
            self.playstateChange()

    def moveSide(self):
        progress = (self.curtime*1000/self.VideoDuring)*100
        # print(progress)
        self.horizontalSlider.setValue(progress)
        # print(self.curtime,self.VideoDuring,self.horizontalSlider.value())
        self.label.setText(TimeFormat(self.curtime))


    def ListenProgrressact(self):
        while True:
            Nextint = self.playint+1
            if Nextint >= len(self.VideoStock) or Nextint==0:
                pass
            else:
                self.LoadVideo(self.VideoStock[Nextint])
            time.sleep(1)
    def ListenProgrress(self):
        listenpro = threading.Thread(target=self.ListenProgrressact)
        listenpro.setDaemon(True)
        listenpro.start()

    def updateplayshow(self,pixs):
        self.label_5.setPixmap(pixs[0])
    def playvideo(self,pause = None):
        self.movie.show()
        self.playvideothread = threading.Thread(target=self.playvideo1,args=(pause,))
        self.playvideothread.setDaemon(True)
        self.playvideothread.start()

        # self.playvideothread.join()
    def playvideo1(self,pause = None):
        # curtime = (self.horizontalSlider.value() / 100) * self.VideoDuring/1000
        curtime = self.curtime
        curFrams = 0
        if pause:
            self.closeact = 1
            cv2.destroyAllWindows()
        for i in range(self.numidex,len(self.VideoStock)):
        # for i in self.VideoStock:
            print(i)
            self.playint = i
            if self.closeact:
                cv2.destroyAllWindows()
                break
            info = self.VideoStock[i]
            print(info)
            self.LoadVideo(info)
            videopath = self.FaPath + info['name']
            video = cv2.VideoCapture(videopath)  # 读取视频（视频源为视频文件）

            if not self.fps:
                self.fps = video.get(cv2.CAP_PROP_FPS)  # 读取视频帧速率
                try:
                    # cap.set(cv2.CAP_PROP_POS_MSEC, timespan[0])
                    self.image_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))  # 视频帧宽度
                    self.image_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 视频帧高度
                    self.label_5.resize(self.label_5.width(), self.label_5.width() * self.image_height / self.image_width)
                except:
                    pass
            # self.label_movie = QtWidgets.QLabel(self.ui.Main)
            # self.label_movie.setObjectName("label_movie")
            # # self.label_movie.resize(200, 200)
            # self.label_movie.setText('andsh')
            video.set(cv2.CAP_PROP_POS_MSEC,self.modms)
            self.modms = 0
            # 显示视频
            while True:
                if self.closeact:
                    cv2.destroyAllWindows()
                    break
                ret, frame = video.read()  # 读取一帧视频，一帧就是一张图像
                if ret == False:
                    break
                show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
                # showImage=showImage.copy(self.x1, self.y1,self.x2, self.y2)
                pix = QtGui.QPixmap.fromImage(showImage)
                # self.labelShow.resize(image_width,image_height)
                pix = pix.scaled(self.label_5.width(), self.label_5.height(), Qt.IgnoreAspectRatio)
                self.signalUpdateplay.emit([pix])
                # self.label_5.setPixmap(pix)
                curFrams += 1
                self.curtime = curtime+curFrams/self.fps
                # cv2.imshow("myframe", frame)  # 显示
                # self.moveSide()
                self.signalmoveSide.emit()
                cv2.waitKey(int(1000/self.fps))  # 用帧率来计算显示帧间隔
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
            self.videos[i] = None
            self.VideoStock[i] = {'name':'{}_{}#'.format(starttime,endtime)+self.FileName,'path':self.path,
                                  'start':starttime,'end':endtime}
            starttime = endtime
        self.playvideo()
        # for i in self.VideoStock:
        #     # print(self.VideoStock[i])
        #     self.LoadVideo(self.VideoStock[i])

    def LoadVideo(self,info):
        videopath = self.FaPath + info['name']
        audioopath = videopath + '.wav'
        if os.path.exists(videopath):
            return
        url = 'http://' + self.ui.host + '/preview/'
        data = {
            'client': 'windows',
            'VideoFram': [info['start'], info['end']],
            'framidexs':[int(self.VideoRate*info['start']),int(self.VideoRate*info['end'])],
            # 'AudioFram':[int(StartAudioFram),int(EndAudioFram)],
            'filepath': self.path,

        }
        r = self.s.post(url, data=json.dumps(data), headers=self.ui.SBCRe.headers)
        with open(videopath , 'wb') as f:
            f.write(r.content)
        if self.HveAud:
            data['HveAud'] = self.HveAud
            r = self.s.post(url, data=json.dumps(data), headers=self.ui.SBCRe.headers)
            wf = wave.open(audioopath, 'wb')
            wf.setnchannels(self.Audchannels)
            wf.setsampwidth(self.Audsampwidth)
            wf.setframerate(self.Audframerate)
            wf.writeframes(r.content)
            wf.close()




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
            'filepath': self.path,

        }
        print(int(StartVideoFram),int(EndVideoFram))
        r = self.s.post(url, data=json.dumps(data), headers=self.ui.SBCRe.headers)
        data = json.loads(r.text)
        print(len(data['VideoFrams']))

    def GetVideoInfo(self):
        self.movie.show()
        t = threading.Thread(target=self.GetVideoInfoact)
        t.setDaemon(True)
        t.start()
    def GetVideoInfoact(self):
        url = 'http://'+self.ui.host+'/preview/'
        data = {
            'client': 'windows',
            'filepath': self.path
        }
        res = self.s.post(url, data=json.dumps(data), headers=self.ui.SBCRe.headers)
        try:
            redata = json.loads(res.text)
        except:
            return
        self.VideoDuring = redata['timeduring']
        self.fename = redata['fename']
        print(redata)
        self.HveAud = redata['HveAud']
        self.label_2.setText(TimeFormat(redata['timeduring']))
        self.label_4.setText(redata['fename'])
        self.VideoDuring = self.VideoDuring*1000
        self.VideoRate = redata['VideoRate']
        self.Audsampwidth = redata['audsampwidth']
        self.Audchannels = redata['audchannels']
        self.Audframerate = redata['audframerate']
        self.ListenProgrress()
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
