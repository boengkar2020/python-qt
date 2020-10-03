#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 20:30:03 2020

@author: sukarno
"""

import sys
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QDialog, QPushButton, QLineEdit, QHBoxLayout

class Form(QDialog):
    def __init__ (self, parent=None):
        super(Form,self).__init__(parent)
        self.setWindowTitle("My Form")
        self.initUI()

    def initUI(self):
        self.btn = QPushButton("Send")
        self.btn.clicked.connect(self.click_handle)

        self.edit = QLineEdit("Wirite text here...")

        hlayout = QHBoxLayout()
        hlayout.addWidget(self.edit)
        hlayout.addWidget(self.btn)


        self.setLayout(hlayout)

    @Slot()
    def click_handle(self):
        print(self.edit.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())
