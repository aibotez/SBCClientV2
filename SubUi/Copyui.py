from . import Moveui
import sys,hashlib
from PyQt5.QtWidgets import QTreeWidgetItem, QTreeWidget, QWidget, QVBoxLayout, QPushButton, QApplication,QMessageBox,QInputDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon,QBrush,QColor
from PyQt5 import QtCore, QtGui, QtWidgets


def str_trans_to_md5(src):
    src = src.encode("utf-8")
    myMd5 = hashlib.md5()
    myMd5.update(src)
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest
class CopyUi(Moveui.Ui_Dialog):
    def __init__(self,Dialog,ui,ChosedFiles):
        super().__init__()
        self.ui = ui
        self.ChosedFiles = ChosedFiles
        self.Dialog = Dialog
        self.init()

    def init(self):
        self.setupUi(self.Dialog)
        self.label_3.setText('')
        self.Dialog.setWindowTitle('复制文件到')
        self.pushButton.setText('复制到此处')
        self.pushButton.clicked.connect(self.MoveFile)
        self.treeView.setHeaderHidden(True)
        self.label.mousePressEvent = lambda e:self.NewFolderBox()
        # self.tree.clicked.connect(self.get_checked1)
        self.treeView.itemClicked.connect(self.get_CurPath)
        self.treeView.expanded.connect(self.nodeExpand)
        self.TreeNodes = {}
        # 顶级分支
        self.tree_main = QTreeWidgetItem(self.treeView)
        self.tree_main.setText(0, 'home')
        self.tree_main.setIcon(0, QIcon(r'img/filecon/foldersm.png'))
        item = QTreeWidgetItem()
        self.tree_main.addChild(item)
        self.TreeNodes[str_trans_to_md5('/home/')] = {'path':'/home/','item':self.tree_main,'expand':0}
        # self.qvl = QVBoxLayout()
        # self.qvl.addWidget(self.treeView)
        # self.qvl.addWidget(self.pushButton)
        # self.setLayout(self.qvl)
    def MoveReplacebox(self,ChosedFile):
        def calback(num):
            nonlocal replacechose
            replacechose = num
        replacechose = 0
        box = QMessageBox(QMessageBox.Question, '提示', '目标路径下含有“{}”是否要替换原文件？'.format(ChosedFile['fename']),
                          QMessageBox.NoButton, self.ui.MainWindow)
        sure = box.addButton('替换', QMessageBox.YesRole)
        cancel = box.addButton('取消', QMessageBox.YesRole)
        sureAll = box.addButton('全部替换', QMessageBox.YesRole)
        cancelAll = box.addButton('全部取消', QMessageBox.YesRole)
        box.show()
        sure.clicked.connect(lambda: calback(1))
        cancel.clicked.connect(lambda: calback(0))
        sureAll.clicked.connect(lambda: calback(2))
        cancelAll.clicked.connect(lambda: calback(3))
        box.exec_()
        return replacechose
    def NewFolderBox(self):
        CurPath = self.get_CurPath()
        text, okPressed = QInputDialog.getText(self.Dialog, "新建文件夹", CurPath, QtWidgets.QLineEdit.Normal, "")
        if text and okPressed:
            NewFolder = CurPath+text
            info = {}
            info['NewFolderName'] = text
            info['CurPath'] = CurPath
            self.ui.SBCRe.NewFolder(info)
            self.ui.signalRefresh.emit()
            self.TreeNodes[str_trans_to_md5(CurPath)]['expand'] = 0
            self.TreeNodes[str_trans_to_md5(CurPath)]['item'].setExpanded(True)
            self.nodeExpand()
    def checkpath(self,move2path):
        if self.ChosedFiles[0]['fepath'] in move2path:
            return 1
        srcpath = self.ChosedFiles[0]['fepath'].split('/')
        if not srcpath[-1]:
            del srcpath[-1]
        del srcpath[-1]
        srcpath = '/'.join(srcpath)+'/'
        if srcpath == move2path:
            return 1
        return 0
    def MoveFile(self):
        move2path = self.get_CurPath()
        if self.checkpath(move2path):
            return
        CurFileList = self.ui.SBCRe.GetFileList(move2path)
        fenameRo = [i['filename']+str(i['isdir']) for i in CurFileList]
        ChosedFiles = []
        replacechose = 0
        for i in self.ChosedFiles:
            ChosedFile = i
            if ChosedFile['fename']+str(ChosedFile['isdir']) in fenameRo:
                if replacechose != 2 or replacechose != 3:
                    replacechose = self.MoveReplacebox(ChosedFile)
                if replacechose == 0:
                    pass
                elif replacechose == 1:
                    ChosedFiles.append(i)
                elif replacechose == 2:
                    ChosedFiles.append(i)
                elif replacechose == 3:
                    pass
            else:
                ChosedFiles.append(i)
        if move2path:
            moveinfo = {
                'move2path':move2path,
                'netOper': 'CopyFile',
                'movefilesinfo':ChosedFiles
            }
            res = self.ui.SBCRe.SBCFileCopy(moveinfo)
            self.Dialog.destroy()

    def GetBranch(self,path,FaTree):
        childs = [FaTree.child(i) for i in range(FaTree.childCount())]
        for i in childs:
            FaTree.removeChild(i)
        treename = []
        try:
            CurFileList = self.ui.SBCRe.GetFileList(path)
            treename = [i['filename'] for i in CurFileList if i['isdir']]
        except:
            return
        # self.NewFolderBox()
        for text in treename:
            item = QTreeWidgetItem()
            item.setText(0, text)
            item.setIcon(0, QIcon(r'img/filecon/foldersm.png'))
            # item.setCheckState(0, Qt.Unchecked)
            FaTree.addChild(item)

            itemchild = QTreeWidgetItem()
            item.addChild(itemchild)
            self.TreeNodes[str_trans_to_md5(path +text+'/')] = {'path':path + text+'/','item':item, 'expand': 0}
    def nodeExpand(self):
        TreeNodes = {}
        for i in self.TreeNodes:
            TreeNodes[i] = self.TreeNodes[i]
        for i in TreeNodes:
            nodei = TreeNodes[i]
            if nodei['item'].isExpanded() and not nodei['expand']:
                self.TreeNodes[i]['expand']=1
                self.GetBranch(nodei['path'],nodei['item'])
    def get_CurPath(self):
        CurPath = '/'
        item = self.treeView.currentItem()
        CurPathFa = [item.text(0)]
        while item.parent():
            item = item.parent()
            CurPathFa.append(item.text(0))
        CurPath0 = [CurPathFa[len(CurPathFa)-i-1] for i in range(len(CurPathFa))]
        CurPath = '/'+'/'.join(CurPath0)+'/'
        self.label_3.setText(CurPath)
        return CurPath


