#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 22:58:00 2020

@author: sukarno
"""

import sys
from ui._preferences_pyside2 import Ui_Dialog
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QDialog


class Preferences(QDialog):
    def __init__ (self,parent=None):
        super(Preferences,self).__init__ (parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.sendButton.clicked.connect(self.send_handle)

    @Slot()
    def send_handle(self):
        print(self.ui.nameText.text())
        print(self.ui.addressText.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Preferences()
    dlg.show()
    sys.exit(app.exec_())
