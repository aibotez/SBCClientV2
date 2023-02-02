import sys,base64,threading
from PyQt5.QtWidgets import QApplication, QMainWindow

from InitWindow import initWindow

# zhen.zhou
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = QMainWindow()

    SBCMain = initWindow(Main)
    # SBCMain = SBCMain.initFrame()
    Main.show()
    # SBCMain.SBCMain.show()
    # sys.exit()
    sys.exit(app.exec_())