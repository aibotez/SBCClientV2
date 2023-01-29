from . import FileInfosui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtCore import *

def size_format(size):
    if size < 1024:
        return '%i' % size + 'B'
    elif 1024 <= size < 1024*1024:
        return '%.1f' % float(size/1024) + 'KB'
    elif 1024*1024 <= size < 1024*1024*1024:
        return '%.1f' % float(size/(1024*1024)) + 'MB'
    elif 1024*1024*1024 <= size < 1024*1024*1024*1024:
        return '%.1f' % float(size/(1024*1024*1024)) + 'GB'
    elif 1024*1024*1024*1024 <= size:
        return '%.1f' % float(size/(1024*1024*1024*1024)) + 'TB'
def FileConChose(fetype):
    if fetype == 'folder':
        return 'img/filecon/folder1.png'
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
class FileInfosUi(FileInfosui.Ui_Dialog):
    def __init__(self,Dialog,ui,ChosedFile):
        super().__init__()
        self.ui = ui
        self.ChosedFile = ChosedFile
        self.Dialog = Dialog
        self.init()
    def init(self):
        self.setupUi(self.Dialog)
        self.label.setPixmap(QtGui.QPixmap(FileConChose(self.ChosedFile['fetype'])))
        self.label.setScaledContents(True)
        metrics = QFontMetrics(self.label_2.font())
        new_file_name = metrics.elidedText(self.ChosedFile['fename'], Qt.ElideRight, 360)
        self.label_2.setText(new_file_name)
        self.label_6.setText(self.ChosedFile['fepath'])
        self.label_8.setText('')
        # print(self.ui.nav['SBC'][-1]['path'])
        self.GetFileInfo()
    def GetFileInfo(self):
        self.ChosedFile['path'] = self.ChosedFile['fepath']
        FilePorper = self.ui.SBCRe.SBCFileInfos(self.ChosedFile)
        self.label_4.setText(size_format(FilePorper['size']))
        if self.ChosedFile['isdir']:
            self.label_8.setText('{}个文件夹，{}个文件'.format(FilePorper['FolderNums'],FilePorper['FileNUms']))
        self.label_12.setText(FilePorper['ctime'])
        self.label_10.setText(FilePorper['mtime'])