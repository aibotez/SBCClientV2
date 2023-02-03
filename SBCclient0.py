import sys,base64,threading
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from InitWindow import initWindow

# zhen.zhou
if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    Main = QMainWindow()

    SBCMain = initWindow(Main)
    # SBCMain = SBCMain.initFrame()
    Main.show()
    # SBCMain.SBCMain.show()
    # sys.exit()
    sys.exit(app.exec_())