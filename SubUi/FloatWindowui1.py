from SubUi import FloatWindowui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QAction,QFileDialog,QDialog
from PyQt5.QtGui import QFontMetrics,QCursor, QIcon

class FloatWd(FloatWindowui.Ui_Dialog):
    def __init__(self,ui,Dialog):
        super().__init__()
        self.ui = ui
        self.Dialog = Dialog
        self.init()


    def init(self):

        self.setupUi(self.Dialog)


        self.Dialog.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.Dialog.setWindowOpacity(0.9)
        self.Dialog.setCursor(Qt.PointingHandCursor)
        # self.Dialog.setWindowFlags(Qt.FramelessWindowHint|Qt.Tool)
        self.Dialog.setAttribute(Qt.WA_TranslucentBackground)

        self.shadow = QtWidgets.QGraphicsDropShadowEffect()  # 设定一个阴影,半径为10,颜色为#444444,定位为0,0
        self.shadow.setBlurRadius(10)
        self.shadow.setColor(QtGui.QColor("#444444"))
        self.shadow.setOffset(0, 0)
        self.frame_3.setGraphicsEffect(self.shadow)  # 为frame设定阴影效果

        self.Dialog.mousePressEvent = self.mousePressEvent
        self.Dialog.mouseMoveEvent = self.mouseMoveEvent
        self.Dialog.mouseMoveEvent = self.mouseMoveEvent
        self.label_6.setText('')
        self.label_7.setText('')
        self.label_9.setText('')
        self.label_10.setText('')
        self.label_11.setText('')
        self.label_9.setMaximumSize(QtCore.QSize(20, 20))
        self.label_9.setMinimumSize(QtCore.QSize(20, 20))

        desktop = QApplication.desktop()
        self.Screenwidth = desktop.width()
        self.Screenheight = desktop.height()
        window_width = self.Dialog.geometry().width()
        window_height = self.Dialog.geometry().height()
        self.Dialog.setGeometry(self.Screenwidth - window_width - 10, self.Screenheight - window_height-10, window_width, window_height)

        # 鼠标按下时，记录鼠标相对窗口的位置


    def close(self,e):
        self.Dialog.close()
    def creat_menu(self,e):
        self.groupBox_Upmenu = QMenu()
        self.actionClose = self.groupBox_Upmenu.addAction(u'关闭')
        self.actionMin = self.groupBox_Upmenu.addAction(u'最小化')
        self.groupBox_Upmenu.popup(QCursor.pos())
        self.groupBox_Upmenu.setStyleSheet("QMenu{\n"
                                        "    margin:0px 10px 10px 0px;\n"
                                        "    font-size:18px;\n"
                                        "}\n")
        self.actionClose.triggered.connect(self.close)
        # self.actionUpfolder.triggered.connect(self.fileoperclick.UpFolder)
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if event.button() == QtCore.Qt.LeftButton:
                self.Dialog.Move = True  ##鼠标按下时设置为移动状态
                self.Point = event.globalPos() - self.Dialog.pos()  ##记录起始点坐标
                event.accept()
        else:
            self.creat_menu(0)
    def mouseMoveEvent(self, QMouseEvent):  ##移动时间
        if QtCore.Qt.LeftButton and self.Dialog.Move:  ##切记这里的条件不能写死，只要判断move和鼠标执行即可！
            self.Dialog.move(QMouseEvent.globalPos() - self.Point)  ##移动到鼠标到达的坐标点！
            QMouseEvent.accept()
    def mouseReleaseEvent(self, QMouseEvent):  ##结束事件
        self.Dialog.Move = False





