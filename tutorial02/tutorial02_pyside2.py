#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 20:17:42 2020

@author: sukarno
"""

import sys
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QPushButton


@Slot()
def click_handle():
    print("I have clicked")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    btn = QPushButton("Click Me!!")
    btn.clicked.connect(click_handle)
    btn.show()
    sys.exit(app.exec_())
