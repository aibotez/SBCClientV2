import sys,base64,threading
from PyQt5.QtWidgets import QApplication, QMainWindow

from InitWindow import initWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = QMainWindow()
    Main.show()

    SBCMain = initWindow(Main)
    # SBCMain = SBCMain.initFrame()

    sys.exit(app.exec_())