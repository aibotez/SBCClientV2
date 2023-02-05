from SubUi import Moveui
import sys,hashlib
from PyQt5.QtWidgets import QTreeWidgetItem, QTreeWidget, QWidget, QVBoxLayout, QPushButton, QApplication,QMessageBox,QInputDialog,QDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon,QBrush,QColor
from PyQt5 import QtCore, QtGui, QtWidgets


def str_trans_to_md5(src):
    src = src.encode("utf-8")
    myMd5 = hashlib.md5()
    myMd5.update(src)
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest
class ChoseRoPathUi(Moveui.Ui_Dialog):
    def __init__(self,ui):
        super().__init__()
        self.ui = ui
        self.init()

    def init(self):
        self.ChosedRoPath = ''
        self.ui.SBCChoseRoPathWindowDialog = QDialog()
        self.ui.SBCChoseRoPathWindowDialog.show()
        self.Dialog = self.ui.SBCChoseRoPathWindowDialog
        self.setupUi(self.Dialog)
        self.label_3.setText('')
        self.Dialog.setWindowTitle('选择文件夹路径')
        self.pushButton.setText('确认')
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
        self.ui.SBCChoseRoPathWindowDialog.exec_()
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
        self.ChosedRoPath = move2path
        self.Dialog.close()
        return move2path

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


