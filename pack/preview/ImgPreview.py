import threading

import requests,time

# coding:utf-8
import sys

from PyQt5.QtCore import QRect, QRectF, QSize, Qt
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QPainter, QPixmap, QWheelEvent
from PyQt5.QtWidgets import (QApplication, QGraphicsItem, QGraphicsPixmapItem,
                             QGraphicsScene, QGraphicsView)
from PyQt5.QtCore import *


class ImageViewer(QGraphicsView):
    """ 图片查看器 """
    signalShowImg = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        self.setWindowTitle('小黑云图片预览')
        self.zoomInTimes = 0
        self.maxZoomInTimes = 22
        self.signalShowImg.connect(self.Previewact1)

        # 创建场景
        self.graphicsScene = QGraphicsScene()

        # # 图片
        self.pixmap = QPixmap(r'C:\Users\zz\Pictures\20191203150409589.png')
        self.pixmapItem = QGraphicsPixmapItem(self.pixmap)
        self.displayedImageSize = QSize(0, 0)

        # 初始化小部件
        self.__initWidget()

    def Previewact(self, imgbase64):
        t = threading.Thread(target=lambda :self.signalShowImg.emit([imgbase64]))
        t.setDaemon(True)
        t.start()
    def Previewact1(self,imgbase64s):
        imgbase64 = imgbase64s[0]
        # self.close()
        # graphicsScene = QGraphicsScene()
        self.show()
        self.graphicsScene.deleteLater()
        self.graphicsScene = QGraphicsScene()
        self.pixmap = QPixmap()
        self.pixmap.loadFromData(imgbase64)
        self.pixmapItem = QGraphicsPixmapItem(self.pixmap)
        self.displayedImageSize = QSize(600, 500)
        # self.__initWidget(graphicsScene)
        # self.show()
        self.__initWidget()
        # self.graphicsScene.addItem(self.pixmapItem)
        # self.setScene(self.graphicsScene)

    def __initWidget(self):
        """ 初始化小部件 """
        self.resize(700, 500)

        # 隐藏滚动条
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # 以鼠标所在位置为锚点进行缩放
        self.setTransformationAnchor(self.AnchorUnderMouse)

        # 平滑缩放
        self.pixmapItem.setTransformationMode(Qt.SmoothTransformation)
        self.setRenderHints(QPainter.Antialiasing |
                            QPainter.SmoothPixmapTransform)

        # 设置场景
        self.graphicsScene.addItem(self.pixmapItem)
        self.setScene(self.graphicsScene)
        self.resize0()


    def wheelEvent(self, e: QWheelEvent):
        """ 滚动鼠标滚轮缩放图片 """
        if e.angleDelta().y() > 0:
            self.zoomIn()
        else:
            self.zoomOut()


    def resize0(self):
        if self.zoomInTimes > 0:
            return
        # 调整图片大小
        ratio = self.__getScaleRatio()
        self.displayedImageSize = self.pixmap.size()*ratio
        if ratio < 1:
            self.fitInView(self.pixmapItem, Qt.KeepAspectRatio)
        else:
            self.resetTransform()

    def resizeEvent(self, e):
        """ 缩放图片 """
        super().resizeEvent(e)

        if self.zoomInTimes > 0:
            return

        # 调整图片大小
        ratio = self.__getScaleRatio()
        self.displayedImageSize = self.pixmap.size()*ratio
        if ratio < 1:
            self.fitInView(self.pixmapItem, Qt.KeepAspectRatio)
        else:
            self.resetTransform()

    # def setImage(self, imagePath: str):
    #     """ 设置显示的图片 """
    #     self.resetTransform()
    #
    #     # 刷新图片
    #     self.pixmap = QPixmap(imagePath)
    #     self.pixmapItem.setPixmap(self.pixmap)
    #
    #     # 调整图片大小
    #     self.setSceneRect(QRectF(self.pixmap.rect()))
    #     ratio = self.__getScaleRatio()
    #     self.displayedImageSize = self.pixmap.size()*ratio
    #     if ratio < 1:
    #         self.fitInView(self.pixmapItem, Qt.KeepAspectRatio)

    def resetTransform(self):
        """ 重置变换 """
        super().resetTransform()
        self.zoomInTimes = 0
        self.__setDragEnabled(False)

    def __isEnableDrag(self):
        """ 根据图片的尺寸决定是否启动拖拽功能 """
        v = self.verticalScrollBar().maximum() > 0
        h = self.horizontalScrollBar().maximum() > 0
        return v or h

    def __setDragEnabled(self, isEnabled: bool):
        """ 设置拖拽是否启动 """
        self.setDragMode(
            self.ScrollHandDrag if isEnabled else self.NoDrag)

    def __getScaleRatio(self):
        """ 获取显示的图像和原始图像的缩放比例 """
        if self.pixmap.isNull():
            return 1

        pw = self.pixmap.width()
        ph = self.pixmap.height()
        rw = min(1, self.width()/pw)
        rh = min(1, self.height()/ph)
        return min(rw, rh)

    def fitInView(self, item: QGraphicsItem, mode=Qt.KeepAspectRatio):
        """ 缩放场景使其适应窗口大小 """
        super().fitInView(item, mode)
        self.displayedImageSize = self.__getScaleRatio()*self.pixmap.size()
        self.zoomInTimes = 0

    def zoomIn(self, viewAnchor=QGraphicsView.AnchorUnderMouse):
        """ 放大图像 """
        if self.zoomInTimes == self.maxZoomInTimes:
            return

        self.setTransformationAnchor(viewAnchor)

        self.zoomInTimes += 1
        self.scale(1.1, 1.1)
        self.__setDragEnabled(self.__isEnableDrag())

        # 还原 anchor
        self.setTransformationAnchor(self.AnchorUnderMouse)

    def zoomOut(self, viewAnchor=QGraphicsView.AnchorUnderMouse):
        """ 缩小图像 """
        if self.zoomInTimes == 0 and not self.__isEnableDrag():
            return

        self.setTransformationAnchor(viewAnchor)

        self.zoomInTimes -= 1

        # 原始图像的大小
        pw = self.pixmap.width()
        ph = self.pixmap.height()

        # 实际显示的图像宽度
        w = self.displayedImageSize.width()*1.1**self.zoomInTimes
        h = self.displayedImageSize.height()*1.1**self.zoomInTimes

        if pw > self.width() or ph > self.height():
            # 在窗口尺寸小于原始图像时禁止继续缩小图像比窗口还小
            if w <= self.width() and h <= self.height():
                self.fitInView(self.pixmapItem)
            else:
                self.scale(1/1.1, 1/1.1)
        else:
            # 在窗口尺寸大于图像时不允许缩小的比原始图像小
            if w <= pw:
                self.resetTransform()
            else:
                self.scale(1/1.1, 1/1.1)

        self.__setDragEnabled(self.__isEnableDrag())

        # 还原 anchor
        self.setTransformationAnchor(self.AnchorUnderMouse)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ImageViewer()
    w.Previewact(2)
    # w.show()
    sys.exit(app.exec_())