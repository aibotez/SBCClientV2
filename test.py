from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia


class myLabel(QtWidgets.QLabel):  # 自定义的QLabel类

    def __init__(self, parent=None):
        super(myLabel, self).__init__(parent)

    def mousePressEvent(self, e):  ##重载一下鼠标点击事件
        # 左键按下
        if e.buttons() == QtCore.Qt.LeftButton:
            self.setText("左")
        # 右键按下
        elif e.buttons() == QtCore.Qt.RightButton:
            self.setText("右")
        # 中键按下
        elif e.buttons() == QtCore.Qt.MidButton:
            self.setText("中")
        # 左右键同时按下
        elif e.buttons() == QtCore.Qt.LeftButton | QtCore.Qt.RightButton:
            self.setText("左右")
        # 左中键同时按下
        elif e.buttons() == QtCore.Qt.LeftButton | QtCore.Qt.MidButton:
            self.setText("左中")
        # 右中键同时按下
        elif e.buttons() == QtCore.Qt.MidButton | QtCore.Qt.RightButton:
            self.setText("右中")
        # 左中右键同时按下
        elif e.buttons() == QtCore.Qt.LeftButton | QtCore.Qt.MidButton | QtCore.Qt.RightButton:
            self.setText("左中右")


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.label = myLabel("点我")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())
