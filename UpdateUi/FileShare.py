

class FileShare():
    def __init__(self,ui):
        self.ui = ui
        self.ShareWindow = self.ui.ShareWindow
        self.bindSignal()

    def GetShareFile(self):
        ShareLink = self.ShareWindow.lineEdit.text()
        print(ShareLink)
        self.ui.SBCRe.GetSBCShareFile(ShareLink)
    def bindSignal(self):
        self.ShareWindow.pushButton_13.clicked.connect(lambda: self.GetShareFile())
        self.ShareWindow.lineEdit.returnPressed.connect(self.GetShareFile)