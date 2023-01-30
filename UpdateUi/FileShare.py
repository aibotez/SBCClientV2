from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QAction,QFileDialog,QMessageBox,QDialog

class FileShare():
    def __init__(self,ui):
        self.ui = ui
        self.ShareWindow = self.ui.ShareWindow
        self.bindSignal()

    def UpdateUi(self,infos):
        pass

    # http://10.147.17.148:90/SBCShare/?SBCShare=UQT1
    def GetShareFile(self):
        ShareLink = self.ShareWindow.lineEdit.text()
        print(ShareLink)
        SBCShare = self.ui.SBCRe.GetSBCShareFile0(ShareLink)
        print(SBCShare)
        if 'check' in SBCShare:
            if SBCShare['check'] == '分享不存在':
                QMessageBox.information(self.ui.MainWindow, '提示', '分享文件不存在')
                return
            elif SBCShare['check'] == '分享已超时':
                QMessageBox.information(self.ui.MainWindow, '提示', '分享文件已超时')
                return
            elif SBCShare['check'] == 'password':
                QMessageBox.information(self.ui.MainWindow, '提示', '分享文件不存在')
                pass

    def bindSignal(self):
        self.ShareWindow.pushButton_13.clicked.connect(lambda: self.GetShareFile())
        self.ShareWindow.lineEdit.returnPressed.connect(self.GetShareFile)