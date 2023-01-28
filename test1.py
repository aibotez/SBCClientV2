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
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        # 实例化一个树形结构，隐藏了header
        self.tree = QTreeWidget()
        self.tree.setHeaderHidden(True)
        # self.tree.clicked.connect(self.get_checked1)
        self.tree.itemClicked.connect(self.get_CurPath)
        self.tree.expanded.connect(self.nodeExpand)
        self.TreeNodes = {}
        # 顶级分支
        self.tree_main = QTreeWidgetItem(self.tree)
        self.tree_main.setText(0, 'home')
        self.tree_main.setIcon(0, QIcon(r'img/filecon/foldersm.png'))
        item = QTreeWidgetItem()
        self.tree_main.addChild(item)
        self.TreeNodes[str_trans_to_md5('/Home/')] = {'path':'/home/','item':self.tree_main,'expand':0}
        self.pushButton = QPushButton('选好了')
        self.qvl = QVBoxLayout()
        self.qvl.addWidget(self.tree)
        self.qvl.addWidget(self.pushButton)
        self.setLayout(self.qvl)

        # 绑定一下槽函数，传入主要的分支节点
        self.pushButton.clicked.connect(lambda: self.get_checked(self.tree_main))

    def GetBranch(self,path,FaTree):
        childs = [FaTree.child(i) for i in range(FaTree.childCount())]
        for i in childs:
            FaTree.removeChild(i)
        treename = ['foldr1', 'sbc', 'suy']
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



    # @staticmethod
    def gen_branch(self,node: QTreeWidgetItem, texts: list):
        """ 给定某个节点和列表 在该节点生成列表内分支"""
        for text in texts:
            item = QTreeWidgetItem()
            item.setText(0, text)
            # item.setCheckState(0, Qt.Unchecked)
            node.addChild(item)


    def get_CurPath(self):
        CurPath = '/'
        item = self.tree.currentItem()
        CurPathFa = [item.text(0)]
        while item.parent():
            item = item.parent()
            CurPathFa.append(item.text(0))
        CurPath0 = [CurPathFa[len(CurPathFa)-i-1] for i in range(len(CurPathFa))]
        CurPath = '/'+'/'.join(CurPath0)+'/'
        print(CurPath)
        return CurPath
    def get_checked(self, node: QTreeWidgetItem) -> list:
        """ 得到当前节点选中的所有分支， 返回一个 list """
        temp_list = []
        # 此处看下方注释 1
        for item in node.takeChildren():
            # 判断是否选中
            if item.checkState(0) == Qt.Checked:
                temp_list.append(item.text(0))
                # 判断是否还有子分支
                if item.childCount():
                    temp_list.extend(self.get_checked(item))
            node.addChild(item)
        print(temp_list)
        return temp_list


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Demo()
    win.show()
    sys.exit(app.exec_())

# # coding=utf-8
#
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         hbox = QHBoxLayout(self)
#         left = QFrame(self)
#         # QFrame 控件添加StyledPanel样式能使QFrame 控件之间的界限更加明显
#         # left.setFrameShape(QFrame.StyledPanel)
#         right = QFrame(self)
#         # right.setFrameShape(QFrame.StyledPanel)
#         splitter1 = QSplitter(Qt.Horizontal)
#         splitter1.addWidget(left)
#         splitter1.setSizes([20, ])  # 设置分隔条位置
#         splitter1.addWidget(right)
#         hbox.addWidget(splitter1)
#         self.setLayout(hbox)
#
#         # 树
#         self.tree = QTreeWidget(left)
#         self.tree.setStyleSheet("background-color:#eeeeee;border:outset;color:#215b63;")
#         self.tree.setAutoScroll(True)
#         self.tree.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.EditKeyPressed)
#         self.tree.setTextElideMode(Qt.ElideMiddle)
#         # self.tree.setIndentation(30)
#         self.tree.setRootIsDecorated(True)
#         self.tree.setUniformRowHeights(False)
#         self.tree.setItemsExpandable(True)
#         self.tree.setAnimated(False)
#         self.tree.setHeaderHidden(True)
#         self.tree.setExpandsOnDoubleClick(True)
#         self.tree.setObjectName("tree")
#
#         # 设置根节点
#         root = QTreeWidgetItem(self.tree)
#         root.setText(0, '系统管理')
#         # 设置树形控件的列的宽度
#         # self.tree.setColumnWidth(0, 150)
#         # 设置子节点1
#         child1 = QTreeWidgetItem()
#         child1.setText(0, '增加人员信息')
#         root.addChild(child1)
#         # 设置子节点2
#         child2 = QTreeWidgetItem(root)
#         child2.setText(0, '查询人员信息')
#         # 加载根节点的所有属性与子控件
#         self.tree.addTopLevelItem(root)
#         # 设置stackedWidget
#         self.stackedWidget = QStackedWidget(right)
#
#         # 设置第一个面板
#         self.form1 = QWidget()
#         self.formLayout1 = QHBoxLayout(self.form1)
#         self.label1 = QLabel()
#         self.label1.setText("增加人员信息面板")
#         self.label1.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
#         self.label1.setAlignment(Qt.AlignCenter)
#         self.label1.setFont(QFont("Roman times", 50, QFont.Bold))
#         self.formLayout1.addWidget(self.label1)
#
#         # 设置第二个面板
#         self.form2 = QWidget()
#         self.formLayout2 = QHBoxLayout(self.form2)
#         self.label2 = QLabel()
#         self.label2.setText("查询人员信息面板")
#         self.label2.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
#         self.label2.setAlignment(Qt.AlignCenter)
#         self.label2.setFont(QFont("Roman times", 50, QFont.Bold))
#         self.formLayout2.addWidget(self.label2)
#
#         # 将两个面板，加入stackedWidget
#         self.stackedWidget.addWidget(self.form1)
#         self.stackedWidget.addWidget(self.form2)
#
#         # 树节点监听事件
#         self.tree.clicked.connect(self.onClicked)
#
#         # 窗口最大化
#         self.showMaximized()
#         self.setWindowTitle('树窗口分隔案列')
#         self.show()
#
#     def onClicked(self, qmodeLindex):
#         item = self.tree.currentItem()
#         print('Key=%s,value=%s' % (item.text(0), item.text(1)))
#         if item.text(0) == '增加人员信息':
#             self.on_pushButton1_clicked()
#         elif item.text(0) == '查询人员信息':
#             self.on_pushButton2_clicked()
#         else:
#             print('返回主界面')
#
#     # 按钮一：打开第一个面板
#     def on_pushButton1_clicked(self):
#         self.stackedWidget.setCurrentIndex(0)
#
#     # 按钮二：打开第二个面板
#     def on_pushButton2_clicked(self):
#         self.stackedWidget.setCurrentIndex(1)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())