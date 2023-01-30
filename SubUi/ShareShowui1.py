from . import ShareShowui
from PyQt5 import QtCore, QtGui, QtWidgets
import sip
from PyQt5.QtGui import QFontMetrics,QCursor, QIcon
from PyQt5.QtCore import *
from functools import partial


def FileConChose(fetype):
    if fetype == 'folder':
        return 'img/filecon/foldersm.png'
    if fetype == 'zip':
        return 'img/filecon/zipcon.png'
    if fetype == 'img':
        return 'img/filecon/imgcon.jpg'
    if fetype == 'pdf':
        return 'img/filecon/pdfcon.jpg'
    if fetype == 'ppt':
        return 'img/filecon/pptcon.jpg'
    if fetype == 'exe':
        return 'img/filecon/execon.jpg'
    if fetype == 'excel':
        return 'img/filecon/excelcon.jpg'
    if fetype == 'word':
        return 'img/filecon/wordcon.jpg'
    if fetype == 'html':
        return 'img/filecon/htmlcon.jpg'
    else:
        return 'img/filecon/wj.jfif'
class ShareShow(ShareShowui.Ui_Form):
    def __init__(self,frame_ShareShow):
        super().__init__()
        self.frame_ShareShow = frame_ShareShow
        self.init()
        self.CurFrames = []


    def init(self):
        self.setupUi(self.frame_ShareShow)
        self.formLayout.removeWidget(self.frame_13)
        sip.delete(self.frame_13)
        self.label.setText('')
        self.label_2.setText('')
        self.frame_2.setMaximumSize(QtCore.QSize(500, 30))

    def clearframe(self):
        for i in self.CurFrames:
            self.formLayout.removeWidget(i)
            sip.delete(i)
        self.CurFrames = []
        # for i in range(self.formLayout.count()):
        #     self.formLayout.itemAt(i).widget().deleteLater()
        #     # sip.delete(self.frame_13)

    def add(self,info):
        self.frame_13 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_13.setMinimumSize(QtCore.QSize(0, 36))
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 36))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_17.setContentsMargins(3, 0, 9, 0)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_18.addWidget(self.checkBox_2)
        self.label_32 = QtWidgets.QLabel(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setMinimumSize(QtCore.QSize(30, 30))
        self.label_32.setMaximumSize(QtCore.QSize(30, 30))
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_18.addWidget(self.label_32)
        self.label_36 = QtWidgets.QLabel(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        self.label_36.setMinimumSize(QtCore.QSize(0, 30))
        self.label_36.setMaximumSize(QtCore.QSize(16777215, 36))
        self.label_36.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_18.addWidget(self.label_36)
        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(1, 1)
        self.horizontalLayout_18.setStretch(2, 20)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_18)
        self.label_37 = QtWidgets.QLabel(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_17.addWidget(self.label_37)
        self.label_38 = QtWidgets.QLabel(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_17.addWidget(self.label_38)
        self.horizontalLayout_17.setStretch(0, 7)
        self.horizontalLayout_17.setStretch(1, 2)
        self.horizontalLayout_17.setStretch(2, 2)

        self.formLayout.setWidget(self.formLayout.count(), QtWidgets.QFormLayout.SpanningRole, self.frame_13)

        self.label.setText(info['ShareUserName']+'分享的文件')
        metrics = QFontMetrics(self.label_36.font())
        new_file_name = metrics.elidedText(info['fename'], Qt.ElideRight, 260)
        self.label_36.setText(new_file_name)
        self.label_37.setText(info['date'])
        self.label_38.setText(info['big'])
        self.label_32.setPixmap(QtGui.QPixmap(FileConChose(info['fetype'])))
        self.label_32.setScaledContents(True)

        self.CurFrames.append(self.frame_13)