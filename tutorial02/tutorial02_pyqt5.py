#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 20:17:42 2020

@author: sukarno
"""

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QPushButton


@pyqtSlot()
def click_handle():
    print("I have clicked")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    btn = QPushButton("Click Me!!")
    btn.clicked.connect(click_handle)
    btn.show()
    sys.exit(app.exec_())