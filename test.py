from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia


# -*- coding:utf-8 -*-
import threading
import time
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.Qt import QThread


class a():
    def __init__(self):
        self.s = 6

    def a_a(self):
        print('a_a')

class b(a):
    def __init__(self):
        super().__init__()
        pass

    def b_b(self):
        print(self.s)

class bc(b):
    def __init__(self):
        super().__init__()
        pass

    def c_c(self):
        self.b_b()

c = bc()

c.c_c()
