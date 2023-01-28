from . import Moveui
import sys,hashlib
from PyQt5.QtWidgets import QTreeWidgetItem, QTreeWidget, QWidget, QVBoxLayout, QPushButton, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon,QBrush,QColor


def str_trans_to_md5(src):
    src = src.encode("utf-8")
    myMd5 = hashlib.md5()
    myMd5.update(src)
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest
class MoveUi(Moveui.Ui_Dialog):
    def __init__(self,Dialog,ui,ChosedFiles):
        super().__init__()
        self.ui = ui
        self.ChosedFiles = ChosedFiles
        self.Dialog = Dialog
        self.init()

    def init(self):
        self.setupUi(self.Dialog)
        self.label_3.setText('')
        self.pushButton.clicked.connect(self.MoveFile)
        self.treeView.setHeaderHidden(True)
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

    def MoveFile(self):
        move2path = self.get_CurPath()
        if move2path:
            moveinfo = {
                'move2path':move2path,
                'netOper': 'MoveFile',
                'movefilesinfo':self.ChosedFiles
            }
            res = self.ui.SBCRe.SBCFileMove(moveinfo)

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
        for text in treename:
            item = QTreeWidgetItem()
            item.setText(0, text)
            item.setIcon(0, QIcon(r'img/filecon/foldersm.png'))
            # item.setCheckState(0, Qt.Unchecked)
            FaTree.addChild(item)
            itemchild = QTreeWidgetItem()
            item.addChild(itemchild)
            self.TreeNodes[str_trans_to_md5(path +text)] = {'path':path + text+'/','item':item, 'expand': 0}
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


