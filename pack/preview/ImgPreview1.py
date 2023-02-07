# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:33:16 2019
@author: Tiny
"""
# =============================================================================
''' 采用PyQt5实现，基本功能如下：
    1. 图片缩放(点选/快捷键两种方式，单次缩放尺度小伙伴们自己可调);
    2. 图片旋转(点选/快捷键两种方式，单次旋转角度小伙伴们自己可调);
    3. 图片移动(点选/快捷键两种方式，单次移动距离小伙伴们自己可调)-->待开发,后续续上。'''
# =============================================================================
# =============================================================================
''' 该代码存在一个问题：'''
#   图片缩小很小时，长宽比例保持的不好，且再次放大后，图片失真，图片信息丢掉很多！
''' 内存中存放原图，针对原图设定一个缩放ratio变量，在原图基础上做缩放'''
# =============================================================================
# =============================================================================
''' 注意：'''
#   1. self.imageLabel.setScaledContents(True) #允许QLabel缩放它的内容充满整个可用的空间。
#        小伙伴可以看一下设置不设置该局的图片显示区别；
#   2. 注意一下PyQt4和PyQt5的个别函数用法的区别;
#   3. 很多函数类似，完全可以编写为一个函数，不需要那么多行代码，都是重复的;
#   4. 在别人的基础上改的，玩玩，大家可做个参考。
# =============================================================================
# =============================================================================
''' PyQt5 与PyQt4 的一些区别，供小伙伴们参考:'''
#   需用QtWidgets.QLabel(),  # PyQt4
#              不是QLabel();  # PyQt5
#
#    需用QtWidgets.QAction(QIcon, QString, QObject),  # PyQt4
#              不是QAction(QIcon, QString, QObject);  # PyQt5
#
#    The old style:
#        self.connect(origin, SIGNAL('completed'), self._show_results)  # PyQt4
#    should now be written in the new style:
#        origin.completed.connect(self._show_results)  # PyQt5
#
#    PyQt5中已经不再支持PyQt4种不推荐方法 QMatrix
#         可通过QTransform 实现
# =============================================================================
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtWidgets  # , QtCore, QtGui

'''定义主窗口(包含菜单栏、工具栏)'''


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        f = QFont("ZYSong18030", 12)  # 设置字体,字号
        self.setFont(f)
        self.setWindowTitle("Image Processor")  # 窗口命名
        self.resize(862, 706)

        self.imageLabel = QtWidgets.QLabel()  # 需用QtWidgets.QLabel(),不是QLabel()
        #        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)  # 允许QLabel缩放它的内容充满整个可用的空间
        self.setCentralWidget(self.imageLabel)  # 注释掉该句,则运行不会显示图片

        self.image = QImage()
        if self.image.load("image/cc.png"):  # 如果载入图片,则
            self.imageLabel.setPixmap(QPixmap.fromImage(self.image))  # 显示图片
            self.resize(self.image.width(), self.image.height())  # 重设大小

        self.createActions()  # 创建“放大”、“缩小”及“旋转”等的QAction
        self.createMenus()  # 创建菜单栏
        self.createToolBars()  # 创建工具栏

    '''创建缩放、旋转的QAction'''

    def createActions(self):
        self.zoomInAction = QtWidgets.QAction(QIcon("image/zoomIn.gif"),
                                              self.tr("放大"), self)  # 不是QAction(QIcon, QString, QObject)
        self.zoomInAction.setShortcut("Ctrl+I")  # 设置快捷键
        self.zoomInAction.setStatusTip(self.tr("放大"))  # 设置标题栏
        #        self.connect(self.zoomInAction,SIGNAL("triggered()"),
        #                     self.slotZoomin)                              # PyQt4
        self.zoomInAction.triggered.connect(self.slotZoomIn)  # PyQt5

        self.zoomOutAction = QtWidgets.QAction(QIcon("image/zoomOut.gif"),
                                               self.tr("缩小"), self)  # 不是QAction(QIcon, QString, QObject)
        self.zoomOutAction.setShortcut("Ctrl+O")  # 设置快捷键
        self.zoomOutAction.setStatusTip(self.tr("缩小"))  # 设置标题栏
        #        self.connect(self.zoomOutAction,SIGNAL("triggered()"),
        #                     self.slotZoomOut)                              # PyQt4
        self.zoomOutAction.triggered.connect(self.slotZoomOut)  # PyQt5

        self.rotateAction = QtWidgets.QAction(QIcon("image/rotate.gif"),
                                              self.tr("顺旋"), self)  # 不是QAction(QIcon, QString, QObject)
        self.rotateAction.setShortcut("Ctrl+R")  # 设置快捷键
        self.rotateAction.setStatusTip(self.tr("顺旋"))  # 设置标题栏
        #        self.connect(self.rotateAction,SIGNAL("triggered()"),
        #                     self.slotRotate)                               # PyQt4
        self.rotateAction.triggered.connect(self.slotRotate)  # PyQt5

        self.rotateAntiAction = QtWidgets.QAction(QIcon("image/rotateAnti.gif"),
                                                  self.tr("逆旋"), self)  # 不是QAction(QIcon, QString, QObject)
        self.rotateAntiAction.setShortcut("Ctrl+E")  # 设置快捷键
        self.rotateAntiAction.setStatusTip(self.tr("逆旋"))  # 设置标题栏
        #        self.connect(self.rotateAntiAction,SIGNAL("triggered()"),
        #                     self.slotRotateAnti)                           # PyQt4
        self.rotateAntiAction.triggered.connect(self.slotRotateAnti)  # PyQt5

    '''创建菜单栏'''

    def createMenus(self):
        zoomMenu = self.menuBar().addMenu(self.tr("缩放"))  # 缩放菜单选项
        zoomMenu.addAction(self.zoomInAction)  # 放大子选项
        zoomMenu.addAction(self.zoomOutAction)  # 缩小子选项
        rotateMenu = self.menuBar().addMenu(self.tr("旋转"))  # 旋转菜单选项
        rotateMenu.addAction(self.rotateAction)  # 顺旋子选项
        rotateMenu.addAction(self.rotateAntiAction)  # 逆旋子选项

    '''创建工具栏'''

    def createToolBars(self):
        fileToolBar = self.addToolBar("Print")
        fileToolBar.addAction(self.zoomInAction)
        fileToolBar.addAction(self.zoomOutAction)
        fileToolBar.addAction(self.rotateAntiAction)
        fileToolBar.addAction(self.rotateAction)

    '''图片放大(倍数可设)'''

    def slotZoomIn(self):
        if self.image.isNull():  # 没图片,则不执行任何操作
            return
        #        martix =QMatrix()        # PyQt4,PyQt5中已废弃
        transform = QTransform()  # PyQt5
        #        martix.scale(2,2)        # PyQt4,PyQt5中已废弃
        transform.scale(1.2, 1.2)  # PyQt5
        self.image = self.image.transformed(transform);  # 相应的matrix改为transform
        self.imageLabel.setPixmap(QPixmap.fromImage(self.image))  # 显示图片到Qlabel控件
        self.resize(self.image.width(), self.image.height())

    '''图片缩小(倍数可设)'''

    def slotZoomOut(self):
        if self.image.isNull():  # 没图片,则不执行任何操作
            return
        #        martix =QMatrix()        # PyQt4,PyQt5中已废弃
        transform = QTransform()  # PyQt5
        #        martix.scale(2,2)        # PyQt4,PyQt5中已废弃
        transform.scale(0.8, 0.8)  # PyQt5
        self.image = self.image.transformed(transform);  # 相应的matrix改为transform
        self.imageLabel.setPixmap(QPixmap.fromImage(self.image))  # 显示图片到Qlabel控件
        self.resize(self.image.width(), self.image.height())

    '''图片顺旋(角度可设)'''

    def slotRotate(self):
        if self.image.isNull():  # 没图片,则不执行任何操作
            return
        #        martix =QMatrix()        # PyQt4,PyQt5中已废弃
        transform = QTransform()  # PyQt5
        #        martix.rotate(90)        # PyQt4,PyQt5中已废弃
        transform.rotate(90)  # PyQt5
        self.image = self.image.transformed(transform);  # 相应的matrix改为transform
        self.imageLabel.setPixmap(QPixmap.fromImage(self.image))  # 显示图片到Qlabel控件
        self.resize(self.image.width(), self.image.height())

    '''图片逆旋(角度可设)'''

    def slotRotateAnti(self):
        if self.image.isNull():  # 没图片,则不执行任何操作
            return
        #        martix =QMatrix()        # PyQt4,PyQt5中已废弃
        transform = QTransform()  # PyQt5
        #        martix.rotate(90)        # PyQt4,PyQt5中已废弃
        transform.rotate(-90)  # PyQt5
        self.image = self.image.transformed(transform);  # 相应的matrix改为transform
        self.imageLabel.setPixmap(QPixmap.fromImage(self.image))  # 显示图片到Qlabel控件
        self.resize(self.image.width(), self.image.height())


'''主函数'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
