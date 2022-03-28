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

    # app = QtWidgets.QApplication(sys.argv)
    # myshow = MyWindow()
    # myshow.show()
    # sys.exit(app.exec_())

    from PyQt5.QtCore import pyqtSignal, QObject


    class signal(QObject):
        # 自定义一个信号
        my_sighal = pyqtSignal(str)

        # 定义一个发送信号的函数
        def run(self, text):
            self.my_sighal.emit(text)


    class slot(QObject):
        # 这个函数将用于绑定信号
        def action(self, text):
            print("I received that signal:" + text)


    if __name__ == '__main__':
        # 创建类的对象
        send = signal()
        receive = slot()

        # 将信号与动作进行绑定
        send.my_sighal.connect(receive.action)
        # 发送信号
        send.run("hello")
        #
        # # 将信号与槽函数解绑
        # send.my_sighal.disconnect(receive.action)
        # send.run("hello")

