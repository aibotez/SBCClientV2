from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia


# -*- coding:utf-8 -*-
import threading
import time
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.Qt import QThread


class aa():
    def __init__(self):
        self.saa = 8

    def a_a(self):
        print('a_a')

class a():
    def __init__(self):
        self.s = 6

    def a_a(self):
        print('a_a')

class b(a,aa):
    def __init__(self):
        a.__init__(self)
        aa.__init__(self)

    def b_b(self):
        # self.saa = 8
        print(self.saa)

class bc(b):
    def __init__(self):
        super().__init__()
        pass

    def c_c(self):
        self.b_b()

# c = b()
#
# c.b_b()

def te(ma):
    ma['ab'] = 1


m = {}
te(m)
print(m)
