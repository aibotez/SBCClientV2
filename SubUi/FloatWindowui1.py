from SubUi import FloatWindowui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *

class FloatWd(FloatWindowui.Ui_MainWindow):
    def __init__(self,ui):
        super().__init__()
        self.ui = ui
        self.init()


    def init(self):
        Main = QMainWindow()

        self.setupUi(Main)
        Main.show()

        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        # self.setWindowOpacity(0.9)
        # self.setCursor(Qt.PointingHandCursor)
        # self.setupUi(self.ui.MainWindow)
