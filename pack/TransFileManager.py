import os,time,sys
sys.path.append('..')
from . import DBManager
from UpdateUi import TransShowUpdate
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5 import QtGui,QtCore,QtWidgets,QtCore

class TransFileManager():
    # def __init__(self,DownRecordFile,UpRecordFile,FinishRcordFile):
    def __init__(self,MainUi,ui):
        self.ui = ui
        # self.ui.TranspArrow.setText("↑↓")
        self.dbManager = DBManager.DBManager()
        self.MainUi = MainUi
        self.Transhow = TransShowUpdate.TransShowUpdate(ui)

        # self.DownRecordFile = DownRecordFile
        # self.UpRecordFile = UpRecordFile
        # self.FinishRcordFile = FinishRcordFile
        self.TranspArrowShow()




    def TranspArrowShow(self):
        print('Tra')
        self.label = QtWidgets.QLabel(self.MainUi) #
        self.label.setGeometry(200,20,20,20)
        # self.label.setText("ABCDFED")

        # png = QtGui.QPixmap()  # 创建一个绘图类
        self.label.setPixmap(QtGui.QPixmap('./img/del1.png'))
        # png.load("img/del1.png")  # 从png中加载一个图片
        # print(66)
        # self.label.setPixmap(png)  # 设置文本标签的图形
        self.label.setScaledContents(True) # 图片随文本部件的大小变动
        self.anim = QtCore.QPropertyAnimation(self.label,b'geometry') # 设置动画的对象及其属性
        self.anim.setDuration(2000) # 设置动画间隔时间
        self.anim.setStartValue(QtCore.QRect(200,20,20,20)) # 设置动画对象的起始属性
        self.anim.setEndValue(QtCore.QRect(50, 500, 0, 0)) # 设置动画对象的结束属性
        self.anim.start() # 启动动画
        # self.ui.TranspArrow.setText("↑↓")
    def AddDownRecord(self,DownInfo):
        self.TranspArrowShow()
        # self.Transhow.AddDown(DownInfo)

        AdW = self.dbManager.AddUserDownRecord(DownInfo)
        if AdW == 'Have':
            reply = QMessageBox.question(self.MainUi,'提示', '该文件正在下载，重新下载？',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                pass
            else:
                return
        self.Transhow.RefreshDowning()


        # while True:
        #     try:
        #         with open(self.DownRecordFile,'a+') as f:
        #             f.write(DownInfo['FileName']+'\t'+DownInfo['FileMd5']+'\t'+DownInfo['FilePath']+'\t'+DownInfo['RoFilePath']+'\n')
        #         break
        #     except Exception as e:
        #         print('TranspFile')
        #         print(e)

    def GetDownRecord(self):
        DownInfo = self.dbManager.GetUserDownRecordAll()
        # DownInfo = []
        # with open(self.DownRecordFile,'r') as f:
        #     Rd = f.readline()
        # if Rd:
        #     for i in Rd:
        #         if len(Rd) >2:
        #             DownInfoi = i.split('\a')
        #             DownInfo.append({'FileName':DownInfoi[0],'FileMd5':DownInfoi[1],'FilePath':DownInfoi[2],'RoFilePath':DownInfoi[3]})
        return DownInfo

